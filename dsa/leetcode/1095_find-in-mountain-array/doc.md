# Find in Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1095 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/find-in-mountain-array/) |

## Problem Description

### Goal

This is an interactive problem. A mountain array has length at least three and contains an interior peak: its values are strictly increasing from index 0 through the peak, then strictly decreasing from the peak through the final index.

Given `target` and a `MountainArray`, return the minimum index whose value equals `target`, or `-1` when the value is absent. The underlying array cannot be accessed directly. Only `MountainArray.get(index)` and `MountainArray.length()` are available, and a submission that makes more than 100 calls to `MountainArray.get` is rejected.

### Function Contract

**Inputs**

- `target`: an integer to locate, with $0 \leq \texttt{target} \leq 10^9$.
- `mountain_arr`: a mountain array of length $n$, where $3 \leq n \leq 10^4$ and every value lies in $[0,10^9]$. LeetCode exposes it through `get(index)` and `length()`; the app-local adapter receives the same values as a list.

**Return value**

The smallest index containing `target`, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `target = 3, mountain_arr = [1, 2, 3, 4, 5, 3, 1]`
- Output: `2`

The target occurs on both slopes at indices 2 and 5, so the smaller index is required.

**Example 2**

- Input: `target = 3, mountain_arr = [0, 1, 2, 4, 2, 1]`
- Output: `-1`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Find the peak without reading the whole array.** At a midpoint `mid`, comparing `get(mid)` with `get(mid + 1)` reveals the slope. If the values rise, the peak lies strictly to the right; otherwise the peak is at `mid` or to its left. Repeating this binary decision isolates the unique peak in $O(\log n)$ calls.

**Search the increasing side first.** The prefix ending at the peak is strictly increasing, so ordinary binary search applies. Returning immediately when it finds `target` guarantees the minimum index: every index on this slope precedes every index on the decreasing slope.

**Reverse the comparison on the decreasing side.** If the first search fails, binary-search the suffix after the peak. Here a midpoint value smaller than `target` means moving left, while a larger value means moving right. The strict ordering on each side makes both searches valid, and searching their union covers the entire mountain.

The peak search never discards the peak because its slope comparison retains the half containing the transition. Each subsequent search discards only values that cannot equal the target under that side's strict order. Thus a found index is valid, the increasing-side priority makes it minimal, and failure of both searches proves absence.

#### Complexity detail

Peak discovery and the two side searches each use $O(\log n)$ time and `MountainArray.get` calls, for $O(\log n)$ overall. At $n \leq 10^4$, the three searches stay below the 100-call limit. They maintain only interval endpoints and current values, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Linear scan:** It would find the first occurrence in $O(n)$ time but can exceed the 100-call interactive limit.
- **Cache queried values:** Memoization can avoid duplicate `get` calls, though the uncached three-search method already fits the limit and uses constant space.
- **Target on both slopes:** Search the strictly increasing prefix first so the returned index is the minimum one.
- **Target equals the peak:** The first binary search includes the peak and returns it without searching the descending suffix.
- **Target absent:** Both ordered searches terminate with `-1`; no full traversal is needed.
- **Three-element mountain:** The peak search and side intervals remain valid at the minimum permitted length.

</details>
