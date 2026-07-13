# Factor Combinations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/factor-combinations/) |

## Problem Description
### Goal
Given a positive integer `n`, find every way to express it as a product of at least two integer factors. Every factor must be greater than `1` and strictly smaller than `n`, so the trivial one-factor representation `[n]` is excluded.

Return each distinct factor combination once, writing factors within a combination in nondecreasing order so permutations do not create duplicates. The product of all entries must equal `n` exactly, and combinations may contain repeated factors when divisibility permits. Outer result order is unrestricted. Prime values and other inputs with no nontrivial factorization return an empty list.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

All unique nondecreasing factor combinations whose product is `n`.

### Examples
**Example 1**

- Input: `n = 12`
- Output: `[[2,6],[3,4],[2,2,3]]`

**Example 2**

- Input: `n = 37`
- Output: `[]`

**Example 3**

- Input: `n = 16`
- Output: `[[2,8],[4,4],[2,2,4],[2,2,2,2]]`

### Required Complexity

- **Time:** $O(\sqrt{n} + output)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Canonical order removes permutation duplicates**

Backtrack with a remaining product and a minimum allowed factor. Try divisors only through the square root of the remainder. For every divisor `f`, emit the completed pair `f, remainder / f`, then recurse so that the quotient may be split further.

The current path is nondecreasing, every chosen value divides the previous remainder, and `product(path) * remainder = n`. Passing `f` as the next minimum preserves canonical order.

**The smallest remaining factor is always discoverable**

In any nontrivial factorization of `remainder`, its smallest factor cannot exceed `sqrt(remainder)`. The divisor loop therefore reaches the first factor of every valid continuation. Emitting its paired quotient covers the two-factor completion; recursing covers decompositions of that quotient. Since factors may only be appended in nondecreasing order, every factor multiset follows one canonical path and cannot reappear as a permutation.

#### Complexity detail

Divisor exploration is output-sensitive, with a top-level $O(\sqrt{n})$ scan and work proportional to generated combinations. Recursion depth is at most $O(\log n)$ because every selected factor is at least two, excluding returned output storage.

#### Alternatives and edge cases

- **Generate ordered factor sequences:** repeats permutations and requires expensive deduplication.
- Prime numbers and values below four have no valid combination; repeated factors remain valid.

</details>
