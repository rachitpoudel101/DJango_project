from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render (request,"generator/home.html")

def about(request):
    return render (request,"generator/about.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("upercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSRTUVWXYZ"))
    
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()_-+"))
    
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
        
        
    length = int(request.GET.get('length'))
    thepass = ""
    for x in range(length):
        thepass += random.choice(characters)
    return render (request,"generator/password.html",{'pass':thepass})