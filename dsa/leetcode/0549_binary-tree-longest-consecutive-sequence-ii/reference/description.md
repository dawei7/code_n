## Description

Given the `root` of a binary tree, return the length of its longest consecutive path.

Along a consecutive path, every adjacent pair of node values differs by exactly one, and the entire value sequence
must be consistently increasing or consistently decreasing. Thus `[1,2,3,4]` and `[4,3,2,1]` are valid sequences,
whereas `[1,2,4,3]` is not because one adjacent difference has magnitude two.

The path is not restricted to downward parent-to-child movement. It may travel from a child through its parent and
then into another child, provided the values along that complete traversal still form one increasing or decreasing
consecutive sequence.
