"""
Description
-----------
Convert an infix arithmetic expression (operators
            between operands, with parentheses) into a postfix
            expression (Reverse Polish Notation - operators
            after operands). Use the shunting-yard algorithm
            with a stack of operators. Precedence: */ higher
            than +-. Left-associative throughout. Operands are
            single lowercase letters or digits in this spec.
            O(n) time, O(n) space.
            Source: https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/

Examples
--------
Example 1:
Input:  expr = 'a+b*c', n = 5
Output: 'abc*+'

Example 2:
Input:  expr = '(a+b)*c', n = 7
Output: 'ab+c*'

Example 3:
Input:  expr = 'a+b*c-d/e', n = 9
Output: 'abc*+de/-'
"""

def solve(expr, n):
    # Write your code here.
    return None
