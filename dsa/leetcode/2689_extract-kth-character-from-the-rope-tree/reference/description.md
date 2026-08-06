## Description

A rope binary tree represents a string without requiring every internal node to store the complete concatenation. Each node has ordinary `left` and `right` children plus a string `val` and a nonnegative integer `len`.

A leaf has no children, has `len = 0`, and stores a non-empty lowercase string in `val`. An internal node has at least one child, stores an empty string in `val`, and has a positive `len` equal to the length of the complete string represented by its subtree. The string of an internal node is the string of its left subtree followed by the string of its right subtree; a missing child contributes an empty string.

Given the rope root and a valid one-based position `k`, return the $k$-th character of the represented root string.
