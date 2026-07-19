# Merge Triplets to Form Target Triplet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1899 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) |

## Problem Description

### Goal

You are given an array `triplets`, whose elements each contain exactly three integers, and a three-integer `target`. In one operation, choose two distinct triplet indices `i` and `j`, then replace `triplets[j]` by the coordinate-wise maximum of those two triplets. Thus each coordinate of the destination can stay unchanged or increase, but can never decrease.

You may perform this operation any number of times, including zero. Determine whether `target` can appear as one of the triplets after some sequence of operations. Return `True` when it can be formed and `False` otherwise.

### Function Contract

**Inputs**

- `triplets`: an array of $n$ triplets, with $1 \le n \le 10^5$.
- `target`: the desired triplet.
- Every coordinate in `triplets` and `target` is an integer from $1$ through $1000$.

**Return value**

Return `True` if coordinate-wise maximum operations between distinct triplets can make some element equal `target`; otherwise return `False`.

### Examples

**Example 1**

- Input: `triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5]`
- Output: `True`
- Explanation: Merging the first triplet into the third gives `[2, 7, 5]`. The middle triplet is not used because its second coordinate exceeds the target.

**Example 2**

- Input: `triplets = [[3, 4, 5], [4, 5, 6]], target = [3, 2, 5]`
- Output: `False`
- Explanation: No coordinate-wise maximum can produce `2` in the second position because both available values are already larger.

**Example 3**

- Input: `triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target = [5, 5, 5]`
- Output: `True`
- Explanation: Eligible triplets collectively provide exact values `5` in all three coordinates without exceeding the target.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Discard any triplet that overshoots.** Coordinate-wise maxima never decrease. If a triplet has even one coordinate larger than the corresponding target coordinate, every future triplet containing its contribution will still overshoot and therefore cannot equal `target`. Such a triplet is unusable.

**Collect exact coordinate witnesses.** Every remaining triplet is coordinate-wise at most `target`, so merging any collection of them cannot exceed the target. Track three Boolean flags. For each usable triplet, set flag $c$ when its coordinate $c$ equals the target's coordinate $c$. If all three flags become true, the witnessing triplets' coordinate-wise maximum is exactly `target`: it is no larger in any coordinate, and each coordinate reaches the required value.

The converse is also necessary. Any sequence that creates `target` can use no overshooting source, and some contributing source must supply the final exact value in each coordinate because maxima only select existing coordinate values. Therefore the three flags characterize precisely when formation is possible. If one triplet already equals `target`, all flags are set and the permitted zero-operation case succeeds.

#### Complexity detail

Let $n$ be the number of triplets. The algorithm inspects each triplet's three fixed coordinates once, taking $O(n)$ time. It stores only three Boolean flags and loop variables, so its auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Simulate merge operations:** Repeatedly modifying triplets obscures the monotone structure and may take quadratic work; only the existence of safe coordinate witnesses matters.
- **Merge every triplet indiscriminately:** A single coordinate above `target` permanently contaminates a maximum, so overshooting triplets must be excluded.
- **Require one triplet to match all coordinates:** Different safe triplets may supply different target coordinates and can be merged.
- **Already-present target:** Zero operations are allowed, so a target triplet succeeds even when it is the only element.
- **Missing exact coordinate:** Values below a target coordinate cannot combine to make that larger value; maxima choose among existing values rather than adding them.
- **Distinct operation indices:** Each actual merge uses `i != j`, but this does not prevent combining several safe witnesses into a destination triplet.

</details>
