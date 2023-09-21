from django.urls import path
from .import views
from .views import SectionView

app_name = "table10"

urlpatterns = [
    path('view',views.SectionView,name = "formView"),
    path('list',views.form_list,name = "form-list"),
    path('update<str:pk>',views.form_update,name = "update10"),
    path('list/detail/<str:pk>',views.form_detail, name = "formDetail"),
]