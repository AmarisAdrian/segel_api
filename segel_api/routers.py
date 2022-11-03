from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.config.views import *

app_name = 'api'
router = routers.DefaultRouter()
router.register('departamento',DepartamentoViewSet,basename="departamento")
urlpatterns =  [
    path('',include(router.urls)),
]
urlpatterns += router.urls
