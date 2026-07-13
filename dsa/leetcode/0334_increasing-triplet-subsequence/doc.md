# Increasing Triplet Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 334 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/increasing-triplet-subsequence/) |

## Problem Description
### Goal
Given an integer array, determine whether it contains three positions $i < j < k$ whose values satisfy `nums[i] < nums[j] < nums[k]`. The selected elements form a subsequence and therefore do not need to be contiguous.

Return `True` when any strictly increasing triplet exists and `False` otherwise. Equal values cannot satisfy either strict comparison, and the original index order cannot be rearranged even if the values would sort into a triplet. Meet the required linear running time and constant extra space; the function need not return the indices or values of a qualifying triplet.

### Function Contract
**Inputs**

- `nums`: the integer array

**Return value**

`True` if an increasing subsequence of length three exists; otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `True`

**Example 2**

- Input: `nums = [5,4,3,2,1]`
- Output: `False`

**Example 3**

- Input: `nums = [2,1,5,0,4,6]`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep the smallest possible tails for lengths one and two**

Maintain `first`, the smallest value seen that can end an increasing subsequence of length one, and `second`, the smallest possible ending value of an increasing pair seen so far.

For each value, replace `first` when the value is no larger. Otherwise it is greater than `first`; replace `second` when it is no larger than the current pair tail. A value larger than both thresholds completes a length-three subsequence, so return true immediately.

**Use non-strict updates to enforce a strict triplet**

The update comparisons must be `<=`. An equal value replaces a threshold rather than advancing to the next one, so `[1,1,2,2]` never treats equal copies as a strict increase. Only the final `else` proves `value > second >` the earlier value that established `second`.

The current `first` may be replaced after `second` was formed. That does not invalidate `second`: it still represents a real earlier increasing pair, even if its original first value is no longer stored. Lowering `first` merely creates a better opportunity for future pairs.

For `[20,100,10,12,5,13]`, the pair threshold becomes `(20,100)`, then improves to `(10,12)`. Updating `first` to five does not erase that witnessed pair. The final thirteen is greater than twelve, proving subsequence `10,12,13`.

If the scan returns true, the `second` threshold was created by a prior value greater than some still-earlier first, and the current value is greater than `second`, so a valid ordered triplet exists. If the scan ends false, no value ever exceeded the smallest pair tail available in its prefix; therefore no prefix contained a pair that any later value could complete.

#### Complexity detail

The algorithm examines each value once and performs constant work per value, giving $O(n)$ time. It stores only two numeric thresholds, using $O(1)$ space.

#### Alternatives and edge cases

- **Choose each middle index and search both sides:** is correct but can take $O(n^2)$ time.
- **Compute the full longest increasing subsequence:** solves a more general problem and needs additional storage or logarithmic searches.
- **Sort the array:** destroys the original index order and can create a triplet that was not a subsequence.
- Arrays shorter than three and arrays of equal values return false. Negative values and repeated threshold resets require no special handling.

</details>
