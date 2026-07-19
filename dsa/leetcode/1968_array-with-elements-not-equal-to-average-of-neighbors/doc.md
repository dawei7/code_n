# Array With Elements Not Equal to Average of Neighbors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1968 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) |

## Problem Description
### Goal
You are given a 0-indexed array `nums` containing distinct integers. Rearrange
all of its elements so that no interior element equals the arithmetic average
of its two immediate neighbors.

More precisely, for every index $i$ satisfying $1 \le i < N - 1$, the returned
array must obey

$$
2\cdot\texttt{nums[i]} \ne \texttt{nums[i - 1]}+\texttt{nums[i + 1]}.
$$

Return any permutation that meets this condition. The first and last elements
have only one neighbor and therefore impose no average constraint.

### Function Contract
**Inputs**

- `nums`: a list of $N$ distinct integers, where
  $3 \le N \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Any permutation of all input values in which every interior value differs
  from the average of its immediate neighbors.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `[1, 2, 4, 5, 3]`

**Example 2**

- Input: `nums = [6, 2, 0, 9, 7]`
- Output: `[9, 7, 6, 2, 0]`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `[2, 1, 3]`

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn every interior position into a strict extremum**

Sort the distinct values in ascending order, then swap each adjacent pair:
positions `0` and `1`, positions `2` and `3`, and so on. A sorted sequence
`a[0] < a[1] < a[2] < a[3] < ...` consequently begins
`a[1], a[0], a[3], a[2], ...`.

**Why an average equality becomes impossible**

Every odd interior position holds the smaller value of its pair. Its left
neighbor is the larger value from that pair, and its right neighbor belongs
to a later pair, so both neighbors are strictly larger. The middle value is
therefore a strict local minimum.

Every even interior position holds the larger value of its pair. Both adjacent
values come from earlier positions in the sorted order and are strictly
smaller, making it a strict local maximum. The average of two values that are
both strictly above a middle value is also above it; similarly, the average of
two strictly smaller values is below it. Thus no interior value can equal its
neighbors' average. Swapping positions changes no values or multiplicities, so
the result is also a permutation of the input.

#### Complexity detail

Here $N$ is the number of input values. Sorting costs $O(N\log N)$ time, and
the adjacent-pair pass costs $O(N)$ time. The returned list requires $O(N)$
space under the app contract. The pair swaps themselves use $O(1)$ auxiliary
space; a language's sorting routine may use additional implementation-specific
working memory.

#### Alternatives and edge cases

- **Split and interleave sorted halves:** Alternating values from the lower and
  upper halves can also create local minima and maxima, but the exact ordering
  must be proved carefully at the boundary between the halves.
- **Repeatedly repair bad triples:** Detect an average equality and swap a
  neighboring pair. This can be made correct, but a naive rescan after every
  repair can take $O(N^2)$ time.
- **Original order:** Some inputs already satisfy the condition, but returning
  the input without checking is not correct for every array.
- Distinctness is essential to the strict-local-extremum proof; equal values
  could prevent a swapped position from being strictly above or below both
  neighbors.
- When $N$ is odd, the final value is left unswapped. Its only possible
  constrained role is as the right neighbor of the preceding interior
  position, where sorted order preserves the strict inequality.
- The condition can be checked without floating-point arithmetic by comparing
  `2 * nums[i]` with `nums[i - 1] + nums[i + 1]`.

</details>
