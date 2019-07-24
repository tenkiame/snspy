from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Account.as_view(), name='accounts'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
