import models.search as search
from typing import List
import re
import base64


DEFAULT_SESSION_ID = '12345678'


def validate_request(request: search):
    if request.session_id == DEFAULT_SESSION_ID:
        return None

    if request.session_id is None or len(request.session_id) == 0:
        return "Invalid session id"


def filter_response(request: str, cashbacks: List[dict]):
    res = []

    for cashback in cashbacks:
        if is_relevant(request, cashback):
            res.append(cashback)

    return res


def is_relevant(request: str, cashback: dict):
    request_words = to_lower_case_only_alpha(request)
    cashback_header_words = to_lower_case_only_alpha(cashback["header"])
    cashback_description_words = to_lower_case_only_alpha(cashback["description"])

    for word in request_words:
        for word2 in cashback_header_words:
            if len(word) == len(word2) and word[0:-1] == word2[0:-1]:
                return True
        for word2 in cashback_description_words:
            if len(word) == len(word2) and word[0:-1] == word2[0:-1]:
                return True

    return False


def to_lower_case_only_alpha(text: str):
    return [re.sub(r'[^a-zA-ZА-Яа-я]', '', word) for word in text.split(' ') if len(word) > 1]


def get_base64_encoded_image(file_name: str) -> bytes:
    with open(file_name, 'rb') as fin:
        return base64.b64encode(fin.read())
