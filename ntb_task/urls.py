from django.urls import path
from . import views
from .views import ResourceView, index

urlpatterns = [
    path('', index, name='index'),
    path('resources/', ResourceView.as_view(), name='resources'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create/', views.ResourceCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.ResourceEdit.as_view(), name='edit'),

]
