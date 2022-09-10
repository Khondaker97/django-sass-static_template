from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.companies),
    path('dashboard/', views.dashboard),
    path('leads/', views.leads),
    path('intels/', views.intels),
    path('integrations/', views.integrations),
    path('team/', views.team),
    path('help/', views.support),
]