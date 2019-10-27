import sys
from tingg.adapters import TinggAdapter
import random



def get_response():
    init = TinggAdapter(iv_key="h3tckgMNbmj8VP4R", secret_key="Nm6GxzKhPVwn84vq", access_key="$2a$08$wQ2PLnHf6vTFY0KMGN5iFuSCXUwy1iQe.8T/TLK0.4hml45m4sDJy", service_code="INSDEV7654", domain="SANDBOX")

    response = init.get_encryption(msisdn='0724090774',
                                customer_first_name='John',
                                customer_last_name='Doeh',
                                customer_email='john.doeh@jd.com',
                                transaction_id=random.randint(0, sys.maxunicode),
                                account_number='066564ACC',
                                amount=1000,
                                currency_code='UGX',
                                country_code='UG',
                                description='Air ticket',
                                checkout_type="express",
                                due_date=30,
                                payer_client_code='',
                                language_code='en',
                                success_url='http://callbackurl.com/success',
                                fail_url='http://callbackurl.com/fail',
                                callback_url='http://callbackurl.com/callback'
                                )
    print(response)
    return response
    
