import requests
import json
import time

import http.client
from urllib.parse import urlparse

from scorum.api.methods import get_api_name, to_payload
from scorum.utils.logger import setup_logger, DEFAULT_CONFIG, get_logger

setup_logger(**DEFAULT_CONFIG)
log = get_logger("request")


def get_curl_cli(url, api, method, args):
    payload = to_payload(method, api, args)
    return "curl --data '{payload}' {url}".format(payload=json.dumps(payload), url=url)


def call_old(url, api, method, args, retries=5):
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


def call(url, api, method, args, retries=5):
    r = Request()
    return r.call(url, api, method, args, retries)


class Request:
    def __init__(self):
        self._duration = 0

    def duration(self):
        return self._duration

    def call(self, url, api, method, args, retries=5):
        payload = to_payload(method, api, args)
        self._duration = 0

        while retries > 0:
            try:
                url_object = urlparse(url)

                if url_object.scheme == "https":
                    conn = http.client.HTTPSConnection(url_object.netloc)
                else:
                    conn = http.client.HTTPConnection(url_object.netloc)

                headers = {'Content-Type': "application/json"}

                ts = time.time()

                conn.request("POST", url_object.path, json.dumps(payload), headers)

                self._duration = time.time() - ts

                res = conn.getresponse()
                data = res.read().decode('utf-8')

                try:
                    response = json.loads(data)
                    return response["result"]
                except (ValueError, TypeError) as error:
                    print("request failed with code: %d: %s" % (res.code, res.msg))
                    print(data)
                    return None

            except (ConnectionResetError, http.client.HTTPException) as e:
                print("error during request")
                print(e)
                time.sleep(0.5)
                retries -= 1

        return None
