# Max Chunks To Make Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 769 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-chunks-to-make-sorted/) |

## Problem Description

### Goal

Given an array `arr` that is a permutation of the integers from `0` through $n - 1$, divide it into consecutive, nonempty chunks covering the complete array. Sort each chunk independently and concatenate the results in the original chunk order.

Return the maximum number of chunks for which the final concatenation is the globally sorted increasing array. The permutation guarantee means every value occurs exactly once, and chunk boundaries must be cuts between adjacent original positions rather than arbitrary group assignments.

### Function Contract

**Inputs**

- `arr`: a nonempty permutation of `0, 1, ..., len(arr) - 1`.

**Return value**

- The largest number of chunks whose independently sorted concatenation equals the globally sorted array.

### Examples

**Example 1**

- Input: `arr = [4,3,2,1,0]`
- Output: `1`
- Explanation: No proper prefix contains exactly the values that belong in those positions.

**Example 2**

- Input: `arr = [1,0,2,3,4]`
- Output: `4`
- Explanation: `[1,0]`, `[2]`, `[3]`, and `[4]` can be sorted independently.

**Example 3**

- Input: `arr = [0,2,1,4,3]`
- Output: `3`
- Explanation: The maximum partition is `[0]`, `[2,1]`, and `[4,3]`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize a complete sorted prefix**

Maintain the maximum value seen while scanning. A chunk may end at index `i` exactly when the prefix `arr[:i + 1]` contains the values `0` through `i`, because those are the values occupying that prefix after global sorting.

**Use the permutation constraint**

The prefix contains $i + 1$ distinct nonnegative values. If its maximum equals `i`, every prefix value lies in `0..i`; having $i + 1$ distinct values then forces the prefix to contain that entire set. Therefore `prefix_maximum = i` is sufficient for a cut. If the maximum is greater than `i`, that larger value belongs later and sorting a closed prefix cannot move it across the boundary, so the cut is impossible.

Count every index where equality holds. These legal prefix boundaries are compatible with one another: consecutive legal prefixes differ by exactly the values belonging to the intervening sorted positions. Using every legal boundary therefore maximizes the number of chunks.

#### Complexity detail

The scan visits each value once, taking $O(n)$ time. It stores only the running maximum and chunk count, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Running prefix sum:** A prefix sum equal to $i(i + 1) / 2$ also proves the prefix contains the smallest $i + 1$ permutation values, giving $O(n)$ time and $O(1)$ space.
- **Monotonic stack:** The general duplicate-capable method also works here in $O(n)$ time but is more machinery than the permutation invariant requires.
- **Recheck every prefix:** Testing all values in each prefix against its boundary is correct but takes $O(n^2)$ time.
- **Strictly descending permutation:** Only the final index closes a chunk.
- **Increasing permutation:** Every index closes a one-element chunk.
- **Single value:** It forms exactly one chunk.
- **Large value in an early prefix:** That prefix cannot close until the scan reaches the value's target index.

</details>
