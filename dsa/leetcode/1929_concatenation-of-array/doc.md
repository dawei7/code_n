# Concatenation of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1929 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenation-of-array/) |

## Problem Description
### Goal
An integer array `nums` has length $N$. Construct a new array `ans` of length
$2N$ by placing two copies of `nums` next to each other in the same order.

For every index $i$ with $0 \le i < N$, the first half must satisfy
`ans[i] = nums[i]`, while the corresponding position in the second half must
satisfy `ans[i + N] = nums[i]`. Return the completed array.

### Function Contract
**Inputs**

- `nums`: a list of $N$ integers, where $1 \le N \le 1000$ and every value is
  between $1$ and $1000$, inclusive.

**Return value**

- A list of length $2N$ containing `nums` followed immediately by another copy
  of `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `[1, 2, 1, 1, 2, 1]`

**Example 2**

- Input: `nums = [1, 3, 2, 1]`
- Output: `[1, 3, 2, 1, 1, 3, 2, 1]`

**Example 3**

- Input: `nums = [7]`
- Output: `[7, 7]`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Build two consecutive copies**

The result has two consecutive regions, each with exactly $N$ positions. Copy
`nums` into the first region, then copy the same sequence into the second
region. Array concatenation expresses precisely this construction: it
preserves every element and its relative order in each copy.

**Why every result position is correct**

For any valid source index $i$, the first copy places `nums[i]` at index $i$
and the second places it at index `i + N`. These are exactly the two required
positions, and together the two index ranges cover all $2N$ positions without
overlap or omission. The constructed array therefore satisfies the contract.

#### Complexity detail

Here $N$ is the length of `nums`. Producing the returned array requires writing
$2N$ values, so the running time is $O(N)$. The returned list itself stores
$2N$ integers and therefore uses $O(N)$ space. Apart from that required output,
the direct construction needs only constant auxiliary state.

#### Alternatives and edge cases

- **Two explicit copy loops:** Preallocate $2N$ positions and assign each
  source value to indices `i` and `i + N`. This has the same asymptotic costs
  and can avoid incremental resizing, but is more verbose than direct
  concatenation.
- **Repeated growing-list concatenation:** Rebuilding a larger list for every
  individual element remains correct, but repeatedly copies the existing
  prefix and can take $O(N^2)$ time.
- A one-element input still produces two elements; neither copy may be omitted.
- Duplicate values remain duplicate values. Their positions, rather than
  uniqueness, determine the result.
- The second copy starts only after all $N$ elements of the first copy, so
  interleaving each value with itself would not satisfy the required order.

</details>
