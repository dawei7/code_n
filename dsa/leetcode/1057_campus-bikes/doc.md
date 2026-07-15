# Campus Bikes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1057 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/campus-bikes/) |

## Problem Description

### Goal

A campus is represented by the X-Y plane. There are $W$ workers and $B$ bikes, where $W \le B$. Array `workers` gives the position of every worker, and `bikes` gives the position of every bike. Every worker and bike location is unique.

Assign one bike to each worker by repeatedly examining the workers and bikes that are still available. Choose the worker-bike pair having the shortest **Manhattan distance**. If several pairs have that same shortest distance, choose the pair with the smallest worker index; if a tie remains, choose the smallest bike index. Assign that bike to that worker and continue until no worker is available.

For points $(x_1,y_1)$ and $(x_2,y_2)$, their Manhattan distance is

$$
\lvert x_1-x_2 \rvert + \lvert y_1-y_2 \rvert.
$$

Return an array `answer` of length $W$ in which `answer[i]` is the 0-indexed bike assigned to worker `i`.

### Function Contract

**Inputs**

- `workers`: an array of $W$ coordinate pairs, where $1 \le W \le 1000$.
- `bikes`: an array of $B$ coordinate pairs, where $W \le B \le 1000$.
- Each coordinate is an integer in $[0,999]$, and all worker and bike locations are unique.
- Let $D$ be the greatest possible Manhattan distance between two allowed locations; here $D=1998$.

**Return value**

- An integer array of length $W$ mapping each worker index to its assigned bike index.

### Examples

**Example 1**

- Input: `workers = [[0, 0], [2, 1]], bikes = [[1, 2], [3, 3]]`
- Output: `[1, 0]`
- Explanation: Worker 1 and bike 0 form the uniquely closest pair. After they are assigned, worker 0 receives bike 1.

**Example 2**

- Input: `workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]]`
- Output: `[0, 2, 1]`
- Explanation: Worker 0 first receives bike 0. Workers 1 and 2 are equally far from bike 2, so the smaller worker index gives that bike to worker 1; worker 2 then receives bike 1.

### Required Complexity

- **Time:** $O(WB+D)$
- **Space:** $O(WB+D)$

<details>
<summary>Approach</summary>

#### General

**Turn the comparison rule into bucket order:** Every Manhattan distance is an integer from $0$ through $D$. Create one bucket for each distance. Enumerate workers in increasing index order and, for each worker, enumerate bikes in increasing index order. Append `(worker_index, bike_index)` to the bucket for that pair's distance. Within any one bucket, this insertion order already matches the required worker-index and bike-index tie breakers.

**Process globally closest pairs first:** Visit buckets from distance zero upward. For every stored pair, assign it only when its worker has no bike yet and its bike has not been used. Otherwise skip it because an earlier pair has already made at least one endpoint unavailable. Stop as soon as all $W$ workers have bikes.

Every available pair appears exactly once, and bucket traversal orders those pairs lexicographically by `(distance, worker_index, bike_index)`. Therefore, the first pair encountered whose endpoints are both available is precisely the pair demanded by the assignment rule at that moment. Recording it and continuing applies the same argument after each assignment, so the final array is exactly the prescribed allocation.

#### Complexity detail

Creating all pair records takes $O(WB)$ time and space. Initializing and scanning the distance buckets costs $O(D)$, while each pair is visited at most once. The total time is $O(WB+D)$ and the total auxiliary space is $O(WB+D)$. Under the stated coordinate bounds, $D=1998$, but keeping it explicit describes why bucket ordering is efficient.

#### Alternatives and edge cases

- **Sort every pair:** Sorting triples `(distance, worker_index, bike_index)` directly expresses the rule but costs $O(WB\log(WB))$ time and $O(WB)$ space.
- **Priority queue of all pairs:** A min-heap also yields pairs in the required order, but its removals retain the extra logarithmic factor and stale pairs still need to be skipped.
- **Repeated search among available pairs:** Rescanning all unassigned worker-bike pairs before every assignment uses less stored pair data but can require $O(W^2B)$ time.
- **Equal distances:** Worker index is compared before bike index; inserting pairs in nested worker-then-bike order preserves both tie breakers inside a distance bucket.
- **Already assigned endpoint:** A pair is ignored if either its worker or bike is unavailable, even if it precedes all remaining valid pairs in the global order.
- **More bikes than workers:** Unused bikes are expected; processing ends immediately after every worker has one assignment.
- **Single worker:** The nearest bike is chosen, with the smallest bike index resolving equal distances.

</details>
