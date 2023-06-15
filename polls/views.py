from django.shortcuts import render
#from django.template import loader
from django.http import HttpRequest,HttpResponseRedirect
from Bestiariusz import settings
import json

languages={
    "en":"en.json",
    "pl":"pl.json",
    }

# Create your views here.
def index(request):
    return HttpResponseRedirect("/strzyga/")

def strzyga(request):
    assert isinstance(request, HttpRequest)
    if request.GET.get('lang'):
        language = request.GET['lang']
    else: language = "en"
    params=json.load(open(settings.BASE_DIR+'\\polls\\lang\\'+languages[language]))
    return render(request,'strzyga.html',params)

