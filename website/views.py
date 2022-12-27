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
    return render(request, "website/index.html", context=context)


def aboutus(request):
    return render(request, "website/about-us.html")


def gallery(request):
    return render(request, "website/gallery.html")


def activities(request):
    packages = Package.objects.all()

    context = {
        'packages': packages
    }
    return render(request, "website/activities.html", context)
