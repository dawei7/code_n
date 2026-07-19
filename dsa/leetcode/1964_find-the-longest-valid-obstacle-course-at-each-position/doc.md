# Find the Longest Valid Obstacle Course at Each Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1964 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Binary Indexed Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/) |

## Problem Description
### Goal
The array `obstacles` lists obstacle heights in their original order. For
every index `i`, choose a subsequence from indices zero through `i` that must
include the obstacle at `i`.

The chosen indices must retain their array order, and their heights must be
non-decreasing: every height is at least the one immediately before it. Return
an array whose value at `i` is the greatest possible length of such an
obstacle course ending exactly at `i`.

### Function Contract
**Inputs**

- `obstacles`: a list of $N$ positive heights, where $1\le N\le10^5$ and each
  height is at most $10^7$.

**Return value**

- A length-$N$ list where position `i` contains the longest non-decreasing
  subsequence length that ends at `obstacles[i]`.

### Examples
**Example 1**

- Input: `obstacles = [1, 2, 3, 2]`
- Output: `[1, 2, 3, 3]`

**Example 2**

- Input: `obstacles = [2, 2, 1]`
- Output: `[1, 2, 1]`

**Example 3**

- Input: `obstacles = [3, 1, 5, 6, 4, 2]`
- Output: `[1, 1, 2, 3, 2, 2]`

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Keep the smallest tail for each length**

Maintain `tails`, where `tails[length - 1]` is the smallest ending height found
for any non-decreasing course of that length in the processed prefix. Smaller
tails are never worse: they permit every future obstacle that a larger tail
would permit. These representative heights stay sorted.

**Extend through equal heights**

For a new height, use an upper-bound search to find the first tail strictly
greater than it. Every preceding tail is less than or equal to the new height,
so the longest extendable course has length equal to that insertion index.
Appending the new obstacle produces the reported length `index + 1`.

If the index is new, append the height; otherwise replace the larger existing
tail at that index. The replacement preserves the best achievable lengths and
improves or retains their extension opportunities. Because the current
obstacle is explicitly appended to the chosen predecessor course, the reported
value ends at the required index. Using upper bound rather than lower bound is
essential: equal heights are allowed to extend a non-decreasing course.

#### Complexity detail

Each of the $N$ obstacles performs one binary search in a `tails` array of
length at most $N$, giving $O(N\log N)$ time. The tails and answer arrays each
store at most $N$ integers, so the auxiliary and output storage are $O(N)$.

#### Alternatives and edge cases

- **Predecessor dynamic programming:** For each index, inspect every earlier
  height no greater than the current height. This is direct and correct but
  takes $O(N^2)$ time.
- **Fenwick tree over compressed heights:** Query the best length at heights
  no greater than the current one and update its height. This also takes
  $O(N\log N)$ time but needs coordinate compression and more machinery.
- Equal consecutive heights produce increasing answers because equality is
  valid in a non-decreasing course.
- A strictly decreasing array gives answer one at every position.
- The smallest-tail representatives need not describe one single course;
  each position represents the best tail among courses of that length.

</details>
