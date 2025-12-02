# student_utils/helpers/__init__.py

import sys
import os

# Нормальды пакет ретінде импортталғанда осы жол жұмыс істейді:
try:
    from .formatting import prefix_message, timestamped_prefix
except Exception:
    # Егер скрипт ретінде тікелей іске қосылса, project_root-ты sys.path-қа қосып,
    # абсолютті импорт арқылы қажетті атауларды алуға тырысамыз.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from student_utils.helpers.formatting import prefix_message, timestamped_prefix

__all__ = ["prefix_message", "timestamped_prefix"]

if __name__ == "__main__":
    # Қарапайым қолмен тест (python -m student_utils.helpers немесе тікелей іске қосқанда көрінеді)
    print(prefix_message("Task completed"))
    print(timestamped_prefix("Task completed"))