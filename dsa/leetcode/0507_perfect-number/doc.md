# Perfect Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 507 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/perfect-number/) |

## Problem Description
### Goal
Given a positive integer `num`, a positive divisor is an integer that divides it evenly. The proper positive divisors exclude `num` itself but include `1`; paired factors must each be counted once, including the square root only once when `num` is a perfect square.

Return `True` exactly when `num` equals the sum of all its proper positive divisors, which makes it a perfect number, and return `False` otherwise. The value `1` is not perfect because it has no positive divisor smaller than itself. The function returns only the classification, not the divisor list or sum.

### Function Contract
**Inputs**

- `num`: a positive integer

**Return value**

- `True` when `num` is perfect; otherwise `False`

### Examples
**Example 1**

- Input: `num = 28`
- Output: `True`

**Example 2**

- Input: `num = 7`
- Output: `False`

**Example 3**

- Input: `num = 1`
- Output: `False`

### Required Complexity

- **Time:** $O(\sqrt{num})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Start with the universal proper divisor**

Every integer greater than one has proper divisor `1`, so initialize the sum with `1`. The number `1` itself has no positive divisor smaller than itself and must be rejected separately.

**Discover divisors in complementary pairs**

If `divisor` divides `num`, then `floor(num / divisor)` is a divisor as well. At least one member of every pair is no larger than `sqrt(num)`, so test candidates from `2` while `divisor * divisor <= num`. Add both members when divisible.

**Avoid counting a square root twice**

For a perfect square, the pair collapses to one value at `divisor * divisor = num`. Add that divisor only once. Every proper divisor other than `1` then appears in exactly one discovered pair: its smaller partner reaches the loop, and the larger partner is recovered by division. Comparing the complete sum with `num` gives the required result.

#### Complexity detail

The loop tests at most `floor(sqrt(num)) - 1` candidates, so time is $O(\sqrt{num})$. The running sum and loop variables use $O(1)$ space.

#### Alternatives and edge cases

- **Test every value below `num`:** is direct but takes $O(num)$ time.
- **Prime factorization formula:** can derive the divisor sum from prime exponents, but trial factorization still takes $O(\sqrt{num})$ time and is more elaborate here.
- **Known-perfect-number table:** is constant time only for a fixed constraint and does not implement the mathematical test generally.
- **One:** is not perfect because it has no proper positive divisors.
- **Prime input:** has proper-divisor sum `1` and is not perfect.
- **Perfect square:** its square-root divisor must contribute once.
- **Two:** initializes the sum to `1` but still correctly fails the equality test.

</details>
