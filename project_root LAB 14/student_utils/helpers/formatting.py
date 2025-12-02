# student_utils/helpers/formatting.py

from datetime import datetime

def prefix_message(message, prefix="INFO"):
    """Return message prefixed with [prefix].

    Example:
      prefix_message("Task completed") -> "[INFO] Task completed"
    """
    return f"[{prefix}] {message}"

def timestamped_prefix(message, prefix="INFO"):
    """Return message prefixed with an ISO timestamp and the given prefix.

    Example:
      timestamped_prefix("Job done") -> "[2025-12-02T12:34:56] [INFO] Job done"
    """
    ts = datetime.now().isoformat(timespec="seconds")
    return f"[{ts}] [{prefix}] {message}"