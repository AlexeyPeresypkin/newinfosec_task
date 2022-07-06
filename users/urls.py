from django.urls import path
from . import views
from .views import ResourceView

urlpatterns = [
    path('', ResourceView.as_view(), name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create/', views.ResourceCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.ResourceEdit.as_view(), name='edit'),

]
