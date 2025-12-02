# student_utils/__init__.py

import sys
import os

# Әдеттегі пакет импортында мына блок жұмыс істейді:
try:
    from .math_tools import add, average, median
    from .string_tools import to_upper, count_words, reverse_text
    # helpers - пакетті экспорттау (subpackage)
    from . import helpers  # allows: from student_utils import helpers
except Exception:
    # Егер файл тікелей іске қосылса немесе relative импорт сәтсіз болса,
    # project_root-ты sys.path-қа қосып, абсолютті импорт арқылы қажетті атауларды аламыз.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from student_utils.math_tools import add, average, median
    from student_utils.string_tools import to_upper, count_words, reverse_text
    from student_utils import helpers

__all__ = [
    "add",
    "average",
    "median",
    "to_upper",
    "count_words",
    "reverse_text",
    "helpers",
]

if __name__ == "__main__":
    # Қарапайым қолмен тексеріс (python -m student_utils немесе тікелей іске қосқанда көрінеді)
    print("Smoke tests for student_utils:")
    print("add(5,10) ->", add(5, 10))
    print("to_upper('hello') ->", to_upper("hello"))
    print("median([3,1,2]) ->", median([3, 1, 2]))
    # helpers-ті пайдалану
    try:
        from student_utils.helpers import prefix_message
        print("prefix_message('Task completed') ->", prefix_message("Task completed"))
    except Exception as e:
        print("Could not import helpers:", e)