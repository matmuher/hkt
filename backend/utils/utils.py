import models.search as search


def validate_request(request: search):
    if request.session_id is None or len(request.session_id) == 0:
        return "Invalid session id"
