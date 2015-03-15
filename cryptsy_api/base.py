# -*- coding: utf-8 -*-
from . import config, utils


class Api(object):
    _path = None,
    _config = config.CryptsyApiConfig

    def __init__(self, public_key='', private_key='', config=None, session=None):
        self._config = config or self._config
        if public_key or private_key:
            self._config = type('CryptsyApiConfig', (), self._config)
        self._session = utils.session(session)
        self._public_key = self._config.public_key
        self._private_key = self._config.private_key

        self._url = self._config.url

        self._timeout = self._config.timeout
        self._tries = self._config.tries

    def _request(self, request_method, *path, url=None, headers=None, signed=True, **params):
        params, data, headers = utils.cleanup_dict(params), None, headers or {}
        if signed:
            params, headers = utils.sign(self._public_key, self._private_key, params, headers)
        if request_method in ('POST', 'PUT', 'PATCH'):
            data, params = params, None
        url = utils.join_not('/', None, url or self._url, *(self.path + path))
        for _ in range(self._tries):
            try:
                response = self._session.request(request_method, url, params, data, headers,
                                                 timeout=self._timeout, allow_redirects=True)
                result = response.json()
                break
            except Exception as e:
                result = e
        if isinstance(result, Exception):
            raise result
        return utils.postprocess(result)

    def _get(self, *args, **kwargs):
        return self._request('GET', *args, **kwargs)

    def _public_get(self, *route, **params):
        return self._get(*route, **dict(dict(url=self._config.public_url, signed=False), **params))

    def _options(self, *args, **kwargs):
        return self._request('OPTIONS', *args, **kwargs)

    def _head(self, *args, **kwargs):
        return self._request('HEAD', *args, **kwargs)

    def _post(self, *args, **kwargs):
        return self._request('POST', *args, **kwargs)

    def _put(self, *args, **kwargs):
        return self._request('PUT', *args, **kwargs)

    def _patch(self, *args, **kwargs):
        return self._request('PATCH', *args, **kwargs)

    def _delete(self, *args, **kwargs):
        return self._request('DELETE', *args, **kwargs)
