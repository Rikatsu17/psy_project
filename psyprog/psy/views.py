from django.shortcuts import render

# Create your views here.
menu = [{'title': 'home', 'url_name': 'home'},
        {'title': 'about', 'url_name': 'about'},
        {'title': 'services', 'url_name': 'services'},
        {'title': 'contact', 'url_name': 'contact'},]
def index(request):
    return render(request, 'psy/index.html')
def about(request):
    return render(request, 'psy/about.html')
def services(request):
    return render(request, 'psy/services.html')
def contact(request):
    return render(request, 'psy/contact.html')