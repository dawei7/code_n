# Linked List Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3063 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-frequency/) |

## Problem Description

### Goal

You are given the head of a singly linked list. Suppose its nodes contain exactly $k$ distinct values.

Construct and return the head of a new linked list containing $k$ nodes. For every distinct value in the input, the output must contain one node whose value is that input value's frequency. The frequency nodes may appear in any order; the distinct input values themselves do not appear in the result unless one of them also happens to be a frequency.

### Function Contract

**Inputs**

- `head`: The first node of a non-empty singly linked list containing $n$ integers.

The list satisfies $1 \le n \le 10^5$, and every node value is in the range $1$ through $10^5$. Let $k$ denote the number of distinct values in the list.

**Return value**

Return the head of a $k$-node linked list containing each distinct input value's occurrence count exactly once. Any ordering of those $k$ frequencies is valid.

### Examples

**Example 1**

- Input: `head = [1, 1, 2, 1, 2, 3]`
- Output: `[3, 2, 1]`
- Explanation: The values `1`, `2`, and `3` occur three, two, and one times, respectively. Any permutation of `[3, 2, 1]` is also valid.

**Example 2**

- Input: `head = [1, 1, 2, 2, 2]`
- Output: `[2, 3]`
- Explanation: The two distinct values occur two and three times.

**Example 3**

- Input: `head = [6, 5, 4, 3, 2, 1]`
- Output: `[1, 1, 1, 1, 1, 1]`
- Explanation: All six input values are distinct, so every frequency is one.
