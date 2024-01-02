from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from django.contrib import messages
def home(request):
    return render(request,'index.html')

def searchword(request):
    
    if request.method=='GET':

        word=request.GET.get('searchbox')
        
        app_id  = "b69d484e"
        app_key  = "Your Oxford Dictionary API Key"
        endpoint = "entries"
        language_code = "en-us"
        word_id = word
        
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
        r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
        
        print(r.status_code)
        if r.status_code!=200:
            return render(request,'index.html',{'error':r.text})
        res=(r.json())
        
        examples=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
        
        etymologies=res['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies']
        definitions=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
        idxarr=['Etymology: ','Definition ','Example ']
        arr=[etymologies,definitions,examples]
        # print(arr['results']['lexicalEntries']['entries'])
        return render(request,'index.html',{'arr':arr,'word':word_id.lower()})

# Create your views here.
