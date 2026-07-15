# Check If It Is a Good Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1250 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-it-is-a-good-array/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. You may select a nonempty subset of its values, multiply every selected value by an arbitrary integer, and add the resulting products.

The array is *good* when some choice of subset and integer multipliers produces a sum equal to $1$. Return whether `nums` is good. Multipliers may be positive, negative, or zero; the question concerns existence rather than constructing the subset or coefficients.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- Let $M = \max(\texttt{nums})$.

**Return value**

- Return `true` if an integer linear combination of selected array values can equal $1$; otherwise return `false`.

### Examples

**Example 1**

- Input: `nums = [12, 5, 7, 23]`
- Output: `true`
- Explanation: The values admit an integer linear combination equal to $1$.

**Example 2**

- Input: `nums = [29, 6, 10]`
- Output: `true`
- Explanation: For example, $29 + 6 - 3 \cdot 10 = 5$ and further integer combinations yield $1$ because the common greatest divisor is $1$.

**Example 3**

- Input: `nums = [3, 6]`
- Output: `false`
- Explanation: Every integer linear combination is divisible by $3$, so it cannot equal $1$.

### Required Complexity

- **Time:** $O(n \log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The set of all integer linear combinations of a collection of integers is exactly the set of multiples of their greatest common divisor. Consequently, the question is equivalent to asking whether the greatest common divisor of all values in `nums` is $1$.

**Why subsets do not change the criterion**

Choosing a subset is equivalent to assigning coefficient zero to every omitted value. Bézout's identity says that the greatest common divisor of all array values can itself be written as an integer linear combination of them. Therefore, when the overall greatest common divisor is $1$, suitable coefficients exist and the array is good.

Conversely, every array value is divisible by the overall greatest common divisor. Every integer multiple and every sum of those multiples remains divisible by it. If that divisor is greater than $1$, no subset and no integer coefficients can produce $1$.

**Accumulating the common divisor**

Start with `current = 0` and update `current = gcd(current, value)` for each value. Since $\gcd(0,x)=x$, the first update initializes the accumulator naturally. Once `current == 1`, it can never increase again, so returning `true` immediately is safe. If the scan ends without reaching $1$, return `false`.

#### Complexity detail

Euclid's algorithm takes $O(\log M)$ time per value in the stated upper bound, so processing $n$ values takes $O(n \log M)$ time. The accumulator uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prime-factor intersection:** Factor every number and test whether any prime divides them all; this is correct but trial division can cost $O(n\sqrt M)$ and requires more machinery than repeated GCD.
- **Enumerating coefficients:** Searching integer multipliers has no useful finite bound and does not exploit the number-theoretic characterization.
- **Array containing `1`:** The singleton subset containing that value proves the array is good immediately.
- **Single-element array:** It is good exactly when its only value is `1`.
- **Repeated or all-even values:** Repetition does not affect the GCD; if a common divisor greater than $1$ remains, the result is `false`.

</details>
