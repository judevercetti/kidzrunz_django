from django.shortcuts import render

from website.models import Package, Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    packages = Package.objects.all()

    context = {
        'services': services,
        'packages': packages
    }
    return render(request, "index.html", context=context)
