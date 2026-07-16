# Max Value of Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1499 |
| Difficulty | Hard |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/max-value-of-equation/) |

## Problem Description
### Goal

The array `points` describes points on a two-dimensional plane. Each entry is `[x_i, y_i]`, and the points are already ordered so their $x$-coordinates are strictly increasing.

Choose two distinct points with indices $i<j$ whose horizontal distance satisfies $lvert x_i-x_j\rvert \le k$. Among all such pairs, maximize

$$
y_i+y_j+lvert x_i-x_j\rvert.
$$

At least one pair is guaranteed to satisfy the distance restriction. Return the largest equation value, which may be negative.

### Function Contract
**Inputs**

Let $N$ be the number of points.

- `points`: a list of $N$ coordinate pairs with $2 \le N \le 10^5$.
- Every point has the form `[x_i, y_i]`, where $-10^8 \le x_i,y_i \le 10^8$.
- The $x$-coordinates are strictly increasing: $x_i < x_j$ whenever $i<j$.
- `k`: an integer with $0 \le \texttt{k} \le 2\cdot10^8$.
- At least one index pair satisfies the horizontal-distance limit.

**Return value**

Return the maximum value of $y_i+y_j+lvert x_i-x_j\rvert$ over all valid pairs $i<j$.

### Examples
**Example 1**

- Input: `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1`
- Output: `4`
- Explanation: The valid pairs produce $3+0+1=4$ and $10-10+1=1$; the larger value is $4$.

**Example 2**

- Input: `points = [[0,0],[3,0],[9,2]], k = 3`
- Output: `3`
- Explanation: Only the first two points satisfy the distance limit, and their equation value is $3$.

**Example 3**

- Input: `points = [[1,1],[2,2],[3,3]], k = 2`
- Output: `6`
- Explanation: The first and third points give $1+3+2=6$.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Separate the current point from the best prior contribution**

For a prior point $i$ and current point $j$, strict $x$ ordering gives $x_i<x_j$, so the absolute value disappears:

$$
y_i+y_j+lvert x_i-x_j\rvert
=(y_i-x_i)+(y_j+x_j).
$$

For fixed $j$, the second term is constant. The task is therefore to find the largest $y_i-x_i$ among earlier points satisfying $x_j-x_i\le k$.

Sweep `points` from left to right. A deque stores candidate prior points as pairs of their $x_i$ coordinate and score $y_i-x_i$.

**Expire candidates by horizontal distance**

Before evaluating the current point $(x_j,y_j)$, remove deque entries from the front while $x_j-x_i>k$. Because input $x$-coordinates increase, expired candidates form a prefix: once a point is too far left, it can never become valid for a later point.

After eviction, every remaining entry lies inside the current distance window. If the deque is non-empty, its front score will be the best prior contribution, so combine it with $x_j+y_j$ and update the answer.

**Maintain decreasing candidate scores**

Before inserting the current point for future iterations, compute its score $y_j-x_j$. Remove entries from the back while their scores are less than or equal to this new score.

Such an entry is permanently dominated. The new point has at least as large a score and a larger $x$-coordinate, so it expires no earlier and is at least as valuable for every future point. Keeping the older entry can never improve an answer.

Append the new point after evaluating the current one. That order enforces $i<j$ and prevents a point from pairing with itself.

**Why the deque front is always optimal**

The deque contains exactly the undominated candidates from the active horizontal window. Their scores decrease from front to back, so the first entry has the maximum $y_i-x_i$ among all valid earlier points. Expiration removes only points that violate the distance constraint, and dominance removal discards only points that a newer candidate can replace in every future comparison.

Thus every computed value uses the best legal partner for its current point. Considering each point once as $j$ covers every possible pair endpoint, so the maximum over those best partners is the global answer.

#### Complexity detail

Each point is appended once, removed from the front at most once, and removed from the back at most once. Although the algorithm contains two loops, the total number of deque operations is $O(N)$, giving $O(N)$ time. In the worst case the deque stores all active points, so auxiliary space is $O(N)$.

The benchmark keeps every prior point inside the distance window. The monotonic deque processes the points once, while a correct implementation that tests every earlier point for every current endpoint performs $O(N^2)$ work, completes all tiers, and is rejected by scaling.

#### Alternatives and edge cases

- **Max heap:** store candidates by descending $y_i-x_i$ and lazily remove expired points. This is $O(N\log N)$ time and $O(N)$ space and is simpler when monotonic dominance is less obvious.
- **Enumerate every pair:** directly test the distance and equation for each $i<j$. It is correct but takes $O(N^2)$ time.
- **Balanced search structure:** maintain active scores in a multiset with insertions, expirations, and maximum queries in $O(\log N)$ each, for $O(N\log N)$ total time.
- **Strictly increasing coordinates:** no sorting or normalization is needed; changing the input order would destroy the one-way expiration argument.
- **Exact distance boundary:** a pair with $x_j-x_i=k$ is valid; expire only when the difference is greater than $k$.
- **All negative equation values:** initialize the answer below every legal result rather than at zero.
- **Expired high score:** a very large $y_i-x_i$ must still be removed once its horizontal distance exceeds $k$.
- **Equal candidate scores:** keep the newer point because it expires later and is never worse for a future endpoint.
- **Single valid pair:** the deque may be empty at many points; update the answer only when a legal prior candidate exists.
- **Coordinate extremes:** the equation may combine values near the stated bounds, so fixed-width implementations should use a sufficiently wide integer type.

</details>
