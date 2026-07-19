# Count Ways to Build Rooms in an Ant Colony

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) |
| Frontend ID | 1916 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Tree, Depth-First Search, Graph Theory, Topological Sort, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An ant colony plans $N$ rooms numbered from `0` through `N - 1`. For each room `i`, `prevRoom[i]` identifies the room that must be built immediately before room `i` becomes accessible through a direct connection. Room `0` is the root and has parent `-1`; every other room is eventually reachable from it, so these connections form a rooted tree.

Only one room can be built at a time. Any unbuilt room may be chosen once its parent has already been built. Count all distinct orders that build every room while respecting those parent-before-child dependencies, and return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `prevRoom`: a length-$N$ parent array describing a rooted tree at room `0`.
- `prevRoom[0] = -1`; for each other room, `prevRoom[i]` is a valid room index.
- $2 \le N \le 10^5$.

**Return value**

- Return the number of valid complete construction orders modulo $1\,000\,000\,007$.

### Examples

**Example 1**

- Input: `prevRoom = [-1,0,1]`
- Output: `1`

The chain forces the order `0, 1, 2`.

**Example 2**

- Input: `prevRoom = [-1,0,0,1,2]`
- Output: `6`

The two child chains may be interleaved in six parent-respecting ways after room `0`.

**Example 3**

- Input: `prevRoom = [-1,0,0]`
- Output: `2`

After room `0`, its two children may be built in either order.
