# Nth Magical Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 878 |
| Difficulty | Hard |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/nth-magical-number/) |

## Problem Description
### Goal
A positive integer is magical when it is divisible by `a` or by `b`. Consider all such positive integers once each and arrange them in increasing order, including numbers divisible by both divisors only once.

Given `n`, `a`, and `b`, find the $n$th magical number in that order. The value itself may be very large, so return it modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the one-based target position, where $1 \leq n \leq 10^9$.
- `a`: a divisor between $2$ and $4\cdot10^4$.
- `b`: a divisor between $2$ and $4\cdot10^4$.
- Let $L=\operatorname{lcm}(a,b)$.

**Return value**

Return the $n$th positive integer divisible by `a` or `b`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 1, a = 2, b = 3`
- Output: `2`

**Example 2**

- Input: `n = 4, a = 2, b = 3`
- Output: `6`

The sequence begins `[2,3,4,6]`.

**Example 3**

- Input: `n = 5, a = 2, b = 4`
- Output: `10`

Every multiple of `4` is already a multiple of `2`, so the magical sequence is the positive even integers.

### Required Complexity
- **Time:** $O(\log(n\min(a,b)))$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count magical numbers at or below a candidate**

For a positive integer $x$, the numbers no greater than $x$ that are divisible by `a` or `b` can be counted by inclusion-exclusion:

$$
C(x)=\left\lfloor\frac{x}{a}\right\rfloor
+\left\lfloor\frac{x}{b}\right\rfloor
-\left\lfloor\frac{x}{L}\right\rfloor.
$$

The final term removes the duplicate count for multiples of both divisors. As $x$ increases, $C(x)$ never decreases, so the predicate $C(x)\geq n$ is monotone.

**Find the first value whose count reaches the target**

The answer is at least `1` and at most `n * min(a, b)`, because the first $n$ multiples of the smaller divisor are all magical. Binary-search that closed value range. If `C(mid) >= n`, retain `mid` as a possible answer by moving the upper bound to it; otherwise, discard `mid` and everything below it.

When the bounds meet, their common value is the smallest $x$ with at least $n$ magical numbers at or below it. Minimality means $x$ itself is magical and occupies position $n$. Apply the modulus only after finding this actual value so it does not disturb ordering or the count comparisons.

#### Complexity detail

The search interval ends at $n\min(a,b)$ and is halved on each iteration. Computing $C(x)$ uses a constant number of arithmetic operations, so time is $O(\log(n\min(a,b)))$. Only fixed scalar state is stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Merge the multiples:** Advancing the next multiple of `a` and `b` generates the sequence correctly but takes $O(n)$ time.
- **Enumerate one least-common-multiple period:** The pattern repeats every $L$, permitting a block calculation, but enumerating and storing a period can be much larger and more intricate than binary search.
- **Test every positive integer:** Divisibility checks require time proportional to the answer and are too slow for the upper bounds.
- **Equal divisors:** When `a == b`, every magical number is a multiple of that shared value and inclusion-exclusion still counts it once.
- **One divisor divides the other:** The least-common-multiple subtraction collapses the count to the multiples of the smaller divisor.
- **Common multiples:** A value divisible by both `a` and `b` occupies only one position in the sequence.
- **Modulo timing:** Reduce only the final answer; applying the modulus during binary search would destroy the monotone numeric order.
- **Wide arithmetic:** Fixed-width implementations need a type capable of representing `n * min(a, b)` and the intermediate least common multiple.

</details>
