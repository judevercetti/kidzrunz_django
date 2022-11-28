from django.shortcuts import render

from website.models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()[:4]

    context = {
        'services': services
    }
    return render(request, "index.html", context=context)
