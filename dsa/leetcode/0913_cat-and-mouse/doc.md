# Cat and Mouse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 913 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/cat-and-mouse/) |

## Problem Description
### Goal

Mouse and Cat play a turn-based game on an undirected graph. For each node `a`, `graph[a]` lists exactly the nodes joined to `a` by an edge. Mouse begins at node `1` and moves first, Cat begins at node `2` and moves second, and node `0` is the hole.

On every turn, the active player must traverse one incident edge. Cat may never move to node `0`. Mouse wins as soon as it reaches the hole, while Cat wins as soon as both players occupy the same node. If a position repeats with Mouse and Cat on the same nodes as before and with the same player due to move, the game is a draw.

Assume that both players choose moves optimally. Return `1` when Mouse can force a win, `2` when Cat can force a win, and `0` when neither player can force a win and optimal play leads to a draw.

### Function Contract
**Inputs**

- `graph`: an adjacency list for an undirected graph. Let $n$ be the number of nodes, with $3 \le n \le 50$.
- Every adjacency list is nonempty and contains unique valid neighbors other than its own node. The input guarantees that both players can always make a legal move under the game rules.

**Return value**

An integer outcome: `1` for a Mouse win, `2` for a Cat win, or `0` for a draw under optimal play.

### Examples
**Example 1**

- Input: `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]`
- Output: `0`
- Explanation: Each player can prevent the other from forcing a win, so optimal play repeats a state.

**Example 2**

- Input: `graph = [[1,3],[0],[3],[0,2]]`
- Output: `1`
- Explanation: Mouse moves directly from node `1` to the hole.

**Example 3**

- Input: `graph = [[2],[2],[0,1]]`
- Output: `2`
- Explanation: Mouse's only move enters Cat's starting node.
