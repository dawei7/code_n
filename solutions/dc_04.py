"""Solution for dc_04: Karatsuba Multiplication.


            Multiply two non-negative integers using Karatsuba's
            divide-and-conquer algorithm. Split each operand into
            high and low halves; compute three recursive products
            and combine. Recursion bottoms out on 1-digit factors.
            O(n^log2(3)) ~ O(n^1.585) time.
            Source: https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/
            

Inputs passed to solve():
    x: first non-negative integer (small in tests).
    y: second non-negative integer.
    n: digit count (used only to size the cutoff).

Goal:
    x * y as a plain integer.

Samples:
Sample 1 input:  x = 1234, y = 5678, n = 4
Sample 1 output: 7006652

Sample 2 input:  x = 0, y = 12345, n = 5
Sample 2 output: 0

Sample 3 input:  x = 7, y = 8, n = 1
Sample 3 output: 56

"""

def solve(x, y, n):
    # Write your code here.
    return None
