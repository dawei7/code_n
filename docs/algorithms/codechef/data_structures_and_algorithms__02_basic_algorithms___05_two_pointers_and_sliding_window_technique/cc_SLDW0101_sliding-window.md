# Sliding Window

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLDW0101 |
| Difficulty Rating | 932 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SLDW0101](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0101) |

---

## Problem Statement

The sliding window technique is a subset of two pointers, where the two pointers move in the same direction and the elements between these two pointers are considered to be inside the window. This window can move along the array. This technique is used when we need to find some sub-array in the array.

We'll look at some sliding window examples in the next problems and how we can solve them.

---

## Input Format

- The first line of the input contains a single integer $N$, denoting the length of the array $A$.
- The second line of the input contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

- Output the two indices $i$ and $j$.

---

## Constraints

- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
