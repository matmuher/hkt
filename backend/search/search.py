import base64
import utils.utils as utils
from utils.utils import get_base64_encoded_image
import logging
tbank_image_path = 'mock_images/tbank.jpg'
ya_pay_image_path = 'mock_images/ya_pay.jpg'

logger = logging.getLogger("search logger")


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


def search(session: str, text):
    res = mock_search()

    if text is not None and len(text) > 0:
        res = utils.filter_response(text, res)

    return res

