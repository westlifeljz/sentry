from __future__ import absolute_import

import logging

from .base import BaseEventTempStore
from sentry.cache.redis import RedisClusterCache

logger = logging.getLogger(__name__)


class RedisClusterEventTempStore(BaseEventTempStore):
    def __init__(self, **options):
        super(RedisClusterEventTempStore, self).__init__(inner=RedisClusterCache(**options))
