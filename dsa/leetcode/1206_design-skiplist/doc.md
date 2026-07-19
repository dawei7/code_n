# Design Skiplist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1206 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-skiplist/) |

## Problem Description

### Goal

Design a skiplist without using a built-in ordered-set library. A skiplist is made from several layers of sorted linked lists. Every stored value appears at the bottom layer, while progressively fewer nodes appear in higher layers; those sparse layers let an operation skip over ranges that a single linked list would traverse one node at a time.

Implement initialization, lookup, insertion, and deletion with expected logarithmic time per operation and expected linear total space. Duplicate values are allowed. Deleting a value removes any one occurrence, leaving other copies searchable.

### Function Contract

**Operations**

- `Skiplist()`: Create an empty skiplist.
- `search(target)`: Return `true` exactly when at least one copy of `target` is present.
- `add(num)`: Insert one occurrence of `num`.
- `erase(num)`: If `num` is present, remove one occurrence and return `true`; otherwise leave the structure unchanged and return `false`.
- Values and search targets lie between 0 and $2\times10^4$, inclusive. At most $5\times10^4$ method calls follow construction.
- Let $n$ be the number of values currently stored, counting duplicates.

**Return value**

- The operation stream returns `null` for construction and `add` calls, and the Boolean result for each `search` or `erase` call.

### Examples

**Example 1**

- Input: `operations = ["Skiplist","add","add","add","search","add","search","erase","erase","search"]`, `arguments = [[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]`
- Output: `[null,null,null,null,false,null,true,false,true,false]`

**Example 2**

- Input: `operations = ["Skiplist","add","add","search","erase","search"]`, `arguments = [[],[5],[5],[5],[5],[5]]`
- Output: `[null,null,null,true,true,true]`

One copy of `5` remains after a successful erase.

**Example 3**

- Input: `operations = ["Skiplist","search","erase"]`, `arguments = [[],[10],[10]]`
- Output: `[null,false,false]`
