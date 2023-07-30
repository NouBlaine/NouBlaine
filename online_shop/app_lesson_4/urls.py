from django.urls import path
from .views import lesson_4_view

urlpatterns = [
    path('', lesson_4_view)
]