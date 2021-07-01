from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<application>/', views.application_index, name='application_index'),
    path('<application>/<int:id>', views.details, name='details'),
    path('<application>/<int:id>/<parameter>', views.parameter, name='parameter')
]