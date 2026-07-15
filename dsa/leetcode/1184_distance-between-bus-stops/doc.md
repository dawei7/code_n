# Distance Between Bus Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1184 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distance-between-bus-stops/) |

## Problem Description

### Goal

A bus route has $n$ stops numbered from `0` through `n - 1` and arranged in a circle. For every index `i`, `distance[i]` gives the distance along the edge joining stop `i` to stop `(i + 1) % n`.

The bus can travel around the circle in either direction: clockwise or counterclockwise. Given the stops `start` and `destination`, return the shorter of the two route distances connecting them. The two directions may have equal length, and an edge is allowed to have distance zero.

### Function Contract

**Inputs**

- `distance`: A list of length $n$, where $1\le n\le10^4$ and $0\le\texttt{distance[i]}\le10^4$. Entry `distance[i]` is the distance between neighboring stops `i` and `(i + 1) % n`.
- `start`: An integer satisfying $0\le\texttt{start}<n$.
- `destination`: An integer satisfying $0\le\texttt{destination}<n$.

**Return value**

- The minimum travel distance from `start` to `destination` over the two directions around the circular route.

### Examples

**Example 1**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 1`
- Output: `1`

The direct edge has length `1`; the route around the other three edges has length `9`.

**Example 2**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 2`
- Output: `3`

The two direction lengths are `1 + 2 = 3` and `3 + 4 = 7`.

**Example 3**

- Input: `distance = [1,2,3,4]`, `start = 0`, `destination = 3`
- Output: `4`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the circle to two complementary arcs.** Swapping `start` and `destination` when necessary makes `start <= destination`. The consecutive edges with indices from `start` through `destination - 1` form one route between the stops. Every remaining edge forms the route in the opposite direction.

**Accumulate both quantities in one pass.** Walk through `distance`, adding every edge to `total`. Add an edge to `direct` exactly when its index lies in the normalized half-open interval `[start, destination)`. The complementary arc then has length `total - direct`, so returning the smaller value checks both directions. These arcs partition all circle edges, which proves that neither possible route is omitted or counted twice.

#### Complexity detail

The single pass examines all $n$ edge distances once, for $O(n)$ time. Apart from the two accumulated distances and normalized stop indices, no storage grows with the route, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Prefix sums:** A prefix array makes later arc queries constant time, but this problem asks only one pair and the array would use unnecessary $O(n)$ space.
- **Generic shortest-path algorithm:** Modeling the stops as a weighted graph and running Dijkstra's algorithm is correct, but it ignores the fact that a cycle has exactly two simple routes between the stops.
- **Same stop:** When `start == destination`, the direct arc is empty and the answer is `0`.
- **Reversed indices:** Normalizing their order changes which arc is called direct but does not change either route length.
- **Zero-distance edges:** They contribute zero normally; multiple stops may therefore have a shortest travel distance of zero.
- **Equal arcs:** If both directions have the same length, that shared value is returned.
- **One-stop circle:** The only valid start and destination are both `0`, so the result is `0` regardless of the self-edge value.

</details>
