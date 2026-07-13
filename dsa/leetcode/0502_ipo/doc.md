# IPO

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 502 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/ipo/) |

## Problem Description
### Goal
You begin with capital `w` and are given parallel arrays `profits` and `capital` describing distinct projects. Project `i` may be started only when current capital is at least `capital[i]`; after completion, its nonnegative `profits[i]` is added immediately to the available capital.

Choose and complete at most `k` distinct projects to maximize final capital, using each project no more than once. A project made affordable by an earlier profit may be selected later, while an unaffordable project cannot be chosen in anticipation of future gains. Return the greatest capital reachable after the allowed completions, not the selected project indices or total profit alone.

### Function Contract
**Inputs**

- `k`: the maximum number of projects that may be completed
- `w`: the initial capital
- `profits`: the profit earned by each project
- `capital`: the minimum capital required by the corresponding project

**Return value**

- The maximum capital achievable after at most `k` selections

### Examples
**Example 1**

- Input: `k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]`
- Output: `4`

**Example 2**

- Input: `k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]`
- Output: `6`

**Example 3**

- Input: `k = 1, w = 2, profits = [1,2], capital = [2,3]`
- Output: `3`

### Required Complexity

- **Time:** $O(n \log n + k \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reveal projects in capital order**

Sort `(required_capital, profit)` pairs by their requirement. Maintain a pointer to the first project not yet made available. At each selection step, advance the pointer while requirements are no greater than current capital and insert those profits into a max-heap.

**Choose the largest currently feasible profit**

Pop the maximum profit and add it to current capital. If the heap is empty, no unselected project is affordable, so no further selection can change capital and the process stops early.

**Why the greedy choice is safe**

Suppose an optimal plan chooses a smaller affordable profit while a larger one is available. Swapping the larger project into that step leaves at least as much capital afterward. Since project feasibility depends only on having enough capital, every later project in the original plan remains feasible. Repeating this exchange proves that taking the maximum affordable profit at each step can achieve an optimal final capital.

**Never select a project twice**

Each sorted project crosses the pointer and enters the heap once, and each chosen profit is removed once. Projects left in the heap remain available for later steps.

#### Complexity detail

Sorting `n` projects costs $O(n \log n)$. Each project is pushed at most once, and at most `k` profits are popped, adding $O((n + k) \log n)$ heap work. The sorted pairs and heap use $O(n)$ space.

#### Alternatives and edge cases

- **Two heaps:** a min-heap by capital plus a max-heap by profit avoids the initial sort but keeps the same asymptotic bounds.
- **Scan every project each round:** is correct but takes $O(k \cdot n)$ time.
- **Dynamic programming over subsets:** is exponential and unnecessary because profits never reduce capital.
- **No affordable project:** return the current capital immediately.
- **$k = 0$:** no project may be selected.
- **Zero-profit project:** selecting it cannot unlock anything beyond the current capital and may be skipped when no positive alternative exists.
- **More selections than projects:** the heap eventually empties after every project is used.

</details>
