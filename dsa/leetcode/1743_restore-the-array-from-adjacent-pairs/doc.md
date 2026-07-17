# Restore the Array From Adjacent Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1743 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/) |

## Problem Description

### Goal

An unknown integer array `nums` contains $n$ unique values. You are given all $n-1$ pairs of values that were adjacent in that array. Within any pair, the two values may appear in either order, and the pairs themselves are presented in arbitrary order.

Reconstruct and return an array whose consecutive values produce exactly the supplied adjacent pairs. A valid reconstruction is guaranteed to exist. If both orientations of the original path are possible, either orientation is a valid answer.

### Function Contract

**Inputs**

- `adjacentPairs`: $n-1$ two-element lists describing unordered adjacency between unique array values, where $2 \le n \le 10^5$.
- Every value lies between $-10^5$ and $10^5$, and the pairs collectively describe one path containing all $n$ values.

**Return value**

- Return any length-$n$ array of unique values whose unordered consecutive pairs are exactly `adjacentPairs`.

### Examples

**Example 1**

- Input: `adjacentPairs = [[2,1],[3,4],[3,2]]`
- Output: `[1,2,3,4]`
- Explanation: Its consecutive unordered pairs are `{1,2}`, `{2,3}`, and `{3,4}`.

**Example 2**

- Input: `adjacentPairs = [[4,-2],[1,4],[-3,1]]`
- Output: `[-2,4,1,-3]`
- Explanation: The reverse array `[-3,1,4,-2]` is equally valid.

**Example 3**

- Input: `adjacentPairs = [[100000,-100000]]`
- Output: `[100000,-100000]`
- Explanation: With two values, the sole pair determines adjacency but not orientation.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Interpret the pairs as an undirected path**

Create an adjacency list. For each pair `[u,v]`, add `v` to `u`'s neighbors and `u` to `v`'s neighbors. Because all original values are unique and every consecutive pair is present, this graph is exactly a path: its two endpoints have degree one and every interior value has degree two.

**Choose either endpoint**

Find any value with one neighbor and place it first. Choosing the other endpoint would simply reverse the reconstruction, which the contract also accepts.

**Walk without returning to the previous value**

At each interior value, one neighbor is the value just appended and the other is the only possible next value. Append the neighbor that differs from the previous value and continue until all $n$ vertices are present. Every supplied edge is traversed once, so the output contains all and only the required adjacencies.

#### Complexity detail

Building the graph processes the $n-1$ pairs once, and the path walk visits each of the $n$ values once, for $O(n)$ time. The adjacency map contains $n$ vertices and $2(n-1)$ neighbor entries, while the output contains $n$ values, so auxiliary storage is $O(n)$.

#### Alternatives and edge cases

- **Repeatedly scan all pairs:** Searching the raw pair list for the next neighbor avoids an adjacency map but can take $O(n^2)$ time.
- **Recursive depth-first search:** A DFS from an endpoint reconstructs the path, but a legal $10^5$-node path can exceed the language recursion limit.
- **Two values:** Either ordering of the only pair is valid.
- **Negative values:** Values are identifiers; their sign has no effect on adjacency.
- **Shuffled and reversed pairs:** Neither pair order nor orientation carries global left-to-right information.
- **Either endpoint first:** The two possible outputs are reversals and must both be accepted.
- **Unique values:** Remembering only the previous value is sufficient because a path has no repeated vertex or branch.

</details>
