## Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as <a href="https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A" target="_blank">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
### Function Contract

**Inputs**

- `root`: A binary-tree root, represented by a level-order list with `null` placeholders in app cases.

**Return value**

The app adapter serializes `root`, deserializes the resulting string, and returns the reconstructed root for level-order comparison. The native `Codec` exposes separate `serialize(root)` and `deserialize(data)` operations.

### Examples
#### Example 1

![](images/serdeser.jpg)

- **Input:** `root = [1,2,3,null,null,4,5]`
- **Output:** `[1,2,3,null,null,4,5]`
#### Example 2

- **Input:** `root = []`
- **Output:** `[]`
### Constraints

- The number of nodes in the tree is in the range $[0, 10^{4}]$.

- $-1000 \le \text{Node.val} \le 1000$