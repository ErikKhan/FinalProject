# Hitting the Wheels

There are many pros and cons of buying a car. Some cars are powerful but not fuel economic, some have few great qualities but lack other important ones. Most of the economic mid range cars do lack basic safety features like airbags and ABS. I personally feel that these must be the compulsory features in every car so thats why i built this website where one can get information about cars like reviews, price, condition. This website will help the users to buy a car the smart way and can also communicate with owners of the car to get the feel for cars. Even if they have questions related to any other subjects then can just go and use the forum. Its very user friendly forum. 

This project consists of two applications. One is about the **ratings of the cars** and the other is a **discussion forum**. It contains four django models as well as a User model. It is developed by using django, Python and Javascript. I wanted to make a project like this to expand my knowledge of Django DataBases and techniques like getting data from database, storing data and also role based authentications. All webpages of the project are mobile-responsive. My project satisfies all the distinctiveness and complexity requirements as mentioned. 


## Installation:
- Install project dependencies
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
- Create superuser with python manage.py createsuperuser
- Go to website address and register an account and then Sign In.

## Files and directories:
- Project - Main application directory
   - Blog
     - admin.py - Here I added some admin classes and re-registered User model
     - forms.py - Added a form for adding a post
     - models.py - Contains Two blog models and user model
     - urls.py - All application URLs
     - views.py - All Blog Views
   - home
     - admin.py - Here I added some model classes so I can see in the admin Panel
     - forms.py - Added a form for adding a Car model. Only admin can do it. 
     - models.py - Contains Two models and user model
     - urls.py - All application URLs
     - views.py - All Car Views
   - project - Project Directory     
   - static - Contains all static content
     - All the images in this folder
     - main.js - for image to move like a slideshow
     - style.css - for styling
     - tinyinject.js - Tiny MCE is an open-source online rich text editor that can be used to simplify website content creation.
   - templates - contains all application templates
     - Blog - Contains all the blog templates
     - home - conatins all the Car rating or home templates
     - base.html - So all the templates can use the base file   


## Ratings:
This application offers a wealth of information when it comes to vehicle reviews. Writing a car review that proves useful for other potential car-buyers is a fun and rewarding experience. It’s also a great way to sharpen your observational and analytical skills. If one have a passion for automobiles and a knack for writing, *Car reviews* provide the ideal outlet for you to knit your interests together. It will help the customers which car to buy. The *Cost* of car, *performance*, *safety features*, *engine specifications*, *technological innovations* etc. This website will really help customers at what kind of car they need or want to buy. It will help them very much. One can also read and leave a comment if one needs any information about a specific car. Most of the things is done by Admin. Admin can use the Admin panel or on the website to post a car. Only Admin can *add*, *delete* or *edit* any Car specifications. Other users who are registered on this website can leave a rating and can also leave a comment. Users can only *edit* or *delete* or *edit rating* their comment. If they want to delete a pop up will come using Javascript onclick to ask if the user is sure to delete. I have used *dynamic URLs* in this application. This approach has many advantages in web development, avoiding a great deal of the redundant and tedious HTML editing that often must be done on static sites. Rating has been done by mathimatical equation using python. 

## Discussion forum:
This application offers discussion forum. An application which allows members to hold discussions online. The discussion is started by one member by posting a topic and other members reply. This allows members of the same group to share information and ideas. Discussion forum has many advantages.
- Emphisis on learning instead of teaching
- Improve communication
- Better engagement 

This applications can be used by Admin but User who are registered can also start a forum regarding any topic for example 
- Cars
- Weather
- Stock Exchange
- Web Programming

Users can leave comments, add a comment and can reply to a comment as well. User can see how many people have viewed one's post and can also see how many comments it has. It saves the count which is then displayed in (). Admin can use the Admin panal to use the open-source online rich text editor. Admin can post a picture in the blog or make the font italic, bold etc. In this application for Urls I have used *slug based routing*. In one of the models I have used slug field. My system currently has some Post models in the database and each one has a slug associated with it. On the main page one can search for any posts. Just go to the search bar and then search for the post one would like to read. *Pagination* is also done, where user can only see five post per page or click next to see the next five pages and vise versa. 

## Conclusion:
Finally I can say that by all counts and with proven results, it is not wonder that I have developed myself a fullstack developer. Through this course, I learned about many new concepts, especially in regards to using client-side JavaScript to build dynamic web pages, saving and getting data from databases using django and python. I have also learned the act of testing, the codes I have written to make sure everything run smoothly without any bugs. 


