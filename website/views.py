from django.shortcuts import render

from website.models import Gallery, Package, Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    packages = Package.objects.all()

    cards = [
        {
            'title': 'About us',
            'description': 'Welcome to KidzRunz!',
            'image': '',
            'link': '/about'
        },
        {
            'title': 'Mentoring Activate Packages',
            'description': 'Packages aimed at youths',
            'image': '',
            'link': '/activities'
        },
        {
            'title': 'Director\'s Story',
            'description': 'Meet Kenneth Holder',
            'image': '',
            'link': '/leadership'
        },
        {
            'title': 'Our services',
            'description': 'Included but not limited to',
            'image': '',
            'link': '/services'
        },
        {
            'title': 'Mission and Ethos',
            'description': 'To give back to the community',
            'image': '',
            'link': '/mission'
        },
        {
            'title': 'Terms and Conditions',
            'description': None,
            'image': '',
            'link': '/terms-and-conditions'
        },
        {
            'title': 'Safeguarding and Enhanced DBS',
            'description': None,
            'image': '',
            'link': '/safeguarding-and-enhanced-dbs'
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
            'title': 'Who CAMS are',
            'description': 'Child Activity Mentor Support (CAMS)',
            'image': '',
            'link': '/who-cams-are'
        },
        {
            'title': 'Mindfulness approach',
            'description': 'We take a mindfulness approach',
            'image': '',
            'link': '/mindfulness-approach'
        },
        {
            'title': 'CAMS PACE APPROACH',
            'description': 'Creating a safe and nurturing environment',
            'image': '',
            'link': '/cams-pace-approach'
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


def contactus(request):
    return render(request, "website/contact-us.html")


def consultation(request):
    return render(request, "website/consultation.html")


def leadership(request):
    return render(request, "website/leadership.html")


def mission(request):
    return render(request, "website/mission.html")


def services(request):
    return render(request, "website/services.html")


def termsandconditions(request):
    return render(request, "website/terms-and-conditions.html")


def safeguardingandenhanceddbs(request):
    return render(request, "website/safeguarding-and-enhanced-dbs.html")


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


def who_cams_are(request):
    return render(request, "website/who-cams-are.html")


def mindfuless_approach(request):
    return render(request, "website/mindfulness-approach.html")


def cams_pace_approach(request):
    return render(request, "website/cams-pace-approach.html")
