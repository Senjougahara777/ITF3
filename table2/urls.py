from django.urls import path
from . import views
from .views import BasicInfoView

app_name = "table2"

urlpatterns =[
    path('view',views.BasicInfoView,name="form-view"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update2"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),   
]