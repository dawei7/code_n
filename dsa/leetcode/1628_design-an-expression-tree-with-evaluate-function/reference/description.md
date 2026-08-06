## Description

Design an expression-tree implementation for a valid postfix expression. Each token is either an integer operand or one of the binary operators `+`, `-`, `*`, and `/`. In postfix order, an operator follows the complete encodings of its left and right operands.

Implement a concrete subclass of the provided abstract `Node` interface. Calling `evaluate()` on the root must recursively compute the expression's integer value. Also implement `TreeBuilder.buildTree(postfix)`, which constructs and returns the root node. Division truncates toward zero, and every division in the valid input has a nonzero divisor.
