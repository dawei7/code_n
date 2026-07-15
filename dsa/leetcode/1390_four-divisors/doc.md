# Four Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1390 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/four-divisors/) |

## Problem Description

### Goal

Given an integer array `nums`, examine the positive divisors of every value independently. A value contributes only when it has exactly four distinct positive divisors; its contribution is the sum of those four divisors.

Values with fewer or more than four divisors contribute zero. Return the sum of all qualifying contributions across the array. Equal values at different positions are separate occurrences and each can contribute.

### Function Contract

**Inputs**

- `nums`: an array of $m$ positive integers, where $1 \le m \le 10^4$ and `nums[i]` is at most $10^5$.

Let $V = \max(\texttt{nums})$.

**Return value**

- The total of the divisor sums for precisely those array entries that have exactly four positive divisors.

### Examples

**Example 1**

- Input: `nums = [21,4,7]`
- Output: `32`
- Explanation: `21` has divisors `1, 3, 7, 21`, while `4` and `7` do not have four divisors.

**Example 2**

- Input: `nums = [21,21]`
- Output: `64`
- Explanation: Each occurrence of `21` contributes `32`.

**Example 3**

- Input: `nums = [8,9,16]`
- Output: `15`
- Explanation: `8` contributes `1 + 2 + 4 + 8`; the square `9` has three divisors, and `16` has five.

### Required Complexity

- **Time:** $O(m\sqrt{V})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Divisors arrive in complementary pairs.** Every divisor $d$ of a value $x$ has a partner $x/d$. Apart from a perfect-square root, one member of each pair is at most $\sqrt{x}$ and the other is at least $\sqrt{x}$. It is therefore enough to test candidate divisors from `2` through `isqrt(x)`; `1` and `x` are always the first pair.

Track whether exactly one additional factor pair has been found. When `x % d == 0`, let `other = x // d`. If `d == other`, then $x$ is a perfect square and this unpaired square root prevents the divisor count from being four. Otherwise add both factors to the tentative sum. A second additional pair proves that the value has more than four divisors, so it contributes zero and its scan can stop.

If the scan ends with exactly one distinct additional pair, the complete divisor set is `1`, `x`, `d`, and `x // d`, so the accumulated sum is valid. With no additional pair, the value is prime or one and has too few divisors. Because every possible pair has a representative in the scanned range, ending with exactly one pair also proves that no omitted divisor can create a fifth divisor.

#### Complexity detail

For each of the $m$ values, at most $\lfloor\sqrt{x}\rfloor - 1$ candidates are tested. Since $x \le V$, total time is $O(m\sqrt{V})$. The counters and tentative sum occupy $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every integer through the value:** Testing all candidates from $1$ to $x$ is straightforward and correct, but costs $O(mx)$ in the worst case instead of using paired divisors.
- **Prime factorization:** Exactly four divisors occur for $p^3$ or $pq$ with distinct primes. Factoring each number can exploit that characterization, but trial division has the same asymptotic bound and requires more bookkeeping.
- **Perfect squares:** A discovered pair with equal members contributes only one distinct divisor; such a value cannot have exactly four divisors.
- **More than one interior pair:** The value has at least six divisors and must contribute zero rather than a partial sum.
- **Primes and one:** They have fewer than four divisors and contribute zero.
- **Repeated values:** Every array position contributes independently, even when its value occurred earlier.

</details>
