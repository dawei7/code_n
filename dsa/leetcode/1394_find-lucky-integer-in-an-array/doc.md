# Find Lucky Integer in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1394 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-lucky-integer-in-an-array/) |

## Problem Description

### Goal

An integer is lucky in an array when its numeric value equals the number of times it occurs. For example, `3` is lucky only when the array contains exactly three occurrences of `3`.

Given an integer array `arr`, return the largest lucky integer it contains. Several different values may satisfy the frequency rule at the same time, so the numeric maximum determines the answer. If no array value has frequency equal to itself, return `-1`.

### Function Contract

**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{arr[i]} \le 500$.

Let $u$ be the number of distinct values in `arr`.

**Return value**

- The greatest value whose frequency equals that value, or `-1` if no such value exists.

### Examples

**Example 1**

- Input: `arr = [2,2,3,4]`
- Output: `2`

**Example 2**

- Input: `arr = [1,2,2,3,3,3]`
- Output: `3`

**Example 3**

- Input: `arr = [2,2,2,3,3]`
- Output: `-1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(u)$

<details>
<summary>Approach</summary>

#### General

Count every array value in a hash table during one pass. Then examine each `(value, frequency)` pair and retain the largest value for which `value == frequency`.

The counter contains the exact multiplicity of every distinct input value, so the equality test accepts precisely the lucky integers. Taking the maximum among all accepted values implements the required tie rule. Starting from `-1` also supplies the required result when no pair qualifies.

#### Complexity detail

Counting $n$ entries and scanning $u \le n$ distinct keys takes $O(n)$ expected time. The frequency table stores $u$ entries and uses $O(u)$ space.

#### Alternatives and edge cases

- **Count by rescanning the array:** Calling a linear frequency operation for every distinct value is correct but can require $O(nu)$, or $O(n^2)$, time.
- **Fixed frequency array:** Because values are at most 500, an array of 501 counters also gives $O(n)$ time and $O(1)$ space relative to the fixed domain.
- **Several lucky values:** Return the numerically largest one, not the most recently encountered one.
- **Value one:** A single occurrence of `1` is lucky.
- **Near miss:** A value occurring one too many or one too few times is not lucky.
- **No lucky value:** Return `-1`, even though all input values are positive.

</details>
