from django.urls import path
from .import views
from .views import NdtpView

app_name = "table9"

urlpatterns = [
    path('view',views.NdtpView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update9"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]