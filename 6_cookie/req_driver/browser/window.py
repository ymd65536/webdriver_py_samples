from ..config import const
from ..common import _request as req


def start_session(caps='{"capabilities":{}}'):
    return req.post(
        const.WEB_DRIVER_URL,
        headers=const.REQUEST_HEADERS,
        data=caps
    ).get("sessionId")


def delete_session(session_id):
    return req.delete(
        "/".join([const.WEB_DRIVER_URL, session_id]),
        headers=const.REQUEST_HEADERS,
    )


def open_url(session_id, url, file=True):

    if not file:
        res = req.post(
            "/".join([const.WEB_DRIVER_URL, session_id, 'url']),
            headers=const.REQUEST_HEADERS,
            data='{"url": "' + url + '"}'
        )
    else:
        res = req.post(
            "/".join([const.WEB_DRIVER_URL, session_id, 'url']),
            headers=const.REQUEST_HEADERS,
            data='{"url": "' + "file://" + url + '"}'
        )

    return res


def get_title(session_id):
    return req.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'title']),
        headers=const.REQUEST_HEADERS,
    )


def get_window_handles(session_id):
    return req.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window', 'handles']),
        headers=const.REQUEST_HEADERS,
    )


def switch_to_window(session_id, window_handle):
    return req.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window']),
        headers=const.REQUEST_HEADERS,
        data='{"handle": "' + window_handle + '"}'
    )


def window_maximize(session_id, window_handle):
    return req.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window', 'maximize']),
        headers=const.REQUEST_HEADERS,
        data='{"handle": "' + window_handle + '"}'
    )
