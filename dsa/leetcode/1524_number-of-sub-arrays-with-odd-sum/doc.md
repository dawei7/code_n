# Number of Sub-arrays With Odd Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1524 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) |

## Problem Description
### Goal

Given an integer array, count its nonempty contiguous subarrays whose element sum is odd. Subarrays are distinguished by their start and end indices, so equal values occurring in different positions still form different choices.

Because an array of length up to $10^5$ can contain quadratically many subarrays, the raw count may be large. Return the count modulo $10^9+7$ without enumerating every interval.

### Function Contract
**Inputs**

- `arr`: A list of $n$ integers with $1 \leq n \leq 10^5$.
- Every array value lies between 1 and 100, inclusive.

**Return value**

Return the number of nonempty contiguous subarrays whose sum is odd, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `arr = [1, 3, 5]`
- Output: `4`
- Explanation: The odd-sum intervals are the three singletons and the whole array.

**Example 2**

- Input: `arr = [2, 4, 6]`
- Output: `0`
- Explanation: Every possible sum is even.

**Example 3**

- Input: `arr = [1, 2, 3, 4, 5, 6, 7]`
- Output: `16`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent every subarray as a difference of prefixes**

Include the empty prefix before index 0, whose sum is even. For each array position, track only whether the cumulative prefix sum is even or odd; the exact sum is unnecessary.

The sum of a subarray is the difference between its ending prefix and the prefix immediately before its start. That difference is odd exactly when the two prefix parities differ. Therefore every pair consisting of one even prefix and one odd prefix identifies one odd-sum subarray, and every odd-sum subarray produces exactly such a pair.

**Count opposite-parity prefix pairs**

Scan the array once, toggling the current parity whenever the value is odd. Count how many of the $n+1$ prefixes are even and how many are odd. If those totals are `even` and `odd`, the number of opposite-parity pairs is `even * odd`.

The empty prefix must initialize the even count to one; omitting it loses every odd-sum subarray that begins at index 0. Apply the modulus to the final product.

#### Complexity detail

Each element contributes one parity update and one counter increment, so the running time is $O(n)$. The parity bit and two counters use $O(1)$ auxiliary space.

The product may be quadratic in $n$, but Python integers remain exact and the required modulo is applied before returning.

#### Alternatives and edge cases

- **Ending-at-position dynamic programming:** track counts of odd- and even-sum subarrays ending at the current index. It is also linear but uses a more operational recurrence.
- **Nested interval enumeration:** carrying a running sum for every start is correct but takes $O(n^2)$ time.
- **Prefix-sum array:** storing every prefix and then counting parities works, but the full $O(n)$ array is unnecessary.
- **All even values:** every prefix remains even, so the answer is zero.
- **All odd values:** prefix parity alternates, producing a balanced product of even and odd prefix counts.
- **Single odd value:** one even and one odd prefix produce exactly one qualifying subarray.
- **Single even value:** both prefixes are even and the result is zero.
- **Modulo:** reduce the final count by $10^9+7$ even though ordinary small cases do not overflow.

</details>
