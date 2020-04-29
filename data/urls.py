from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_data, name = 'post_data'),
    path('data/new/',views.new_data,name = 'new_data'),
    path('data/delete/',views.delete_data,name = 'delete_data'),
]
