# Mice and Cheese

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2611 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/mice-and-cheese/) |

## Problem Description

### Goal

There are two mice and $n$ different types of cheese. Every cheese type must be eaten by exactly one mouse. If the first mouse eats cheese type $i$, it contributes `reward1[i]` points; if the second mouse eats it, it contributes `reward2[i]` points instead.

Choose an assignment that makes the first mouse eat exactly `k` cheese types and maximizes the combined score earned by both mice. The second mouse eats every type not assigned to the first mouse.

### Function Contract

**Inputs**

- `reward1`: A positive integer array of length $n$ containing the first mouse's reward for each cheese type.
- `reward2`: A positive integer array of the same length containing the second mouse's reward for each cheese type.
- `k`: The exact number of cheese types assigned to the first mouse, where $0 \leq k \leq n$.

The shared constraints are $1 \leq n \leq 10^5$ and $1 \leq \texttt{reward1[i]}, \texttt{reward2[i]} \leq 1000$.

**Return value**

Return the maximum total points obtainable under the exact-`k` assignment rule.

### Examples

#### Example 1

- **Input:** `reward1 = [1, 1, 3, 4], reward2 = [4, 4, 1, 1], k = 2`
- **Output:** `15`
- **Explanation:** Assigning indices `2` and `3` to the first mouse gives `3 + 4`; the second mouse receives indices `0` and `1`, adding `4 + 4`.

#### Example 2

- **Input:** `reward1 = [1, 1], reward2 = [1, 1], k = 2`
- **Output:** `2`
- **Explanation:** The first mouse must eat both cheese types, and each contributes one point.
