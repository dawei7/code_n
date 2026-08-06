## Description

You are given a zero-indexed binary matrix `grid`. One operation chooses any
cell currently containing `1` and changes it to `0`; zero cells cannot be
changed into ones.

The matrix is well-isolated when no two remaining `1` cells share a horizontal
or vertical edge. Diagonal contact does not count as adjacency. Choose which
ones to remove so that every originally adjacent pair has at least one endpoint
flipped, while using as few operations as possible.

Return that minimum operation count. The positions of the flips themselves are
not required, and disconnected groups of ones are all covered by the same
global minimum.
