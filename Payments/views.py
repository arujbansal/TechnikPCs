from django.shortcuts import render
from PayTM import Checksum
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


# Create your views here.
def make_payment(request):
    now = datetime.now()
    current_time = now.strftime("%H%M%S")

    MERCHANT_KEY = 'bQfzzkKzeCbR7jOl'
    param_dict = {
        'MID': 'amitgo59443067266036',
        'ORDER_ID': str(current_time),  # order id
        'TXN_AMOUNT': str(1000),  # amount demanded for.
        'CUST_ID': "abcd@gmail.com",
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'STAGING',  # for demo purpose only.
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'https://5a73a80b.ngrok.io/payment_check/'
        # on this url paytm will send you the status of request
    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request, 'Payments/make_payment.html', {'data': param_dict})


@csrf_exempt
def payment_notification(request):
    data = dict()
    for k, v in request.POST.items():
        data.setdefault(k, v)
    return render(request, 'Payments/payment_check.html', data)
