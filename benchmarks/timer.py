"""Execution timing and micro-benchmark harness."""

from __future__ import annotations

import time
from typing import Callable, Any, Dict


def benchmark_execution(fn: Callable[[], Any], iterations: int = 100) -> Dict[str, float]:
    """Measure average, minimum, and total execution latency over multiple runs."""
    times = []
    for _ in range(iterations):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)

    total_time = sum(times)
    return {
        "iterations": float(iterations),
        "total_seconds": total_time,
        "avg_seconds": total_time / max(iterations, 1),
        "min_seconds": min(times) if times else 0.0,
        "max_seconds": max(times) if times else 0.0,
    }
