from django.urls import path
from . import views
urlpatterns = [
	path('',views.inicio,name="inicio"),
	path('index/', views.index, name='index'),
	path('accounts/register/', views.register, name='register'),
]
'''path('login/', views.login, name='login'),'''