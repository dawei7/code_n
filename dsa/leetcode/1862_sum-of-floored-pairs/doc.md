# Sum of Floored Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1862 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Counting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-floored-pairs/) |

## Problem Description
### Goal
Given a positive integer array `nums`, consider every ordered pair of indices
$(i,j)$, including pairs whose indices are equal. The pair contributes the
integer part of `nums[i] / nums[j]`, equivalently
$\left\lfloor \texttt{nums}[i]/\texttt{nums}[j]\right\rfloor$.

Add the contributions of all $n^2$ ordered pairs. Because this sum can be
large, return its remainder modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and
  every value is at most $10^5$.

Let $U = \max(\texttt{nums})$.

**Return value**

The ordered-pair floor-division sum as an integer modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `nums = [2,5,9]`
- Output: `10`

**Example 2**

- Input: `nums = [7,7,7,7,7,7,7]`
- Output: `49`

Every ordered pair contributes one.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `9`

### Required Complexity
- **Time:** $O(n + U\log U)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

**Aggregate equal values**

Build `frequency[x]`, the number of occurrences of value $x$, and a prefix
count over the value domain. The answer depends on values and multiplicities,
so equal array elements never need to be processed separately.

**Group numerators by one quotient**

Fix a denominator value $d$ that occurs in the array. For a positive integer
$q$, every numerator $x$ in

$$
qd \le x \le (q+1)d-1
$$

satisfies $\lfloor x/d\rfloor=q$. Prefix counts return the number of input
values in this interval in constant time. Multiply that count by $q$ and by
`frequency[d]`, since every occurrence of $d$ forms the same pairs.

Enumerate the intervals by taking lower bounds $d,2d,3d,\ldots$ through $U$.
Values below $d$ contribute zero and can be skipped. These intervals partition
all positive numerator values, so every ordered pair is counted once with
exactly its floor quotient. Reduce the accumulated total modulo $10^9+7$.

#### Complexity detail

Counting values and building prefix counts take $O(n+U)$ time. Denominator $d$
visits $\lfloor U/d\rfloor$ ranges, and summing this harmonic series over all
$d$ is $O(U\log U)$. The frequency and prefix arrays use $O(U)$ space.

#### Alternatives and edge cases

- **Enumerate index pairs:** directly evaluating every ordered pair is simple
  but takes $O(n^2)$ time.
- **Sort and binary-search quotient boundaries:** this avoids a full value
  prefix array but adds repeated logarithmic searches and is harder to
  aggregate cleanly.
- Equal indices are included; each such pair contributes one.
- Duplicate values contribute through their full multiplicity on both the
  numerator and denominator sides.
- Apply the modulo to the total, not to individual floor divisions.

</details>
