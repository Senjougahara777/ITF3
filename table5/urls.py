from django.urls import path
from .import views
from .views import StpView

app_name = "table5"



urlpatterns = [
    path('view',views.StpView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update5"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]