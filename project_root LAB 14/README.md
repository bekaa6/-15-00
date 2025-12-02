# student_utils Package

This package contains math and string utility functions, as well as helper functions for message formatting.

Usage example:

from student_utils import add, to_upper, median, reverse_text
from student_utils.helpers import prefix_message, timestamped_prefix

print(add(5, 10))                 # 15
print(to_upper("hello"))          # HELLO
print(median([3, 1, 2]))          # 2
print(reverse_text("abc"))        # cba
print(prefix_message("Done"))     # [INFO] Done
print(timestamped_prefix("Done")) # [2025-12-02T12:34:56] [INFO] Done