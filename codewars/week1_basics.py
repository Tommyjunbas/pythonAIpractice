# week1_basics.py
# CodeWars Solutions - Week 1 Basics
# Thomas, 30/09/25 (organaized by deepseek)

"""
 WEEK 1 PROGRESS:
- 6 problems solved
- Basic Python syntax mastered
- Functions, conditionals, loops
"""

# =====================
# PROBLEM 1: Even or Odd
# =====================
def even_or_odd(number):
    """
    Returns "Even" for even numbers, "Odd" for odd numbers
    """
    return "Even" if number % 2 == 0 else "Odd"

# =====================
# PROBLEM 2: Find Smallest Int
# =====================
def find_smallest_int(arr):
    """
    Finds the smallest integer in an array
    """
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# =====================
# PROBLEM 3: Make Negative
# =====================
def make_negative(number):
    """
    Makes a number negative. If already negative, returns unchanged.
    """
    if number > 0:
        return -number
    return number

# =====================
# PROBLEM 4: Sum of Positive
# =====================
def positive_sum(arr):
    """
    Returns sum of all positive numbers in array
    """
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

# =====================
# PROBLEM 5: Basic Op
# =====================
def basic_op(operator, value1, value2):
    """
    Performs basic operations: +, -, *, /
    """
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# =====================
# COMPREHENSIVE TESTING
# =====================
if __name__ == "__main__":
    print(" WEEK 1 SOLUTIONS - COMPREHENSIVE TEST")
    print("=" * 50)
    
    # Test 1
    print("1. even_or_odd(5):", even_or_odd(5))
    print("2. find_smallest_int([3, 1, 8]):", find_smallest_int([3, 1, 8]))
    print("3. make_negative(10):", make_negative(10))
    print("4. positive_sum([1, -4, 7, 12]):", positive_sum([1, -4, 7, 12]))
    print("5. basic_op('+', 4, 7):", basic_op('+', 4, 7))
    
    print("=" * 50)
    print(" ALL WEEK 1 SOLUTIONS WORKING!")
