
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet, CidadeViewSet, AlunoViewSet


router = DefaultRouter()
router.register(r'estados', EstadoViewSet,)
router.register(r'cidade', CidadeViewSet,)
router.register(r'aluno', AlunoViewSet,)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
