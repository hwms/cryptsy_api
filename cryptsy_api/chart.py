# -*- coding: utf-8 -*-
from . import base

class ChartApi(base.Api):

    def _request(self, *args, **kwargs):
        kwargs = dict(dict(url=self.config.chart_url), **kwargs)
        return super()._request(*args, **kwargs)

    def query(self, marketid, start, end):
        return self._get(marketid=marketid, start=start, end=end, callback='chart', cb=1)
