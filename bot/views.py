from django.shortcuts import render
from django.http import HttpResponse
import webbrowser
import time

# Create your views here.

def home(request):
    return render(request,'home.html')

def bot(request):
    strURL = request.POST['url']
    strNo = int(request.POST['no'])
    for strNo in range(strNo):
        webbrowser.get('chrome').open(strURL, new=2)
        time.sleep(10)
    return render(request, 'home.html')

# Cerate your login here.
def index(request):
    return render(request, 'index.html')

def uin(request):
    if request.method == 'POST':
        strName = request.POST['uName']
        strPass = request.POST['uPass']
        if strName == 'mukilan' and strPass == 'ravi123':
            return render(request, 'home.html')
    else:
        return render(request, 'uin.html')

    