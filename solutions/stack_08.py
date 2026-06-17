"""Solution for stack_08: Evaluate Reverse Polish Notation.


            Evaluate a postfix (Reverse Polish Notation) arithmetic
            expression given as a list of tokens. Operands are
            integers; operators are +, -, *, /. Use a stack:
            on an operand, push it; on an operator, pop the top
            two, apply, push the result. Integer division truncates
            toward zero (Python's default). O(n) time, O(n) space.
            Source: https://www.geeksforgeeks.org/evaluation-of-postfix-expression/
            

Inputs passed to solve():
    tokens: list of n string tokens; operands are integer strings, operators are +, -, *, /.
    n: length of tokens.

Goal:
    the integer result of evaluating the postfix expression.

Samples:
Sample 1 input:  tokens = ['2','1','+','3','*'], n = 5
Sample 1 output: 9 (postfix for (2+1)*3)

Sample 2 input:  tokens = ['4','13','5','/','+'], n = 5
Sample 2 output: 6 (4 + 13/5 = 4 + 2 = 6)


"""

def solve(tokens, n):
    # Write your code here.
    return None
