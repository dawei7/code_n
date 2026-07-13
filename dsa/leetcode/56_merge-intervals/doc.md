# Merge Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 56 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-intervals/) |

## Problem Description
### Goal
You are given a nonempty collection of closed intervals `[start, end]`. Two intervals are overlapping when they share at least one point, including touching at an endpoint, and a chain of overlaps connects all intervals in that chain.

Merge every connected overlap group into its smallest covering interval. Return the resulting non-overlapping intervals in ascending start order while covering exactly the same points as the input collection. Input intervals need not initially be sorted.

### Function Contract
**Inputs**

- `intervals`: a nonempty `List[List[int]]`, where each item is `[start, end]` and `start <= end`

**Return value**

A list of the merged nonoverlapping intervals in ascending start order.

### Examples
**Example 1**

- Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- Output: `[[1,6],[8,10],[15,18]]`

**Example 2**

- Input: `intervals = [[1,4],[4,5]]`
- Output: `[[1,5]]`

**Example 3**

- Input: `intervals = [[5,7]]`
- Output: `[[5,7]]`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sorting makes overlap components contiguous**

Once intervals are ordered by start, every interval transitively connected to the current overlap component appears before the first interval whose start exceeds the component's expanding end. Sorting therefore makes each merged component a contiguous run in scan order.

**Only the last merged interval can still grow**

Initialize the output with the first sorted interval. If the next start is at most the last merged end, the closed intervals touch or overlap; extend the end to the larger endpoint. Otherwise append a new disjoint interval. Earlier output intervals can no longer overlap anything because the last interval starts no earlier and already lies after them.

**The output is the exact union of the processed prefix**

After processing a sorted prefix, the output is sorted and pairwise disjoint, and its union equals the prefix's union. Its last interval is the only one the next sorted interval can possibly overlap.

**Trace a chain of overlaps**

Sorting `[[8,10],[1,3],[2,6],[15,18]]` gives starts 1, 2, 8, 15. `[2,6]` extends `[1,3]` to `[1,6]`; the starts 8 and 15 lie beyond previous ends and form separate output intervals.

**Sorted starts make each merge decision final**

When the next start is at most the current end, the intervals overlap or touch, and extending the current end to their maximum preserves exactly their combined union. When the next start is greater, a gap exists. Because all later starts are no smaller, no future interval can bridge that gap, so the current merged component is final.

Each scan step therefore either enlarges the same connected union component or closes it permanently and begins the next. The output components cover exactly the original intervals and remain pairwise disjoint in sorted order.

#### Complexity detail

Sorting takes $O(n \log n)$ time and the merge scan takes $O(n)$. The output can contain `n` intervals; aside from returned storage, sorting may also require implementation-dependent auxiliary space.

#### Alternatives and edge cases

- **Repeatedly search all interval pairs:** eventually reaches the same union but can take quadratic or worse time.
- **Sweep individual coordinates:** is practical only when the coordinate range is small and wastes work on empty positions.
- **Interval graph components:** makes transitive overlap explicit but materializing all pairwise edges costs $O(n^2)$.
- Closed intervals `[1,4]` and `[4,5]` overlap at point `4` and must merge; the comparison is `next_start <= current_end`.
- Nested intervals do not shrink the current end. A single input interval is returned as the sole merged component.

</details>
