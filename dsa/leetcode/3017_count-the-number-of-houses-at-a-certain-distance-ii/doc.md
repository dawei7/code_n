# Count the Number of Houses at a Certain Distance II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3017 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/) |

## Problem Description

### Goal

There are $N$ houses numbered from $1$ through $N$. Every consecutive pair of houses $i$ and $i+1$ is joined by a bidirectional road. One additional bidirectional road connects houses `x` and `y`; the endpoints may coincide or already be adjacent, in which case this road does not shorten any route.

For every distance $d$ from $1$ through $N$, count the ordered pairs of distinct houses $(a,b)$ whose shortest-path distance is exactly $d$. The pair $(a,b)$ is different from $(b,a)$.

Return an array `answer` of length $N$ where `answer[d - 1]` is that count. Distances that occur for no ordered pair contribute zero.

### Function Contract

**Inputs**

- `n`: The number of houses in the consecutive road chain.
- `x`: One endpoint of the additional bidirectional road.
- `y`: The other endpoint of the additional bidirectional road.

The source constraints guarantee $2 \le N \le 10^5$ and $1 \le \texttt{x},\texttt{y} \le N$.

**Return value**

- A length-$N$ list whose position $d-1$ counts ordered house pairs at shortest distance $d$.

### Examples

#### Example 1

- **Input:** `n = 3`, `x = 1`, `y = 3`
- **Output:** `[6, 0, 0]`
- **Explanation:** The added road turns the three houses into a triangle, so all six ordered pairs are one road apart.

#### Example 2

- **Input:** `n = 4`, `x = 1`, `y = 1`
- **Output:** `[6, 4, 2, 0]`
- **Explanation:** A self-connection creates no shortcut, leaving the original chain distances.

#### Example 3

- **Input:** `n = 5`, `x = 1`, `y = 5`
- **Output:** `[10, 10, 0, 0, 0]`
- **Explanation:** The graph is a five-house cycle. Five unordered pairs have distance one and five have distance two; both orientations are counted.
