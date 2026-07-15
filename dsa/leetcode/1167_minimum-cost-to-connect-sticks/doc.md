# Minimum Cost to Connect Sticks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |

## Problem Description

### Goal

You are given an array `sticks` of positive integers, where `sticks[i]` is the length of the $i$-th stick. Choose any two current sticks of lengths $x$ and $y$ and connect them into one stick of length $x+y$.

Each connection costs $x+y$, and the combined stick remains available for later connections. Continue until exactly one stick remains. Different choices change how often each length contributes to later costs, so return the minimum possible total cost of connecting all the original sticks into one.

### Function Contract

**Inputs**

- `sticks`: An array of $n$ positive stick lengths, where $1 \le n \le 10^4$ and $1 \le \texttt{sticks[i]} \le 10^4$.

**Return value**

- The minimum sum of all connection costs needed to leave one stick.

### Examples

**Example 1**

- Input: `sticks = [2,4,3]`
- Output: `14`

Connect lengths `2` and `3` for cost `5`, then connect `5` and `4` for cost `9`; the total is `14`.

**Example 2**

- Input: `sticks = [1,8,3,5]`
- Output: `30`

**Example 3**

- Input: `sticks = [5]`
- Output: `0`

No connection is needed when only one stick exists.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Make the cheapest merge first.** Every combined length is charged immediately and may be charged again when that combined stick participates in later merges. Suppose an optimal merge tree has two smallest current lengths, $a$ and $b$, at different deepest positions. Exchanging the deeper leaves with any larger lengths cannot increase cost, because deeper leaves contribute to at least as many merge sums. The two smallest lengths can therefore be made siblings at maximum depth, meaning some optimal solution merges them first.

**Maintain the current minimum pair.** Put all lengths in a min-heap. Repeatedly execute `combined = heappop(heap) + heappop(heap)`, add `combined` to the running total, and push it back. The exchange argument applies again to the reduced collection after each merge, so every greedy choice preserves an optimal completion.

When the heap has one element, exactly $n-1$ connections have occurred and the accumulated total contains every paid sum once. A single input stick skips the loop and correctly returns zero.

#### Complexity detail

Heap construction takes $O(n)$ time. Each of the $n-1$ merges performs two removals and one insertion, each costing $O(\log n)$, for $O(n \log n)$ total time. The heap stores $O(n)$ current lengths and therefore uses $O(n)$ space.

#### Alternatives and edge cases

- **Sort after every merge:** Selecting the two shortest sticks remains correct, but repeatedly sorting the entire collection can take $O(n^2 \log n)$ time.
- **Merge in input order:** This can make a large partial stick participate repeatedly and does not minimize total cost.
- **Choose the two longest:** Charging large lengths early is the opposite of the needed greedy rule and can be much more expensive.
- **Single stick:** No merge is performed, so the cost is `0`.
- **Equal lengths:** Any two current minimum sticks may be chosen; ties do not affect optimality.
- **Input mutation:** Heapifying a copy preserves the caller's array while retaining the same asymptotic bounds.

</details>
