from django.urls import path
from .import views
from .views import Stp2View

app_name = "table7"

urlpatterns = [
    path('view',views.Stp2View,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update7"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]