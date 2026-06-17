"""Solution for stack_07: Infix to Postfix Conversion.


            Convert an infix arithmetic expression (operators
            between operands, with parentheses) into a postfix
            expression (Reverse Polish Notation - operators
            after operands). Use the shunting-yard algorithm
            with a stack of operators. Precedence: */ higher
            than +-. Left-associative throughout. Operands are
            single lowercase letters or digits in this spec.
            O(n) time, O(n) space.
            Source: https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/
            

Inputs passed to solve():
    expr: string of operands (lowercase letters/digits), operators (+,-,*,/), and parentheses.
    n: length of expr.

Goal:
    the postfix expression as a string.

Samples:
Sample 1 input:  expr = 'a+b*c', n = 5
Sample 1 output: 'abc*+'

Sample 2 input:  expr = '(a+b)*c', n = 7
Sample 2 output: 'ab+c*'

Sample 3 input:  expr = 'a+b*c-d/e', n = 9
Sample 3 output: 'abc*+de/-'

"""

def solve(expr, n):
    # Write your code here.
    return None
