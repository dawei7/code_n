# Maximum Product of Three Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 628 |
| Difficulty | Easy |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/) |

## Problem Description
### Goal
Given an integer array `nums` containing at least three values, choose three numbers from three distinct array positions and multiply them together. Negative values and zero may appear, so the three numerically largest values do not always produce the greatest product.

Return the maximum product obtainable from any such choice of three numbers. Each array occurrence can be used at most once, while equal values at different positions remain separate selectable numbers.

### Function Contract
**Inputs**

- `nums`: an integer list containing at least three values

**Return value**

- The maximum product obtainable from values at three distinct indices

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `6`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `24`

**Example 3**

- Input: `nums = [-10,-10,5,2]`
- Output: `500`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the candidates to five extrema**

A maximum product using zero or two negative values must contain the largest available positive-side value. The other two values are either the next two largest values or the two smallest values, whose negative product may be large and positive. No middle value can improve either pair.

**Track three maxima and two minima**

Scan once while maintaining the three largest values in descending order and the two smallest values in ascending order. Insert each number into the appropriate constant-size positions by shifting displaced extrema.

**Compare the only two product shapes**

Compute `largest1 * largest2 * largest3` and `largest1 * smallest1 * smallest2`. The first covers an all-positive choice and also the best possible all-negative product when every result is negative. The second covers the beneficial pair of negative extremes.

**Why no other triple can win**

For a fixed largest factor, the best nonnegative pair is either the two greatest remaining values or the two most negative values. If every product is negative, choosing the three numerically largest values makes it least negative. These are exactly the two recorded candidates, so their maximum is globally optimal.

#### Complexity detail

Each of `n` values performs a constant number of comparisons and assignments against five stored extrema, giving $O(n)$ time. The extrema and answer occupy $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sort the array:** compare the final three values with the first two and final value; it is concise but costs $O(n \log n)$ time.
- **Keep constant-size heaps:** three-largest and two-smallest heaps remain $O(n)$ because their capacities are fixed, but direct variables are simpler.
- **Enumerate every triple:** tests the definition directly but costs $O(n^3)$ time.
- Two large-magnitude negatives can produce the maximum positive product.
- If all values are negative, the answer is the product of the three values closest to zero.
- Zero may be optimal when every nonzero triple is negative and a zero-containing triple exists.
- Repeated values at different indices are distinct valid choices.

</details>
