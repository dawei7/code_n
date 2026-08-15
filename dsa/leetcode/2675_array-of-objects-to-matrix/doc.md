# Array of Objects to Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2675 |
| Difficulty | Hard |
| Category | JavaScript |
| Topics | Object, Array, Recursion, Sorting |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/array-of-objects-to-matrix/) |

## Problem Description

### Goal

Convert an array `arr` of JSON objects or arrays into a rectangular matrix. Items may be nested to any depth and their leaves may be numbers, strings, Booleans, or `null`. A leaf's column name is its complete property path, with successive object keys or array indices joined by periods.

The first matrix row lists every distinct leaf path found anywhere in `arr`, sorted in lexicographically ascending order. Each later row represents the corresponding item from `arr`: put its leaf value under the matching column, and use an empty string when that item has no value at that path. Empty objects and arrays contribute no columns.

### Function Contract

**Inputs**

- `arr`: A valid JSON array containing between 1 and 1000 objects or arrays, with at most 1000 distinct leaf paths overall.

Let $r = \lvert\texttt{arr}\rvert$, let $k$ be the number of distinct leaf paths, and let $S$ be the total number of object properties and array elements visited while recursively flattening all rows.

**Return value**

- Return a matrix with $r + 1$ rows and $k$ columns. Its header is the sorted path list, followed by one aligned value row per input item.

### Examples

#### Example 1

- **Input:** `arr = [{"b":1,"a":2},{"b":3,"a":4}]`
- **Output:** `[["a","b"],[2,1],[4,3]]`

#### Example 2

- **Input:** `arr = [{"a":1,"b":2},{"c":3,"d":4},{}]`
- **Output:** `[["a","b","c","d"],[1,2,"",""],["","",3,4],["","","",""]]`

#### Example 3

- **Input:** `arr = [{"a":{"b":1,"c":2}},{"a":{"b":3,"d":4}}]`
- **Output:** `[["a.b","a.c","a.d"],[1,2,""],[3,"",4]]`

#### Example 4

- **Input:** `arr = [[{"a":null}],[{"b":true}],[{"c":"x"}]]`
- **Output:** `[["0.a","0.b","0.c"],[null,"",""],["",true,""],["","","x"]]`

#### Example 5

- **Input:** `arr = [{},{},{}]`
- **Output:** `[[],[],[],[]]`
