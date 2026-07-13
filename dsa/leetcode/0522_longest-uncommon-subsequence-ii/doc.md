# Longest Uncommon Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 522 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) |

## Problem Description
### Goal
Given an array of strings, a subsequence is formed by deleting characters while preserving the remaining order. An uncommon subsequence may be derived from one input string but must not be a subsequence of any other string in the array.

Return the maximum length of any uncommon subsequence, or `-1` when no candidate satisfies that condition. Equal input strings are separate competitors, so their full text cannot be uncommon. A candidate may be the complete source string, and comparison against another string concerns subsequence containment rather than simple equality, substring membership, or frequency alone.

### Function Contract
**Inputs**

- `strs`: an array of lowercase English strings

**Return value**

- The longest uncommon-subsequence length, or `-1` if none exists

### Examples
**Example 1**

- Input: `strs = ["aba", "cdc", "eae"]`
- Output: `3`

**Example 2**

- Input: `strs = ["aaa", "aaa", "aa"]`
- Output: `-1`

**Example 3**

- Input: `strs = ["aabbcc", "aabbcc", "cb", "abc"]`
- Output: `2`

### Required Complexity

- **Time:** $O(k^2 \cdot L)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Only complete input strings need consideration**

Suppose a subsequence of one source string is absent from every other input. If the complete source string were a subsequence of another input, then all of its subsequences would also occur there, contradicting the assumption. Therefore the complete source is itself uncommon and is at least as long as the candidate. Some optimum is always a whole input string.

**Eliminate duplicate candidates**

Count every string first. A string appearing more than once is a subsequence of its identical copy, so it cannot be uncommon. Duplicate strings must still remain among the containers tested against other candidates.

**Test longer unique strings first**

Sort candidates by decreasing length. For a unique candidate, check whether it is a subsequence of any other string using two pointers: advance the candidate pointer only when characters match while scanning the potential container. The first candidate absent from every other string has the maximum possible length.

**Why returning the first survivor is correct**

The whole-string argument guarantees that every possible optimum appears in the candidate list. Duplicate filtering removes only strings known to occur twice. The pairwise tests reject exactly candidates contained in another input, and descending order ensures no rejected-or-unseen candidate can be longer than the first survivor.

#### Complexity detail

With `k` strings of maximum length `L`, at most $k(k - 1)$ subsequence tests each scan $O(L)$ characters, for $O(k^2 \cdot L)$ time; sorting adds $O(k \log k)$. Counts and the ordered list use $O(k)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every subsequence:** is correct but generates up to $2^{L}$ candidates per string.
- **Compare all strings without sorting:** preserves the same worst-case bound but must track the best surviving length instead of returning early.
- **Group by length before testing:** can skip impossible shorter-container checks and has the same core logic.
- **All strings identical:** no uncommon subsequence exists.
- **Unique longest string:** is immediately uncommon because no shorter string can contain it.
- **Duplicate long strings:** may allow a shorter unique string to be the answer.
- **Equal-length different strings:** neither complete string is a subsequence of the other.

</details>
