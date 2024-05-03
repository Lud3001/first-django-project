from django.shortcuts import render
from django.http import HttpResponse

def test(request):
   # return HttpResponse('<h1>Hello, world!</h1>')
   return render(request, 'main/test.html')
