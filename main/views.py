from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Docker Django World!<br>Docker is a life saver :)")