from django.urls import path
from Notas.views import notasList, categoriasList

urlpatterns = [
    
    #path('listadoNotas/', listadoNotas, name = "listadoNotas"),
    path('notas/list/', notasList.as_view(template_name='inicio.html'), name='notas_list'),
    path('categorias/list/', categoriasList.as_view(template_name='categorias.html'), name='categorias_list'),
    #path('notas/single/', vistaNota.as_view(template_name='single.html'), name='single'),
]