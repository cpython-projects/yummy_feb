from .models import Contacts

def app_title(request):

    return {
        'title': 'Yummy<span>.</span>'
    }


def footer(request):
    res = Contacts.objects.first()

    return {
        'address': '',
        'reservations': res.reservations if res else '',
        'opening_hours': ''
    }
