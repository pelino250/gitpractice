from django.http import HttpResponse

def hello_mau(request):
    return HttpResponse("Welcome to Maureen's Django App!")

