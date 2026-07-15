# Restore The Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1416 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/restore-the-array/) |

## Problem Description

### Goal

An integer array was converted into one digit string by concatenating the decimal representations of its elements. Every original element was between $1$ and `k`, inclusive, and none of those decimal representations had a leading zero.

Given the resulting string `s` and the limit `k`, count how many different arrays could have produced `s`. Different split positions define different arrays. Return the count modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `s`: a digit string of length $n$, where $1 \le n \le 10^5$ and every character is from `0` through `9`.
- `k`: the largest permitted array value, where $1 \le k \le 10^9$.

**Return value**

- The number of valid ways to split `s` into decimal integers from $1$ through `k` with no leading zeros, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `s = "1000", k = 10000`
- Output: `1`

**Example 2**

- Input: `s = "1000", k = 10`
- Output: `0`

**Example 3**

- Input: `s = "1317", k = 2000`
- Output: `8`

### Required Complexity

- **Time:** $O(n \log k)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Define a suffix count.** Let `dp[i]` be the number of valid arrays represented by the suffix beginning at index `i`. The empty suffix has one valid completion, so `dp[n] = 1`. Compute states from right to left.

A piece cannot begin at `s[i]` when that character is `0`, because every element must be positive and leading zeros are forbidden. Otherwise, extend a numeric value one digit at a time from `i`. For every endpoint whose value remains at most `k`, add the completion count immediately after that endpoint. Stop as soon as the value exceeds `k`; adding more digits can only make a positive decimal integer larger.

Only the first $O(\log k)$ digits can form a permitted value. Each valid restored array has one unique first split and a valid suffix counted by the corresponding later state. Conversely, every transition chooses an allowed first element and joins it to a valid suffix. These disjoint choices prove that their sum is exactly `dp[i]`, so `dp[0]` is the required count.

#### Complexity detail

At each of the $n$ starting positions, at most $\lfloor \log_{10} k \rfloor + 1$ digits are examined. Time is $O(n \log k)$, where the logarithm represents the decimal digit count up to a constant base factor. The dynamic-programming array uses $O(n)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** Cache the count from each index. It has the same asymptotic work but recursion depth can reach $n$.
- **Unmemoized backtracking:** Explore every split directly. It repeats suffix work and can take exponential time.
- **Leading zero:** Any state beginning with `0` contributes zero, even if a longer substring would have a positive numeric value.
- **Internal zero:** Zero digits are allowed inside a multi-digit value such as `10`; only the first digit is restricted.
- **Value equal to k:** The upper bound is inclusive.
- **Long input:** Accumulate digits numerically and stop after the maximum relevant length instead of converting every possible substring.
- **Modulo:** Reduce each state while summing transitions.

</details>
