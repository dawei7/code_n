# Number Of Rectangles That Can Form The Largest Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1725 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/) |

## Problem Description

### Goal

You are given an array `rectangles`, where `rectangles[i] = [l_i, w_i]` gives the length and width of the $i$-th rectangle. A rectangle may be cut into a square of side length $k$ whenever $k \le l_i$ and $k \le w_i$. Consequently, the largest square obtainable from that rectangle has side length $\min(l_i,w_i)$.

Let `maxLen` be the greatest square side length obtainable from any supplied rectangle. Return how many rectangles can produce a square whose side length is exactly `maxLen`. Each input pair contains two positive, unequal dimensions, although different rectangles may yield the same maximum square size.

### Function Contract

**Inputs**

- `rectangles`: an array of $n$ pairs `[l_i, w_i]`, where $1 \le n \le 1000$, each pair has exactly two entries, $1 \le l_i,w_i \le 10^9$, and $l_i \ne w_i$.

**Return value**

- Return the number of rectangles whose smaller dimension equals the largest smaller dimension in the array.

### Examples

**Example 1**

- Input: `rectangles = [[5,8],[3,9],[5,12],[16,5]]`
- Output: `3`
- Explanation: The largest square sides available from the four rectangles are `5`, `3`, `5`, and `5`, so three rectangles attain `maxLen = 5`.

**Example 2**

- Input: `rectangles = [[2,3],[3,7],[4,3],[3,7]]`
- Output: `3`
- Explanation: The obtainable maximum sides are `2`, `3`, `3`, and `3`.

**Example 3**

- Input: `rectangles = [[100,1]]`
- Output: `1`
- Explanation: With one rectangle, its smaller dimension necessarily determines `maxLen`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce each rectangle to one relevant value**

A square cut from `[l_i, w_i]` must fit within both dimensions, so its side cannot exceed $\min(l_i,w_i)$. That bound is also attainable by cutting along the longer dimension. Therefore, every rectangle is represented completely for this task by `side = min(length, width)`; the larger dimension cannot affect either the global optimum or the count.

**Maintain the best side and its frequency**

Scan the rectangles once while storing `best_side` and `count`. When `side` exceeds `best_side`, the new rectangle establishes a strictly better `maxLen`, so discard the obsolete count and set `count = 1`. When `side` equals `best_side`, increment the count. A smaller side changes neither value.

After any processed prefix, `best_side` is the largest attainable square side in that prefix, and `count` is exactly its frequency. Each update preserves those two facts. Once the entire array has been processed, they describe the required `maxLen` and the number of rectangles that can produce it.

#### Complexity detail

Let $n$ be the number of rectangles. The scan computes one minimum and performs constant additional work for each rectangle, taking $O(n)$ time. Only the current best side, its count, and the current pair are retained, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Two passes:** One pass can compute the largest smaller dimension and a second can count its occurrences. This is also $O(n)$ time and $O(1)$ space, but the one-pass update combines both tasks without revisiting the input.
- **Sort all attainable sides:** Sorting makes the maximum and its trailing frequency easy to identify, but costs $O(n\log n)$ time and $O(n)$ storage for a separately constructed side array.
- **Single rectangle:** Its smaller dimension is automatically the global maximum, so the answer is one.
- **Orientation:** `[a,b]` and `[b,a]` have the same attainable square side because only their minimum matters.
- **Tied maxima:** Every rectangle with the maximum smaller dimension counts, regardless of its larger dimension.
- **Maximum dimensions:** Values up to $10^9$ require only comparison; no multiplication or area calculation is needed.

</details>
