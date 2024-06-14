from django.urls import path
from .views import upload_file
from .views import upload_file, test_view

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('test/', test_view, name='test_view'),
]
