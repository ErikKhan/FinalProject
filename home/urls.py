from django.contrib import admin
from django.urls import path, include
from home import views


app_name= "home"

urlpatterns = [
    path('', views.home, name="home"),
   
    
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('addrating/<int:id>/', views.add_rating, name="add_rating"),
    path('editrating/<int:car_id>/<int:review_id>/', views.editRating, name="edit_rating"),
    path('deleterating/<int:car_id>/<int:review_id>/', views.deleteRating, name="delete_rating"),
   
]