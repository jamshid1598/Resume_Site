from django.urls import path, include

from .views import home, update, create_multiple_cv

app_name='Home'

urlpatterns = [
    path('', home, name='main-home'),
    path('update/<int:id>/', update, name='cv-update'),
    path('create/', create_multiple_cv, name='cv-create')
]