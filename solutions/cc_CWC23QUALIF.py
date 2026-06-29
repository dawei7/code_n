"""
Description
-----------
The cricket World Cup has started in Chefland. There are many teams participating in the group stage matches. Any team that scores $12$ or more points in the group stage matches qualifies for the next stage.

You know the score that a particular team has scored in the group stage matches. Determine if the team has qualified for the next stage or not.

Examples
--------
Example 1 (official combined stdin/stdout):
Input:
  3
Output:
  No

Example 2 (official combined stdin/stdout):
Input:
  17
Output:
  Yes
"""

def solve():
    # Read stdin with input(), just like on CodeChef.
    # Print the answer with print().
    rating = int(input())
    if rating < 12:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    solve()
