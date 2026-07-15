# Numbers At Most N Given Digit Set

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 902 |
| Difficulty | Hard |
| Topics | Array, Math, String, Binary Search, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) |

## Problem Description
### Goal
You are given an array `digits` of distinct one-character digits sorted in non-decreasing order. Every entry is between `"1"` and `"9"`, so no generated positive integer has a leading-zero issue.

Form positive integers by choosing characters from `digits`, with each available digit usable as many times as desired. The number of chosen positions is not fixed.

Given the positive integer `n`, return how many constructible positive integers are less than or equal to `n`.

### Function Contract
Let $k=\lvert\texttt{digits}\rvert$ and let $d$ be the number of decimal digits in `n`.

**Inputs**

- `digits`: $k$ unique digit strings, sorted in non-decreasing order, where $1 \leq k \leq 9$.
- `n`: an integer with $1 \leq n \leq 10^9$.

**Return value**

Return the count of positive integers no greater than `n` whose every decimal digit belongs to `digits`.

### Examples
**Example 1**

- Input: `digits = ["1","3","5","7"], n = 100`
- Output: `20`

All one- and two-digit choices are valid, giving $4+4^2=20$ numbers.

**Example 2**

- Input: `digits = ["1","4","9"], n = 1000000000`
- Output: `29523`

**Example 3**

- Input: `digits = ["7"], n = 8`
- Output: `1`

### Required Complexity
- **Time:** $O(d\log k)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count every shorter length immediately**

Every constructible number with fewer than $d$ digits is automatically smaller than `n`. For length $\ell$, each of the $\ell$ positions has $k$ choices, so begin with

$$
\sum_{\ell=1}^{d-1} k^\ell.
$$

**Match the boundary length from left to right**

Convert `n` to its decimal string. At position `i`, binary-search `digits` for how many available characters are smaller than `n[i]`. Choosing any such smaller character makes the remaining suffix unrestricted, adding `smaller * k ** remaining` constructible numbers.

If `n[i]` is unavailable, no constructible number can keep matching the prefix, so stop. If it is available, continue to the next position. When every position matches, add one for `n` itself.

Every shorter number is counted once by its length. Among $d$-digit numbers, consider the first position where a candidate differs from `n`. The prefix scan counts it exactly at that position when its digit is smaller, followed by every possible suffix; a larger digit is correctly excluded. The only candidate with no differing position is `n`, added exactly when all of its digits are available. These disjoint groups contain precisely all valid integers at most `n`.

#### Complexity detail

The $d$ boundary positions each perform a binary search among $k$ digits, taking $O(d\log k)$ time. The running count and a constant number of indices use $O(1)$ auxiliary space; the decimal representation has at most ten characters under the fixed input bound.

#### Alternatives and edge cases

- **Digit dynamic programming:** A tight-prefix DP generalizes to zero and repeated constraints, but carries unnecessary state for this zero-free digit set.
- **Enumerate constructible numbers:** Depth-first generation is correct but visits every candidate up to `n` and can grow exponentially with $d$.
- **Test every integer through `n`:** Checking decimal digits directly can take time proportional to `n` and ignores the combinatorial structure.
- **Single available digit:** There is at most one constructible number of each length, and the prefix comparison decides the boundary length.
- **All digits of `n` available:** Add one for `n` after counting numbers that first become smaller at an earlier position.
- **Missing boundary digit:** Stop immediately after adding choices smaller at that position; no equal prefix can continue.
- **`n` shorter than available examples:** Only lengths below $d$ and the valid prefix of length $d$ contribute.
- **Upper bound `1000000000`:** Although `n` has ten digits, its leading `"1"` is handled by the same prefix rule and no generated number may use zero.

</details>
