from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name = 'details'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('update/updatemovie/<int:id>/', views.updatemovie, name='updatemovie'),
    path('delete/<int:id>/', views.delete, name='delete')
]