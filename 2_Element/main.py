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
            "/".join([const.WEB_DRIVER_URL, sessionId, 'window']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Handle: {0}".format(window_handles[0]))

        res = requests.post(
            "/".join([const.WEB_DRIVER_URL, sessionId, 'window', 'maximize']),
            headers={'Content-Type': 'application/json'},
            data='{"handle": "' + window_handles[0] + '"}'
        ).json()
        print("Window Maximize: {0}".format(res.get("value")))

    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, sessionId, 'element']),
        headers={'Content-Type': 'application/json'},
        data='{"using": "css selector", "value": "' +
        "[type='" + "button" + "']" + '"}'
    ).json()
    btn_element = res.get("value").get(const.ELEMENT_KEY)
    print("Element: {0}".format(btn_element))

    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, sessionId,
                  'element', btn_element, 'attribute', 'type']),
        headers={'Content-Type': 'application/json'},
    ).json()
    ui_type = res.get("value")
    print("Type: {0}".format(ui_type))

    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, sessionId,
                  'element', btn_element, 'attribute', 'value']),
        headers={'Content-Type': 'application/json'},
    ).json()
    ui_value = res.get("value")
    print("Value: {0}".format(ui_value))

    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, sessionId, 'element']),
        headers={'Content-Type': 'application/json'},
        data='{"using": "link text", "value":' + '"google link"' + "}"
    ).json()
    link_element = res.get("value").get(const.ELEMENT_KEY)
    print("Element: {0}".format(link_element))

    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, sessionId,
                  'element', link_element, 'attribute', 'href']),
        headers={'Content-Type': 'application/json'},
    ).json()
    anchor_attr = res.get("value")
    print("Value: {0}".format(anchor_attr))

    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, sessionId, 'element']),
        headers={'Content-Type': 'application/json'},
        data='{"using": "tag name", "value":' + '"h1"' + "}"
    ).json()
    h1_element = res.get("value").get(const.ELEMENT_KEY)
    print("Element: {0}".format(h1_element))

    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, sessionId,
                  'element', h1_element, 'property', 'innerHTML']),
        headers={'Content-Type': 'application/json'},
    ).json()
    h1_innerHTML = res.get("value")
    print("Value: {0}".format(h1_innerHTML))

    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, sessionId, 'element']),
        headers={'Content-Type': 'application/json'},
        data='{"using": "xpath", "value":' + '"/html/body/div/h1"' + "}"
    ).json()
    h1_xpath_element = res.get("value").get(const.ELEMENT_KEY)
    print("Element: {0}".format(h1_xpath_element))

    res = requests.get(
        "/".join([const.WEB_DRIVER_URL, sessionId,
                  'element', h1_xpath_element, 'property', 'innerHTML']),
        headers={'Content-Type': 'application/json'},
    ).json()
    h1_xpath_innerHTML = res.get("value")
    print("Value: {0}".format(h1_xpath_innerHTML))

    for cnt in range(5):
        os.system('sleep 1')

    requests.delete(
        "/".join([const.WEB_DRIVER_URL, sessionId]),
        headers={'Content-Type': 'application/json'},
    )

    print("End WebDriver")
