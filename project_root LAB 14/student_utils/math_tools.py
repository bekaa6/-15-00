# student_utils/math_tools.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def average(numbers):
    """Return the arithmetic mean of a sequence of numbers.

    Note: Raises ZeroDivisionError for empty sequences (consistent with sum/len behavior).
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """Return the median of a sequence of numbers.

    If the sequence has an odd length, the middle value is returned.
    If the sequence has an even length, the average of the two middle values is returned.

    Example:
      median([1, 3, 2]) -> 2
      median([1, 2, 3, 4]) -> 2.5

    Raises:
      ValueError: if numbers is empty.
    """
    nums = sorted(numbers)
    n = len(nums)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2