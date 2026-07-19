# All O`one Data Structure

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 432 |
| Difficulty | Hard |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/all-oone-data-structure/) |

## Problem Description
### Goal
Design an `AllOne` structure that maintains positive counts for string keys. `inc(key)` inserts a missing key with count one or increases an existing count. `dec(key)` decreases an existing key and removes it entirely when its count reaches zero.

`getMaxKey()` returns any key currently having the largest count, while `getMinKey()` returns any key having the smallest count; both return `""` when empty. Ties may be resolved arbitrarily. Every operation must run in average $O(1)$ time, so retrieving an extreme cannot scan or sort all stored keys. Preserve counts consistently across the complete operation sequence.

### Function Contract
**Inputs**

- `operations`: an ordered trace containing `inc key`, `dec key`, `getMaxKey`, and `getMinKey` operations; every decremented key currently exists

**Return value**

- Return the string produced by each retrieval operation, in order. A retrieval on an empty structure returns `""`; when several keys tie, any tied key is valid.

### Examples
**Example 1**

- Input: `operations = [["inc", "hello"], ["inc", "hello"], ["getMaxKey"], ["getMinKey"], ["inc", "leet"], ["getMaxKey"], ["getMinKey"]]`
- Output: `["hello", "hello", "hello", "leet"]`

**Example 2**

- Input: `operations = [["getMaxKey"], ["getMinKey"]]`
- Output: `["", ""]`

**Example 3**

- Input: `operations = [["inc", "a"], ["inc", "b"], ["getMaxKey"], ["getMinKey"]]`
- Output: `["a", "b"]`
