# Kth Distinct String in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2053 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-distinct-string-in-an-array/) |

## Problem Description

### Goal

A string is *distinct* in `arr` only when it occurs exactly once in the complete array. Filter the array conceptually to those distinct strings while preserving their original relative order; repeated values contribute no entry at all, regardless of where their copies occur.

Given the one-based rank `k`, return the string occupying that position in the ordered distinct sequence. If the array contains fewer than `k` strings with total frequency one, return the empty string `""`.

### Function Contract

**Inputs**

- `arr`: an array of $n$ lowercase strings, where $1 \le n \le 1000$ and each string has length from $1$ through $5$.
- `k`: a one-based rank satisfying $1 \le k \le n$.

**Return value**

- Return the `k`th string, in original array order, whose total frequency is exactly one.
- Return `""` when fewer than `k` such strings exist.

### Examples

**Example 1**

- Input: `arr = ["d","b","c","b","c","a"], k = 2`
- Output: `"a"`
- Explanation: Only `"d"` and `"a"` occur once, in that order.

**Example 2**

- Input: `arr = ["aaa","aa","a"], k = 1`
- Output: `"aaa"`
- Explanation: Every value is distinct, so the first array element is also the first distinct string.

**Example 3**

- Input: `arr = ["a","b","a"], k = 3`
- Output: `""`
- Explanation: Only `"b"` is distinct, so a third distinct string does not exist.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Frequency must be known globally**

First count every string with a hash map. A value seen for the first time cannot yet be returned because another copy may occur later; completing the frequency pass resolves that uncertainty for every position.

**Recovering original order**

Scan `arr` again rather than iterating over the map. Whenever a string's stored count is one, decrement `k`. The string that makes `k` zero is the requested answer. If the scan ends first, return `""`.

The first pass labels exactly the values satisfying the definition of distinct. The second pass visits precisely those qualifying occurrences in their original order, so its countdown assigns ranks one through the number of distinct strings and returns exactly the requested rank.

#### Complexity detail

Both passes inspect $n$ strings, and source strings have a fixed maximum length of five, so the total expected time is $O(n)$. The frequency map stores at most $n$ different strings and uses $O(n)$ space.

#### Alternatives and edge cases

- **Repeated linear counting:** Calling `arr.count(value)` at every position avoids an explicit map but rescans the array up to $n$ times, costing $O(n^2)$.
- **Set alone:** A set records presence but not whether a value occurs once or multiple times, so it cannot identify distinct strings by itself.
- Duplicate copies are all excluded; the first copy of a repeated string is not distinct.
- When all values repeat, every valid `k` produces `""`.
- The rank is one-based and applies only after non-distinct values are removed.

</details>
