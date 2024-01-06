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

    print("json response {0}".format(res))
    print("{0} {1}".format("sessionId", sessionId))

    for cnt in range(10):
        print("sleep {0}".format(cnt))
        os.system('sleep 1')

    requests.delete(
        const.WEB_DRIVER_URL + '/' + sessionId,
        headers={'Content-Type': 'application/json'},
    )
