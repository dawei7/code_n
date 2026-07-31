## Description

You are given the root of a binary tree. Visit its levels from top to bottom, numbering the root level as $1$. The direction alternates: nodes on odd-numbered levels are inspected from left to right, while nodes on even-numbered levels are inspected from right to left.

Within one level, accumulate node values in that inspection order until reaching the first node that fails the level's child requirement. An odd-level node must have a left child; an even-level node must have a right child. The failing node and every node after it in that level's inspection order contribute nothing to the sum.

This early stop affects only the sum for the current level. The traversal still discovers every child in the tree, so the result contains one entry for every existing level. Return an array `ans` in which `ans[i]` is the accumulated value for level $i+1$.
