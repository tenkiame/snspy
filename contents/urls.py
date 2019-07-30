from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('create/', views.BlogAddView.as_view(), name='blogcreate'),
    path('', views.BlogListView.as_view(), name='bloglist'),
    path('<int:blog_pk>/', views.BlogDetailView.as_view(), name='blogdetail'),
    path('<int:object_pk>/edit/', views.BlogEditView.as_view(), name='blogedit'),
    path('<int:object_pk>/delete/', views.BlogDeleteView.as_view(), name='blogdelete'),
    path('tagcreate/', views.TagAddView.as_view(), name='tagadd'),
    path('taglist/', views.TagListView.as_view(), name='taglist'),
    path('tagEdit/', views.TagEditView.as_view(), name='tagedit'),
    path('tagdelete/', views.TagDeleteView.as_view(), name='tagdelete'),
    path('imagecadd/', views.ImageAddView.as_view(), name='imageadd'),
    path('imagelist/', views.ImageListView.as_view(), name='imagelist'),
    path('imageedit/', views.ImageEditView.as_view(), name='imageedit'),
    path('imagedelete/', views.ImageDeleteView.as_view(), name='imagedelete'),
]
