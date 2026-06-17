"""Solution for greedy_09: Lemonade Change.

Each lemonade costs $5. Customers pay in $5, $10, or $20 bills
(given in order). Return True if we can give correct change to every
customer; False otherwise.
Greedy: for a $20 bill, prefer $10 + $5 over three $5s so the $5
supply lasts longer.
Requirement: O(n), O(1) extra space.
Source: https://www.geeksforgeeks.org/lemonade-change/

Inputs passed to solve():
    bills: list of n bills (each is 5, 10, or 20).
    n: number of customers.

Goal:
    True if every customer can receive correct change, False otherwise.

Samples:
Sample 1 input:  bills = [5, 5, 5, 10, 20], n = 5
Sample 1 output: True

Sample 2 input:  bills = [5, 5, 10, 10, 20], n = 5
Sample 2 output: False

Sample 3 input:  bills = [5, 10, 5, 20], n = 4
Sample 3 output: True

"""

def solve(bills, n):
    # Write your code here.
    return None
