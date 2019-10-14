import uuid
import yandex_checkout
from django.shortcuts import redirect
from yandex_checkout import Configuration, Payment
from django.http import HttpResponse


class YandexPayment:

    def create_order():
        Configuration.configure('636209', 'test_n-yaQVPk9GtMB7roDJ5LeICDeLA5mBLhHutZ_SxlTJQ')
        payment = Payment.create({
            "amount": {
                "value": "100.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://www.merchant-website.com/return_url"
            },
            "capture": True,
            "description": "Заказ №1"
        }, uuid.uuid4())
        confirmation_url = payment.confirmation.confirmation_url
        return confirmation_url

