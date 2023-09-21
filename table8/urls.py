from django.urls import path
from .import views
from .views import UtpView

app_name = "table8"

urlpatterns = [
    path('view',views.UtpView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update8"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]