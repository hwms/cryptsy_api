# -*- coding: utf-8 -*-
import hashlib
import hmac
import sys
import urllib

import requests
import time


__all__ = ['PY3', 'cleanup_dict', 'join_not', 'postprocess', 'sign', 'with_metaclass']

PY3 = sys.version_info[0] == 3

if PY3:
    urlencode = urllib.parse.urlencode  # @UndefinedVariable
else:
    urlencode = urllib.urlencode  # @UndefinedVariable


def cleanup_dict(dct=None):
    return type(dct)((k, v) for k, v in dct.items() if v is not None) if dct else {}


def sign(public_key, private_key, params=None, headers=None):
    params = dict(params or {}, nonce=int(time.time()))
    content = str(urlencode(params)).encode('utf8')
    sign = hmac.new(private_key.encode('utf8'), content, hashlib.sha512).hexdigest()
    headers = dict(headers or {}, Sign=sign, Key=public_key)
    return params, headers


def join_not(sep, not_obj, *args):
    return sep.join(str(a) for a in args if a is not not_obj)


def postprocess(self, result):
    if not isinstance(result, dict) or 'success' not in result:
        return True, result
    if not int(result['success']):
        return False, result['error']
    result_ = result.get('data', None)
    if result_ is None:
        result_ = result.get('return', None)
    if result_ is None:
        result_ = result
        result_.pop('success')
    return True, result_


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass. (from six)"""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


def session(session=None):
    session = session or requests.Session()
    session.verify = False
    session.headers = dict({
        'Accept': '*/*',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla 5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko 20100101 Firefox 5.0'
        }, **session.headers)
    return session
