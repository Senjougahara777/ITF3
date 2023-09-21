from django.urls import path
from . import views
from .views import TtpdView

app_name = "table4"

urlpatterns =[
    path('view',views.TtpdView,name="form-view"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update4"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),   
]