"""Solution for math_04: Karatsuba Multiplication.

Multiply two non-negative integers using Karatsuba's
divide-and-conquer algorithm. Split each operand in half,
compute 3 half-sized products (ac, bd, and (a+b)(c+d) - ac - bd),
and combine. Asymptotically O(n^log_2(3)) ~ O(n^1.585), faster
than grade-school O(n^2).
Source: https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication/

Inputs passed to solve():
    x: first non-negative integer.
    y: second non-negative integer.

Goal:
    x * y.

Samples:
Sample 1 input:  x = 1234, y = 5678
Sample 1 output: 7006652

Sample 2 input:  x = 99, y = 99
Sample 2 output: 9801


"""

def solve(x, y):
    # Write your code here.
    return None
