# Maximum Product Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) |

## Problem Description
### Goal
Given a nonempty list of integers, choose a contiguous subarray containing at least one element and multiply all values in that interval. The interval may begin and end anywhere but cannot skip elements or combine separated portions of the input.

Return the largest product obtainable over all such intervals. Negative values matter because two negative factors can turn a small or negative running product into a large positive one, while zero splits products and is itself a valid one-element result. The chosen interval is not returned. When every longer product is worse, a single input value may supply the answer.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

The maximum product among all contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [2,3,-2,4]`
- Output: `6`

**Example 2**

- Input: `nums = [-2,0,-1]`
- Output: `0`

**Example 3**

- Input: `nums = [-2,3,-4]`
- Output: `24`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A negative factor can turn the worst ending product into the best**

For every position, retain both maximum and minimum products among nonempty subarrays ending exactly there. A large negative minimum is not dominated: multiplying it by a later negative value can make it the next large positive maximum.

**Every ending product either restarts or extends one previous extreme**

For current `x`, candidates are `x`, `previous_high * x`, and `previous_low * x`. Taking their maximum and minimum is the direct recurrence. An equivalent optimized form swaps high and low when $x < 0$, then computes `high = max(x, high * x)` and `low = min(x, low * x)`.

Both updates must use the previous extremes; swapping first or saving old values prevents an updated high from contaminating the low calculation.

**Endpoint extrema and global optimum have separate meanings**

After processing index `i`, `high` and `low` are respectively the maximum and minimum products of all nonempty subarrays ending at `i`, while `best` is the maximum product over every ending position through `i`.

**Trace two negatives converting the minimum into the maximum**

For `[-2,3,-4]`, the ending extremes become `(-2,-2)`, then `(3,-6)`. Multiplying by `-4` turns the previous low `-6` into high `24`, which becomes the global answer.

**Both product extremes are necessary after a sign change**

Every subarray ending at the current position either consists only of the current number or extends a subarray ending one position earlier. Among those extensions, only the previous maximum and minimum products can become new extremes: a positive multiplier preserves their order, while a negative multiplier reverses it. Zero is handled by the single-element candidate and restarts both ranges.

The recurrence therefore captures the maximum and minimum product of every possible ending subarray. Updating the global answer from each ending maximum considers every nonempty subarray exactly when its right endpoint is processed.

#### Complexity detail

Each number causes constant arithmetic and comparisons once, giving $O(n)$ time. Three running products provide $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all subarrays:** is straightforward but costs $O(n^2)$ time.
- **Prefix and suffix products:** can also solve the problem linearly, but the two-extreme recurrence states the negative-sign effect directly.
- **Track only the maximum:** fails when a large negative product later meets another negative number.
- A one-element array returns that element, including a negative value. Initialize from the first element rather than one or zero.
- Zero naturally makes both ending extrema zero and permits a fresh subarray to begin at the next position.

</details>
