from django.contrib import admin
from django.urls import path
from gerentes.views import *
from usuarios.views import *
from vendedores.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView),
    path('logout/', logoutView),
    path('', home),
    path('home/', home),
    path('lista_produtos/', listarProdutos),
    path('cadastrar_produtos/', cadastrarProdutos),
    path('opc_mod_produtos/', opcModificarProdutos),
    path('opc_mod_produtos/modificar_produtos/', modificarProdutos),
    path('deletar_produtos/', deletarProdutos),
    path('v/home', homeV)
]
