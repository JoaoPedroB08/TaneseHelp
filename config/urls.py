from django.contrib import admin
from django.urls import path
from oficina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.custom_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),

    path('caixas/', views.lista_caixas, name='lista_caixas'),
    path('caixas/nova/', views.nova_caixa, name='nova_caixa'),
    path('caixas/excluir/<int:id>/', views.excluir_caixa, name='excluir_caixa'),

    path('caixas/<int:caixa_id>/ferramentas/', views.lista_ferramentas, name='lista_ferramentas'),
    path('caixas/<int:caixa_id>/ferramentas/nova/', views.nova_ferramenta, name='nova_ferramenta'),
]