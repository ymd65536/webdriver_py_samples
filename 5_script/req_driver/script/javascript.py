from ..config import const
from ..common import _request as req


def scroll_to_bottom(session_id):
    req.post(
        "/".join([const.WEB_DRIVER_URL, session_id, 'execute', 'sync']),
        headers=const.REQUEST_HEADERS,
        data='{"script": ' +
        '"window.scrollTo(0, document.body.scrollHeight);"' +
        ', "args":[]' + "}"
    )
