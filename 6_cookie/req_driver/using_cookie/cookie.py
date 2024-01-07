from ..config import const
from ..common import _request as req


def add_cookie(session_id, cookie):
    data = '{"cookie": ' + cookie + '}'

    res = req.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'cookie']),
        headers=const.REQUEST_HEADERS,
        data=data
    )
    print(res)

    return res


def get_all_cookies(session_id):
    return req.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'cookie']),
        headers=const.REQUEST_HEADERS,
    )


def named_cookie(session_id, name):
    return req.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'cookie', name]),
        headers=const.REQUEST_HEADERS,
    )


def delete_cookie(session_id, name):
    return req.delete(
        "/".join([const.WEB_DRIVER_URL, session_id, 'cookie', name]),
        headers=const.REQUEST_HEADERS,
    )


def delete_all_cookies(session_id):
    return req.delete(
        "/".join([const.WEB_DRIVER_URL, session_id, 'cookie']),
        headers=const.REQUEST_HEADERS,
    )
