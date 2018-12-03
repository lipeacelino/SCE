from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

'''
    pesquisar... authenticate user django with validation group
'''


def loginView(request):

    data = {}
    if request.method == 'POST':
        #usr_aux = User.objects.get(username=request.POST.get('usuario'))
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuarioObj = authenticate(request, username=usuario, password=senha)

        if usuarioObj is not None:
            if usuarioObj.groups.filter(name='Gerentes').exists():
                login(request, usuarioObj)
                return redirect('/home/')
            elif usuarioObj.groups.filter(name='Vendedor').exists():
                login (request, usuarioObj)
                return redirect('/v/home')
            else:
                data['erroAutenticacao'] = True

        else:
            data['erroAutenticacao'] = True

    return render(request, 'usuarios/login.html', data)

def logoutView(request):
    logout(request)
    #redirect('home/')
    return redirect('/login')
