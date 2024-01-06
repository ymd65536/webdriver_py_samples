import requests
from ..config import const


def get_session_id():
    res = requests.post(
        const.WEB_DRIVER_URL,
        headers={'Content-Type': 'application/json'},
        data='{"capabilities":{}}'
    ).json()
    return res.get("value").get("sessionId")


def open_url(session_id, url):
    res = {}
    print("Open URL: {0}".format(url))
    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'url']),
        headers={'Content-Type': 'application/json'},
        data='{"url": "' + "file://" + url + '"}'
    ).json()

    return res.get("value")


def get_title(session_id):
    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'title']),
        headers={'Content-Type': 'application/json'},
    ).json()
    return res.get("value")


def get_window_handles(session_id):
    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window', 'handles']),
        headers={'Content-Type': 'application/json'},
    ).json()

    if res.get("value"):
        return res.get("value")
    else:
        return []


def switch_to_window(session_id, window_handle):
    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window']),
        headers={'Content-Type': 'application/json'},
        data='{"handle": "' + window_handle + '"}'
    ).json()
    return res.get("value")


def window_maximize(session_id, window_handle):
    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'window', 'maximize']),
        headers={'Content-Type': 'application/json'},
        data='{"handle": "' + window_handle + '"}'
    ).json()
    return res.get("value")
