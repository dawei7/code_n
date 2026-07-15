# Height Checker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1051 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/height-checker/) |

## Problem Description

### Goal

A school is arranging students in one line for its annual photo. The requested arrangement is **non-decreasing order** by height; let `expected[i]` be the height that should appear at 0-indexed position `i` in that ordering.

The array `heights` gives the students' current order, with `heights[i]` representing the student at position `i`. Return the number of indices for which `heights[i] != expected[i]`. Students with equal heights are indistinguishable for this comparison.

### Function Contract

**Inputs**

- `heights`: the $N$ current heights, where $1 \le N \le 100$ and every height lies in $[1,H]$, with $H=100$.

**Return value**

- The number of positions whose current height differs from the height at that position in non-decreasing order.

### Examples

**Example 1**

- Input: `heights = [1,1,4,2,1,3]`
- Output: `3`
- Explanation: The expected order is `[1,1,1,2,3,4]`; indices `2`, `4`, and `5` differ.

**Example 2**

- Input: `heights = [5,1,2,3,4]`
- Output: `5`
- Explanation: Every position differs from `[1,2,3,4,5]`.

**Example 3**

- Input: `heights = [1,2,3,4,5]`
- Output: `0`

### Required Complexity

- **Time:** $O(N+H)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Count each possible height:** Build a frequency array indexed from $1$ through $H$. This records the multiset of student heights without comparison sorting.

**Generate the expected order incrementally:** Iterate height values in increasing order. For each value, consume its recorded frequency and compare that value with the corresponding positions of the original `heights` array. Advance one shared position after every comparison.

**Count mismatching indices:** Increment the answer whenever the current original height differs from the generated expected height. Repeating every value according to its count produces exactly the unique non-decreasing sequence with the same multiset.

The frequency table preserves every input height and its multiplicity. Visiting its indices increasingly therefore generates the same `expected` array that sorting would produce. Since each generated value is compared at its exact position, the counter includes every and only index satisfying `heights[i] != expected[i]`.

#### Complexity detail

Counting and comparing process $N$ array entries, while scanning the height domain costs $O(H)$. Total time is $O(N+H)$. The frequency array contains $H+1$ counters, using $O(H)$ space. Here $H=100$ is fixed, so these bounds are also linear time and constant auxiliary space with respect to $N$ alone.

#### Alternatives and edge cases

- **Comparison sorting:** Compare `heights` with `sorted(heights)` in $O(N log N)$ time and $O(N)$ space for the copy.
- **Insertion sort:** Explicitly sort a copy and compare it, but descending input takes $O(N^2)$ time.
- **In-place sorting:** It can reduce the extra copy but destroys the current order needed for comparison unless that order is saved elsewhere.
- **Already non-decreasing:** Every position matches and the answer is zero.
- **All equal heights:** Sorting changes nothing.
- **Duplicate heights:** Frequencies preserve multiplicity, so equal students occupy the correct number of consecutive positions.
- **Single student:** The only height is already in its expected position.
- **Boundary heights:** Values `1` and `100` are ordinary frequency indices and need no special handling.

</details>
