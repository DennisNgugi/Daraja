import requests

from datetime import datetime
from access_token import generate_access_token
from encode import generate_password
import keys


formatted_time = datetime.now().strftime('%Y%m%d%H%M%S')
# print(formatted_time)

decode_password = generate_password(formatted_time)

my_access_token = generate_access_token()


def lipa_na_mpesa():

    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": decode_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA":  keys.phone_number,
        "PartyB":  keys.business_shortcode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": " 123456 ",
        "TransactionDesc": "Pay School Fess "
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
