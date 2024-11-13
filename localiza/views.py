from django.shortcuts import render
import requests
from django.core.paginator import Paginator

def polos(request):
   
    api_url = 'https://api-emec.vercel.app/enderecos/18751'
    response = requests.get(api_url)
    data = response.json()  


    enderecos = list(data.items())  
    paginator = Paginator(enderecos, 12)  
    page_number = request.GET.get('page')
    enderecospaginator = paginator.get_page(page_number)

    context = {

        'enderecos': enderecospaginator, 
    }
    return render(request, 'polos.html', context)
