## General

**Start with the natural partition dynamic program**

Let `prefix[e]` be the sum of the first `e` elements:

$$
P_e=\sum_{r=0}^{e-1}\texttt{nums}[r],
\qquad P_0=0.
$$

Then the sum of the contiguous subarray from index `j` through `e - 1` is $P_e-P_j$. Its triangular value is

$$
T(P_e-P_j)
=
\frac{(P_e-P_j)(P_e-P_j+1)}2.
$$

Define

$$
\operatorname{dp}_g[e]
$$

as the minimum score for partitioning the first `e` elements into exactly `g` nonempty subarrays.

If the final group begins at index `j`, the first `j` elements must form exactly `g - 1` groups, and the last group contributes $T(P_e-P_j)$. The recurrence is

$$
\operatorname{dp}_g[e]
=
\min_{g-1\le j<e}
\left(
\operatorname{dp}_{g-1}[j]+T(P_e-P_j)
\right).
$$

The lower bound $j\ge g-1$ leaves at least one element for each earlier group. The strict upper bound $j<e$ ensures the last group is nonempty.

A direct implementation tries every split `j` for every endpoint `e` and every group count, costing $O(KN^2)$. With $N=1000$, the source improves this transition to amortized constant time per state using a monotone convex hull.

**Expand the triangular cost into a query term and a line**

Write $X=P_e$ for the current endpoint sum and $Y=P_j$ for a candidate split sum. Expanding the subarray value gives

$$
\begin{aligned}
T(X-Y)
&=\frac{(X-Y)^2+(X-Y)}2\\
&=\frac{X^2+X}{2}-XY+\frac{Y^2-Y}{2}.
\end{aligned}
$$

Insert this into the recurrence:

$$
\operatorname{dp}_g[e]
=
\frac{X^2+X}{2}
+
\min_j
\left(
(-Y)X+
\operatorname{dp}_{g-1}[j]
+
\frac{Y^2-Y}{2}
\right).
$$

For a fixed split `j`, everything except `X` is constant. It defines a line

$$
L_j(X)=m_jX+b_j
$$

with

$$
m_j=-P_j
$$

and

$$
b_j=\operatorname{dp}_{g-1}[j]+\frac{P_j^2-P_j}{2}.
$$

The transition becomes:

1. query the minimum line value at $X=P_e$;
2. add the endpoint-only quantity $(X^2+X)/2$.

The source represents a line as the tuple `(slope, intercept)`. `evaluate(line, x)` returns `slope * x + intercept`.

All divisions are exact integer divisions. For any integer $q$, $q(q-1)$ and $q(q+1)$ are products of consecutive integers, so each is even.

**Why this hull has monotone slopes and monotone queries**

Every array element is positive. Therefore the prefix sums are strictly increasing:

$$
P_0<P_1<\cdots<P_N.
$$

Candidate splits are inserted in increasing index order, so their slopes $-P_j$ are strictly decreasing.

Endpoints are processed in increasing order, so query coordinates $X=P_e$ are also strictly increasing.

This is the ideal setting for a deque-based monotone convex hull:

- decreasing slopes allow useless newly surrounded lines to be removed from the back;
- increasing query coordinates allow lines that have permanently lost to the next line to be removed from the front.

No binary search over line intersections and no general Li Chao tree is necessary.

**Build one DP layer with exactly the legal split points**

`previous` stores the preceding group layer. Initially, before any group exists, only the empty prefix is feasible:

`previous[0] = 0`

Every other entry is `infinity`. This encodes $\operatorname{dp}_0[0]=0$ and makes partitioning a nonempty prefix into zero groups impossible.

For a layer `groups`, the earliest legal split is `start = groups - 1`. The source constructs the line for this split before scanning endpoints. The first legal endpoint is `end = groups`, which leaves exactly one element in every group in the most constrained case.

For each `end`, the source performs the hull query before inserting a line for split `end`. This order enforces `j < e`. If it inserted the current endpoint first, the query could choose `j = e` and create an empty final subarray.

After computing `current[end]`, the state `previous[end]` may become a legal split for a later endpoint. When it is finite, the source converts it into a line and adds it to the hull.

At the end of the layer, `previous = current` advances from exactly `groups - 1` groups to exactly `groups` groups. Repeating through `k` layers makes `previous[n]` the requested score for the whole array and exactly `k` nonempty parts.

**Remove lines from the front when the next one is already better**

At increasing query coordinate `total`, the source compares the first two hull lines:

`evaluate(hull[0], total) >= evaluate(hull[1], total)`.

If the second line is no worse, the first line is removed. Since the second line was inserted later, it has a smaller slope. As `X` increases further, that smaller slope only becomes more favorable relative to the first. The first line can never again be the minimum for any future query.

Using `>=` also removes the older line on a tie. Either produces the same current value, while the later line's smaller slope is at least as good for every larger query.

The loop continues until the front line is strictly better than the second at the current coordinate or only one line remains. The surviving front is then the minimum line for this query.

**Remove a redundant middle line during insertion**

Suppose the last two stored lines are `first` and `middle`, and `last` is the new line. Their slopes satisfy

$$
m_{\text{first}}>m_{\text{middle}}>m_{\text{last}}.
$$

The middle line is useful only if it becomes optimal after the first line but before the last line. Let the intersection of the first and middle lines occur at one coordinate, and the intersection of middle and last at another. If the first intersection is at or after the second, there is no increasing-query interval where middle is strictly best.

The source tests that ordering without floating-point division:

`(middle_intercept - first_intercept) * (middle_slope - last_slope) >= (last_intercept - middle_intercept) * (first_slope - middle_slope)`

This is the cross-multiplied comparison of the two intersection coordinates. All slope differences in the denominators are positive because slopes are strictly decreasing, so multiplying does not reverse the inequality.

If the condition holds, `middle` is popped from the back. The test repeats because the new line may also make several earlier tail lines redundant. Finally, the new line is appended.

Integer cross multiplication is important: large prefix sums and DP costs can make floating-point intersection calculations imprecise near ties.

**Trace the optimal split in the first example**

For `nums = [5,1,2,1]`, the prefix sums are `[0,5,6,8,9]`.

With one group, every prefix has only split 0, so the scores are its triangular values:

- first one element: $T(5)=15$;
- first two elements: $T(6)=21$;
- first three elements: $T(8)=36$;
- all four elements: $T(9)=45$.

For two groups ending at `e = 4`, the conceptual recurrence considers:

$$
\begin{aligned}
j=1 &: 15+T(9-5)=15+10=25,\\
j=2 &: 21+T(9-6)=21+6=27,\\
j=3 &: 36+T(9-8)=36+1=37.
\end{aligned}
$$

The minimum is 25, corresponding to `[5]` and `[1,2,1]`. The convex hull computes the same minimum by evaluating the three split lines at $X=9$ without explicitly scanning all three for this endpoint.

**Why the optimized transition is still the original DP**

Every finite previous state becomes exactly one line before it is needed by future endpoints. The algebra proves that evaluating that line and adding the endpoint-only term equals the original split score exactly.

Back removal discards only a line with no coordinate at which it can beat both its neighbors. Front removal discards only a line that has lost permanently under increasing queries. Thus the deque always retains a line attaining the minimum for every current query.

The source therefore evaluates the same set of legal partition choices as the quadratic recurrence, but it compresses the minimum search through line geometry.

## Complexity detail

Prefix construction takes $O(N)$ time and space. For one group layer, at most $N$ lines are inserted. Each line enters the deque once, can be popped from the back at most once, and can be popped from the front at most once. All hull operations across that layer total $O(N)$.

There are $K$ layers, so total time is $O(KN)$. This matches the manifest and improves on the direct $O(KN^2)$ recurrence.

`previous` and `current` each use $O(N)$ space. The prefix array and hull also use $O(N)$. Only two DP layers coexist, so total auxiliary space is $O(N)$ rather than $O(KN)$.

The sentinel `10**100` is vastly above any legal score: the total input sum is at most $10^7$, whose triangular value is about $5\cdot10^{13}$. It safely marks impossible states without being selected as a real optimum.

## Alternatives and edge cases

- **Quadratic partition DP:** Implement the recurrence directly by trying every split. It is the clearest reference model but costs $O(KN^2)$ time.
- **Li Chao tree:** A general minimum-line structure handles arbitrary slope and query order in $O(\log C)$ per operation. It would give roughly $O(KN\log C)$ time and is unnecessary because positive values provide both monotonicities.
- **Floating-point intersection deque:** Storing intersection coordinates can work, but exact cross multiplication avoids rounding errors for large integer costs and tied boundaries.
- **k equals one:** Only split 0 is legal, so the answer is the triangular value of the total array sum.
- **k equals N:** Every group contains one element, and the answer is the sum of the individual triangular values.
- **Exactly k groups:** Separate layers and the `groups - 1` start index prevent solutions with fewer groups from leaking into the result.
- **Nonempty groups:** Querying before inserting the current endpoint excludes split `j = e` and therefore excludes an empty last group.
- **Positive-element guarantee:** It makes prefix sums strictly increasing and slopes strictly decreasing. Allowing zeros would create equal slopes requiring deduplication; allowing negatives would break monotone query order and invalidate this deque implementation.
- **Large values:** Python integer arithmetic keeps expanded costs and cross products exact without overflow.
- **Tied line values:** Front removal keeps the newer, smaller-slope line, which cannot be worse at future larger query coordinates.
- **Impossible intermediate states:** Infinite entries are not inserted as lines, preventing a sentinel from contaminating valid hull arithmetic.
