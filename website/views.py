from django.shortcuts import render

from website.models import Gallery, Package, Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    packages = Package.objects.all()

    cards = [
        {
            'title': 'About us',
            'description': 'We consider each child’s uniqueness',
            'image': '',
            'link': '/about'
        },
        {
            'title': 'Package 3-6-9',
            'description': 'Packages aimed at youths',
            'image': '',
            'link': '/activities'
        },
        {
            'title': 'Career tips & mindfulness',
            'description': None,
            'image': '',
            'link': ''
        },
        {
            'title': 'CBT & DBT therapy',
            'description': None,
            'image': '',
            'link': ''
        },
        {
            'title': 'Parents stories',
            'description': None,
            'image': '',
            'link': ''
        },
        {
            'title': 'Referrals',
            'description': None,
            'image': '',
            'link': ''
        },
        {
            'title': 'Events and activities',
            'description': None,
            'image': '',
            'link': '/activities'
        },
        {
            'title': 'Sponsors and donate',
            'description': None,
            'image': '',
            'link': ''
        },
        {
            'title': 'Gallery',
            'description': None,
            'image': '',
            'link': '/gallery'
        },
        {
            'title': 'Contact details',
            'description': None,
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
