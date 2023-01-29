from django.shortcuts import render

from website.models import Gallery, Package, Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    packages = Package.objects.all()

    cards = [
        {
            'title': 'About us',
            'description': '',
            'image': '',
            'link': '/about'
        },
        {
            'title': 'Packages',
            'description': '',
            'image': '',
            'link': '/activities'
        },
        {
            'title': 'Career tips & mindfulness',
            'description': '',
            'image': '',
            'link': ''
        },
        {
            'title': 'CBT & DBT therapy',
            'description': '',
            'image': '',
            'link': ''
        },
        {
            'title': 'Parents stories',
            'description': '',
            'image': '',
            'link': ''
        },
        {
            'title': 'Referrals',
            'description': '',
            'image': '',
            'link': ''
        },
        {
            'title': 'Events and activities',
            'description': '',
            'image': '',
            'link': '/activities'
        },
        {
            'title': 'Sponsors and donate',
            'description': '',
            'image': '',
            'link': ''
        },
        {
            'title': 'Gallery',
            'description': '',
            'image': '',
            'link': '/gallery'
        },
        {
            'title': 'Contact details',
            'description': '',
            'image': '',
            'link': '/about'
        },
    ]

    context = {
        'services': services,
        'packages': packages,
        'link_cards': cards
    }
    return render(request, "website/index.html", context=context)


def aboutus(request):
    return render(request, "website/about-us.html")


def gallery(request):
    context = {
        'gallery': Gallery.objects.all(),
    }
    return render(request, "website/gallery.html", context=context)


def activities(request):
    packages = Package.objects.all()

    context = {
        'packages': [{
            'name': package.name,
            'image': package.image,
            'price': package.price,
            'duration': package.duration,
            'description': package.description.splitlines(),
        } for package in packages]
    }
    return render(request, "website/activities.html", context)
