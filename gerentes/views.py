from django.shortcuts import render, redirect
from produtos.models import Produto
from produtos.forms import cadProdForm
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data ['msg'] = "Bem-vindo ao SisEstoque!"
            data ['exibeInicio'] = True
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)

def listarProdutos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data ['msg'] = 'Produtos Cadastrados:'
            data ['exibeProdutos'] = True
            data ['qsProdutos'] = Produto.objects.all()
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)

def cadastrarProdutos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data ['msg'] = 'Cadastro de Produto:'
            data ['exibeCadastroProd'] = True

            if request.method == 'POST':
                form = cadProdForm(request.POST)
                if form.is_valid():
                    form.save()
                    data['exibeAlert'] = True
                    data['msg_alert'] = 'Produto cadastrado com sucesso!'
                    data['link'] = '/cadastrar_produtos'

            else:
                data['form'] = cadProdForm()
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)

def opcModificarProdutos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data['exibeOpcModProd'] = True
            data['qsProdutos'] = Produto.objects.all()
            codProd = request.POST.get('opcaoProduto','')

            if request.method == 'POST':
                data['qsProdutos'] = Produto.objects.filter(codigo=codProd)
                data['exibeOpcModProd'] = False
                data['exibeModProd'] = True
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)


def modificarProdutos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data['exibeModProd'] = True

            if request.method == 'POST':
                if 'form1' in request.POST:  #form1 é o form da view opcModificarProdutos
                    data['exibeModProd'] = True
                    codProdEsc = request.POST.get('opcaoProduto','') #produto escolhido na tela anterior
                    request.session['codProdEsc'] = codProdEsc
                    codigo = request.POST.get('codigo', '')
                    nome = request.POST.get('nome', '')
                    quantidade = request.POST.get('quantidade', '')
                    preco = request.POST.get('preco', '')

                    data['prod'] = Produto.objects.get(pk=codProdEsc)

            if request.method == 'POST':
                if 'form2' in request.POST: #form 2 é o form dessa view mesmo
                    produto = Produto.objects.get(pk=request.session.get('codProdEsc'))
                    if request.method == 'POST':
                        form = cadProdForm(request.POST, instance=produto)
                        form.save()
                        data['exibeAlert'] = True
                        data['msg_alert'] = 'Produto modificado com sucesso!'
                        data['link'] = '/opc_mod_produtos'
                    '''
                    codigo = request.POST.get('codigo', '')
                    nome = request.POST.get('nome', '')
                    quantidade = request.POST.get('quantidade', '')
                    preco = request.POST.get('preco', '')
                    Produto.objects.filter(pk=request.session.get('codProdEsc')).update(codigo=codigo, nome=nome, quantidade=quantidade, preco=preco)
                    '''
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)

def deletarProdutos(request):
    if request.user.is_authenticated:
        usuario = User.objects.get(username=request.user)
        if usuario.groups.filter(name='Gerentes').exists():
            data = {}
            data ['exibeDelProdutos'] = True
            data ['qsProdutos'] = Produto.objects.all()

            if request.method == 'POST':
                codProd = request.POST.get('opcaoProduto', '')
                Produto.objects.filter(codigo=codProd).delete()
                data['exibeAlert'] = True
                data['msg_alert'] = 'Produto deletado com sucesso!'
                data['link'] = '/deletar_produtos'
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
    return render(request, 'gerentes/home.html', data)
