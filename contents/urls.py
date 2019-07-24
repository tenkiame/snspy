from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.BlogAddView.as_view(), name='create'),
    path('', views.BlogListView.as_view(), name='list'),
    path('<int:blog_pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('<int:object_pk>/edit/', views.BlogEditView.as_view(), name='edit'),
    path('<int:object_pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
]
