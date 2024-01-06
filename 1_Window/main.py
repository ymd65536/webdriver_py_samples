import requests  # 「pip install requests」などが必要
import config.const as const

# sleep用
import os

if __name__ == '__main__':

    print("Run WebDriver")

    res = requests.post(
        const.WEB_DRIVER_URL,
        headers={'Content-Type': 'application/json'},
        data='{"capabilities":{}}'
    ).json()

    sessionId = res.get("value").get("sessionId")
    open_url = os.path.join(os.getcwd(), "index.html")

    res = requests.post(
        "".join([const.WEB_DRIVER_URL, '/', sessionId, '/url']),
        headers={'Content-Type': 'application/json'},
        data='{"url": "' + "file://" + open_url + '"}'
    ).json()

    res = requests.get(
        "".join([const.WEB_DRIVER_URL, '/', sessionId, '/title']),
        headers={'Content-Type': 'application/json'},
    ).json()
    window_title = res.get("value")
    print("Window Title: {0}".format(window_title))

    res = requests.get(
        "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/handles']),
        headers={'Content-Type': 'application/json'},
    ).json()

    if res.get("value"):
        window_handles = res.get("value")

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Handle: {0}".format(window_handles[0]))
        for cnt in range(2):
            os.system('sleep 1')

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/rect']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' +
            window_handles[0] + '", "width": 800, "height": 600}'
        ).json()
        print("Window Rect: {0}".format(res.get("value")))
        for cnt in range(2):
            os.system('sleep 1')

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/rect']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' +
            window_handles[0] + '", "x": 0, "y": 0}'
        ).json()
        print("Window Rect: {0}".format(res.get("value")))
        for cnt in range(2):
            os.system('sleep 1')

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/minimize']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Minimize: {0}".format(res.get("value")))
        for cnt in range(2):
            os.system('sleep 1')

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/maximize']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Maximize: {0}".format(res.get("value")))

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/',
                    sessionId, '/window/fullscreen']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Fullscreen: {0}".format(res.get("value")))
        for cnt in range(5):
            os.system('sleep 1')

        res = requests.post(
            "".join([const.WEB_DRIVER_URL, '/', sessionId, '/window/maximize']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Maximize: {0}".format(res.get("value")))
        for cnt in range(5):
            os.system('sleep 1')

    requests.delete(
        "".join([const.WEB_DRIVER_URL, '/', sessionId]),
        headers={'Content-Type': 'application/json'},
    )

    print("End WebDriver")
