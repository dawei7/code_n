## General

**Express the final subarray with prefix sums**

Let $P_i$ be the sum of the first $i$ elements, with $P_0=0$, and define the triangular-value function

$$
T(s)=\frac{s(s+1)}{2}.
$$

Let $D_g(i)$ be the minimum score for partitioning the first $i$ elements into exactly $g$ nonempty subarrays. If the final subarray begins at index $j$, its sum is $P_i-P_j$, so

$$
D_g(i)=\min_{g-1\le j<i}\left(D_{g-1}(j)+T(P_i-P_j)\right).
$$

The base state is $D_0(0)=0$; all other zero-group states are impossible. The range $g-1\le j<i$ both leaves enough elements for the earlier groups and guarantees that the final subarray is nonempty.

**Turn every split point into a line**

Expanding the quadratic term separates everything depending only on $i$ from the interaction with $j$:

$$
\begin{aligned}
D_g(i)
&=\frac{P_i^2+P_i}{2}
 +\min_j\left(
   -P_jP_i+D_{g-1}(j)+\frac{P_j^2-P_j}{2}
 \right).
\end{aligned}
$$

For a fixed split point $j$, the expression inside the minimum is a line evaluated at $x=P_i$:

$$
m_j=-P_j,
\qquad
b_j=D_{g-1}(j)+\frac{P_j^2-P_j}{2},
\qquad
m_jx+b_j.
$$

Therefore each DP transition is a minimum-line query plus the common term $(P_i^2+P_i)/2$.

**Exploit the two monotone orders**

Every array value is positive, so the prefix sums $P_i$ are strictly increasing. As split points advance, line slopes $-P_j$ are strictly decreasing; as endpoints advance, query coordinates $P_i$ are strictly increasing. Those two orders permit a lower convex hull stored in a deque:

- before inserting a line, remove trailing lines whose intersection order makes them permanently redundant;
- before answering a query, remove the front line while the next line is at least as good at the current coordinate;
- query endpoint $i$ before inserting its line, ensuring that only split points $j<i$ are considered.

Each line enters the deque once and leaves it at most once. A layer begins with the line for $j=g-1$, then processes endpoints $i=g,g+1,\ldots,N$ in order.

**Why the final state is exact**

For the first group, the recurrence considers its only legal starting prefix and assigns the correct triangular value. Assume the previous layer contains the optimum for every prefix using exactly $g-1$ groups. Every legal $g$-group partition of the first $i$ elements has one final cut $j$; the recurrence combines the optimal earlier partition at that cut with the exact value of its last subarray. Conversely, every candidate in the recurrence describes such a legal partition.

The algebraic line form does not add or remove candidates, and the convex hull returns the minimum among all lines inserted for legal split points. Thus every computed $D_g(i)$ is exact, and $D_K(N)$ is precisely the requested minimum score.

## Complexity detail

For each of the $K$ DP layers, every endpoint contributes at most one line and one query. Amortized deque work is constant per operation, so total time is $O(KN)$.

The prefix sums, previous layer, current layer, and hull each use $O(N)$ storage. Reusing the two DP rows keeps auxiliary space at $O(N)$ rather than $O(KN)$.

The benchmark defines size as $N$ and sets $K=N/2$. Along that workload, the accepted method takes $O(N^2)$ time because both dimensions grow together. The slower control scans every earlier cut for every state, taking $O(KN^2)=O(N^3)$ on the same tiers and therefore adding one observable growth exponent.

## Alternatives and edge cases

- **Quadratic transition scan:** Evaluate every legal $j$ directly for every state. This is the clearest recurrence implementation but costs $O(KN^2)$ time and is too slow at the upper bounds.
- **Divide-and-conquer DP optimization:** Convex segment costs satisfy the required monotonicity of optimal split points, giving another valid optimization route, usually $O(KN\log N)$ with a standard recursive layer computation. The monotone hull obtains $O(KN)$ here by using the expanded quadratic form.
- **Li Chao tree:** A general dynamic line container can evaluate the same recurrence in $O(KN\log S)$ time, where $S=\sum\texttt{nums}$, but it ignores the stronger monotone slope and query order.
- **Balanced sums without dynamic programming:** Convexity favors similar subarray sums, but contiguity and the exact number of groups can prevent a locally balanced cut from belonging to the global optimum.
- **`k = 1`:** The entire array is the only subarray, so the result is $T(P_N)$.
- **`k = N`:** Every element forms its own subarray, so the answer is $\sum_i T(\texttt{nums}[i])$.
- **Nonempty final group:** Insert the line for endpoint $i$ only after querying $D_g(i)$; inserting it first would incorrectly allow an empty last subarray.
- **Positive-value guarantee:** Strictly increasing prefix sums are what make both query order and slope order monotone. A version permitting negative values would need a more general hull data structure or another optimization.
- **Intersection comparisons:** Use cross multiplication rather than floating-point intersection coordinates so ties and large values remain exact.
- **Wide integer arithmetic:** Prefix sums can reach $10^7$, and a triangular value can exceed 32-bit range. Fixed-width implementations need 64-bit arithmetic for scores, products, slopes, and intercepts.
