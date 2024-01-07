from ..config import const
from ..common import _request as req


def click_element(session_id, element_id):
    res = req.post(
        "/".join([const.WEB_DRIVER_URL, session_id,
                 'element', element_id, 'click']),
        headers=const.REQUEST_HEADERS,
        data='{"type": "pointerDown", "duration": 0}'
    )

    if res is None:
        res = req.post(
            "/".join([const.WEB_DRIVER_URL, session_id,
                     'element', element_id, 'click']),
            headers=const.REQUEST_HEADERS,
            data='{"type": "pointerUp", "duration": 0}'
        )
    return res


def send_keys(session_id, element_id, keys):
    res = req.post(
        "/".join([const.WEB_DRIVER_URL, session_id,
                  'element', element_id, 'value']),
        headers=const.REQUEST_HEADERS,
        data='{"type": "keyDown", "text": "' + keys + '"}'
    )
    if res is None:
        res = req.post(
            "/".join([const.WEB_DRIVER_URL, session_id,
                     'element', element_id, 'click']),
            headers=const.REQUEST_HEADERS,
            data='{"type": "keyUp", "duration": 0}'
        )
    return res


def checkbox(session_id, element_id):
    res = req.post(
        "/".join([const.WEB_DRIVER_URL, session_id,
                 'element', element_id, 'click']),
        headers=const.REQUEST_HEADERS,
        data='{"type": "pointerDown", "duration": 0}'
    )

    if res is None:
        req.get(
            "/".join([const.WEB_DRIVER_URL, session_id,
                      'element', element_id, 'selected']),
            headers=const.REQUEST_HEADERS,
            data='{"type": "pointerUp", "duration": 0}'
        )
    return res


def is_selected(session_id, element_id):
    res = req.get(
        "/".join([const.WEB_DRIVER_URL, session_id,
                  'element', element_id, 'selected']),
        headers=const.REQUEST_HEADERS
    )
    return res
