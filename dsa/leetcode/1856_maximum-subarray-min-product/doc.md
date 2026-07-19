# Maximum Subarray Min-Product

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-subarray-min-product/) |
| Frontend ID | 1856 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For any non-empty contiguous subarray of the positive integer array `nums`, define its min-product as the smallest value in that subarray multiplied by the sum of all its values. Different subarrays may share the same minimum while having different sums and products.

Find the greatest min-product over every possible non-empty subarray. The unreduced maximum is guaranteed to fit in a signed 64-bit integer. Only after choosing that true maximum, return it modulo $10^9+7$; applying the modulus to candidates before comparing them would change their ordering.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers.
- $1\le n\le10^5$.
- Every element satisfies $1\le\texttt{nums[i]}\le10^7$.

**Return value**

- For every non-empty subarray, multiply its sum by its minimum value.
- Return the maximum such product modulo $1\,000\,000\,007$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 2]`
- Output: `14`

The subarray `[2, 3, 2]` has minimum 2, sum 7, and min-product 14.

**Example 2**

- Input: `nums = [2, 3, 3, 1, 2]`
- Output: `18`

**Example 3**

- Input: `nums = [3, 1, 5, 6, 4, 2]`
- Output: `60`

The subarray `[5, 6, 4]` contributes $4(5+6+4)=60$.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn each value into a candidate minimum**

For a fixed element value, every array entry is positive, so the best subarray using that value as its minimum is the widest contiguous interval around it containing no smaller value. Extending within that legal region increases the sum without lowering the chosen minimum.

Maintain an increasing stack of pairs `(left, minimum)`. Each pair says that `minimum` can govern an interval beginning at `left` and continuing through the processed suffix. When a new value is no greater than the stack top, the top cannot extend across the new position. Pop it and evaluate its maximal interval ending immediately before the current index.

Carry the popped entry's left boundary into the new value. This allows the smaller or equal value to govern everything the popped minimum could cover. Popping equal values assigns their combined widest interval to one representative and avoids losing candidates on plateaus.

**Read interval sums in constant time**

A prefix-sum array gives the sum of `[left, right)` as `prefix[right] - prefix[left]`. After the scan, every remaining stack entry can extend to the array end, so evaluate those final intervals as well. Compare full integer products throughout and apply the modulus only once to the greatest product.

#### Complexity detail

Prefix sums take $O(n)$ time and space. Every index is pushed once and popped at most once from the monotonic stack, so all boundary processing is $O(n)$ time. The prefix array and stack each use $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining a running sum and minimum avoids a third loop but still costs $O(n^2)$ time.
- **Separate left and right boundary arrays:** Two monotonic-stack passes are equally linear but store more explicit boundary state.
- **Equal minima:** A consistent strict/non-strict boundary rule is required so plateaus receive their full interval.
- **Strictly increasing input:** No stack entry pops during the scan; the final flush must evaluate every suffix.
- **Strictly decreasing input:** Each new element pops earlier minima and inherits their left boundary.
- **Single element:** Its min-product is the square of that value.
- **Modulo timing:** Maximize unreduced products first, then reduce only the answer.
- **Large sums:** Implementations with fixed-width integers need a 64-bit type for sums and products.

</details>
