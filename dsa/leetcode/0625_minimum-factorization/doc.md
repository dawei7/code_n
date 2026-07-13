# Minimum Factorization

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 625 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-factorization/) |

## Problem Description
### Goal
Given a positive integer `a`, find the smallest positive integer whose decimal digits have a product equal to `a`. The order of the output digits affects the numerical value, so among all valid digit factorizations you must return the numerically smallest one.

For an input smaller than `10`, the one-digit value itself is the smallest result. Otherwise, construct the answer from digit factors `2` through `9`. Return `0` if no such digit factorization exists or if the smallest valid result is greater than the maximum signed 32-bit integer, $2^{31} - 1$.

### Function Contract
**Inputs**

- `a`: a positive 32-bit integer

**Return value**

- The smallest integer whose decimal digits multiply to `a`
- An input below 10 is already its own smallest one-digit result
- Return `0` when no factorization into digits 2 through 9 exists or the smallest result exceeds $2^{31} - 1$

### Examples
**Example 1**

- Input: `a = 48`
- Output: `68`

**Example 2**

- Input: `a = 15`
- Output: `35`

**Example 3**

- Input: `a = 13`
- Output: `0`

### Required Complexity

- **Time:** $O(\log a)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use composite digits to minimize digit count**

Repeatedly divide `a` by candidate digits from 9 down to 2. Large composite digits package several prime factors into one decimal position: for example, 9 replaces two 3s and 8 replaces three 2s. Taking every available large digit therefore avoids a longer representation made from its smaller factors.

**Build the final digits in ascending order**

The factors are discovered from largest to smallest. Add each discovered digit at the current decimal place, starting with the units place. Later, smaller factors occupy more significant places, so the visible number is ordered increasingly from left to right. Among representations with the minimum digit count, that order is numerically smallest.

**Detect impossible prime factors**

After testing digits 9 through 2, a remaining value other than 1 contains a prime factor greater than 7 and cannot be represented by decimal digits. Return zero in that case.

**Respect the special and overflow contracts**

For $a < 10$, return `a` itself. For larger inputs, return zero if the constructed minimum exceeds the signed 32-bit maximum. Since any other valid representation is no smaller, overflow of this minimum proves that no allowed answer exists.

#### Complexity detail

Every successful division reduces the remaining value by at least a factor of two, and there are only eight candidate digits, so the total work is $O(\log a)$. The numeric result, place value, remaining factor, and loop variables use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate candidate integers:** test digit products from 10 upward until one matches; it is correct with feasibility and overflow guards but grows exponentially in the number of required digits.
- **Dynamic programming over divisors:** compute the smallest representation for each divisor state; it is more general but stores many states unnecessary for the fixed digit set.
- **Prime-factor grouping:** count factors 2, 3, 5, and 7, then explicitly combine them into 9, 8, 6, and 4; it reaches the same result with more case analysis.
- Inputs 1 through 9 are already valid one-digit answers and return unchanged.
- A remaining prime factor greater than 7 makes the answer impossible.
- Repeated factors may combine into fewer composite digits, such as `36 -> 49`.
- A representable product can still return zero when its minimum digit number exceeds $2^{31} - 1$.

</details>
