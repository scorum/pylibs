import requests
import json
import time

from scorum.api.methods import get_api_name, to_payload
from scorum.utils.logger import setup_logger, DEFAULT_CONFIG, get_logger

setup_logger(**DEFAULT_CONFIG)
log = get_logger("request")


def get_curl_cli(url, api, method, args):
    payload = to_payload(method, api, args)
    return "curl --data '{payload}' {url}".format(payload=json.dumps(payload), url=url)


def call(url, api, method, args, retries=5):
    payload = to_payload(method, api, args)
    r = 0
    while retries:
        try:
            r = requests.post(url, json=payload)
            retries = 0
        except Exception as e:
            log.error("Error during request: %s\n Remain attempts: %d", e, retries)
            time.sleep(0.5)
            retries -= 1

    if not isinstance(r, requests.Response):
        raise ConnectionError("Failed to retrieve response from: %s", url)

    try:
        response = json.loads(r.text)
        return response["result"]
    except KeyError:
        log.error("request failed with code: %d: %s\n%s" % (r.status_code, r.reason, r.text))
