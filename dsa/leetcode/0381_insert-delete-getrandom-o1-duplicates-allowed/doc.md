# Insert Delete GetRandom O(1) - Duplicates allowed

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 381 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) |

## Problem Description
### Goal
Design a `RandomizedCollection` that stores integer occurrences and permits duplicates. `insert(val)` always adds one occurrence and returns whether the value was absent before that insertion. `remove(val)` deletes one occurrence and returns whether any occurrence was available to remove.

`getRandom()` selects uniformly across all currently stored occurrences, so a value's probability is proportional to its multiplicity; it is called only when the collection is nonempty. Preserve state across operations, including repeated values, and make insertion, one-occurrence removal, and random selection run in average $O(1)$ time. A failed removal leaves the collection unchanged.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["insert", value]`, `["remove", value]`, and `["getRandom"]` operations

**Return value**

- One result per operation. Insert returns whether the value was previously absent, remove returns whether an occurrence existed, and getRandom returns a current value with probability proportional to its multiplicity.

### Examples
**Example 1**

- Input: `operations = [["insert",1],["insert",1],["insert",2],["getRandom"],["remove",1],["getRandom"]]`
- Output: `[True,False,True,1,True,2]`

**Example 2**

- Input: `operations = [["insert",5],["remove",5],["remove",5]]`
- Output: `[True,True,False]`

**Example 3**

- Input: `operations = [["insert",-2],["insert",-2],["getRandom"]]`
- Output: `[True,False,-2]`
