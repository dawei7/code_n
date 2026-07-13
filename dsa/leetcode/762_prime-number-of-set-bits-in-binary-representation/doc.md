# Prime Number of Set Bits in Binary Representation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 762 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) |

## Problem Description

### Goal

Given integers `left` and `right`, consider every integer in the inclusive range `[left, right]`. For each value, count the set bits—the `1` digits—in its binary representation.

Return how many range values have a prime number of set bits. Primality applies to the bit count rather than to the integer itself; counts such as `2`, `3`, and `5` qualify, while `0` and `1` are not prime. Both interval endpoints are included.

### Function Contract

**Inputs**

- `left`: the positive lower endpoint of the range.
- `right`: the upper endpoint, with `left <= right`.

**Return value**

- The number of values in `[left, right]` whose set-bit count is prime.

### Examples

**Example 1**

- Input: `left = 6`, `right = 10`
- Output: `4`
- Explanation: `6`, `7`, `9`, and `10` have respectively `2`, `3`, `2`, and `2` set bits.

**Example 2**

- Input: `left = 10`, `right = 15`
- Output: `5`
- Explanation: Every value except `15`, which has four set bits, qualifies.

**Example 3**

- Input: `left = 1`, `right = 1`
- Output: `0`
- Explanation: One set bit is not a prime count.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count bits for every value in the interval**

Visit each integer from `left` through `right` once. A population-count operation gives the number of `1` bits in its binary representation. Increment the answer exactly when that count belongs to the fixed set of primes.

**Why the prime set is constant**

The input values have a bounded machine-word size, so their population count also has a small fixed upper bound. The only relevant prime counts are `2, 3, 5, 7, 11, 13, 17, 19`. Membership in this constant set takes constant expected time.

Each range value contributes once. The algorithm increments for a value precisely when its set-bit count is in the prime set, which is the definition of a qualifying integer. The final total therefore counts exactly the requested values.

#### Complexity detail

Let `n = right - left + 1`. With a fixed-width population-count operation and constant-size prime lookup, the scan takes $O(n)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prime bit mask:** Encode all prime bit counts in one integer and test the population count with a shift and mask; this has the same $O(n)$ time and $O(1)$ space.
- **Explicit bit loop:** Repeatedly clear the lowest set bit or shift each number to count ones, adding a logarithmic factor when integer width is treated as variable.
- **Test primality separately:** Trial division is unnecessary because the possible counts are tiny and fixed.
- **One-element range:** Return either zero or one according to that value's bit count.
- **Counts zero and one:** Neither is prime.
- **Powers of two:** They have one set bit and never qualify.
- **Inclusive upper endpoint:** The loop must examine `right` itself.

</details>
