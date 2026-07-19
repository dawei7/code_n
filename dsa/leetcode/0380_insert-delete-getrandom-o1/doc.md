# Insert Delete GetRandom O(1)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 380 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) |

## Problem Description
### Goal
Design a `RandomizedSet` storing distinct integers. `insert(val)` adds a missing value and returns `True`, or leaves an existing value unchanged and returns `False`. `remove(val)` deletes a present value and returns `True`, or returns `False` when it was absent.

`getRandom()` returns one currently stored value, with every value having equal probability; it is called only when the set is nonempty. Preserve state across operations, including negative values and zero. All three methods must run in average $O(1)$ time, so random selection cannot scan the set and removal cannot require shifting an unbounded sequence without an accompanying constant-time strategy.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["insert", value]`, `["remove", value]`, and `["getRandom"]` operations

**Return value**

- One result per operation: insert and remove return whether they changed the set, while getRandom returns any current value. Native LeetCode calls the corresponding `RandomizedSet` methods directly.

### Examples
**Example 1**

- Input: `operations = [["insert",1],["remove",2],["insert",2],["getRandom"],["remove",1],["insert",2],["getRandom"]]`
- Output: `[True,False,True,1,True,False,2]`

**Example 2**

- Input: `operations = [["insert",5],["insert",5],["remove",5]]`
- Output: `[True,False,True]`

**Example 3**

- Input: `operations = [["insert",-3],["getRandom"]]`
- Output: `[True,-3]`
