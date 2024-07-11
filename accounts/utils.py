import requests
from django.conf import settings

def get_eskiz_token():
    response = requests.post('https://notify.eskiz.uz/api/auth/login', data={
        'email': settings.ESKIZ_EMAIL,
        'password': settings.ESKIZ_PASSWORD
    })
    response_data = response.json()
    if response.status_code == 200:
        return response_data['data']['token']
    else:
        raise Exception("Failed to get Eskiz token")

def send_sms(phone_number, message):
    token = get_eskiz_token()
    response = requests.post('https://notify.eskiz.uz/api/message/sms/send', headers={
        'Authorization': f'Bearer {token}'
    }, data={
        'mobile_phone': phone_number,
        'message': message,
        'from': '4546',
        'callback_url': 'http://your_callback_url'
    })
    return response.json()
