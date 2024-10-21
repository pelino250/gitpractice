from django.http import HttpResponse

def hello_elvis(request):
    return HttpResponse("Hello there!")