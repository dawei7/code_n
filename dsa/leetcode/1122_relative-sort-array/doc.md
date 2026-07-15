# Relative Sort Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1122 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/relative-sort-array/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`. Every value in `arr2` also occurs in `arr1`, and the values of `arr2` are distinct. The order of `arr2` therefore supplies a priority ordering for selected values of `arr1`, including all repeated copies of those values.

Reorder `arr1` so that its values that appear in `arr2` come first, grouped in the same relative order as the corresponding values in `arr2`. Place every value that does not appear in `arr2` after those priority groups, in ascending order, and return the resulting array.

### Function Contract

**Inputs**

- `arr1`: an integer array of length $n$, where $1 \le n \le 1000$ and every value is in $[0, 1000]$.
- `arr2`: an integer array of length $m$, where $1 \le m \le 1000$; its values are distinct, lie in $[0, 1000]$, and each occurs in `arr1`.

Let $V = 1001$ be the size of the allowed value domain.

**Return value**

An array containing exactly the values of `arr1`, with values named by `arr2` grouped first in `arr2` order and all remaining values afterward in ascending order.

### Examples

**Example 1**

- Input: `arr1 = [2,3,1,3,2,4,6,7,9,2,19]`, `arr2 = [2,1,4,3,9,6]`
- Output: `[2,2,2,1,4,3,3,9,6,7,19]`

**Example 2**

- Input: `arr1 = [28,6,22,8,44,17]`, `arr2 = [22,28,8,6]`
- Output: `[22,28,8,6,17,44]`

### Required Complexity

- **Time:** $O(n + m + V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Turn repeated values into counts.** Because every allowed value is between $0$ and $1000$, create a frequency array with $V$ entries and count all values of `arr1`. This replaces the original positions—which are irrelevant to the required result—with the exact multiplicity that must be emitted for each value.

**Honor the priority array first.** Visit `arr2` from left to right. For each `value`, append it `counts[value]` times, then set `counts[value] = 0`. This puts all copies of each priority value in the required group and prevents that value from being emitted again later. The distinctness guarantee for `arr2` means no priority group is visited twice.

**Use the numeric domain for the remainder.** Scan the frequency array from index $0$ through $1000$ and append each index according to its remaining count. Increasing indices produce exactly the required ascending suffix. The first phase emits every occurrence whose value is in `arr2`; the second emits every other occurrence once, so the result is both correctly ordered and a permutation of `arr1`.

#### Complexity detail

Counting `arr1` takes $O(n)$ time, visiting `arr2` takes $O(m)$ time, emitting the $n$ output values takes $O(n)$ time, and scanning the fixed value domain takes $O(V)$ time. Together this is $O(n + m + V)$. The frequency array uses $O(V)$ auxiliary space; the returned array is output space.

#### Alternatives and edge cases

- **Frequency map plus sorted leftovers:** A hash map avoids scanning unused domain values, but sorting its remaining distinct keys costs $O(u \log u)$ for $u$ leftover values.
- **Custom comparison key:** Sorting all of `arr1` by each value's position in `arr2` is simple, but it costs at least $O(n \log n)$ and can become $O(nm)$ if positions are found by repeated linear searches.
- **Repeated priority values in `arr1`:** Every copy must remain together in its priority group; a single position lookup without frequency tracking can lose duplicates.
- **No leftover values:** Once all priority groups are emitted, the domain scan adds nothing and the result is already complete.
- **Values absent from `arr2`:** Their original order is irrelevant; they must appear in ascending numeric order, including repeated copies.

</details>
