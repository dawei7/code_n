# Numbers With Same Consecutive Differences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 967 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [numbers-with-same-consecutive-differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) |

## Problem Description

### Goal

Given integers `n` and `k`, generate every positive integer with exactly `n` decimal digits such that the absolute difference between each pair of consecutive digits is exactly `k`.

The first digit cannot be zero, because representations with leading zeroes do not count as `n`-digit integers. Zero may appear in later positions. Return all valid integers in any order, without duplicates.

### Function Contract

**Inputs**

- `n`: the required number of digits, where $2 \le n \le 9$.
- `k`: the required absolute difference, where $0 \le k \le 9$.
- Let $F_\ell$ be the number of valid length-$\ell$ prefixes generated from nonzero first digits, and define

$$
T = \sum_{\ell=1}^{n} F_\ell,
\qquad
F = \max_{1\le \ell\le n} F_\ell.
$$

**Return value**

Return all `n`-digit integers whose adjacent digits differ by exactly `k`; result order is unrestricted.

### Examples

**Example 1**

- Input: `n = 3, k = 7`
- Output: `[181,292,707,818,929]`
- Explanation: A leading-zero form such as `070` is not a three-digit integer and is excluded.

**Example 2**

- Input: `n = 2, k = 1`
- Output: `[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]`

### Required Complexity

- **Time:** $O(T)$
- **Space:** $O(F)$

<details>
<summary>Approach</summary>

#### General

**Start with every legal leading digit.** The one-digit frontier is `[1,2,...,9]`; beginning here prevents leading zeroes without adding a later special case.

**Extend only valid prefixes.** For each current number, inspect its last digit `d`. The only possible next digits are `d - k` and `d + k`. Append each candidate that lies from `0` through `9`, constructing the new number with `number * 10 + next_digit`. Repeating this breadth-first expansion until the prefixes have length `n` produces only valid numbers.

**Avoid the `k = 0` duplicate.** When `k` is zero, the two candidate formulas name the same digit. Iterate over their set, or otherwise suppress the duplicate, so each result appears once. For positive `k`, the candidates are distinct whenever both are in range.

**Why the frontier is complete.** Every valid number has a nonzero leading digit and, at each later position, its next digit must be one of the two candidates derived from the previous digit. Inductively, its prefix appears at every expansion level and the full number reaches the final frontier. Thus the returned frontier contains exactly all valid answers.

#### Complexity detail

Every generated prefix is extended once, so the total work is $O(T)$. Only the current and next frontiers are needed; their maximum size, including the returned final list, is $O(F)$.

#### Alternatives and edge cases

- **Depth-first backtracking:** Recursively choose the next valid digit and append at depth `n`. It has the same output-sensitive bounds and uses an additional depth-$n$ call stack.
- **Scan all `n`-digit integers:** Check every adjacent pair of every candidate number. This examines $9\times10^{n-1}$ integers and wastes nearly all work.
- **Linear duplicate search:** Before appending each new prefix, scan the whole next frontier to see whether it already exists. This is correct but can make a level quadratic in its frontier size.
- **Zero difference:** Each answer repeats one nonzero digit, producing exactly nine results.
- **Difference nine:** The only possible adjacent transition is between `9` and `0`.
- **Internal zero:** Values such as `101` are valid when their adjacent differences satisfy `k`; only a leading zero is forbidden.

</details>
