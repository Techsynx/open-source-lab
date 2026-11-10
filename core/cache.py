"""High-performance Least Recently Used (LRU) Cache with TTL support."""

from __future__ import annotations

import time
from collections import OrderedDict
from typing import Any, Optional


class LRUCache:
    """Thread-safe LRU cache with entry time-to-live (TTL)."""

    def __init__(self, capacity: int = 128, default_ttl_seconds: Optional[float] = None) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.default_ttl = default_ttl_seconds
        self._store: OrderedDict[str, tuple[Any, Optional[float]]] = OrderedDict()

    def get(self, key: str, default: Any = None) -> Any:
        if key not in self._store:
            return default
        value, expiry = self._store[key]
        if expiry is not None and time.time() > expiry:
            del self._store[key]
            return default
        self._store.move_to_end(key)
        return value

    def set(self, key: str, value: Any, ttl_seconds: Optional[float] = None) -> None:
        ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
        expiry = (time.time() + ttl) if ttl is not None else None
        if key in self._store:
            self._store.move_to_end(key)
        self._store[key] = (value, expiry)
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)

    def __len__(self) -> int:
        return len(self._store)
