from django.urls import path,include 
from .import views    
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login',views.loginPage,name = "login"),
    path('logout',views.logout_user,name = "logout"),
    path('404',view404.as_view(),name ="error"),
    path('profile<str:user_id>',views.ProfileView,name ="profile"),
    path('area_manager',views.Area_manager_profile_view,name ="manager"),
    path('CDN',views.CDN_profile_view,name = "cdn"),
    path('HOT',views.HOT_profile_view,name = "hot"),
    path('statistics<str:pk>',views.StatisticsView,name = "statistics"),   
    path('help',HelpView.as_view(),name = "help"),
    path('contact',ContactView.as_view(),name = "contact")
]