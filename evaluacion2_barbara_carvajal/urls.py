from django.contrib import admin
from django.urls import path
from modelsForm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('proyectos/', views.listadoProyectos, name='listadoProyectos'),
    path('agregarProyecto/', views.agregarProyecto, name='agregarProyecto'),
    path('eliminarProyecto/<int:id>/', views.eliminarProyecto, name='eliminarProyecto'),
    path('actualizarProyecto/<int:id>/', views.actualizarProyecto, name='actualizarProyecto'),
]
