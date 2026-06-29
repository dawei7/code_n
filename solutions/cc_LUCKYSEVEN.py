"""
Description
-----------
Chef considers the number $7$ lucky. As a result, he believes that the $7$-th letter he sees on a day is his *lucky letter* of the day.

You are given a string $S$ of length $10$, denoting the first $10$ letters Chef saw today.
What is Chef's *lucky letter*?

Examples
--------
Example 1 (official combined stdin/stdout):
Input:
  proceeding
Output:
  d

Example 2 (official combined stdin/stdout):
Input:
  outofsight
Output:
  i
"""

def solve():
    # Read stdin with input(), just like on CodeChef.
    # Print the answer with print().
    print(input()[6])


if __name__ == "__main__":
    solve()
