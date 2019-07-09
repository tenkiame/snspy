from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    #ここから
    path('create/', views.BlogAddView.as_view(), name='create'),
    path('', views.BlogListView.as_view(), name='list'),
]
