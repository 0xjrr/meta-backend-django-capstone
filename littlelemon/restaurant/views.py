from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.

def sayHello(request):
 return HttpResponse('Hello World')