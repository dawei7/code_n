## Description

A rooted tree contains `n` nodes numbered from `0` through `n - 1`. It is encoded by `parent`: node `0` is the root, and every later node `i` has direct parent `parent[i]`. Each node `i` also carries the integer value `nums[i]`.

Consider a nonempty subset of the nodes. It is **valid** only when both of these conditions hold:

- the selected values have a sum divisible by `k`; and
- no selected node is adjacent to another selected node, meaning a node and its direct parent may not both belong to the subset.

Count all valid subsets and return the count modulo $10^9+7$.
