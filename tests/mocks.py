# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from django.apps import apps
from haystack.models import SearchResult


class MockSearchResult(SearchResult):
    def __init__(self, app_label, model_name, pk, score, **kwargs):
        super(MockSearchResult, self).__init__(app_label, model_name, pk, score, **kwargs)
        self._model = apps.get_model('core', model_name)
