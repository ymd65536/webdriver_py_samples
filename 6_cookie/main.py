import req_driver.browser.window as win
import req_driver.using_cookie.cookie as cookie

# sleep用
import os

if __name__ == '__main__':

    print("Run WebDriver")

    sessionId = win.start_session()
    open_url = "https://google.com"

    win.open_url(sessionId, open_url, file=False)
    window_title = win.get_title(sessionId)
    print("Window Title: {0}".format(window_title))
    window_handles = win.get_window_handles(sessionId)

    if window_handles:
        print(window_handles)
        sw = win.switch_to_window(sessionId, window_handles[0])

        maximize = win.window_maximize(sessionId, window_handles[0])
        print("Window Maximize: {0}".format(maximize))

    cookie.add_cookie(
        sessionId, '{"name":"ymd","value":"65536","domain":"google.com"}')

    cookies = cookie.get_all_cookies(sessionId)
    print("Cookies: {0}".format(cookies))

    print("--------------------")

    named_cookie = cookie.named_cookie(sessionId, "ymd")
    print("Named Cookie: {0}".format(named_cookie))

    delete_cookie = cookie.delete_cookie(sessionId, "ymd")

    print("--------------------")

    cookies = cookie.get_all_cookies(sessionId)
    print("Cookies: {0}".format(cookies))

    cookie.delete_all_cookies(sessionId)
    cookies = cookie.get_all_cookies(sessionId)
    print("Cookies: {0}".format(cookies))

    os.system('sleep 1')
    win.delete_session(sessionId)

    print("End WebDriver")
