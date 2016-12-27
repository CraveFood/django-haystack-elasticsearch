# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings

# Default values on elasticsearch
FUZZINESS = getattr(settings, 'HAYSTACK_FUZZINESS', 'AUTO')
FUZZY_MIN_SIM = getattr(settings, 'HAYSTACK_FUZZY_MIN_SIM', 0.5)
FUZZY_MAX_EXPANSIONS = getattr(settings, 'HAYSTACK_FUZZY_MAX_EXPANSIONS', 50)

# For the geo bits, since that's what Solr & Elasticsearch seem to silently
# assume...
WGS_84_SRID = 4326
