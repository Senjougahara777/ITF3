from django.urls import path
from .import views
from .views import DtpaView

app_name = "table6"

urlpatterns = [
    path('view',views.DtpaView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update6"),
    path('DTPAupdate<str:pk>',views.form_update,name = "dtpa_update"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]