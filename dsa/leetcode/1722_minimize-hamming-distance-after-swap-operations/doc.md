# Minimize Hamming Distance After Swap Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1722 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) |

## Problem Description

### Goal

You are given equal-length integer arrays `source` and `target`. Each pair `[a, b]` in `allowedSwaps` permits swapping the values currently stored at the distinct 0-indexed positions `a` and `b`. Any permitted swap may be applied repeatedly and the operations may occur in any order.

The Hamming distance is the number of indices where the resulting `source` value differs from `target` at the same index. Rearrange `source` using the allowed operations and return the minimum Hamming distance achievable.

### Function Contract

**Inputs**

- `source`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{source[i]} \le 10^5$.
- `target`: an integer array of the same length, where $1 \le \texttt{target[i]} \le 10^5$.
- `allowedSwaps`: at most $10^5$ distinct-index pairs `[a, b]` with $0 \le a,b<n$.
- Let $m = \lvert \texttt{allowedSwaps} \rvert$.

**Return value**

- Return the smallest possible number of indices where `source[i] != target[i]`.

### Examples

**Example 1**

- Input: `source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]`
- Output: `1`
- Explanation: The first component can place $2,1$ exactly, and the second can place $4$ but has no $5$.

**Example 2**

- Input: `source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []`
- Output: `2`
- Explanation: With no permitted swap, the two middle mismatches cannot be changed.

**Example 3**

- Input: `source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]`
- Output: `0`
- Explanation: All indices are connected transitively, so the source multiset can be permuted into the target order.

### Required Complexity

- **Time:** $O((n+m)\alpha(n))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Convert permitted swaps into components**

Treat indices as graph vertices and every allowed pair as an undirected edge. Repeated swaps along a path can move values between any two vertices in the same connected component, while no operation can move a value between different components. Use disjoint-set union with union by size and path compression to identify these components.

**Count the values available to each component**

For every source index, find its component representative and increment that component's counter for `source[index]`. These counters describe exactly the multiset of values that can be assigned among the component's positions; the order in which swaps realize a permutation does not matter.

**Consume target requests component by component**

Scan target positions. If the position's component still has an unused copy of `target[index]`, consume one and match that position. Otherwise, no value from another component can be imported, so this position must contribute one mismatch. Greedy consumption is correct because equal values are interchangeable, and only their multiplicity within the same component affects how many requests can be satisfied.

#### Complexity detail

Disjoint-set operations over $n$ indices and $m$ swap edges take $O((n+m)\alpha(n))$ amortized time, where $\alpha$ is the inverse Ackermann function. Building and consuming all component counters adds $O(n)$ expected time. Parent, size, and frequency structures use $O(n)$ space.

#### Alternatives and edge cases

- **Depth-first component traversal:** Building adjacency lists and visiting every component once gives $O(n+m)$ traversal plus the same frequency accounting, with $O(n+m)$ graph storage.
- **Sort values within components:** Sorting each component's source and target values also reveals unmatched multiplicities but raises the bound to $O(n\log n)$ in the largest component.
- **Rediscover a component per position:** Repeating DFS or BFS for every target index is correct when matches are consumed carefully, but can take $O(n(n+m))$ time.
- **No allowed swaps:** Every index is its own component, so the answer is the ordinary Hamming distance.
- **Duplicate values:** Counters must preserve multiplicity; a set would incorrectly reuse one available copy.
- **Redundant edges and cycles:** Union-find safely ignores unions between indices already in the same component.
- **Equal global multisets:** A zero answer still requires each needed value to occur in the correct connected component, not merely somewhere in `source`.

</details>
