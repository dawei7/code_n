# Set Mismatch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 645 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/set-mismatch/) |

## Problem Description
### Goal
A set originally contained every integer from `1` through `n` exactly once. After an error, one number was duplicated in place of another, causing one value to occur twice and a different value to disappear. The array `nums` represents the set after this corruption.

Find both affected values and return them as `[duplicate, missing]` in that order. Exactly one number is repeated and exactly one number from the original range is absent; equal array entries identify the repeated value, not two independent missing positions.

### Function Contract
**Inputs**

- `nums`: a length-`n` list whose original values were exactly `1` through `n`, but one value appears twice and one other value is absent

**Return value**

- `[duplicate, missing]` in that order

### Examples
**Example 1**

- Input: `nums = [1,2,2,4]`
- Output: `[2,3]`

**Example 2**

- Input: `nums = [1,1]`
- Output: `[1,2]`

**Example 3**

- Input: `nums = [2,2]`
- Output: `[2,1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare the observed and expected sums**

Let the duplicated value be `d` and the missing value be `m`. The observed sum differs from $1 + \ldots + n$ by $d - m$; call this difference `delta`.

**Use square sums to obtain a second equation**

The observed square sum differs from $1 ^{2} + \ldots + n ^{2}$ by $d^{2} - m^{2}$. Factoring gives $(d - m)(d + m)$, so division by the nonzero `delta` yields $d + m$.

**Solve the two linear identities**

With `difference = d - m` and `pair_sum = d + m`, compute `d = (difference + pair_sum) / 2`, then `m = d - difference`. The contract guarantees exactly one duplicate and one missing value, so these divisions are integral.

**Why aggregate differences isolate the mismatch**

Every uncorrupted value occurs once in both the observed and expected collections and cancels from both aggregate differences. Only the extra `d` and absent `m` remain, producing the two identities above. Their unique solution is therefore exactly the corrupted pair.

#### Complexity detail

One pass accumulates the observed sum and square sum for `n` values, taking $O(n)$ time. Expected sums are computed from closed formulas, and a constant number of integer totals uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sign marking:** use each value as an index and negate the corresponding array entry; it achieves $O(n)$ time and $O(1)$ extra space but mutates the input.
- **Hash set:** detects the duplicate while accumulating unique values in $O(n)$ time, but uses $O(n)$ space.
- **Sort then scan:** adjacent equality reveals the duplicate and a gap reveals the missing value, costing $O(n \log n)$ time or mutating the input.
- **Scan for every expected value:** repeatedly searches the array and is correct but takes $O(n^2)$ time.
- The missing value may be `1` or `n`.
- The duplicate may occur in any two input positions.
- A two-element input can be either `[1,1]` or `[2,2]`.
- Fixed-width implementations must use sufficiently wide totals for the square sum.

</details>
