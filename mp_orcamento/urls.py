from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('orcamentos/cliente/1/', tabela_clientes, name='tabela_cliente'),
    path('orcamentos/cliente/estatisticas_dos_clientes/', estatisticas_dos_clientes, name='estatisticas_dos_clientes'),
]