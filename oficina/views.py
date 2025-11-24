from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.db.models import ProtectedError
from .models import Caixa, Ferramenta

def custom_login(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        senha_input = request.POST.get('senha')
        
        try:
            user = User.objects.get(email=email_input)
            if user.check_password(senha_input):
                login(request, user)
                
                if user.email == 'admin@gmail.com':
                    return redirect('/admin/')
                else:
                    return redirect('lista_caixas')
            else:
                return render(request, 'login.html', {'erro': 'Senha incorreta!'})
                
        except User.DoesNotExist:
            return render(request, 'login.html', {'erro': 'E-mail não cadastrado!'})
            
    return render(request, 'login.html')

def fazer_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def lista_caixas(request):
    caixas = Caixa.objects.filter(dono=request.user)
    return render(request, 'lista_caixas.html', {'caixas': caixas})

@login_required(login_url='login')
def nova_caixa(request):
    if request.method == 'POST':
        identificacao = request.POST.get('identificacao')
        Caixa.objects.create(dono=request.user, identificacao=identificacao)
        return redirect('lista_caixas')
    return render(request, 'nova_caixa.html')

@login_required(login_url='login')
def excluir_caixa(request, id):
    caixa = get_object_or_404(Caixa, id=id)
    if request.method == 'POST':
        try:
            caixa.delete()
            return redirect('lista_caixas')
        except ProtectedError:
            return render(request, 'confirmar_exclusao.html', {
                'caixa': caixa, 
                'erro': 'ERRO CRÍTICO: Caixa contém ferramentas e não pode ser destruída.'
            })
    return render(request, 'confirmar_exclusao.html', {'caixa': caixa})

@login_required(login_url='login')
def lista_ferramentas(request, caixa_id):
    caixa = get_object_or_404(Caixa, id=caixa_id)
    ferramentas = Ferramenta.objects.filter(caixa=caixa)
    return render(request, 'lista_ferramentas.html', {'caixa': caixa, 'ferramentas': ferramentas})

@login_required(login_url='login')
def nova_ferramenta(request, caixa_id):
    caixa = get_object_or_404(Caixa, id=caixa_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Ferramenta.objects.create(caixa=caixa, nome=nome, descricao=descricao)
        return redirect('lista_ferramentas', caixa_id=caixa.id)
    return render(request, 'nova_ferramenta.html', {'caixa': caixa})