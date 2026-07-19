# Next Greater Numerically Balanced Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Backtracking, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-numerically-balanced-number/) |

## Problem Description

### Goal

An integer is *numerically balanced* when each digit that appears in its decimal representation occurs exactly as many times as the digit's value. For example, `22` is balanced because digit `2` occurs twice, while `1022` is not: the presence of digit `0` would require it to occur zero times, which is impossible once it appears.

Given an integer `n`, find the smallest numerically balanced integer that is strictly greater than `n`. The answer must therefore satisfy both the digit-frequency rule and the minimality requirement; returning `n` itself is never allowed, even when `n` is already balanced.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^6$.

**Return value**

- Return the smallest integer greater than `n` for which every occurring digit $d$ appears exactly $d$ times.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `22`
- Explanation: Digit `2` occurs exactly twice, and no smaller balanced integer is greater than `1`.

**Example 2**

- Input: `n = 1000`
- Output: `1333`
- Explanation: Digit `1` occurs once and digit `3` occurs three times. A value such as `1022` is invalid because an occurring zero can never have zero occurrences.

**Example 3**

- Input: `n = 3000`
- Output: `3133`
- Explanation: `3133` has one `1` and three `3` digits and is the first balanced value after `3000`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Deriving every possible digit multiset**

A balanced number cannot contain `0`, and choosing any other digit fixes its multiplicity: choosing `3`, for example, contributes exactly three copies of `3`. Enumerate subsets of digits `1` through `7`, retain only those whose required multiplicities total at most seven positions, and form every distinct permutation of each resulting multiset. Seven positions are sufficient because $n \le 10^6$ and the balanced value `1224444` guarantees an answer within that length.

**Selecting the strict successor**

Convert the permutations to integers, remove duplicates, and sort them. A right-biased binary search locates the first generated value strictly greater than `n`. Every generated number has exactly the required multiplicity for each selected digit, while every balanced number of relevant length corresponds to one enumerated subset and one of its permutations. The binary-search successor is therefore both valid and minimal.

#### Complexity detail

The source constraint fixes the representation at no more than seven digits. Only $2^7-1$ nonempty digit subsets can be considered, just 18 of them fit within seven positions, and they produce 278 distinct balanced values. Generation, storage, sorting, and binary search are therefore all bounded by constants independent of `n`, giving $O(1)$ time and $O(1)$ space under the legal contract.

#### Alternatives and edge cases

- **Forward enumeration:** Test successive integers and count each candidate's digits. This is simple and accepted by the platform, but a large gap can perform hundreds of thousands of interpreted iterations.
- **Precomputed balanced values:** A sorted constant table permits binary search, but embedding unexplained answers is less maintainable than deriving them.
- A candidate containing `0` is always invalid because zero cannot appear exactly zero times while being present.
- Starting from `n + 1` enforces the strict inequality when `n` is itself balanced.
- For `n = 0`, the answer is `1`, whose only digit occurs once.

</details>
