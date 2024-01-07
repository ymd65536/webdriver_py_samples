import req_driver.config.const as const
import req_driver.browser.window as win
import req_driver.using_elements.element as ele
import req_driver.using_elements.input_element as input_ele

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

    print("---")

    input_elements = ele.find_elements(sessionId, "tag name", "input")

    for input_element in input_elements:
        print("Element: {0}".format(input_element.get(const.ELEMENT_KEY)))

        input_element_type = ele.get_property(
            sessionId, input_element.get(const.ELEMENT_KEY), 'type')

        if ele.is_input_type_text(input_element_type):
            print("input text")
            res = input_ele.send_keys(
                sessionId, input_element.get(const.ELEMENT_KEY), "test")
            os.system('sleep 1')

        if ele.is_input_type_password(input_element_type):
            print("input password")
            res = input_ele.send_keys(
                sessionId, input_element.get(const.ELEMENT_KEY), "password")

        if ele.is_input_type_checkbox(input_element_type):
            print("input checkbox")
            res = input_ele.is_selected(
                sessionId, input_element.get(const.ELEMENT_KEY))
            print(f"is checked {res}")

            res = input_ele.checkbox(
                sessionId, input_element.get(const.ELEMENT_KEY))

            res = input_ele.is_selected(
                sessionId, input_element.get(const.ELEMENT_KEY))
            print(f"is checked {res}")

        if ele.is_input_type_button(input_element_type):
            print("input button")
            res = input_ele.click_element(
                sessionId, input_element.get(const.ELEMENT_KEY))
            print(res)

    for cnt in range(5):
        os.system('sleep 1')

    win.delete_session(sessionId)

    print("---")
    print("End WebDriver")
