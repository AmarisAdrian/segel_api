from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.config.views import *
from app.campana.views import *
from app.divipol.views import *
from app.anexo.views import *
from app.puesto_votacion.views import *
from app.registro_votante.views import *
from app.usuario.views import *
from app.votante.views import *
from app.zona_votacion.views import *

app_name = 'api'
router = routers.DefaultRouter()
router.register('departamento',DepartamentoViewSet,basename="departamento")
router.register('ciudad',CiudadViewSet,basename="ciudad")
router.register('configuracion',configuracionViewSet,basename="configuracion")
router.register('log',LogViewSet,basename="log")
router.register('estado-usuario',EstadoUsuarioViewSet,basename="estado-usuario")
router.register('tipo-documento',TipoDocumentoViewSet,basename="tipo-usuario")
router.register('genero',GeneroModelViewSet,basename="genero")
router.register('campana',CampanaViewSet,basename="campana")
router.register('divipol',DivipolViewSet,basename="divipol")
router.register('anexo-usuario',AnexoUsuarioViewSet,basename="anexo-usuario")
router.register('anexo-votante',AnexoVotanteViewSet,basename="anexo-votante")
router.register('puesto-votacion',PuestoVotacionViewSet,basename="puesto-votacion")
router.register('registro-votante',RegistroVotanteViewSet,basename="registro-votante")
router.register('usuario',UsuarioViewSet,basename="usuario")
router.register('votante',VotanteViewSet,basename="votante")
router.register('zona-votacion',ZonaVotacionViewSet,basename="zona-votacion")

urlpatterns =  [
    path('',include(router.urls)),
]
urlpatterns += router.urls
