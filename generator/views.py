from django.shortcuts import render
import random
#from django.http import HttpResponse

def about(request):
    #return HttpResponse('Hello world') retorna una linea html
    return render(request,'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklopqrstuvwxyz')
    generated_password = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('-_#$!|°%&/()=?\¿¡+*{}[].,@'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length'))
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html',{'password':generated_password})
