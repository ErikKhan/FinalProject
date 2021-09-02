from django.shortcuts import render, HttpResponse, redirect
from .models import Car
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from blog.models import Post
from math import ceil
from django.db.models import Avg
from .forms import *

def home(request):
    
    cars = Car.objects.all()
    n= len(cars)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'car': cars}
    return render(request,"home/home.html", params)
    

def detail(request, id):
    car = Car.objects.get(id=id) # select * from car where id=id
    reviews = Rating.objects.filter(car=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "car": car,
        "reviews": reviews,
        "average": average
    }
    return render(request, 'home/details.html', context)
   

    



def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home:home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home:home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home:home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created! Click on Login now")
        return redirect('home:home')

    else:
        return HttpResponse("404 - Not found")



def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home:home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home:home")

    return HttpResponse("<h3>Create your Account using Signup</h3>")
   

    

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home:home')




def create(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = CarForm(request.POST or None)

                
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("home:home")
            else:
                form = CarForm()
            return render(request, 'home/create.html', {"form": form, "controller": "Add Car"})
        
        
        else:
            return redirect("home:home")

    
    return redirect("home:handleLogin")   

def edit(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the car linked with id
            car = Car.objects.get(id=id)

            # form check
            if request.method == "POST":
                form = CarForm(request.POST or None, instance=car)
                # check if form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("home:detail", id)
            else:
                form = CarForm(instance=car)
            return render(request, 'home/create.html', {"form": form, "controller": "Edit"})
        # if they are not admin
        else:
            return redirect("home:home")

    # if they are not loggedin
    return redirect("home:handleLogin") 

def delete(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the car
            car = Car.objects.get(id=id)

            # delete the car
            car.delete()
            return redirect("home:home")
        # if they are not admin
        else:
            return redirect("home:home")

    # if they are not loggedin
    return redirect("home:handleLogin") 


def add_rating(request, id):
    if request.user.is_authenticated:
        car = Car.objects.get(id=id)
        if request.method == "POST":
            form = RatingForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.car = car
                data.save()
                return redirect("home:detail", id)
        else:
            form = RatingForm()
        return render(request, 'home/details.html', {"form": form})
    else:
        return redirect("home:handleLogin")

def editRating(request, car_id, review_id):
    if request.user.is_authenticated:
        car = Car.objects.get(id=car_id)
        # review
        review = Rating.objects.get(car=car, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission
            if request.method == "POST":
                form = RatingForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                         error = "Out or range. Please select rating from 0 to 10."
                         return render(request, 'home/editrating.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("home:detail", car_id)
            else:
                form = RatingForm(instance=review)
            return render(request, 'home/editrating.html', {"form": form})
        else:
            return redirect("home:detail", car_id)
    else:
        return redirect("home:handleLogin")


# delete reivew
def deleteRating(request, car_id, review_id):
    if request.user.is_authenticated:
        car = Car.objects.get(id=car_id)
        # review
        review = Rating.objects.get(car=car, id=review_id)

        # check if the review was done by the logged in user
        if request.user == review.user:
            # grant permission to delete
            review.delete()

        return redirect("home:detail", car_id)
            
    else:
        return redirect("home:handleLogin")