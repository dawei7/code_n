# Find Greatest Common Divisor of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1979 |
| Difficulty | Easy |
| Topics | Array, Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |

## Problem Description
### Goal
Given an integer array `nums`, identify its smallest value and its largest
value. Return the greatest common divisor of those two endpoints.

The greatest common divisor is the largest positive integer that divides both
endpoint values without a remainder. Values between the minimum and maximum
do not otherwise affect the requested result. The array contains only positive
integers and may include repeated values at either endpoint.

### Function Contract
**Inputs**

- `nums`: a list of $N$ positive integers, where $2 \le N \le 1000$.
- Every value is in the inclusive range from `1` through `1000`.
- Let $M=\max(\texttt{nums})$.

**Return value**

- $\gcd(\min(\texttt{nums}),\max(\texttt{nums}))$.

### Examples
**Example 1**

- Input: `nums = [2, 5, 6, 9, 10]`
- Output: `2`

**Example 2**

- Input: `nums = [7, 5, 6, 8, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [3, 3]`
- Output: `3`

### Required Complexity
- **Time:** $O(N+\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the array to the two required endpoints**

Scan `nums` to find its minimum and maximum. The contract asks only for the
greatest common divisor of these two values, so no other array value needs to
participate in the number-theory calculation.

**Apply the Euclidean remainder identity**

For positive integers $a$ and $b$ with $a\le b$,

$$
\gcd(a,b)=\gcd(b\bmod a,a).
$$

Replacing the larger pair by the remainder pair preserves every common
divisor: a number divides both $a$ and $b$ exactly when it divides $a$ and
`b % a`. Repeating the replacement strictly reduces the nonzero second
operand until the remainder becomes zero. The remaining positive operand is
therefore the greatest common divisor.

#### Complexity detail

Finding the endpoints reads all $N$ values in $O(N)$ time. Euclid's algorithm
performs $O(\log M)$ remainder steps in the worst case, giving
$O(N+\log M)$ total time. Endpoint values and Euclidean state require $O(1)$
auxiliary space.

#### Alternatives and edge cases

- **Repeated subtraction:** Replace the larger endpoint by its difference
  from the smaller until they match. This is correct but can take $O(M)$
  iterations for endpoints `1` and `M`.
- **Test divisors downward:** Try candidates from the smaller endpoint to `1`.
  This may also take linear time in the value bound.
- **Sort the array:** Sorting exposes the endpoints but costs
  $O(N\log N)$ time when a linear scan is enough.
- When all entries are equal, the minimum, maximum, and returned GCD are that
  shared value.
- A minimum value of `1` forces the answer to `1`.
- Duplicate endpoints do not change the calculation.
- Array values strictly between the minimum and maximum cannot alter the
  requested GCD.

</details>
