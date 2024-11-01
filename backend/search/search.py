import base64
import logging

tbank_image_path = 'mock_images/tbank.jpg'
ya_pay_image_path = 'mock_images/ya_pay.jpg'

def get_base64_encoded_image(file_name: str) -> bytes:
    with open(file_name, 'rb') as fin:
        return base64.b64encode(fin.read())

def mock_search():
    base64_tbank_image = get_base64_encoded_image(tbank_image_path)
    base64_ya_pay_image = get_base64_encoded_image(ya_pay_image_path)

    result = [
        {
            'header': '10% all',
            'description': 'a lot of cashback only for new users till 32th october',
            'image': base64_tbank_image,
            'bic': 12345678
        },
        {
            'header': '300 рублей на первый заказ в Яндекс.Еда',
            'description': 'Всем новым пользователям предоставляется скидка на первый заказ онлайн в сервисе Яндекс.Еда',
            'image': base64_ya_pay_image,
            'bic': 87878787
        }
    ]

    return result


def search():
    return mock_search()

