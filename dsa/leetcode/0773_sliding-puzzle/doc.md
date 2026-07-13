# Sliding Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 773 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Breadth-First Search, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-puzzle/) |

## Problem Description

### Goal

Given a $2 x 3$ board containing each value from `0` through `5` exactly once, value `0` represents the blank square. In one move, swap the blank with one horizontally or vertically adjacent tile.

Return the minimum number of moves needed to reach the solved board `[[1,2,3],[4,5,0]]`. If no sequence of legal swaps can reach that arrangement, return `-1`. The other tiles cannot move except by swapping with the current blank position.

### Function Contract

**Inputs**

- `board`: a $2 x 3$ permutation of the integers `0` through `5`.

**Return value**

- The shortest legal move count to the target board, or `-1` when no legal sequence exists.

### Examples

**Example 1**

- Input: `board = [[1,2,3],[4,0,5]]`
- Output: `1`
- Explanation: Swap the blank with tile `5`.

**Example 2**

- Input: `board = [[1,2,3],[5,4,0]]`
- Output: `-1`
- Explanation: This permutation has the wrong parity and cannot reach the target.

**Example 3**

- Input: `board = [[4,1,2],[5,0,3]]`
- Output: `5`
- Explanation: The shortest legal sequence contains five blank swaps.

### Required Complexity

- **Time:** $O(V+E)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Encode each board as one state**

Flatten the six cells into a string such as `"123405"`. The blank's string index determines its legal swap destinations through a fixed adjacency table for the `2 x 3` geometry. Swapping characters produces every neighboring state.

**Search states in increasing move count**

Run breadth-first search from the input state. Store `(state, distance)` pairs in a queue and a set of states already discovered. The first time the target is removed from the queue, its distance is the answer. If the queue empties, the start lies in the unreachable parity component, so return `-1`.

Each graph edge is one legal move. Breadth-first search visits states in nondecreasing path length, so when it first reaches any state it has found a shortest path to that state. In particular, the first target distance is minimum. Exhausting the connected component without finding the target proves no legal sequence exists.

#### Complexity detail

Let `V` be the number of board permutations reached and `E` the legal swaps between them. BFS takes $O(V + E)$ time and $O(V)$ space for the queue and visited set. For this fixed puzzle, `V` is at most $6! = 720$ and every state has at most three edges.

#### Alternatives and edge cases

- **Bidirectional BFS:** Expanding from both the start and target can reduce the explored frontier while retaining $O(V + E)$ worst-case time.
- **Precomputed distance table:** Because the state space is fixed, one reverse BFS can answer many boards by lookup.
- **Visited list instead of a set:** The search stays correct, but repeated linear membership checks can take $O(V^2)$ time.
- **Depth-first search with pruning:** It can find a solution but does not naturally guarantee minimum moves and may revisit many paths.
- **Already solved board:** Return zero before generating neighbors.
- **Unreachable parity:** BFS explores only the start's 360-state component and returns `-1`.
- **Blank at a corner or edge:** The adjacency table supplies exactly two or three legal swaps as appropriate.

</details>
