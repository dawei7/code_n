# Iterator for Combination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1286 |
| Difficulty | Medium |
| Topics | String, Backtracking, Design, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/iterator-for-combination/) |

## Problem Description
### Goal
Design a `CombinationIterator` initialized with `characters`, a string of sorted distinct lowercase English letters, and an integer `combinationLength`. The iterator represents every subsequence of exactly that length, ordered lexicographically.

Calling `next()` must return the next represented combination in lexicographical order. Calling `hasNext()` must return `true` exactly while another combination remains. Every call to `next()` is guaranteed to occur when such a combination exists.

### Function Contract
**Inputs**

- `characters`: a sorted string of $n$ distinct lowercase English letters, where $1 \le n \le 15$.
- `combinationLength`: the required combination length $k$, where $1 \le k \le n$.
- `operations`: an app-local sequence of `next` and `hasNext` calls; at most $10^4$ calls occur.
- Let $q$ be the number of `next` calls.

**Return value**

For the app-local adapter, a list containing each operation's result in order. The native `next()` method returns a length-$k$ string, and `hasNext()` returns a Boolean.

### Examples
**Example 1**

- Input: `characters = "abc"`, `combinationLength = 2`, operations `next, hasNext, next, hasNext, next, hasNext`
- Output: `["ab",true,"ac",true,"bc",false]`

**Example 2**

- Input: `characters = "abcd"`, `combinationLength = 3`, operations `next, next`
- Output: `["abc","abd"]`

**Example 3**

- Input: `characters = "xy"`, `combinationLength = 2`, operations `hasNext, next, hasNext`
- Output: `[true,"xy",false]`
