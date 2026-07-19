# Minimum Distance to the Target Element

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-distance-to-the-target-element/) |
| Frontend ID | 1848 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An integer array `nums` contains at least one occurrence of `target`, and `start` identifies a valid array index. Moving between neighboring indices costs one unit per step, so reaching index $i$ from `start` has distance $\lvert i-\texttt{start}\rvert$.

Consider every index whose value equals `target`. Return the least distance from `start` to any such index. The target may already occupy the starting position, may occur several times on either side, or may appear only at an endpoint.

### Function Contract

**Inputs**

- `nums`: a list of integers with $1 \le \lvert\texttt{nums}\rvert \le 1000$.
- `target`: an integer guaranteed to occur in `nums`.
- `start`: an index satisfying $0 \le \texttt{start}<\lvert\texttt{nums}\rvert$.
- Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- For every index $i$ where `nums[i] == target`, consider $\lvert i-\texttt{start}\rvert$.
- Return the minimum of those distances.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`, `target = 5`, `start = 3`
- Output: `1`

The target is at index 4, one step from index 3.

**Example 2**

- Input: `nums = [1]`, `target = 1`, `start = 0`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`, `target = 1`, `start = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Scan `nums` with both each value and its index. Whenever the value equals `target`, compute the absolute index difference from `start`. The answer is the minimum of those candidate distances.

Every possible destination is examined exactly once, so no target occurrence can be missed. Non-target indices are never considered as destinations. Taking the minimum over precisely the target positions therefore returns exactly the fewest required adjacent moves. The guarantee that `target` occurs makes the minimum well-defined.

#### Complexity detail

The scan visits $n$ elements, giving $O(n)$ time. A running minimum requires $O(1)$ auxiliary space. The generator expression in the reference streams candidate distances rather than storing all matching indices.

#### Alternatives and edge cases

- **Expand in both directions:** Check equal distances to the left and right of `start`; the first target found is nearest, but boundary handling is more elaborate.
- **Repeated growing slices:** Searching a larger copied interval for every possible distance is correct but can copy and rescan $O(n^2)$ elements.
- **Target at `start`:** The minimum distance is zero.
- **Multiple occurrences:** A farther occurrence must not overwrite a nearer one.
- **Equal left and right distance:** Either position gives the same numeric answer.
- **Endpoint target:** Absolute difference handles index 0 and index $n-1$ without special cases.
- **Single element:** The target guarantee forces distance zero.

</details>
