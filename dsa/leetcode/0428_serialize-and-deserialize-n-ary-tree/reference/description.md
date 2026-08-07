### 1. Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following `3-ary` tree

![](images/narytreeexample.png)

as `[1 [3[5 6] 2 4]]`. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.

![](images/sample_4_964.png)

For example, the above tree may be serialized as `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`.

You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

### 2. Function Contract

**Inputs**

- `root`: An N-ary `Node` that begins the structure, or `None` for an empty tree. Each node exposes `val` and an ordered
  `children` list.

Canonical JSON fixtures encode an app-local node recursively as `[value, children]`; the runner constructs `Node`
objects before calling `solve`.

**Return value**

The app adapter serializes `root`, deserializes that string, and returns the reconstructed `Node`. The immutable
native artifact exposes the source-required `Codec.serialize(root)` and `Codec.deserialize(data)` methods.

### 3. Examples

#### Example 1

- **Input:** `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- **Output:** `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
#### Example 2

- **Input:** `root = [1,null,3,2,4,null,5,6]`
- **Output:** `[1,null,3,2,4,null,5,6]`
#### Example 3

- **Input:** `root = []`
- **Output:** `[]`

### 4. Constraints

- The number of nodes in the tree is in the range $[0, 10^{4}]$.

- $0 \le \text{Node.val} \le 10^{4}$

- The height of the n-ary tree is less than or equal to `1000`

- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.