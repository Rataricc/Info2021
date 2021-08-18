from django.shortcuts import render

from .models import Amigo

# Create your views here.


def listar_amigos(request): 
	template_name="amigos/listar.html"

	lista_de_amigos = Amigo.objects.all()
	print(lista_de_amigos.query)

	ctx={
		'amigos': lista_de_amigos
	}
	return render(request, template_name, ctx)