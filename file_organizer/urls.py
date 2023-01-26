from django.urls import path
from . import views


urlpatterns = [
    path("", views.page, name="index"),
    path('file/', views.FileUploadView.as_view(), name='file')
]