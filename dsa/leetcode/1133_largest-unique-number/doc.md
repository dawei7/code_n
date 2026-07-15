# Largest Unique Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1133 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-unique-number/) |

## Problem Description

### Goal

You are given an integer array `nums`. An integer is unique in this array when it occurs exactly once; an integer that appears two or more times is not unique, regardless of where its copies occur.

Return the largest integer among all unique values in `nums`. The largest value in the array is not necessarily the answer if it is repeated. If no integer occurs exactly once, return `-1`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 2000$ and every value lies in $[0,1000]$.

Let $V=1001$ be the size of the allowed value domain.

**Return value**

The greatest value whose frequency in `nums` is exactly one, or `-1` if no such value exists.

### Examples

**Example 1**

- Input: `nums = [5,7,3,9,4,9,8,3,1]`
- Output: `8`
- Explanation: `9` is repeated, while `8` is the largest value appearing once.

**Example 2**

- Input: `nums = [9,9,8,8]`
- Output: `-1`

### Required Complexity

- **Time:** $O(n + V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Count the bounded values.** Allocate a frequency array with $V$ entries and increment `counts[value]` for every value in `nums`. After this scan, `counts[value] == 1` is exactly the definition of uniqueness.

**Search in answer order.** Traverse candidate values from `1000` down to `0`. The first value with frequency one is greater than every remaining candidate and is therefore the required largest unique number. Return immediately when it is found; if the entire domain is scanned without one, return `-1`.

Counting separates the two requirements cleanly: frequency determines whether a value is eligible, and the descending scan determines the greatest eligible value. Every possible input value has exactly one frequency slot, so neither duplicates nor input order can affect the conclusion.

#### Complexity detail

Counting the $n$ input values takes $O(n)$ time and scanning the bounded domain takes $O(V)$ time, for $O(n+V)$ total. The frequency array contains $V$ integers and uses $O(V)$ space; here $V$ is fixed at $1001$.

#### Alternatives and edge cases

- **Hash-map counts:** A dictionary gives expected $O(n)$ counting and stores only observed values, but still needs a maximum over the unique keys and uses space proportional to the number of distinct values.
- **Sort then scan groups:** Sorting makes equal values adjacent and uses $O(n \log n)$ time, which is unnecessary for the bounded domain.
- **Repeated `count` calls:** Testing each candidate with a fresh full-array scan is correct but can take $O(n^2)$ time when many values are distinct.
- **All values repeated:** No frequency equals one, so the required sentinel is `-1`.
- **Zero is unique:** `0` is a valid answer and must not be confused with the `-1` sentinel.

</details>
