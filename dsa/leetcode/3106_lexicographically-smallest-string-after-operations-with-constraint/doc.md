# Lexicographically Smallest String After Operations With Constraint

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3106 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [lexicographically-smallest-string-after-operations-with-constraint](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/) |

## Problem Description

### Goal

Given a lowercase string `s` and an integer budget `k`, measure the distance between two equal-length strings position by position. Place the lowercase English letters in cyclic order, so `a` and `z` are adjacent. If letters are represented by integers from $0$ through $25$, their minimum cyclic distance is

$$
d(x,y)=\min\bigl(\lvert x-y\rvert,\ 26-\lvert x-y\rvert\bigr).
$$

The distance between two strings is the sum of this value over corresponding positions. For example, `distance("ab", "cd") == 4`, while `distance("a", "z") == 1` because the alphabet wraps around.

You may change any character of `s` to any lowercase English letter, and may perform any number of changes. Return the lexicographically smallest string `t` whose total distance from `s` is at most `k`.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 100$, consisting only of lowercase English letters.
- `k`: The maximum allowed total cyclic distance, where $0 \le k \le 2000$.

**Return value**

- The lexicographically smallest length-$n$ string `t` satisfying `distance(s, t) <= k`.

### Examples

#### Example 1

- **Input:** `s = "zbbz", k = 3`
- **Output:** `"aaaz"`
- **Explanation:** Changing the first three characters to `a` costs $1+1+1=3$.

#### Example 2

- **Input:** `s = "xaxcd", k = 4`
- **Output:** `"aawcd"`
- **Explanation:** Changing the first `x` to `a` costs $3$ through the cyclic wrap, and changing the second `x` backward to `w` costs the remaining $1$.

#### Example 3

- **Input:** `s = "lol", k = 0`
- **Output:** `"lol"`
- **Explanation:** A zero budget permits no positive-distance change.
