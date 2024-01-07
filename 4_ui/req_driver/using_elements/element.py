from ..config import const
from ..common import _request as req


def find_elements(session_id, using, value):
    return req.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'elements']),
        headers=const.REQUEST_HEADERS,
        data='{"using": "' + using + '", "value": "' + value + '"}'
    )


def get_property(session_id, element_id, property_name):
    return req.get(
        "/".join([const.WEB_DRIVER_URL, session_id,
                  'element', element_id, 'property', property_name]),
        headers=const.REQUEST_HEADERS,
    )


def is_input_type_text(input_element_type):
    return input_element_type == 'text'


def is_input_type_password(input_element_type):
    return input_element_type == 'password'


def is_input_type_checkbox(input_element_type):
    return input_element_type == 'checkbox'


def is_input_type_button(input_element_type):
    return input_element_type == 'button'
