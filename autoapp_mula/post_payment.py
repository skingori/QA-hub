import time
import requests
import json
import random


class PostPayment(object):

    ENDPOINT = "https://beep2.cellulant.com:9212/checkout/v2/checkout-proxy/CheckoutAPIRequestHandler.php"

    def __init__(self,
                 charge_amount,
                 service_code,
                 client_code,
                 country_code,
                 currency_code
                 ):

        self.ClientCode = client_code
        self.ServiceCode = service_code
        self.ChargeAmount = int(charge_amount)
        self.CountryCode = country_code
        self.CurrencyCode = currency_code

    def post_params(self):

        data = {

            "MSISDN": "254724090774",
            "accountNumber": "LJEFPH",
            "amount": "%s" % self.ChargeAmount,  # int(x=(self.Amount-30)),
            "checkoutRequestType": 5,
            "clientCode": "%s" % self.ClientCode,
            "countryCode": "%s" % self.CountryCode,
            "currencyCode": "%s" % self.CurrencyCode,
            "invoiceNumber": f"{random.randrange(200, 10000)}",
            "narration": "Simulate payment",
            "paymentMode": "mobile",
            "serviceCode": "%s" % self.ServiceCode
        }

        post = requests.post(url=self.ENDPOINT, data=json.dumps(data))

        data = json.loads(post.text)

        print(data.get('DATA')['beepTransactionID'])
        print(post.json())


Payment = PostPayment(
    charge_amount="1625480",
    service_code="ETP",
    currency_code="TZS",
    client_code="DTBTZ",
    country_code="TZ"
)

Payment.post_params()