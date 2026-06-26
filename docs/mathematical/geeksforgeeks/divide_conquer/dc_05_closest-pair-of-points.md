# Formal Mathematical Specification: Closest Pair of Points

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i$ is defined by the coordinate pair $(x_i, y_i) \in \mathbb{R}^2$. 

We define the Euclidean distance function $d: \mathbb{R}^2 \times \mathbb{R}^2 \to \mathbb{R}_{\ge 0}$ as:
$$d(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

The objective is to find the minimum distance $\delta^*$ defined by:
$$\delta^* = \min_{1 \le i < j \le n} d(p_i, p_j)$$

Let $S \subset P$ be a subset of points. We define the projection of $S$ onto the $x$-axis as $X(S) = \{x_i \mid p_i \in S\}$. Given a vertical line $L$ defined by $x = x_{mid}$, we partition $P$ into two subsets:
$P_L = \{p \in P \mid x \le x_{mid}\}$ and $P_R = \{p \in P \mid x > x_{mid}\}$.

## 2. Algebraic Characterization

The algorithm relies on the principle of divide and conquer. Let $\delta_L$ and $\delta_R$ be the minimum distances within $P_L$ and $P_R$ respectively. Let $\delta = \min(\delta_L, \delta_R)$. 

To account for pairs $(p_i, p_j)$ such that $p_i \in P_L$ and $p_j \in P_R$, we define the "strip" $S_\delta$ as:
$$S_\delta = \{p \in P \mid |x_p - x_{mid}| < \delta\}$$

**Lemma (The Sparsity Property):** For any point $p \in S_\delta$, there are at most 7 points $q \in S_\delta$ such that $y_q \in [y_p, y_p + \delta]$. 
*Proof Sketch:* Consider a rectangle of size $2\delta \times \delta$ centered at the dividing line. This rectangle can be partitioned into two $\delta \times \delta$ squares. Within each square, no two points can be closer than $\delta$. By the pigeonhole principle, each $\delta \times \delta$ square can contain at most 4 points (one at each corner). Thus, the total number of points in the $2\delta \times \delta$ region is at most 8. Excluding the point $p$ itself, we need only check the next 7 points in the $y$-sorted order.

The recurrence relation governing the algorithm is:
$$T(n) = 2T\left(\frac{n}{2}\right) + f(n)$$
where $f(n)$ represents the cost of the merge step. If the strip is sorted by $y$ at each level, $f(n) = O(n \log n)$, leading to $T(n) = O(n \log^2 n)$. If the points are pre-sorted by $y$, $f(n) = O(n)$, leading to $T(n) = O(n \log n)$.

## 3. Complexity Analysis

### Time Complexity
The algorithm follows the Master Theorem for divide and conquer recurrences. 

1. **Base Case:** For $n \le 3$, the brute force calculation takes $O(1)$ time.
2. **Divide:** Finding the median $x_{mid}$ takes $O(1)$ time given a sorted array.
3. **Conquer:** Two recursive calls on sets of size $n/2$.
4. **Merge:** 
   - Constructing the strip $S_\delta$ takes $O(n)$.
   - Sorting $S_\delta$ by $y$ takes $O(n \log n)$.
   - The linear scan of the strip takes $O(n \cdot k)$, where $k=7$ is a constant.

The recurrence $T(n) = 2T(n/2) + O(n \log n)$ yields $T(n) = O(n \log^2 n)$ by Case 2 of the Master Theorem. By maintaining a globally sorted list of points by $y$ and passing it through the recursion (filtering in $O(n)$), the merge step becomes $O(n)$, yielding:
$$T(n) = 2T(n/2) + O(n) \implies T(n) = O(n \log n)$$

### Space Complexity
The space complexity is dominated by the recursion stack and the storage of the auxiliary arrays (the sorted points and the strip).
- **Recursion Stack:** The depth of the recursion tree is $\lceil \log_2 n \rceil$.
- **Auxiliary Storage:** At each level of the recursion, we store a subset of points of size at most $n$. 
- **Total Space:** Since the arrays are passed by reference or created within the scope of the recursive call, the total auxiliary space is $O(n)$ to maintain the sorted order and the strip. Thus, the space complexity is $O(n)$.