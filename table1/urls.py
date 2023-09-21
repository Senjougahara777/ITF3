from django.urls import path
from .import views
from .views import BasicFormView

app_name = "table1"



urlpatterns = [
    path('view',views.BasicFormView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update1"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]