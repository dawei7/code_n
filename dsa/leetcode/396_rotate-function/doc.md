# Rotate Function

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 396 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-function/) |

## Problem Description
### Goal
Given an integer array of length $n$, consider all $n$ cyclic right rotations. For one rotated arrangement $B$, define its score as $F=\sum_{i=0}^{n-1} iB_i$.

Return the maximum score among the original arrangement and every right rotation. Negative values and scores are allowed, so the answer is not automatically zero. Compute successive scores from their relationship rather than rebuilding and rescoring every rotated array in quadratic time. The function returns only the greatest score, not the rotation count or arrangement that achieves it.

### Function Contract
**Inputs**

- `nums`: the integer array to rotate

**Return value**

- Return the greatest value of `sum(index * rotated[index])` over all `len(nums)` cyclic right rotations.

### Examples
**Example 1**

- Input: `nums = [4,3,2,6]`
- Output: `26`

**Example 2**

- Input: `nums = [100]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `8`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compute the unrotated score and total once**

Let `F(0) = sum(i * nums[i])` and `total = sum(nums)`. These two aggregates contain everything needed to derive each next score; the rotated arrays themselves never need to be built.

**Relate adjacent right rotations**

When moving from rotation $k - 1$ to `k`, every value's index increases by one, contributing `total`. The value that wraps from the last position to index zero was `nums[n - k]`; it was included in that increase but actually loses $n - 1$ index units, so subtract `n * nums[n - k]`. Therefore `F(k) = F(k - 1) + total - n * nums[n - k]`.

**Evaluate every score through the recurrence**

Start the best value at `F(0)`, apply the formula for $k = 1$ through $n - 1$, and retain the maximum. Each recurrence exactly accounts for the one wrapping value and the uniform shift of all others, so it produces the same score as explicitly rotating and recomputing.

#### Complexity detail

The initial aggregates scan `n` values, and the recurrence evaluates the remaining $n - 1$ rotations in constant time each, for $O(n)$ time. A fixed number of numeric variables uses $O(1)$ space.

#### Alternatives and edge cases

- **Explicitly score every rotation:** is direct but performs `n` work for each of `n` rotations, taking $O(n^2)$ time.
- **Build each rotated array:** adds $O(n)$ copying per rotation without simplifying the score calculation.
- **Prefix-sum derivation:** can express the same recurrence but stores more information than the total sum requires.
- A one-element array has score zero.
- Negative values require initializing the best score from a real rotation, not zero.
- Equal or zero values may make several rotations tie.
- The wrap index $n - k$ must move backward through the original array.

</details>
