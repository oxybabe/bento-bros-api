"""
URL configuration for bento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import include, path
from menu_app.views import  home, menu, menu_item, seed, appetizer_item, main_item, dessert_item, AppetizerAPIView, MainCourseAPIView, DessertAPIView
from menu_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('menu/', menu),
    path('menu_item/<int:index>', menu_item, name="item"),
    path('seed/', seed),
    path('appetizer/<int:appetizer_item_id>', appetizer_item, name="appetizer_item"), 
    path('main/<int:main_item_id>', main_item, name="main_item"), 
    path('dessert/<int:dessert_item_id>', dessert_item, name="dessert_item"), 
    path('backoffice/', include('menu_app.urls') ), 
    path('api/appetizers/', views.AppetizerAPIView.as_view(), name="appetizer_APIView"),
    path('api/main_course/', views.MainCourseAPIView.as_view(), name="main_course_APIView"), 
    path('api/desserts/', views.DessertAPIView.as_view())
   
 
]
