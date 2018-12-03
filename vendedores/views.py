from django.shortcuts import render
from produtos.models import Produto

def homeV(request):
    if request.user.is_authenticated:
        data = {}
        data ['exibeVenderProd'] = True
        data['qsProdutos'] = Produto.objects.all()

        if request.method == 'POST':
            codProd = request.POST.get('opcaoProduto')
            qtdComp = request.POST.get('quantidade')
            produtoQs = Produto.objects.filter(codigo=codProd)

            produtoObj = Produto.objects.get(codigo=codProd)
            qtdProd = produtoObj.quantidade

            if qtdProd != 0:
                produtoQs.update(quantidade=(qtdProd - int(qtdComp)))
            else:
                data['msg_alert'] = "Quantidade insuficiente no estoque!"
                data['exibeAlert'] = True

    else:
        return redirect('/login/')
    return render(request, 'vendedores/v.home.html', data)
