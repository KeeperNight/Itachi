from django.urls import path

from . import views

urlpatterns=[
    path('',views.about_book,name="book"),
    path('book1/',views.books),
]
