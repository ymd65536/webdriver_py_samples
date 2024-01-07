import requests


def delete(url, headers):
    return requests.delete(
        url,
        headers=headers,
    )


def post(url, headers, data=None):
    res = {}
    if data is None:
        res = requests.post(
            url,
            headers=headers
        ).json()
    else:
        res = requests.post(
            url,
            headers=headers,
            data=data
        ).json()

    return res.get("value")


def get(url, headers, data=None):
    res = {}
    if data is None:
        res = requests.get(
            url,
            headers=headers,
        ).json()
    else:
        res = requests.get(
            url,
            headers=headers,
        ).json()
    return res.get("value")
