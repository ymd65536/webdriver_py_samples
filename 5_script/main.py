import req_driver.browser.window as win
import req_driver.script.javascript as js

# sleep用
import os

if __name__ == '__main__':

    print("Run WebDriver")

    sessionId = win.start_session()
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

    os.system('sleep 1')
    js.execute_script(sessionId, "changeHead1();")
    js.execute_script(sessionId, "changeHead2();")
    js.execute_script(sessionId, "changeNameAttr();")
    js.execute_script(sessionId, "changeCheckbox();")
    js.execute_script(sessionId, "changeParagraph();")

    js.execute_async_script(sessionId, "changeCounterAsync();")
    js.execute_script(sessionId, "changeCounterSync();")

    os.system('sleep 1')

    win.delete_session(sessionId)

    print("End WebDriver")
