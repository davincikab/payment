from datetime import datetime
import json
import base64
import requests
from requests.auth import HTTPBasicAuth

app_name = "Tax assistant"
app_name = "Lipa Tax"

class MpesaC2BCredentials:
    consumer_key = 'wiWhFtX8T2beTsfAsAAsfG8xi8QPfcM6'
    consumer_secret = 'mJhVv2JHG84SnSv4'
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

# get access token and authentication
class MpesaAccessToken:
    req = requests.get(
        MpesaC2BCredentials.api_URL,
        auth = HTTPBasicAuth(MpesaC2BCredentials.consumer_key, MpesaC2BCredentials.consumer_secret)
    )

    # return the access token
    try:
        json_response = json.loads(req.text)
    except json.decoder.JSONDecodeError:
        json_response = {'access_token':''}
    validated_access_token = json_response['access_token']

# lipa na mpesa
class LipaNaMpesa:
    BusinessShortCode = "174379"
    c2bShortCode = "600610"
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    passKey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

    password_text = BusinessShortCode + passKey + timestamp
    online_password = base64.b64encode(password_text.encode())
    decode_password = online_password.decode('utf-8')

    
