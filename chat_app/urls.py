from django.urls import path
from . import views


urlpatterns = [
    path("institute", views.InstituteSignUpView.as_view(), name="insti"),

]
