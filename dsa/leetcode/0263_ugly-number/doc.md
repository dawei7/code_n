# Ugly Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 263 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number/) |

## Problem Description
### Goal
An ugly number is a positive integer whose prime factors, if any, are limited to `2`, `3`, and `5`. Repeated factors are allowed, and `1` is included because it has no prime factors outside the permitted set.

Given an integer `n`, return `True` when it is ugly and `False` otherwise. Zero and negative integers are never ugly. A positive number fails as soon as any remaining prime factor other than `2`, `3`, or `5` is required, even when it also contains permitted factors; the task returns only the classification, not a factorization.

### Function Contract
**Inputs**

- `n`: an integer

**Return value**

`True` exactly when `n` is positive and all of its prime factors belong to `{2,3,5}`.

### Examples
**Example 1**

- Input: `n = 6`
- Output: `true`

**Example 2**

- Input: `n = 1`
- Output: `true`

**Example 3**

- Input: `n = 14`
- Output: `false`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Strip the only permitted prime factors**

Reject nonpositive inputs. For each prime in `2, 3, 5`, repeatedly divide while it is a factor. The remaining quotient reveals whether any disallowed prime factor exists.

At every step, the current quotient times the removed factors equals the original `n`. After processing one allowed prime, that prime no longer divides the quotient.

**The residual quotient is a complete certificate**

If the final quotient is one, the removed twos, threes, and fives reconstruct the original number, proving that no other prime factor is needed. If a quotient greater than one remains, unique prime factorization gives it some prime divisor. All factors `2`, `3`, and `5` were removed exhaustively, so that divisor is disallowed and the original number cannot be ugly.

#### Complexity detail

Every division reduces the positive quotient by at least a factor of two, so there are $O(\log n)$ divisions. Only the quotient and loop variables are stored.

#### Alternatives and edge cases

- **Trial-divide by every possible factor:** does unnecessary work up to the square root.
- One is ugly as the empty product; zero and negative values are not.

</details>
