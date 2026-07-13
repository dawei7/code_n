# Self Dividing Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 728 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/self-dividing-numbers/) |

## Problem Description
### Goal
A self-dividing number is divisible by every decimal digit it contains. Such a number cannot contain digit `0`, because division by zero is undefined.

Given positive integers `left` and `right`, return all self-dividing numbers in the inclusive range `[left, right]`. Test each number against all of its own digits, including repeated digits, and return the qualifying values in increasing numerical order. Both interval endpoints are candidates when they satisfy the definition.

### Function Contract
**Inputs**

- `left`: the positive lower endpoint of the interval
- `right`: the positive upper endpoint of the interval, with `left <= right`

**Return value**

- All self-dividing numbers from `left` through `right` in increasing order

### Examples
**Example 1**

- Input: `left = 1, right = 22`
- Output: `[1,2,3,4,5,6,7,8,9,11,12,15,22]`

**Example 2**

- Input: `left = 47, right = 85`
- Output: `[48,55,66,77]`

**Example 3**

- Input: `left = 128, right = 128`
- Output: `[128]`

### Required Complexity

- **Time:** $O(WD)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep the divisor target unchanged**

For each candidate in the interval, copy it into a working value. Repeatedly take `working % 10` to obtain the next digit and remove that digit with integer division by ten. Divisibility must always be tested against the original candidate, not against the shrinking working copy.

**Reject zero before division**

A zero digit makes the number invalid and cannot be used as a divisor. For every nonzero digit, require `candidate % digit = 0`. Stop as soon as either condition fails; if every digit passes, append the candidate.

**Why the filter is exact and ordered**

Decimal extraction visits every digit of the candidate exactly once. Acceptance therefore means that no digit is zero and every digit divides the original number, which is precisely the self-dividing definition. Scanning candidates from `left` through `right` once produces all qualifying values in increasing order without a later sort.

#### Complexity detail

Let `W = right - left + 1` and let `D` be the maximum decimal digit count in the interval. Each candidate examines at most `D` digits, for $O(WD)$ time. Digit extraction uses only constant auxiliary state, so space is $O(1)$ excluding the returned list.

#### Alternatives and edge cases

- **Convert to a string:** iterate over character digits and convert each back to an integer; it has the same $O(WD)$ time but allocates a digit string of $O(D)$ space per candidate.
- **Enumerate every divisor first:** test all integers up to the candidate and then check whether its digits appear among those divisors; it is correct but can take quadratic work across a wide interval.
- **Precompute answers:** a table can answer many fixed-bound queries quickly, but it adds storage and is unnecessary for one interval.
- **Zero digit:** reject immediately, including numbers ending in zero.
- **Repeated digit:** checking the repeated value again is harmless and keeps the digit scan simple.
- **Single-digit positive number:** it always divides itself and is therefore valid.
- **Inclusive endpoints:** test both `left` and `right`.

</details>
