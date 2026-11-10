"""System telemetry metrics and resource snapshot tools."""

from __future__ import annotations

import os
import platform
import time
from typing import Any, Dict


def collect_system_metrics() -> Dict[str, Any]:
    """Capture snapshot of system metrics including platform, load, and timestamp."""
    metrics: Dict[str, Any] = {
        "timestamp": time.time(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "pid": os.getpid(),
    }
    if hasattr(os, "getloadavg"):
        metrics["load_average"] = os.getloadavg()
    return metrics
