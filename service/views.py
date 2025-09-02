from django.shortcuts import render

def service(request):
    return render(request, "hero/services.html")