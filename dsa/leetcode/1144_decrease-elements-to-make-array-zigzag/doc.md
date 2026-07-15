# Decrease Elements To Make Array Zigzag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1144 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/) |

## Problem Description

### Goal

An array `nums` is zigzag when its adjacent comparisons alternate in one of two strict patterns. It may begin with a peak, so `nums[0] > nums[1] < nums[2] > nums[3] ...`, or it may begin with a valley, so `nums[0] < nums[1] > nums[2] < nums[3] ...`. Equal adjacent values do not satisfy either pattern.

One move chooses any element of `nums` and decrements it by exactly `1`. An element may be chosen repeatedly, and no move can increase a value. Return the minimum number of moves needed to make the whole array zigzag in either of the two permitted patterns.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

The minimum total number of single-unit decrements that produces either valid zigzag pattern.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`
- Explanation: Decrementing `nums[2]` twice gives `[1, 2, 1]`, which follows the valley-peak-valley pattern.

**Example 2**

- Input: `nums = [9, 6, 1, 6, 2]`
- Output: `4`
- Explanation: Four decrements can make the even-indexed positions the peaks of a valid zigzag array.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Choose which parity contains the valleys.** Each valid zigzag form is completely determined by whether even indices or odd indices must be strictly smaller than their neighbors. Evaluate both choices and take the smaller cost.

**Lower each selected position only as far as necessary.** For a selected valley at index `i`, let $b_i$ be the smaller existing value among its available neighbors. The valley must end below $b_i$. If `nums[i] < b_i`, it costs nothing; otherwise it needs exactly `nums[i] - b_i + 1` decrements. A missing neighbor at an endpoint imposes no restriction.

**Why the local costs are independent.** Selected valley indices differ by two, so no two selected positions are adjacent. Their neighboring peak values therefore remain unchanged while calculating a fixed parity. Lowering a selected value to one below its smaller neighbor is both sufficient for its two strict comparisons and necessary because values can only decrease. Summing these forced minima gives the optimum for that parity, and the minimum of the two parity totals gives the global optimum.

#### Complexity detail

Each index is inspected a constant number of times across the two parity choices, so the running time is $O(n)$. The two accumulated costs and a few temporary values use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Unit-by-unit simulation:** Repeatedly decrementing a valley until it becomes small enough is correct, but its time depends on the magnitudes of the values rather than only on $n$.
- **Modify a copied array:** Building each candidate zigzag explicitly is unnecessary because selected valleys are nonadjacent; direct cost calculation avoids $O(n)$ extra space.
- **Single element:** An array of length one satisfies both comparison patterns vacuously, so the answer is `0`.
- **Equal neighbors:** Strict inequalities require at least one decrement; equality is not already zigzag.
- **Endpoints:** The first and last elements compare with only their one existing neighbor.
- **Negative final values:** Repeated decrements may lower an element below zero, which is permitted because the constraints describe only the input values.

</details>
