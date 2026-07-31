## General

**Remove the harmless factor of two**

Let $P_i$ be the sum of the first $i$ elements, with $P_0=0$. It is convenient to double every score, so a subarray of sum $s$ contributes

$$
Q(s)=s^2+s.
$$

The final answer can be divided by two after the exact doubled optimum is known. Positivity makes $P_0,P_1,\ldots,P_N$ strictly increasing.

**Replace the exact group count with a penalty**

Fix a nonnegative integer penalty $p$. Let $F_p(i)$ be the minimum doubled score for the first $i$ elements when every subarray also costs $p$. Alongside it, retain $C_p(i)$, the number of subarrays used; whenever two candidates have the same penalized cost, prefer the one with more subarrays. If the final cut is after position $j$, then

$$
F_p(i)=\min_{0\le j<i}\left(F_p(j)+(P_i-P_j)^2+(P_i-P_j)+p\right).
$$

The base state is $F_p(0)=0$ with zero subarrays. Querying before inserting the line for $i$ guarantees that the newly formed last subarray is nonempty.

**Turn every previous cut into a line**

Expanding the recurrence separates the terms that depend only on $i$:

$$
F_p(i)=P_i^2+P_i+p+\min_j\left(-2P_jP_i+F_p(j)+P_j^2-P_j\right).
$$

Thus a cut after $j$ contributes a line evaluated at $x=P_i$ with

$$
m_j=-2P_j,
\qquad
b_j=F_p(j)+P_j^2-P_j.
$$

Prefix sums increase, so query coordinates increase. The slopes $-2P_j$ decrease as lines are inserted. A lower convex hull in an array therefore answers and inserts in amortized constant time: advance the head while the next line is better at the current prefix sum, and remove trailing lines whose intersection order proves them permanently redundant. Cross multiplication keeps every comparison exact.

Collinear candidates are retained. At a query where line values tie, the stored subarray counts choose the candidate with more parts. This tie rule is essential at a penalty where two exact group counts have equal penalized cost.

**Recover exactly `k` subarrays**

Let $A_r$ be the minimum doubled base score using exactly $r$ subarrays. The segment cost satisfies the Monge inequality. For $a\le b\le c\le d$, the difference between the crossed and uncrossed quadratic terms is

$$
Q(P_d-P_a)+Q(P_c-P_b)-Q(P_c-P_a)-Q(P_d-P_b)
=2(P_b-P_a)(P_d-P_c)\ge0.
$$

Consequently the sequence $A_r$ is discretely convex, and a penalty run minimizes $A_r+pr$. As $p$ increases, its preferred subarray count never increases. At $p=0$, splitting every positive element is optimal; by $p=S^2$, one subarray is optimal. Binary-search the largest integer $p$ whose tie-broken optimum still uses at least `k` parts.

At that boundary, `k` is either selected directly or lies on a flat marginal interval between tied counts. Discrete convexity gives the same recovery formula in both cases:

$$
A_k=F_p(N)-pk.
$$

Because $A_k$ is a doubled score, return $(F_p(N)-pk)/2$.

## Complexity detail

One fixed-penalty run processes each prefix once. Every line is inserted once and removed at most once, so the run takes $O(N)$ time. The penalty lies in the integer interval $[0,S^2]$, giving $O(\log S)$ runs and total time $O(N\log S)$.

The three hull arrays hold at most $N+1$ slopes, intercepts, and subarray counts. They are reused across penalty runs, so auxiliary space is $O(N)$.

The benchmark defines size as $N$, uses `k = N / 2`, and fills the array with ones. Then $S=N$: the accepted method takes $O(N\log N)$ time on these tiers, whereas the exact-group layer DP with a hull takes $O(KN)=O(N^2)$ because $K$ grows with $N$.

## Alternatives and edge cases

- **Exact-group hull DP:** Build one monotone convex hull for each of the `k` DP layers. It is correct and takes $O(KN)$ time, but `k` may equal $N=5\cdot10^4$, making the quadratic worst case too slow here.
- **Direct transition scan:** Try every preceding cut for every exact-group state. This straightforward recurrence costs $O(KN^2)$ time and is even less suitable at the upper bound.
- **Li Chao tree:** It can maintain the same transition lines without monotone assumptions, but adds a logarithmic factor to every query and insertion even though positive elements already order both slopes and coordinates.
- **Greedy balancing:** Convexity favors similar subarray sums, but contiguity can make the locally most balanced next cut incompatible with the best global partition.
- **`k = 1`:** Only the whole array is legal, and the answer is $S(S+1)/2$.
- **`k = N`:** Every element is a singleton, and the answer is $\sum_i\texttt{nums[i]}(\texttt{nums[i]}+1)/2$.
- **Penalty ties:** Prefer more subarrays when penalized costs tie and retain lines that meet at the same intersection; otherwise binary search can cross a flat marginal interval on the wrong side.
- **Positive elements:** Strictly increasing prefix sums make the array-backed monotone hull valid. Allowing zero or negative values would require handling equal or unordered slopes and queries.
- **Wide arithmetic:** $S$ may reach $5\cdot10^7$, so $S^2$, line intercepts, cross products, and the score exceed 32-bit range. Fixed-width languages need 64-bit storage, with wider intermediate products where necessary.
