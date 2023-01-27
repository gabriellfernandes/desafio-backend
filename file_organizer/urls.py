from django.urls import path
from . import views


urlpatterns = [
    path("", views.page, name="index"),
    path('file/', views.FileUploadView.as_view(), name='file'),
    path('file/<str:loja>/', views.FileUploadParamsView.as_view(), name='loja_nome')
]