# Formal Mathematical Specification: Closest Pair of Points

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i$ is represented by a coordinate pair $(x_i, y_i) \in \mathbb{R}^2$. 

We define the distance function $\delta: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}_{\ge 0}$ as the standard Euclidean metric:
$$\delta(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

The objective is to find the minimum distance $\Delta$ defined as:
$$\Delta = \min_{1 \le i < j \le n} \delta(p_i, p_j)$$

Let $S \subset P$ be a subset of points. We define the projection of $S$ onto the $x$-axis as $X(S) = \{x \mid (x, y) \in S\}$. Given a vertical line $L$ defined by $x = x_{mid}$, we partition $P$ into two subsets:
$P_L = \{p \in P \mid x \le x_{mid}\}$ and $P_R = \{p \in P \mid x > x_{mid}\}$.

## 2. Algebraic Characterization

The algorithm relies on the Divide and Conquer paradigm. Let $T(n)$ be the minimum distance for a set of $n$ points. The recurrence relation is governed by the combination of sub-problems:

1. **Divide:** Let $\Delta_L$ and $\Delta_R$ be the minimum distances in $P_L$ and $P_R$ respectively. Let $\delta = \min(\Delta_L, \Delta_R)$.
2. **Conquer (The Strip):** We define the strip $S_\delta$ as:
   $$S_\delta = \{p \in P \mid |x_p - x_{mid}| < \delta\}$$
   For any $p \in S_\delta$, we only consider points $q \in S_\delta$ such that $|y_p - y_q| < \delta$. 

**Geometric Lemma:** For any point $p \in S_\delta$, the number of points $q \in S_\delta$ such that $y_q \in [y_p, y_p + \delta]$ is at most 7. 
*Proof Sketch:* The region $[x_{mid}-\delta, x_{mid}+\delta] \times [y_p, y_p+\delta]$ can be partitioned into two squares of side $\delta/2$. By the Pigeonhole Principle, since any two points in the left (or right) half are at least $\delta$ apart, each square can contain at most 4 points. Thus, the total number of points in the $2\delta \times \delta$ rectangle is bounded by a constant $k=8$ (including $p$ itself).

The recurrence relation for the time complexity is:
$$T(n) = 2T(n/2) + O(n)$$
Where $O(n)$ represents the linear time required to merge the results by scanning the strip $S_\delta$ sorted by $y$-coordinate.

## 3. Complexity Analysis

### Time Complexity
The algorithm's time complexity is derived from the Master Theorem for divide-and-conquer recurrences. Given the recurrence:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
where $f(n) = O(n)$ is the work performed to merge the sub-problems (sorting the strip or filtering pre-sorted lists). 

According to the Master Theorem, for $a=2, b=2, d=1$:
Since $a = b^d$ ($2 = 2^1$), the complexity is:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
If the strip is sorted at each recursive step without pre-sorting, the merge step becomes $O(n \log n)$, leading to $T(n) = O(n \log^2 n)$. By maintaining points sorted by $y$-coordinate throughout the recursion, we ensure the merge step is strictly $O(n)$, achieving the optimal $\Theta(n \log n)$.

### Space Complexity
The space complexity $S(n)$ is determined by the recursion stack depth and the storage of the points:
1. **Recursion Stack:** The depth of the recursion tree is $\lceil \log_2 n \rceil$, contributing $O(\log n)$ to the auxiliary space.
2. **Data Storage:** Storing the points requires $O(n)$ space.
3. **Auxiliary Arrays:** In the optimal implementation, creating the strip $S_\delta$ at each level requires $O(n)$ space.

Thus, the total space complexity is:
$$S(n) = O(n)$$