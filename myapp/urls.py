from django.urls import path
from .views import *
from . import views
urlpatterns=[
    path('create_travel/',create_travel.as_view(),name='create_travel'),
    path('detail_travel/<int:pk>/',detail_travel.as_view(),name='detail_travel'),
    path('update_travel/<int:pk>/',update_travel.as_view(),name='update_travel'),
    path('delete_travel/<int:pk>/',delete_travel.as_view(),name='delete_travel'),
    path('search_travel/<str:Name>/',search_travel.as_view(),name='search_travel'),


    path('travel_create/',views.travel_create,name='travel_create'),
    path('travel_detail/<int:id>/',views.travel_detail,name='travel_detail'),
    path('travel_update/<int:id>/',views.travel_update,name='travel_update'),
    path('travel_delete/<int:id>/',views.travel_delete,name='travel_delete'),
    path('',views.index,name='index'),

]

