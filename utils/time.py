import time
from datetime import datetime, timedelta

DEFAULT_DATE_FMT = "%Y-%m-%dT%H:%M:%S"


def fmt_time_from_now(secs=0, time_format=DEFAULT_DATE_FMT):
    return datetime.utcfromtimestamp(time.time() + int(secs)).strftime(time_format)


def to_date(date: str, fmt=DEFAULT_DATE_FMT, tmdelta=None, op="+"):
    if not tmdelta:
        tmdelta = {}
    if op == "+":
        return datetime.strptime(date, fmt) + timedelta(**tmdelta)
    if op == "-":
        return datetime.strptime(date, fmt) - timedelta(**tmdelta)


def date_to_str(date: datetime, fmt=DEFAULT_DATE_FMT):
    return date.strftime(fmt)


def total_seconds(date: str, fmt=DEFAULT_DATE_FMT):
    return (to_date(date, fmt) - datetime(1970, 1, 1)).total_seconds()


def days_to_seconds(days: int):
    return days * 24 * 60 * 60


def timestamp(fmt="%Y-%m-%dT%H:%M:%S", tmdelta=None):
    if not tmdelta:
        tmdelta = {}
    return (datetime.now() - timedelta(**tmdelta)).strftime(fmt)


def timestamp_utc(fmt="%Y-%m-%dT%H:%M:%S", tmdelta=None):
    if not tmdelta:
        tmdelta = {}
    return (datetime.utcnow() - timedelta(**tmdelta)).strftime(fmt)

