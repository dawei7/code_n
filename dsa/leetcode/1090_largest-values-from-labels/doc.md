# Largest Values From Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1090 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-values-from-labels/) |

## Problem Description

### Goal

There are $n$ items. Item `i` has value `values[i]` and label `labels[i]`, so the two arrays describe the same items by matching index. Values and labels are nonnegative integers.

Choose a subset whose value sum is as large as possible. The subset may contain at most `numWanted` items, and for every label it may contain at most `useLimit` items carrying that label. Return the maximum attainable sum; the subset itself is not required.

### Function Contract

**Inputs**

- `values`: a list of $n$ nonnegative item values, where $1 \le n \le 2\cdot 10^4$.
- `labels`: a length-$n$ list whose entry at each index is that item's nonnegative label.
- `numWanted`: the maximum total number of selected items, from 1 through $n$.
- `useLimit`: the maximum selected count for any one label, from 1 through $n$.

**Return value**

- The greatest possible sum of values among subsets satisfying both selection limits.

### Examples

**Example 1**

- Input: `values = [5, 4, 3, 2, 1]`, `labels = [1, 1, 2, 2, 3]`, `numWanted = 3`, `useLimit = 1`
- Output: `9`

Select values 5, 3, and 1, one from each label.

**Example 2**

- Input: `values = [5, 4, 3, 2, 1]`, `labels = [1, 3, 3, 3, 2]`, `numWanted = 3`, `useLimit = 2`
- Output: `12`

**Example 3**

- Input: `values = [9, 8, 8, 7, 6]`, `labels = [0, 0, 0, 1, 1]`, `numWanted = 3`, `useLimit = 1`
- Output: `16`

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Consider value before every other property:** Pair each value with its label and sort all items by value in descending order. A label matters only for feasibility; among currently feasible items, taking the greatest remaining value can never reduce the options more than taking a smaller item with the same label usage.

**Track both limits while scanning:** Maintain how many selected items use each label and the total selected count. Accept an item when its label count is below `useLimit`; otherwise skip it. Stop after selecting `numWanted` items or exhausting the sorted list.

**Why a greedy choice is safe:** Compare the greedy subset with any optimal subset at the first sorted item chosen by the greedy scan but omitted by the optimum. If the optimum has room, adding it is no worse. Otherwise, replace a later item: the replacement has no greater value, and the greedy item's label still had capacity at that point. Repeating the exchange transforms an optimum to include every greedy choice without decreasing its sum.

Because values are nonnegative, accepting a feasible item until the total limit is reached cannot lower the sum. The accumulated value is therefore maximal.

#### Complexity detail

Sorting $n$ item pairs takes $O(n\log n)$ time. The greedy scan and label-count updates take $O(n)$ expected time. The sorted pairs and at most $n$ label counters require $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Group and merge label lists:** Sort values within each label and repeatedly choose the best available head. It can be implemented with a heap but is more elaborate than one global sort.
- **Selection sort before greedy scanning:** It preserves correctness but takes $O(n^2)$ time.
- **Take the globally largest `numWanted` values first:** It can violate `useLimit` and miss smaller feasible items from other labels.
- **One dominant label:** Select at most `useLimit` of its values even when more are globally largest.
- **`numWanted` larger than feasible positive choices:** The subset is allowed to contain fewer than `numWanted` items.
- **Zero-valued items:** Selecting them does not change the maximum sum.
- **Equal values:** Their order is irrelevant; any feasible tie choice gives the same immediate contribution.

</details>
