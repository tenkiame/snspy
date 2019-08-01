from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.AccountListView.as_view(), name='accountlist'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profileedit'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete/', views.UserDeleteView.as_view(), name='userdelete'),
]
