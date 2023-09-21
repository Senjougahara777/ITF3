from django.urls import path
from . import views
from .views import TnaView

app_name = "table3"

urlpatterns =[
    path('view',views.TnaView,name="form-view"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update3"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),   
]