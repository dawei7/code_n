## Description

A binary tree encodes a Boolean expression. Every leaf is `0` or `1`, representing false or true. Every internal node is an operator: `2` means OR, `3` means AND, `4` means XOR, and `5` means NOT. OR, AND, and XOR nodes have two children; a NOT node has exactly one child, which may be on either side.

Evaluating a leaf yields its Boolean value. Evaluating an internal node first evaluates its child subtrees and then applies the encoded operator. In one operation, you may flip a leaf between `0` and `1`. Given a desired Boolean `result`, return the fewest leaf flips that make the root evaluate to that value. A solution is always possible.
