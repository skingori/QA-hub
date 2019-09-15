import csv
import urllib3
import requests
from requests.exceptions import ConnectionError
import json
from datetime import timedelta
import datetime
import base64
import hashlib
import random
import sys
from Crypto.Cipher import AES
# hoping db will work
from .models import APISettings, WebHook


class QaOperations(object):
    def __init__(self, **date):
        self.min_date = date.get('date_min')
        self.max_date = date.get('date_max')

    @staticmethod
    def _write_requests(data):
        with open("media/requests.json", "w") as write_file:
            json.dump(data, write_file)

    @staticmethod
    def get_date_now():
        today_date = datetime.datetime.utcnow()
        return today_date

    @staticmethod
    def create_future_date(days, today):
        td = timedelta(days=days)
        future_date = today + td
        return future_date

    @staticmethod
    def unix_time_millis(dt):
        epoch = datetime.datetime.utcfromtimestamp(0)
        date_mill = (dt - epoch).total_seconds()
        return int(date_mill)

    @staticmethod
    def create_req_context(payments, service_, username):
        try:
            context = ({})
            context['total_requests'] = service_['DATA']['activeRequests']['currentTotal']
            context['requests'] = service_['DATA']['activeRequests']['data'][0]['data']
            context['rejected_requests'] = service_['DATA']['rejectedRequests']['data'][0]['data']
            context['accepted_requests'] = service_['DATA']['acceptedRequests']['data'][0]['data']
            context['all_requests'] = service_['DATA']['allRequests']['data'][0]['data']
            context['expired_requests'] = service_['DATA']['expiredRequests']['data'][0]['data']
            #
            context['total_payments'] = payments['DATA']['activePayments']['currentTotal']
            context['payments'] = payments['DATA']['activePayments']['data'][0]['data']
            context['rejected_payments'] = payments['DATA']['rejectedPayments']['data'][0]['data']
            context['accepted_payments'] = payments['DATA']['acceptedPayments']['data'][0]['data']
            context['username'] = username

            return context

        except ConnectionError:
            return "Connection Error"
        except TypeError:
            return {"username": username}

    @staticmethod
    def create_all_req_context(service_code, data, request_data, service_, username):
        try:
            context = ({})
            context['checkout_requests'] = service_['DATA']['checkoutRequests']

            context['username'] = username
            context['s_code'] = service_code
            context['MSISDN'] = data['DATA']['MSISDN']
            context['request_data'] = request_data
            context['payerClients'] = service_['DATA']['metaData']['payerClients']

            return context

        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    @staticmethod
    def readfile():
        with open("/tmp/data_file.json", "r") as read_file:
            data = json.load(read_file)
            return data

    @staticmethod
    def login_auth_and_code(data):
        try:
            auth_token = data['DATA']['authorizationToken']
            service_code = QaOperations.get_service_code(data)
            auth_set = json.dumps({"auth_token": auth_token, "service_code": service_code})
            return json.loads(auth_set)
        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    @staticmethod
    def get_service_code(data):
        try:
            code = data['DATA']['serviceDetails']
            # for s_code in code:
            #     return s_code
            for key in code:
                return key
        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    @staticmethod
    def get_profile_context(data, username, service_code):

        response_data = ({})
        response_data['data'] = data['DATA']
        response_data['accessKey'] = data['DATA']['clientAccessKeys']
        response_data['clientDetails'] = data['DATA']['oauthKeyDetails']
        response_data['serviceDetails'] = data['DATA']['serviceDetails']
        response_data['clientCode'] = data['DATA']['clientCode']
        response_data['firstName'] = data['DATA']['firstName']
        response_data['lastName'] = data['DATA']['lastName']
        response_data['serviceCode'] = service_code
        response_data['clientName'] = data['DATA']['clientName']
        response_data['username'] = username

        return response_data

    @staticmethod
    def create_payment_context(payments, username):
        context = ({})
        context['username'] = username
        context['payments'] = payments['DATA']['payments']
        context['payerClients'] = payments['DATA']['metaData']['payerClients']

        return context

    def get_checkout_requests(self, _port, _service_code, _token):
        try:
            header = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {_token}'
            }
            data = {"serviceCode": f"{_service_code}",
                    "date": {
                        "type": "dateBetween",
                        "min": self.min_date,  # 1561906314
                        "max": self.max_date  # 1562597513
                    }
                    }
            get_request_url = APISettings.objects.get(unique_name="fetchCheckoutRequests")
            url = f"{get_request_url.url+':'+_port}"
            path = f"{get_request_url.path}"
            response = requests.post(url=f"{url + path}", data=json.dumps(data), headers=header)

            all_req_response = json.loads(response.text)
            # QaOperations._write_requests(all_req_response)
            return all_req_response

        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    def create_requests(self, _port, _service_code, _token):
        try:
            header = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {_token}'
            }
            data = {"serviceCode": f"{_service_code}",
                    "date": {
                        "type": "dateBetween",
                        "min": self.min_date,  # 1561906314
                        "max": self.max_date  # 1562597513
                    }
                    }
            requests_totals = APISettings.objects.get(unique_name="fetchCheckoutRequestTotals")
            url = f"{requests_totals.url+':'+_port}"
            path = f"{requests_totals.path}"
            response = requests.post(url=f"{url + path}", data=json.dumps(data), headers=header)

            req_response = json.loads(response.text)
            # self._write_requests(req_response)
            return req_response

        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    def create_payments(self, _port, _service_code, _token):
        try:
            content_type = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {_token}'
            }
            data = {"serviceCode": f"{_service_code}",
                    "date": {
                        "type": "dateBetween",
                        "min": self.min_date,  # 1561906314
                        "max": self.max_date  # 1562597513
                    }
                    }
            payments_totals = APISettings.objects.get(unique_name="fetchPaymentTotals")
            url = f"{payments_totals.url + ':' + _port}"
            path = f"{payments_totals.path}"

            response = requests.post(
                url=f"{url + path}", data=json.dumps(data), headers=content_type)

            pay_response = json.loads(response.text)
            # self._write_requests(pay_response)
            return pay_response

        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    def fetch_payments(self, _port, _service_code, _token):
        try:
            header = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {_token}'
            }
            data = {"serviceCode": f"{_service_code}",
                    "date": {
                        "type": "dateBetween",
                        "min": self.min_date,  # 1561906314
                        "max": self.max_date  # 1562597513
                    }
                    }

            fetchPayments = APISettings.objects.get(unique_name="fetchPayments")
            endpoint = f"{fetchPayments.url + ':' + _port}"
            path = f"{fetchPayments.path}"
            response = requests.post(
                url=f"{endpoint + path}", data=json.dumps(data), headers=header)

            all_payments = json.loads(response.text)
            self._write_requests(all_payments)
            return all_payments

        except KeyError:
            raise KeyError('Json Error')
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    @staticmethod
    def simulate_payment(account, amount, msisdn, s_code, client_data, currency, name, port):
        try:
            header = {
                'Content-Type': 'application/json',
            }

            # TODO : Converting json to string
            country = json.loads(client_data).get('country')
            clientCode = json.loads(client_data).get('clientCode')

            data = {
                "countryCode": f"{country}",
                "accountNumber": f"{account}",
                "customerName": f"{name}",
                "MSISDN": f"{msisdn}",
                "chargeAmount": f"{amount}",
                "currencyCode": f"{currency}",
                "serviceCode": f"{s_code}",
                "narration": f"Simulated payment by {name}",
                "payerClientCode": f"{clientCode}"
            }

            simulate_payment = APISettings.objects.get(unique_name="simulatePayment")
            endpoint = f"{simulate_payment.url+':'+port}"
            path = f"{simulate_payment.path}"

            simulate = requests.post(url=endpoint+path, data=json.dumps(data), headers=header)

            return json.loads(simulate.text)

        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError, __name__)
        except ConnectionError:
            print(ConnectionError, __name__)
        except Exception as error:
            print(error)

    @staticmethod
    def login(_port, username, password):
        try:

            data = {
                "emailAddress": f"{username}",
                "password": f"{password}"
            }
            header = {
                'Content-Type': 'application/json',
            }
            login = APISettings.objects.get(unique_name="login")
            end_point = f"{login.url+':'+_port}"
            path = f"{login.path}"
            response = requests.post(url=f"{end_point+path}", headers=header, data=json.dumps(data))
            compare = json.loads(response.text)
            return compare

        except KeyError:
            print(KeyError, __name__)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError)
        except ConnectionError:
            print(ConnectionError)
        except Exception as error:
            print(error)

    @staticmethod
    def create_encryption(
            msisdn,
            email,
            amount,
            currency,
            s_code,
            minutes,
            access_key,
            payer_client,
            country_code
    ):
        get_webHook = WebHook.objects.get(status=1)
        now = datetime.datetime.utcnow()
        me = now + datetime.timedelta(days=0, hours=0, minutes=int(minutes), seconds=0)

        date = (me.strftime("%Y-%m-%d %H:%M:%S"))
        try:

            params = {
                "merchantTransactionID": random.randint(0, sys.maxunicode),
                "customerFirstName": "QA",
                "customerLastName": "Testing App",
                "MSISDN": f"{msisdn}",
                "customerEmail": f"{email}",
                "amount": f"{amount}",
                "currencyCode": f"{currency}",
                "accountNumber": random.randint(100, sys.maxunicode),
                "serviceCode": f"{s_code}",
                "dueDate": f"{date}",
                "serviceDescription": "Testing through QA test system",
                "accessKey": f"{access_key}",
                "countryCode": f"{country_code}",
                "payerClientCode": payer_client,
                "languageCode": "en",
                "successRedirectUrl": "",
                "failRedirectUrl": "",
                "paymentWebhookUrl": f"{get_webHook.url}"
            }

            return json.dumps(params)

        except KeyError:
            print(KeyError)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print(ValueError)
        except ConnectionResetError:
            print(ConnectionResetError)
        except ConnectionError:
            print(ConnectionError)
        except Exception as error:
            print(error)


class QaServices(object):

    def __init__(self, qa_test_case,
                 section_id,
                 pre_conditions,
                 steps,
                 custom_expected,
                 big_data):

        self.test_case = qa_test_case
        self.section = section_id
        self.condition = pre_conditions
        self.steps = steps
        self.expected = custom_expected
        self.data = big_data

    def add_cases_(self):

        f = open("media/data.txt", "w+")
        f.write(f"{self.data.replace(' ', '')}")

        f.close()

        return self._process_txt()

    def _process_txt(self):
        try:
            with open('media/data.txt') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    for i in row:
                        urllib3.disable_warnings()
                        username = ""
                        password = ""

                        data = {
                            'Content-Type': 'application/json',
                            'User-Agent': 'TestRail API v: 2'
                        }
                        # TODO : Change test case
                        if i is not "" or None:
                            set_ = {
                                "title": f"{self.test_case.replace('*case*', i)}",
                                "name": f"{self.test_case.replace('*case*', i)}",
                                "custom_preconds": f"{self.condition}",
                                "custom_steps": f"{self.steps}",
                                "custom_expected": f"{self.expected}"
                            }
                            payload = bytes(json.dumps(set_), 'utf-8')
                            uri_add = f"/index.php?/api/v2/add_case/{self.section}"
                            # This url will be used to get the cases
                            # uri_get = f"/index.php?/api/v2/get_cases/{82}&suite_id={322}&section_id={6238}"
                            post = requests.post(url=f"https://41.84.155.54:9401/testrail{uri_add}",
                                                 auth=(username, password), headers=data, data=payload, verify=False)
                            if post.status_code is not 200:
                                return json.loads(post.text).get("error", "null")
                            else:
                                pass
                        else:
                            pass

        except KeyError as error:
            # Output expected KeyErrors.
            return error
        except ConnectionError:
            return False
        except Exception as exception:
            # Output unexpected Exceptions.
            return exception, False

    @staticmethod
    def get_user_profile_and_keys(data):

        keys_values = data['DATA']['clientAccessKeys']

        for key, value in keys_values.items():
            iv_key = value['ivKey']
            access_key = key
            secret_key = value['secretKey']

            keys = json.dumps({"accessKey": access_key, "iv_key": iv_key, "secret_key": secret_key})

            return json.loads(keys)


class Encryption(object):

    def __init__(self, key, iv_):
        self.byte_string = 16
        self.key = hashlib.sha256(key.encode()).hexdigest()[:32]
        self.iv = hashlib.sha256(iv_.encode()).hexdigest()[:16]

    def encrypt(self, raw):
        """
        Encrypt passed json data with the secret key,iv key.
        """
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, self.iv.encode('utf-8'))
        crypt = cipher.encrypt(self._pad(raw).encode())
        return base64.b64encode(base64.b64encode(crypt)).decode('utf-8')

    def decrypt(self, enc):
        """
        Decrypt the params encrypted from the the encrypt method with secret key and iv key
        """
        decrypt_cypher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, self.iv.encode('utf-8'))
        enc = base64.b64decode(base64.b64decode(enc))
        string = decrypt_cypher.decrypt(enc)

        return self._un_pad(string.decode('utf-8'))

    def _pad(self, s):
        return s + (self.byte_string - len(s) % self.byte_string) * chr(self.byte_string - len(s) % self.byte_string)

    @staticmethod
    def _un_pad(s):
        return s[:-ord(s[len(s) - 1:])]
