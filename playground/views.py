from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> Response
# Request handler
# Action

def say_hello(request):
    # Pull data from db and transform
    # return HttpResponse('Hello World!')
    return render(request, 
                'hello.html', 
                {'name': 'Shaswat',}
                )

def playground_home(request):
    return HttpResponse('Welcome to the playground page!')