# from django.contrib.gis.geoip2 import GeoIP2
import requests
from django.shortcuts import redirect, render
from .yandex import YandexPayment
from .wallet import WalletPayment


def view(request):
    return render(request, 'payment/payment.html', {})


def initial(request):
    ip = request.META.get('REMOTE_ADDR', None)
    url = 'http://ip-api.com/json/' + '24.48.0.1'
    resp = requests.get(url=url)
    country = resp.json().get('countryCode')
    if country != 'UKR':
        confirmation_url = YandexPayment.createOrder()
    else:
        confirmation_url = WalletPayment.createOrder()


