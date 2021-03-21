from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# View da página inicial
def index(request):
    contatos = Contato.objects.all().order_by('nome').filter(ativo=True)

    # Paginação
    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', {'contatos':contatos})


# View de exibição da lista de contatos
def show(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.ativo:
        raise Http404()
    return render(request, 'contatos/show.html', {'contato':contato})


# View para realizar buscas
def search(request):
    search_for = request.GET.get('search_for')

    if search_for is None or not search_for:
        messages.add_message(
            request,
            messages.WARNING,
            'Informe um termo para busca.'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=campos)\
    .filter(
        Q(nome_completo__icontains=search_for) | 
        Q(telefone__icontains=search_for) | 
        Q(email__icontains=search_for)
    )

    # Paginação
    paginator = Paginator(contatos, 5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/search.html', {'contatos':contatos})

