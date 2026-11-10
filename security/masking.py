"""Sensitive credential and token masking utilities."""

from __future__ import annotations

import re

_TOKEN_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{82}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
]


def mask_secrets(text: str, mask: str = "[REDACTED]") -> str:
    """Mask known API keys and authentication tokens in text strings."""
    if not isinstance(text, str):
        return text
    result = text
    for pattern in _TOKEN_PATTERNS:
        result = pattern.sub(mask, result)
    return result
