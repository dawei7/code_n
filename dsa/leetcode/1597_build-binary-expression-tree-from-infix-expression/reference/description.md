## Description

Given a syntactically valid infix arithmetic expression `s`, construct its binary expression tree. Each operand is a single decimal digit, and the available binary operators are `+`, `-`, `*`, and `/`. Parentheses may override the usual precedence rules. Without parentheses, multiplication and division bind more tightly than addition and subtraction, and operators of equal precedence associate from left to right.

Every leaf of the returned tree represents an operand. Every internal node represents an operator whose left and right subtrees are that operator's two operands. The tree must encode the same grouping and evaluation order as the original expression; parentheses affect the structure but do not become nodes themselves.
