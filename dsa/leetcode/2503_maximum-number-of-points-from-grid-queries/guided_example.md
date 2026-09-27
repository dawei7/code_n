# Guided Example: Maximum Number of Points From Grid Queries

Each query value $v$ defines a rule, not a path: standing on the top-left cell
of the matrix, a player may step to a 4-directionally adjacent cell only while
$v$ is **strictly** greater than the value of the cell currently occupied. The
first visit to a cell scores one point, revisits score nothing, and the process
stops the moment the player stands on a cell whose value is not strictly below
$v$. The requested number is the largest score attainable, which is the size of
the largest set of cells the player can ever stand on.

That reframing is the whole problem. Score equals the number of *distinct* cells
reachable under the threshold, because a player who can step onto a cell can
always step back the way they came: revisits are explicitly allowed and cost
nothing. So for each query independently we need

$$
A(v) = \#\{\, u : u \text{ is reachable from } (0,0) \text{ using only cells with value} < v \,\}.
$$

Answering each query with its own search would repeat almost all of the work,
because the sets $A(v)$ are nested. This lesson derives the offline, monotone
sweep that computes every $A(v)$ in one pass.

## 1. The family of reachable sets is monotone

Write $S(v)$ for the set of cells reachable from $(0,0)$ through cells whose
values are all strictly less than $v$. Two facts hold.

- If $u \in S(v)$ and $v \le v'$, then $u \in S(v')$: the witnessing path uses
  only cells below $v$, hence only cells below $v'$. So $S(v) \subseteq S(v')$.
- $A(v) = \lvert S(v) \rvert$, and the answer is $A(v)$, not any particular
  path, so the player's route freedom never needs to be enumerated.

Monotonicity means that sorting the queries ascending turns $k$ independent
searches into a single growing exploration. Between two consecutive thresholds
only the cells whose values lie in the half-open interval
$[v, v')$ can become newly eligible.

## 2. The representative instance

Use the first official example: a $3 \times 3$ matrix and three queries.

| Row \ Col | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | 3 |
| 1 | 2 | 5 | 7 |
| 2 | 3 | 5 | 1 |

| Original query index | Threshold $v$ | Position in sorted order | Required answer |
|:---:|:---:|:---:|:---:|
| 0 | 5 | 2nd | 5 |
| 1 | 6 | 3rd | 8 |
| 2 | 2 | 1st | 1 |

The queries arrive out of order and must be reported in their original order, so
the plan is: sort the thresholds, sweep once, and scatter each count back to its
original index.

## 3. The frontier and its invariant

The sweep keeps a min-heap of **frontier** cells keyed by grid value, together
with a visited flag per cell and a counter of cells already counted.

- The heap starts holding only $(0,0)$.
- A cell is marked visited at the moment it is pushed, never later.
- For a threshold $v$, cells are popped while the smallest frontier value is
  strictly less than $v$; each popped cell increments the counter and pushes its
  four neighbours that are not yet visited.

The invariant, maintained across the whole stream of sorted queries, is:

> every cell that has been popped lies on a path from $(0,0)$ consisting of
> popped cells, every popped cell has a value below the threshold currently being
> processed, and the counter equals the number of popped cells.

Visited-on-push is what makes the heap hold each cell at most once, so a cell can
never be counted twice no matter how many of its neighbours are popped.

## 4. Why no reachable cell is missed

**Soundness (nothing is over-counted).** A cell enters the heap only as a
neighbour of a popped cell, so following the parent links of any popped cell
backwards terminates at $(0,0)$ and yields a genuine 4-directional path. Every
cell on that path was popped before or at the same moment as the cell in
question, and a cell is popped only while its value is strictly below the
current threshold. The path therefore witnesses membership in $S(v)$, and the
counted cell truly contributes a point.

**Completeness (nothing is under-counted).** Suppose $u$ is reachable from
$(0,0)$ by a path $p_0 = (0,0), p_1, \dots, p_\ell = u$ whose values are all
strictly below $v$. Induct along the path. The origin is pushed at construction
and popped as soon as the sweep starts, because its value is strictly below $v$
(if it were not, the path could not exist). If $p_i$ has been popped, then
$p_{i+1}$ was either already visited — hence already pushed, hence popped or
still in the heap — or it was pushed when $p_i$ was popped. In the remaining case
$p_{i+1}$ sits in the heap with a value strictly below $v$, and the pop loop
cannot stop while such an element exists, because the loop stops only when the
minimum frontier value is at least $v$, which is impossible when a smaller
element is present. So $p_{i+1}$ is popped too. By induction $u$ is counted.

**Monotone reuse.** After a query with threshold $v$ is answered, the popped set
is exactly $S(v)$. The next query $v' \ge v$ continues from that state: by
monotonicity $S(v) \subseteq S(v')$, and the cells of $S(v') \setminus S(v)$ are
precisely those the continued sweep pops, because a cell outside $S(v)$ cannot
have been reachable earlier. The count carried forward is therefore the correct
size of the next answer as well.

## 5. Trace at threshold 2, then 5

Sort the thresholds: $2, 5, 6$. The heap initially holds the origin
$(0,0)$ with value 1.

**Threshold $v = 2$.** Only cells with value strictly below 2 may be popped, so
only the value-1 cells qualify.

| Step | Pop | Value | Value $< 2$? | Counter | Pushed this step |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(0,0)$ | 1 | yes | 1 | $(0,1)$ value 2, $(1,0)$ value 2 |

The loop then stops: the heap minimum is 2, which is not strictly below 2. The
answer for the query 2 is $1$, which is the whole reachable set
$\{(0,0)\}$.

**Threshold $v = 5$.** The sweep resumes with the counter at 1.

| Step | Pop | Value | Value $< 5$? | Counter | Pushed this step |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(0,1)$ | 2 | yes | 2 | $(0,2)$ value 3, $(1,1)$ value 5 |
| 2 | $(1,0)$ | 2 | yes | 3 | $(2,0)$ value 3; $(1,1)$ already visited |
| 3 | $(0,2)$ | 3 | yes | 4 | $(1,2)$ value 7 |
| 4 | $(2,0)$ | 3 | yes | 5 | $(2,1)$ value 5; $(1,0)$ already visited |

The loop stops when the heap minimum is 5, and the counter reads $5$. The
reachable set is the five cells with values $1,2,2,3,3$ that form a connected
region around the origin:

| Cell | $(0,0)$ | $(0,1)$ | $(1,0)$ | $(0,2)$ | $(2,0)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Value | 1 | 2 | 2 | 3 | 3 |
| Pop order | 1 | 2 | 3 | 4 | 5 |

## 6. Threshold 6, and the small cell behind a costly wall

Continue with $v = 6$. The heap still holds three cells that were pushed but not
popped: $(1,1)$ with value 5, $(2,1)$ with value 5, and $(1,2)$ with value 7.

| Step | Pop | Value | Value $< 6$? | Counter | Pushed this step |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(1,1)$ | 5 | yes | 6 | all four neighbours already visited |
| 2 | $(2,1)$ | 5 | yes | 7 | $(2,2)$ value 1 |
| 3 | $(2,2)$ | 1 | yes | 8 | $(1,2)$ and $(2,1)$ already visited |

The counter reads $8$ and the loop stops at the frontier value 7. This is the
decisive lesson of the instance: the cell $(2,2)$ has the smallest value in the
whole matrix, yet it is counted **last**, only after two value-5 cells open the
way. Reachability is a property of paths, not of values in isolation. The
bottom-right cell is behind the wall formed by $(1,1) = 5$, $(2,1) = 5$ and
$(1,2) = 7$, so its own tiny value is irrelevant until the threshold clears the
wall.

Scattering the three counts back to the original query positions gives
`[5, 8, 1]`, matching the required output.

| Sorted threshold | Cells in $S(v)$ | Count | Original query index that receives it |
|:---:|:---|:---:|:---:|
| 2 | $(0,0)$ | 1 | 2 |
| 5 | origin plus the four value-2 and value-3 cells | 5 | 0 |
| 6 | those five plus $(1,1)$, $(2,1)$, $(2,2)$ | 8 | 1 |

## 7. A barrier that keeps eligible cells out

The second interesting authored case has a wall of large values with small
values trapped on both sides:

| Row \ Col | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| 0 | 1 | 100 | 2 |
| 1 | 2 | 100 | 2 |
| 2 | 3 | 4 | 5 |

| Threshold $v$ | Eligible cells (value $< v$) | Reachable from $(0,0)$ | Answer |
|:---:|:---|:---:|:---:|
| 3 | the three value-1 and value-2 cells | $(0,0)$ and $(1,0)$ only | 2 |
| 5 | adds the value-3 and value-4 cells | the left column plus $(2,1)$ | 4 |
| 101 | every cell | the entire $3 \times 3$ matrix | 9 |

At $v = 3$ the cells $(0,2) = 2$ and $(1,2) = 2$ satisfy the value test but
cannot be entered, because every route to them crosses the value-100 column or
the value-5 corridor. An implementation that counted cells by value alone would
report a larger, wrong answer; the frontier design never confuses eligibility
with reachability.

## 8. Boundary conditions and strict inequality

| Situation | Correct behaviour | Trap it exposes |
|:---|:---|:---|
| A query equal to the origin value | answer 0, no cell is ever entered | the comparison is strict: equal values are *not* below the threshold |
| A cell whose value equals the threshold | excluded, and it may block the cells behind it | two comparisons must agree: a cell is popped when below $v$, and neighbours are pushed from popped cells |
| Duplicate query values | identical answers, each scattered to its own index | sorting must carry the original index, not overwrite it |
| Queries given in decreasing order | results still come out in the original order | scattering must use the saved index, since the sweep order differs from the input order |
| A value that makes the whole matrix eligible | every cell is counted exactly once | the loop must drain the heap completely without double counting |
| A one-cell-wide corridor of huge values | small cells beyond it stay uncounted | reachability is path-based, not value-based |

Two authored checks confirm the strictness rule. With
`grid = [[1,2],[2,1]]` and thresholds $1, 2, 3$ the answers are $0, 1, 4$: at
$v = 1$ the origin's value 1 is not strictly below 1; at $v = 2$ only the origin
qualifies; at $v = 3$ the four cells, whose values are all strictly below 3,
become reachable. And for a $2 \times 3$ matrix whose entries are all 7, the
thresholds 7 and 8 give $0$ and $6$.

## 9. Complexity: time and auxiliary space

Let $M = mn$ be the number of cells and $k$ the number of queries.

**Time.** Sorting the query thresholds with their original indices costs
$O(k \log k)$. Every cell is pushed onto the heap at most once and popped at most
once, since it is marked visited when pushed; with at most $M$ entries the heap
costs $O(M \log M)$ in total across the entire sweep, not per query. Each pop
inspects four neighbours, so the neighbour work is $O(M)$. The sweep is therefore
$O(k \log k + M \log M)$ overall, independent of how many queries are answered —
the offline sort is what removes the factor of $k$ from the graph search.

**Auxiliary space.** The visited flag array needs $O(M)$ booleans; the heap holds
at most $M$ entries, so $O(M)$; the sorted query list and the answer array need
$O(k)$. Total auxiliary space is $O(M + k)$, which matches the input order of
magnitude and never stores a path. The constraints $mn \le 10^{5}$ and
$k \le 10^{4}$ are what make this comfortably affordable.

| Strategy | Time | Auxiliary space | Trade-off |
|:---|:---:|:---:|:---|
| One heap sweep over sorted thresholds | $O(k \log k + M \log M)$ | $O(M + k)$ | the intended method; reuses the reachable region across all queries |
| Independent heap search per query | $O(k \cdot M \log M)$ | $O(M)$ | correct but re-explores the same region once per query; too slow for $k = 10^{4}$ |
| Flood fill per query over eligible cells | $O(k \cdot M)$ | $O(M)$ | simpler inner loop, still repeats the whole exploration per query |
| Binary search on the sorted cell values plus connectivity | $O(M \log M)$ per query at worst | $O(M)$ | only pays off if the number of distinct values is far smaller than the number of cells |
| Sorting cells once and growing a union-find region | $O(M \log M + k \log k)$ amortised | $O(M + k)$ | competitive in theory, but the merging order must respect the threshold exactly, which is fiddlier than the heap frontier |
