# Circular Array Loop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 457 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/circular-array-loop/) |

## Problem Description
### Goal
Given a nonempty circular integer array, position `i` jumps forward or backward by `nums[i]` steps, with indices wrapping around either end. Repeatedly applying jumps defines a directed route from every starting position.

Return `True` when some route contains a cycle visiting more than one distinct index and every jump in that cycle has the same sign. A one-position self-loop is invalid, and a cycle that mixes positive and negative jumps is invalid. Return `False` when no starting point meets both requirements. Detect cycles without allowing traversal state from a failed direction to fabricate another route.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array; `nums[i]` is the signed jump from index `i`, with indices wrapping around the array

**Return value**

- `True` if some cycle has length greater than one and consists entirely of positive jumps or entirely of negative jumps; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [2, -1, 1, 2, 2]`
- Output: `True`

**Example 2**

- Input: `nums = [-1, -2, -3, -4, -5, 6]`
- Output: `False`

**Example 3**

- Input: `nums = [1, -1, 5, 1, 4]`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Treat jumps as a directed functional graph**

Every index has one wrapped successor `(i + nums[i]) % n`. For each unprocessed start, fix the required direction from its sign and use slow and fast pointers. A step is invalid as soon as it reaches a cleared index, changes direction, or returns to the same index in one jump.

**Detect only admissible cycles**

Advance slow once and fast twice through the validated successor function. If either pointer encounters an invalid step, this start cannot produce an admissible cycle. If the pointers meet, both have followed only same-direction edges and self-loops were excluded, so their meeting lies in a cycle of length at least two.

**Erase failed paths for amortized linear work**

After a failed search, follow the start's same-direction path again and set each visited entry to zero. No valid same-direction cycle can include those nodes: the deterministic path already ended at an invalid edge or joined a path known not to contain one. Later starts skip cleared nodes, so each index participates in only constant many pointer or cleanup operations.

**Wrap negative jumps correctly**

Modulo normalization maps both positive and negative destinations into `[0, n)`. The direction test uses the original jump's sign, not whether its wrapped destination index is numerically larger or smaller.

#### Complexity detail

Although Floyd searches may traverse multiple nodes, clearing every failed path ensures each index is permanently processed once, for $O(n)$ total time. Slow, fast, direction, and cleanup indices use $O(1)$ auxiliary space; the algorithm marks the input array in place.

#### Alternatives and edge cases

- **Per-start visited set:** is straightforward but can revisit the same long failed path from many starts, taking $O(n^2)$ time and $O(n)$ space.
- **Global visitation states:** start-specific traversal identifiers give $O(n)$ time and $O(n)$ space without mutating the input.
- **Copy before marking:** preserves the caller's array while retaining linear time, at the cost of $O(n)$ extra space.
- **One-element self-loop:** is explicitly invalid even when the jump is a multiple of `n`.
- **Direction change:** a path containing both positive and negative jumps is not a valid cycle.
- **Large jump magnitude:** reduce the destination modulo `n` rather than simulating individual steps.
- **All entries one direction:** may still be invalid when paths collapse into self-loops or nonqualifying structure.

</details>
