from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<str:isbn>', views.DetailView.as_view(), name='detail'),
]