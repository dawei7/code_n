# All Divisions With the Highest Score of a Binary Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2155 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/) |

## Problem Description

### Goal

Given a 0-indexed binary array `nums` of length $n$, consider every division
index $i$ from $0$ through $n$. The left part contains the elements at indices
$0$ through $i-1$, and the right part contains the elements at indices $i$
through $n-1$. Either part may be empty: the left part is empty when $i=0$,
and the right part is empty when $i=n$.

The division score is the number of zeros in the left part plus the number of
ones in the right part. Return all distinct division indices whose score is
the highest possible. The platform accepts the indices in any order.

### Function Contract

**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 10^5$ and every
  element is either `0` or `1`.

**Return value**

A list containing every index $i$, $0 \le i \le n$, that attains the maximum
division score.

### Examples

#### Example 1

- **Input:** `nums = [0, 0, 1, 0]`
- **Output:** `[2, 4]`
- **Explanation:** Divisions `2` and `4` both score `3`, which is the maximum.

#### Example 2

- **Input:** `nums = [0, 0, 0]`
- **Output:** `[3]`
- **Explanation:** Placing all three zeros on the left gives the unique maximum
  score.

#### Example 3

- **Input:** `nums = [1, 1]`
- **Output:** `[0]`
- **Explanation:** Keeping both ones on the right gives the unique maximum score.
