from django.urls import path
from .views import *

urlpatterns=[
    path('',book_list,name='book_list'),
    path('Add/',book_create,name='book_create'),
    path('Update/<int:id>',book_update,name='book_update'),
    path('Delete/<int:id>',book_delete,name='book_delete'),]