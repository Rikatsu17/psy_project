from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'psy/index.html')
def about(request):
    return render(request, 'psy/about.html')
def services(request):
    return render(request, 'psy/services.html')
def contact(request):
    return render(request, 'psy/contact.html')