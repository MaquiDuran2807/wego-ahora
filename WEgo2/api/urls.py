from django.contrib import admin
from django.urls import path

from .views import AccountList





urlpatterns = [
    path('account/',AccountList.as_view()),
]
