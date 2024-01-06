import requests  # 「pip install requests」などが必要
import req_driver.config.const as const
import req_driver.browser_win.win as win
import req_driver.using_elements.ele as ele

# sleep用
import os

if __name__ == '__main__':

    print("Run WebDriver")

    sessionId = win.get_session_id()
    open_url = os.path.join(os.getcwd(), "index.html")

    win.open_url(sessionId, open_url)
    window_title = win.get_title(sessionId)
    print("Window Title: {0}".format(window_title))
    window_handles = win.get_window_handles(sessionId)

    if window_handles:

        print(window_handles)
        sw = win.switch_to_window(sessionId, window_handles[0])

        maximize = win.window_maximize(sessionId, window_handles[0])
        print("Window Maximize: {0}".format(maximize))

    print("---")

    res = requests.post(
        "/".join([const.WEB_DRIVER_URL, sessionId, 'elements']),
        headers={'Content-Type': 'application/json'},
        data='{"using": "tag name", "value":' + '"input"' + "}"
    ).json()
    input_elements = res.get("value")

    for input_element in input_elements:
        print("Element: {0}".format(input_element.get(const.ELEMENT_KEY)))

        res = requests.get(
            "/".join([const.WEB_DRIVER_URL, sessionId,
                      'element', input_element.get(const.ELEMENT_KEY), 'property', 'type']),
            headers={'Content-Type': 'application/json'},
        ).json()
        input_element_type = res.get("value")

        if input_element_type == 'text':
            print("input text")

        if input_element_type == 'password':
            print("input password")

        if input_element_type == 'checkbox':
            print("input checkbox")

        if input_element_type == 'button':
            print("input button")

    for cnt in range(5):
        os.system('sleep 1')

    requests.delete(
        "/".join([const.WEB_DRIVER_URL, sessionId]),
        headers={'Content-Type': 'application/json'},
    )
    print("---")
    print("End WebDriver")
