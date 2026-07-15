# Jump Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1306 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-iii/) |

## Problem Description
### Goal
An array `arr` of non-negative integers and a starting index `start` define a jumping process. From a current index $i$, the value `arr[i]` permits a jump to either $i+\texttt{arr[i]}$ or $i-\texttt{arr[i]}$.

A jump may be taken only when its destination remains inside the array. Determine whether some sequence of legal jumps from `start` can reach any index whose stored value is 0. Indices may otherwise be revisited by the raw movement rules, so the search must handle cycles.

### Function Contract
**Inputs**

- `arr`: an array of length $n$, where $1 \le n \le 5\cdot10^4$.
- Each `arr[i]` satisfies $0 \le \texttt{arr[i]} < n$.
- `start`: the initial index, where $0 \le \texttt{start} < n$.

**Return value**

`true` if at least one zero-valued index is reachable from `start` through legal jumps; otherwise, `false`.

### Examples
**Example 1**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 5`
- Output: `true`
- Explanation: One valid route is $5\to4\to1\to3$, and `arr[3] = 0`.

**Example 2**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 0`
- Output: `true`

**Example 3**

- Input: `arr = [3,0,2,1,2]`, `start = 2`
- Output: `false`
- Explanation: The zero at index 1 exists but is not in the component reachable from index 2.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Interpret indices as graph vertices**

Treat every array index as a vertex. Index $i$ has up to two directed edges, one to $i+\texttt{arr[i]}$ and one to $i-\texttt{arr[i]}$, provided the destination is within $[0,n)$. The question is therefore whether a graph search from `start` encounters a vertex carrying zero.

**Search each reachable index once**

Begin breadth-first search with `start` in a queue and mark it visited immediately. When an index is removed, return `true` if its value is zero. Otherwise, generate its two possible destinations and enqueue each legal, unvisited index.

Marking on enqueue is essential: a zero jump creates a self-loop, while other values can create multi-index cycles. The visited structure prevents either from adding unbounded work. If the queue empties, every index reachable through any sequence of legal jumps has been examined and none contains zero, so returning `false` is correct.

#### Complexity detail

Each of the $n$ indices is enqueued at most once, and processing an index examines at most two destinations. The time is $O(n)$ and the queue plus visited structure use $O(n)$ space.

#### Alternatives and edge cases

- **Depth-first search:** An explicit stack gives the same $O(n)$ bounds and reachability result; recursive DFS risks exceeding Python's recursion depth on a long path.
- **Negate values in place:** When all original values are non-negative, mutation can encode visitation without a separate set, but zero needs special handling and modifying the caller's input is avoidable.
- **List-based visitation:** Testing membership in a growing list preserves correctness but can make a length-$n$ path take $O(n^2)$ time.
- **Start already on zero:** Return `true` before generating any destinations.
- **Out-of-bounds destinations:** Discard them; they are not legal jumps and must never be indexed.
- **Cycles and zero jumps:** Mark an index before queueing it so self-loops and mutual cycles terminate.
- **Unreachable zero:** The existence of zero somewhere in `arr` is insufficient; it must lie in the reachable component.

</details>
