# The Number of Good Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1994 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Counting, Number Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-good-subsets/) |

## Problem Description

### Goal

Given an integer array `nums`, call a non-empty choice of its elements good when the chosen elements' product is a product of one or more distinct prime numbers. Equivalently, the product must be square-free and greater than $1$: no prime may occur twice in its factorization, while factors equal to $1$ do not alter it.

A subset is determined by indices, so equal values at different positions produce different choices. Any indices may be deleted, including none or all, although an empty choice and a choice containing only ones are not good. Count all different good subsets and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $1 \le N \le 10^5$ and every value is between $1$ and $30$ inclusive.
- Let $U=30$ be the value-domain size and let $P=10$ be the number of primes not exceeding $30$.

**Return value**

Return the number of index-distinct good subsets modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `6`
- Explanation: The valid index choices produce `[2]`, `[3]`, `[2, 3]`, and the same three products with the single `1` included. The value `4` repeats prime factor $2$ and cannot appear.

**Example 2**

- Input: `nums = [4, 2, 3, 15]`
- Output: `5`
- Explanation: The good subsets are `[2]`, `[3]`, `[15]`, `[2, 3]`, and `[2, 15]`.

**Example 3**

- Input: `nums = [1, 1, 2]`
- Output: `4`
- Explanation: The index containing `2` is required, and either, both, or neither of the two indices containing `1` may accompany it.

### Required Complexity

- **Time:** $O(N+U2^P)$
- **Space:** $O(2^P)$

<details>
<summary>Approach</summary>

#### General

**Encode the only relevant prime factors.** There are ten primes at most $30$. Assign one bit to each. For every value from $2$ through $30$, factor it once: if some prime square divides it, the value can never belong to a good subset; otherwise, its bitmask records exactly the distinct primes in that value.

**Count equal values before choosing them.** Suppose a valid value occurs $c$ times. A good subset can use at most one occurrence because two copies repeat every prime in its mask, but there are $c$ different indices from which to choose that one occurrence. Processing the value once with multiplier $c$ preserves index-distinct counting without repeating the full dynamic program for every array element.

**Build compatible products with mask DP.** Let `ways[mask]` count choices whose product uses exactly the primes in `mask`, beginning with `ways[0] = 1`. For each valid value mask, extend only states disjoint from it. The combined state is `mask | value_mask`, and its added count is the old state's count multiplied by the value's frequency. Iterating masks downward ensures states created for the current value are not reused during the same step.

**Treat ones after all prime-bearing choices.** Ones set no prime bits, so any subset of the indices containing `1` can accompany every nonempty prime mask. If there are $c_1$ ones, multiply the sum of `ways[1:]` by $2^{c_1}$. Excluding `ways[0]` prevents the empty product, including choices made solely of ones, from being counted.

#### Complexity detail

Counting the input costs $O(N)$ time. Factoring the fixed value domain and updating all $2^P$ masks for at most $U$ values costs $O(U2^P)$ time. The frequency table is bounded by $U$, and the dynamic-programming table uses $O(2^P)$ space. Here $U=30$ and $P=10$, but the displayed bounds preserve the roles of those quantities.

#### Alternatives and edge cases

- **Enumerate subsets:** Testing all index choices takes $O(2^N)$ time and is impossible at the maximum input length.
- **Run the mask transition for every occurrence:** This can remain correct because overlapping masks prevent duplicate prime use, but it costs $O(N2^P)$ instead of aggregating equal values first.
- Values divisible by $4$, $9$, or $25$ contain a squared prime factor and must be discarded even when their other factors are distinct.
- Multiple copies of a valid value contribute their frequency as alternative index choices; they may not be selected together.
- Ones multiply valid choices but never create a good subset by themselves.
- Apply the modulus during transitions and modular exponentiation so large duplicate and one counts remain bounded.

</details>
