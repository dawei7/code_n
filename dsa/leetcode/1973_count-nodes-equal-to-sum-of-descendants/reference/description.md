## Description

Given the root of a nonempty binary tree, count the nodes whose stored value
equals the sum of the values stored in all of their descendants. A descendant
is any node strictly below the current node on a path toward a leaf; the
current node itself is not included.

A leaf has no descendants, so its descendant sum is defined as zero. It
therefore contributes to the answer exactly when its own value is `0`.
