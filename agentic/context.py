"""Context assembly and prompt truncation utilities for agentic pipelines."""

from __future__ import annotations

from typing import List, Dict, Any


class ContextWindowBuilder:
    """Builds and enforces maximum token or character bounds for agent contexts."""

    def __init__(self, max_characters: int = 16000) -> None:
        self.max_characters = max_characters
        self._chunks: List[Dict[str, Any]] = []

    def add_chunk(self, identifier: str, content: str, priority: int = 0) -> bool:
        """Add a contextual slice if budget allows; returns True if accepted."""
        length = len(content)
        current_len = sum(len(c["content"]) for c in self._chunks)
        if current_len + length > self.max_characters:
            return False
        self._chunks.append({"id": identifier, "content": content, "priority": priority})
        return True

    def assemble(self) -> str:
        """Join all admitted chunks ordered by priority."""
        sorted_chunks = sorted(self._chunks, key=lambda c: c["priority"], reverse=True)
        return "\n\n".join(f"[{c['id']}]\n{c['content']}" for c in sorted_chunks)
