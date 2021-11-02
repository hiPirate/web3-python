from django.http import HttpResponse
from web3.auto.infura import w3

def index(request):
    return HttpResponse(w3.isConnected())
