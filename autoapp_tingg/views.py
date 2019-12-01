from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views import generic
#
from django.urls import reverse_lazy
from rest_framework.parsers import JSONParser

from .forms import RegistrationForm, LoginForm, TestForm, SimulateForm, SimulateJsonForm, SimulatePayment, \
    RefundJsonForm, CancelForm
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
# import db
from .models import APISettings, WebHook, UISettings, EnvironmentPorts
# end import db
import json
from django.http import JsonResponse
from django.utils.translation import gettext as _
import logging
#
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .services import QaServices, QaOperations, Encryption
from .serializers import CheckoutCallSerial, ResponseCallSerial, SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers

# create logger
appLogger = logging.getLogger('app-logger')


@method_decorator(never_cache, name='dispatch')
class HomeView(View):
    template_name = 'registration/login.html'

    @staticmethod
    def get(request, *args, **kwargs):
        try:
            if request.session['username'] and request.session['session_code'] and request.session['port']:
                # if request.session['username']:
                # get the service code
                username = request.session['username']
                data = request.session['data']
                port = request.session['port']

                future_date = QaOperations.create_future_date(
                    days=-15, today=QaOperations.get_date_now())

                date_min_to_sec = QaOperations.unix_time_millis(future_date)
                date_max_to_sec = QaOperations.unix_time_millis(
                    QaOperations.get_date_now())
                auth_token = QaOperations.login_auth_and_code(data)[
                    'auth_token']

                service_code = request.session['session_code']
                create_req = QaOperations.create_requests(QaOperations(
                    date_max=date_max_to_sec, date_min=date_min_to_sec), _service_code=service_code, _token=auth_token,
                    _port=port)
                payments = QaOperations.fetch_payment_totals(QaOperations(
                    date_max=date_max_to_sec, date_min=date_min_to_sec), _service_code=service_code, _token=auth_token,
                    _port=port)

                success = create_req['SUCCESS']
                stat_code = create_req['STATCODE']

                first_name = data['DATA']['firstName']
                last_name = data['DATA']['lastName']

                if success is True and stat_code == 1:

                    requests = QaOperations.create_req_context(
                        payments, create_req, username, first_name, last_name)

                    return render(request, 'home/home.html', context=requests)
                else:
                    return HttpResponseRedirect(reverse_lazy('main_app:logout'))
            else:
                return HttpResponseRedirect(reverse_lazy('main_app:logout'))
        except KeyError:
            return HttpResponseRedirect(reverse_lazy('main_app:logout'))
        except ValueError:
            return HttpResponseRedirect(reverse_lazy('main_app:logout'))
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect(reverse_lazy('main_app:logout'))


@method_decorator(never_cache, name='dispatch')
class SetDefaultCode(generic.CreateView):

    def get(self, request, *args, **kwargs):
        code = kwargs.get("pk")
        try:
            del request.session['session_code']
            request.session['session_code'] = code
            return HttpResponseRedirect('/profile/')
        except KeyError:
            print(KeyError)
            return HttpResponseRedirect('/profile/')
        except TypeError:
            print(TypeError)
            return HttpResponseRedirect('/profile/')
        except Exception as error:
            print(error)
            return HttpResponseRedirect('/profile/')

    HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class ProfileView(generic.CreateView):
    template_name = 'home/user_profile.html'

    def get(self, request, *args, **kwargs):
        try:
            if request.session['username'] and request.session['session_code'] and request.session['port']:
                username = request.session['username']
                data = request.session['data']
                service_code = request.session['session_code']
                response_data = QaOperations.get_profile_context(data=data, username=username,
                                                                 service_code=service_code)

                return render(request, self.template_name, response_data)
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError, __name__)
        except ConnectionResetError:
            print(ConnectionResetError)
        except ConnectionError:
            print(ConnectionError)
        except Exception as error:
            print(error)
        return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class Login(generic.TemplateView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('/login/')
    template_name = 'registration/register.html'


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class Checkout(generic.TemplateView):
    template_name = 'home/create_checkout.html'

    @staticmethod
    def post(request, *args, **kwargs):
        return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        try:
            if request.session['username'] and request.session['session_code'] and request.session['port']:
                # get the service code
                username = request.session['username']
                data = request.session['data']
                port = request.session['port']

                auth_token = QaOperations.login_auth_and_code(data)[
                    'auth_token']

                service_code = request.session['session_code']
                service = QaOperations.get_checkout_requests(QaOperations(**kwargs),
                                                             _service_code=service_code, _token=auth_token, _port=port)

                success = service['SUCCESS']
                stat_code = service['STATCODE']
                # db = get_list_or_404(UISettings)
                # queryset = serializers.serialize('json', UISettings.objects.all())
                queryset = get_list_or_404(UISettings)

                if success is True and stat_code == 1:
                    requests = QaOperations.create_all_req_context(service_code=service_code,
                                                                   request_data=queryset, data=data,
                                                                   service_=service, username=username)

                    return render(request, self.template_name, context=requests)
                elif "Token has expired" in service.get("REASON"):
                    return HttpResponseRedirect('/logout/')
                else:
                    reason = service.get("REASON")
                    return render(request, self.template_name, context={"message": reason, "username": username})
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class DisplayTests(View):
    template_name = 'home/create_test.html'

    def get(self, request):
        try:
            if request.session['username']:
                username = request.session['username']
                return render(request, self.template_name, {'username': username})
            else:
                return render(request, 'registration/login.html', {})
        except KeyError:
            pass
        except json.decoder.JSONDecodeError:
            pass

        return render(request, 'registration/login.html', {})


class Logout(View):
    template_name = 'registration/login.html'

    def get(self, request):
        try:
            del request.session['username']
            del request.session['data']
            del request.session['port']
        except KeyError:
            print(KeyError)
        except TypeError:
            print(TypeError)
        except Exception as error:
            print(error)
        # return render(request, self.template_name, {"message": 'Logged Out Successfully'})
        return render(request, self.template_name, {"message": ''})


@method_decorator(never_cache, name='dispatch')
class MakeLogin(generic.TemplateView):
    form_class = LoginForm
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):

        return HttpResponseRedirect('/logout/')
        # try:
        #     del request.session['username']
        #     del request.session['data']
        #     del request.session['port']
        # except KeyError:
        #     pass
        # return render(request, self.template_name, {"message": 'Logged Out Successfully'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = request.POST.get("password")
            # environment = request.POST.get("environment", '9001')
            environment = request.POST.get("environment", '') == "on"

            try:
                if environment is True:
                    sandbox_port = get_object_or_404(EnvironmentPorts,
                                                     unique_name="sandbox")
                    request.session['port'] = sandbox_port.port
                elif environment is False:
                    staging_port = get_object_or_404(EnvironmentPorts,
                                                     unique_name="staging")
                    request.session['port'] = staging_port.port
                else:
                    raise TypeError

                port = request.session['port']
                compare = QaOperations.login(
                    username=username, password=password, _port=port)
                # "SUCCESS": false,
                # "DATA": null,
                # "REASON": "Authentication failed",
                # "STATCODE": 0
                success = compare['SUCCESS']
                stat_code = compare['STATCODE']
                reason = compare['REASON']

                if success is True and stat_code == 1:

                    request.session['username'] = username
                    data = request.session['data'] = compare

                    future_date = QaOperations.create_future_date(
                        days=-15, today=QaOperations.get_date_now())
                    date_min = QaOperations.unix_time_millis(future_date)
                    date_max = QaOperations.unix_time_millis(
                        QaOperations.get_date_now())
                    auth_token = QaOperations.login_auth_and_code(data)[
                        'auth_token']
                    service_code = QaOperations.login_auth_and_code(data)[
                        'service_code']
                    request.session['session_code'] = service_code
                    first_name = data['DATA']['firstName']
                    last_name = data['DATA']['lastName']
                    create_req = QaOperations.create_requests(QaOperations(
                        date_max=date_max, date_min=date_min), _service_code=service_code, _token=auth_token,
                        _port=port)
                    payments = QaOperations.fetch_payment_totals(QaOperations(
                        date_max=date_max, date_min=date_min), _service_code=service_code,
                        _token=auth_token, _port=port)
                    context = QaOperations.create_req_context(
                        payments, create_req, username, first_name, last_name)
                    return render(request, 'home/home.html', context=context)
                elif success is False and stat_code == 0:
                    return render(request, self.template_name, {"message": reason})
                else:
                    return render(request, self.template_name, {"message": reason})

            except KeyError:
                return render(request, self.template_name, {"message": KeyError})
            except ConnectionResetError:
                return render(request, self.template_name, {"message": ConnectionResetError})
            except ConnectionError:
                return render(request, self.template_name, {"message": ConnectionError})
            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                return render(request, self.template_name, {"message": ValueError})
            except TypeError:
                message = _("Oopsie!, we've got a problem!")
                return render(request, self.template_name, {"message": message})
        else:
            message = self.form_class(request.POST)
            return render(request, 'registration/login.html', {'message': message})


@method_decorator(never_cache, name='dispatch')
class TestCreate(TemplateView):
    form_class = TestForm
    template_name = 'home/create_test.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            qa_test_case = form.cleaned_data.get("qa_test_case")
            section_id = form.cleaned_data.get("section_id")
            pre_conditions = request.POST.get("pre_conditions")
            steps = request.POST.get("steps")
            expected_result = request.POST.get("expected_result")
            big_data = request.POST.get("big_data")

            username = request.session['username']
            response = QaServices(
                qa_test_case,
                section_id,
                pre_conditions,
                steps,
                expected_result,
                big_data).add_cases_()
            return render(request, self.template_name, context={"message": response, "username": username})

        else:
            try:
                username = request.session['username']
                return render(request, self.template_name, {'form': form, 'username': username})
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

        return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class CreateKeyView(TemplateView):
    template_name = 'user_keys/user_keys.html'

    def get(self, request, *args, **kwargs):
        if request.session['username'] and request.session['session_code'] and request.session['port']:
            username = request.session['username']
            data = request.session['data']
            code = request.session['session_code']

            response = QaOperations.get_profile_context(
                data=data, username=username, service_code=code)
            return render(request, self.template_name, response, status=status.HTTP_200_OK)
        else:
            return HttpResponseRedirect('/logout/')

    success_url = reverse_lazy('/')


@method_decorator(never_cache, name='dispatch')
class SimulateTest(TemplateView):
    form_class = SimulateForm

    def post(self, request):
        try:
            form = self.form_class(request.POST)
            if form.is_valid() and request.session['username']:
                # <process form cleaned data>
                msisdn = request.POST.get("msisdn")
                amount = request.POST.get("amount")
                country = request.POST.get("country")
                currency = form.cleaned_data.get("currency")
                minutes = form.cleaned_data.get("timer")
                experience = request.POST.get("experience")
                payer_client = request.POST.get("payer_client")
                s_code = request.session['session_code']
                username = request.session['username']
                data = request.session['data']
                port = request.session['port']

                iv_key = QaServices.get_user_profile_and_keys(data)["iv_key"]
                secret_key = QaServices.get_user_profile_and_keys(data)[
                    "secret_key"]
                access_key = QaServices.get_user_profile_and_keys(data)[
                    "accessKey"]
                encrypted_params = Encryption(iv_=iv_key, key=secret_key).encrypt(QaOperations.create_encryption(
                    msisdn=msisdn,
                    email=username,
                    amount=amount,
                    currency=currency,
                    s_code=s_code,
                    minutes=minutes,
                    access_key=access_key,
                    country_code=country,
                    payer_client=payer_client))
                return HttpResponseRedirect(
                    f"https://beep2.cellulant.com:{port}/checkout/v2/{experience}"
                    f"/?params={encrypted_params}&accessKey={access_key}&countryCode={country}")
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class SimulateJson(View):
    form_class = SimulateJsonForm

    def post(self, request):
        try:
            form = self.form_class(request.POST)
            if form.is_valid() and request.session['username']:

                # <process form cleaned data>
                json_data = request.POST.get("json_data")
                data_to_json = json.loads(json_data)
                country = data_to_json.get('countryCode')
                data = request.session['data']
                port = request.session['port']

                experience = "express"
                iv_key = QaServices.get_user_profile_and_keys(data)["iv_key"]
                secret_key = QaServices.get_user_profile_and_keys(data)[
                    "secret_key"]
                access_key = QaServices.get_user_profile_and_keys(data)[
                    "accessKey"]
                encrypted_params = Encryption(
                    iv_=iv_key, key=secret_key).encrypt(json_data)
                url = f"https://beep2.cellulant.com:{port}/checkout/v2/{experience}/?params={encrypted_params}&accessKey={access_key}&countryCode={country}"
                redirect = {
                    "redirect_url": url
                }

                return JsonResponse(redirect)
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class Refunds(generic.TemplateView):
    template_name = 'home/refunds.html'
    form_class = RefundJsonForm

    def get(self, request, *args, **kwargs):
        try:
            if request.session['username']:
                merchant_transaction = kwargs.get("merchant_id")
                checkout_request_id = kwargs.get("checkout_id")
                amount = kwargs.get("amount")
                data = request.session["data"]
                port = request.session["port"]
                client_keys = QaOperations.get_client_keys(data)
                get_token = QaOperations.get_oauth_token(
                    client_keys=client_keys, _port=port)
                token = get_token.json().get("access_token")
                username = request.session['username']
                response = {"username": username, "merchantTransactionID": merchant_transaction,
                            "checkoutRequestID": checkout_request_id, "refundAmount": amount, "token": token}

                return render(request, self.template_name, context=response, status=status.HTTP_200_OK)
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            return HttpResponseRedirect('/')
        except ValueError:
            return HttpResponseRedirect('/')
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/')

    def post(self, request):
        try:
            form = self.form_class(request.POST)
            if form.is_valid() and request.session['username']:
                # <process form cleaned data>
                refund_data = request.POST.get("refund")
                cleaned_data = json.loads(refund_data)
                data = request.session["data"]
                port = request.session["port"]
                client_keys = QaOperations.get_client_keys(data)
                get_token = QaOperations.get_oauth_token(
                    client_keys=client_keys, _port=port)
                if get_token.status_code == 200:
                    token = get_token.json().get("access_token")
                    initiate_refund = QaOperations.initiate_refund(
                        data=cleaned_data, token=token, _port=port)
                    return HttpResponse(initiate_refund,
                                        content_type="application/json", status=status.HTTP_200_OK
                                        )
                else:
                    return HttpResponse(json.loads(get_token.json()),
                                        content_type="application/json", status=status.HTTP_200_OK
                                        )
        except KeyError:
            return HttpResponseRedirect('/')
        except ValueError:
            return HttpResponseRedirect('/')
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class CancelRequest(generic.TemplateView):
    template_name = 'home/cancel_request.html'
    form_class = CancelForm

    def get(self, request, *args, **kwargs):
        try:
            if request.session['username']:
                merchant_transaction = kwargs.get("merchant_id")
                checkout_request_id = kwargs.get("checkout_id")
                port = request.session["port"]
                data = request.session["data"]
                s_code = request.session['session_code']
                client_keys = QaOperations.get_client_keys(data)
                get_token = QaOperations.get_oauth_token(
                    client_keys=client_keys, _port=port)
                token = get_token.json().get("access_token")
                username = request.session['username']
                response = {"username": username, "merchantTransactionID": merchant_transaction,
                            "checkoutRequestID": checkout_request_id, "serviceCode": s_code, "token": token}
                return render(request, self.template_name, context=response, status=status.HTTP_200_OK)
            else:
                return HttpResponseRedirect('/')
        except KeyError:
            return HttpResponseRedirect('/')
        except ValueError:
            return HttpResponseRedirect('/')

    def post(self, request):
        try:
            form = self.form_class(request.POST)
            if form.is_valid() and request.session['username']:
                # <process form cleaned data>
                cancel_response = request.POST.get("cancel")
                cleaned_data = json.loads(cancel_response)
                # s_code = request.session['session_code']
                # username = request.session['username']
                port = request.session['port']
                data = request.session['data']
                get_token = QaOperations.get_oauth_token(
                    client_keys=QaOperations.get_client_keys(data), _port=port)
                if get_token.status_code == 200:
                    token = get_token.json().get("access_token")
                    initiate_refund = QaOperations.cancel_request(
                        data=cleaned_data, token=token, _port=port)
                    return HttpResponse(initiate_refund,
                                        content_type="application/json", status=status.HTTP_200_OK
                                        )
                else:
                    return HttpResponse(
                        json.dumps({"nothing to see": "this isn't happening"}),
                        content_type="application/json", status=status.HTTP_400_BAD_REQUEST
                    )

        except KeyError:
            return HttpResponseRedirect('/')
        except ValueError:
            return HttpResponseRedirect('/')
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/')


@method_decorator(never_cache, name='dispatch')
class SimulatePay(View):
    form_class = SimulatePayment

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and request.session["username"]:
            amount = form.cleaned_data.get('amount')
            account_number = form.cleaned_data.get('account_number')
            msisdn = form.cleaned_data.get('msisdn')
            payerClient = request.POST.get('payerClient')
            currency = request.POST.get('currency')

            # Data to get name
            s_code = request.session['session_code']
            username = request.session['username']
            data = request.session['data']
            port = request.session['port']

            user_data = QaOperations.get_profile_context(
                data=data, username=username, service_code=s_code)

            name = f"{user_data.get('firstName') + ' ' + user_data.get('lastName')}"
            response = QaOperations.simulate_payment(account=account_number, msisdn=msisdn, s_code=s_code,
                                                     client_data=payerClient, amount=amount, currency=currency,
                                                     name=name, port=port)
            return HttpResponse(
                json.dumps(response),
                content_type="application/json", status=status.HTTP_200_OK
            )

        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json", status=status.HTTP_400_BAD_REQUEST
            )


class AllPayments(View):
    template_name = "home/payments.html"

    @classmethod
    def get(cls, request):
        try:
            port = request.session['port']
            service_code = request.session['session_code']
            data = request.session['data']
            username = request.session['username']
            token = QaOperations.login_auth_and_code(data)['auth_token']
            payment_response = QaOperations().fetch_payments(
                _port=port, _service_code=service_code, _token=token)
            context = QaOperations.create_payment_context(
                payment_response, username)
            return render(request, template_name=cls.template_name, context=context)
        except KeyError:
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/')


class GetStatusCodes(View):
    template_name = "home/status_codes.html"

    def get(self, request):
        try:
            file_path = "media/requests_all.json"
            data = QaOperations.read_any_file(file_path)
            if "Token has expired" in data.get("REASON"):
                return HttpResponseRedirect('/checkout/')
            else:
                username = request.session['username']
                context = QaOperations.create_status_codes_context(data=data, username=username)
                return render(request, template_name=self.template_name, context=context)
        except ValueError:
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')
        except Exception as error:
            print(error)
            return HttpResponseRedirect(reverse_lazy('main_app:home'))


class GetEndpointsList(ListView):
    template_name = 'home/api_endpoints.html'
    model = APISettings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session['username']
        return context


class APICallBack(APIView):
    @staticmethod
    def post(request):
        serializer = CheckoutCallSerial(data=request.data)
        if serializer.is_valid():
            db = get_object_or_404(WebHook, status=1)
            merchant_id = request.data.get('merchantTransactionID')
            checkout_id = request.data.get('checkoutRequestID')

            call_response = {
                "merchantTransactionID": f"{merchant_id}",
                "checkoutRequestID": f"{checkout_id}",
                "receiptNumber": f"{merchant_id}",
                "statusCode": db.status_code,
                "statusDescription": f"{db.description}"
            }
            appLogger.debug("WEB_HOOK REQUEST:" + str(request.data))
            results = ResponseCallSerial(call_response, many=False)
            appLogger.debug("WEB_HOOK RESPONSE: " + str(results.data))
            return Response(data=results.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpenAPI(APIView):
    """
    This class accepts all the requests
    """
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            appLogger.debug("OPEN API REQUEST:" + str(request.data))
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
