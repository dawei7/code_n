## Description

A binary tree whose depth is less than `5` is supplied as an ascending array of three-digit integers. An encoding with digits `dpv` represents one node: the hundreds digit `d` is its one-based depth from `1` through `4`, the tens digit `p` is its one-based position within that level as positioned in a full binary tree, and the units digit `v` is its value from `0` through `9`.

The encodings are guaranteed to describe one valid connected binary tree. For every path beginning at the root and ending at a leaf, add the values of the nodes on that path. Return the sum of all those root-to-leaf path sums, so a shared ancestor contributes once for every leaf below it.
