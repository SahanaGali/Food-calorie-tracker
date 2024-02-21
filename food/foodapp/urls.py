from django.urls import path
from foodapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('new_food/',views.new_food,name='new_food'),
    path('track/',views.track_food,name='track'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('detail/<int:pk>',views.detail,name='detail'),
    # path('favourite/<int:pk>/',views.favourite,name='favourite'),
    # path('favourites/<int:pk>/',views.favourites,name='favourites'),
]