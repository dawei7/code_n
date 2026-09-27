# Guided Example: Minimum Score of a Path Between Two Cities

## 1. What the Definition of "Path" Actually Permits

Cities $1 \dots n$ are joined by bidirectional weighted roads. The **score** of a path is the
minimum distance among the roads it uses, and the task is to minimise that score over all paths from
city $1$ to city $n$.

The word "path" is looser here than in most graph problems. The contract states explicitly that a
path may contain the same road **multiple** times and may visit cities $1$ and $n$ multiple times.
That single concession changes the problem completely: the object being minimised is a **walk**, not
a simple path. A walk may wander, backtrack, and loop, and its score is only ever lowered by adding
more roads to it, because the score is a minimum rather than a sum.

Formally, if a walk traverses the edges $e_1, \dots, e_k$, its score is

$$
\text{score}(e_1, \dots, e_k) = \min_{1 \le t \le k} \text{distance}(e_t).
$$

Adding one more edge $e_{k+1}$ yields
$\min(\text{score}(e_1, \dots, e_k), \text{distance}(e_{k+1}))$, which can only decrease or stay
equal. Detours are therefore free in the score sense: they never hurt, and they may help.

## 2. The Answer Is the Component Minimum

Let $C$ be the set of cities reachable from city $1$, and let

$$
m = \min \{\, \text{distance}(e) : \text{ both endpoints of } e \text{ lie in } C \,\}.
$$

**Claim.** The minimum possible score equals $m$.

**Lower bound.** Take any walk from city $1$ to city $n$ and any edge $e$ it uses. Both endpoints of
$e$ are visited by the walk, and the walk begins at city $1$, so both endpoints are reachable from
city $1$; hence both lie in $C$ and $e$ is one of the roads counted by $m$. Every edge of the walk
therefore has distance at least $m$, so the walk's score — a minimum over its edges — is at least
$m$. In particular no walk can score below $m$, and roads outside $C$ can never appear in any walk
from $1$ to $n$, however small their distance.

**Upper bound.** Let $e^{*}$ be an edge of $C$ with $\text{distance}(e^{*}) = m$, and let its endpoints
be $u$ and $v$. Because $u \in C$, there is a walk $W_1$ from $1$ to $u$. Concatenate:

$$
1 \xrightarrow{\;W_1\;} u \;\to\; v \;\to\; u \xrightarrow{\;W_2\;} n,
$$

where the middle two steps traverse $e^{*}$ once in each direction and $W_2$ is any walk from $u$ to
$n$ — one exists because the input guarantees that city $n$ is reachable from city $1$, so
$n \in C$ and $u, n$ are in the same component. The concatenation is a legal walk under the stated
rules, it traverses $e^{*}$, and every one of its edges lies in $C$. Its score is therefore at most
$m$ and at least $m$, hence exactly $m$.

The two bounds meet, so the answer is $m$ — computed without ever constructing a walk.

## 3. The Forced-Pair Structure of the Component

The official first example is $n = 4$ with roads
$[[1,2,9], [2,3,6], [2,4,5], [1,4,7]]$, expected `5`. Every city is reachable from city $1$, so
$C = \{1, 2, 3, 4\}$ and $m$ is the minimum over all four roads.

| Road | Endpoints | Distance | Both endpoints in $C$? | Counts toward $m$? |
|:---|:---|:---:|:---:|:---:|
| $e_1$ | $1$–$2$ | 9 | yes | yes |
| $e_2$ | $2$–$3$ | 6 | yes | yes |
| $e_3$ | $2$–$4$ | 5 | yes | yes |
| $e_4$ | $1$–$4$ | 7 | yes | yes |

The minimum is $5$, attained by $e_3$. The official explanation gives the simple path
$1 \to 2 \to 4$ with score $\min(9, 5) = 5$: the light edge happens to lie on a short simple path,
so no detour is needed here. The same value would be obtained by the walk
$1 \to 2 \to 4 \to 2 \to 4 \to 1 \to 4$, and so on — the score cannot rise above $5$ once $e_3$ is
included, which is the monotonicity noted in Section 1.

City $3$ is a leaf hanging off city $2$ and is irrelevant to the answer, but it is part of $C$,
and any road incident to it would count toward $m$.

## 4. A Trace Where the Detour Is Mandatory

The official second example is $n = 4$ with roads $[[1,2,2], [1,3,4], [3,4,7]]$, expected `2`.
Here $C = \{1,2,3,4\}$ and the minimum edge is $1$–$2$ with distance $2$. The catch is that city $2$
is a dead end: the only road out of it is the same road back. A simple path from $1$ to $4$ must go
$1 \to 3 \to 4$ with score $\min(4,7) = 4$, which is **not** the answer.

| Leg | Move | Edge distance | Path minimum after the leg |
|:---:|:---|:---:|:---:|
| 1 | $1 \to 2$ | 2 | 2 |
| 2 | $2 \to 1$ (same road again) | 2 | 2 |
| 3 | $1 \to 3$ | 4 | 2 |
| 4 | $3 \to 4$ | 7 | 2 |

The walk $1 \to 2 \to 1 \to 3 \to 4$ scores $2$, exactly the component minimum. Leg 2 is the step
that a simple-path method would forbid and the reason the naive "shortest-path style" reading of the
problem is wrong. Reusing a road is explicitly permitted, and it converts a dead-end branch into a
free score reduction.

## 5. Traversing the Graph to Collect the Minimum

Because the answer is a minimum over a connected component, the algorithm is a single traversal of
the component of city $1$ that folds every examined road into a running minimum. The traversal must
inspect the adjacency list of each visited city completely:

| Visit order | City | Neighbours examined | Distances folded in | Running minimum |
|:---:|:---:|:---|:---|:---:|
| 1 | $1$ | $2$, $3$ | 2, 4 | 2 |
| 2 | $2$ | $1$ | 2 (already seen road) | 2 |
| 3 | $3$ | $1$, $4$ | 4, 7 | 2 |
| 4 | $4$ | $3$ | 7 | 2 |

Two properties of this table matter. First, a road is examined from both of its endpoints, so each
road's distance is folded in at least twice; that redundancy is harmless for a minimum and is what
makes the traversal order irrelevant. Second, when the traversal reaches a city whose neighbour is
already visited, the road between them still has to be folded in — that road belongs to the
component, and its distance is a legitimate candidate for $m$.

**Why folding in a cycle-closing road matters.** Consider the constructed instance $n = 3$ with roads
$[[1,3,9], [3,2,8], [1,2,5]]$. The component is $\{1,2,3\}$ and the true minimum is $5$, the road
$1$–$2$. A traversal that folds in a distance **only** when it discovers a new city can miss it:
starting at city $1$, the list is scanned as $(3,9)$ then $(2,5)$; the road to city $3$ is taken
first, city $3$ then leads to city $2$ through the distance-$8$ road, and only afterwards does the
scan return to the $(2,5)$ entry — by which time city $2$ is already visited. Such an
order-dependent traversal would report $8$ instead of $5$. The discipline is simple: fold the
distance in unconditionally, and recurse only when the neighbour is new.

## 6. Invariant and Correctness

**Invariant.** After the traversal finishes processing a city $a$, every road with at least one
endpoint already visited and belonging to the scanned portion of $a$'s adjacency list has had its
distance folded into the running minimum, and the visited set contains exactly the cities reached so
far.

**Preservation.** For each adjacency entry $(b, w)$ of the current city, the distance $w$ is folded
in before any decision about recursing. Whether $b$ is new or already visited, the road $a$–$b$ is
part of the component and its weight is a valid candidate; folding it in unconditionally therefore
never loses a candidate. Recursing exactly when $b$ is unvisited adds $b$ to the visited set and
extends the processed region without revisiting any city, so the traversal terminates.

**Soundness.** Every distance folded in belongs to a road whose endpoints are reachable from city
$1$ — the traversal only ever stands on visited cities, which are reachable by construction — so the
running minimum is at least $m$ at all times and never falls below the true component minimum.

**Completeness.** Let $e = (u, v)$ be the component road attaining $m$. Both $u$ and $v$ are
reachable from city $1$, so both are visited; when the traversal stands on $u$ it scans the entry
$(v, \text{distance}(e))$ and folds it in, regardless of $v$'s visited status. Hence every road of
$C$ contributes, the running minimum reaches $m$, and no terminal condition (dead end, cycle,
already visited leaf) prevents that. Since Section 2 proved the optimum equals $m$, the reported
value is correct.

**Why disconnected low roads are ignored correctly.** A road in a different component has both
endpoints unreachable from city $1$, so neither endpoint is ever visited and the road is never
scanned. This is not an omission but a consequence of the graph structure: such a road cannot appear
in any walk from $1$ to $n$.

## 7. Boundary Analysis

Every row is an authored case with a verdict that follows from the component-minimum rule.

| Instance | $n$ | Roads | Component of $1$ | Expected | Why it is a boundary |
|:---|:---:|:---|:---|:---:|:---|
| Direct component route | 4 | $1$–$2$:9, $2$–$3$:6, $2$–$4$:5, $1$–$4$:7 | $\{1,2,3,4\}$ | 5 | The light road lies on a simple path; no detour needed. |
| Detour lowers the score | 4 | $1$–$2$:2, $1$–$3$:4, $3$–$4$:7 | $\{1,2,3,4\}$ | 2 | Requires reusing a road into a dead end; a simple-path reading gives 4. |
| Minimum graph | 2 | $1$–$2$:10000 | $\{1,2\}$ | 10000 | One road, one candidate, and the maximum possible distance. |
| Light side branch | 5 | $1$–$2$:9, $2$–$5$:8, $2$–$3$:1, $3$–$4$:7 | all five cities | 1 | The lightest road leads away from every route to city $5$. |
| Lower road elsewhere | 6 | $1$–$2$:8, $2$–$6$:7, $3$–$4$:1, $4$–$5$:2 | $\{1,2,6\}$ | 7 | Distances 1 and 2 belong to another component and must be ignored. |
| Cycle with a light chord | 5 | $1$–$2$:10, $2$–$3$:6, $3$–$1$:4, $2$–$4$:3, $4$–$5$:9 | all five cities | 3 | The minimum sits on a road discovered after both endpoints are reachable. |
| Distance range | 4 | $1$–$2$:10000, $2$–$3$:5000, $3$–$4$:1 | $\{1,2,3,4\}$ | 1 | Large intermediate distances do not dilute a minimum. |

The "light side branch" row is the clearest demonstration that this is not a shortest-path problem.
The road $2$–$3$ with distance $1$ leads to a leaf-like wing and appears on no simple route from $1$
to $5$; nevertheless the answer is $1$, because the walk may step into the branch, use the light
road, and step back out. A Dijkstra-style method that optimises a sum, or a simple-path enumeration,
would both produce $8$ here.

## 8. Alternatives and Their Cost

| Approach | Idea | Verdict |
|:---|:---|:---|
| Component traversal with a running minimum | Fold in every road seen from a visited city. | Chosen method: one linear pass, and the proof in Section 2 shows it is exact. |
| Enumerate all simple paths | Try every simple $1 \to n$ path and take the best minimum. | Wrong and infeasible: exponentially many paths, and the true optimum may need a repeated road. |
| Shortest-path style optimisation | Run Dijkstra or Bellman-Ford on summed distances. | Solves a different problem; totals and minima behave in opposite ways, as the detour example shows. |
| Minimax path search | Find the path that maximises its minimum edge (a widest-path problem). | Also the wrong direction, and equally wrong here: the task minimises the minimum. |
| Union-find over thresholded roads | Add roads in increasing order until $1$ and $n$ connect. | Correct but $O(m \log m)$ for the sort plus near-linear union-find; more machinery than a single traversal needs. |
| Label propagation of component minima | Propagate each component's running minimum until stable. | Equivalent to a traversal, but often implemented with repeated passes that are easy to get wrong. |

The union-find row is the strongest alternative and it does compute $m$ correctly: the first road
weight at which cities $1$ and $n$ join the same set is exactly the component minimum. It is
rejected only on cost — sorting dominates, and the answer never needs the roads to be ordered.

## 9. Complexity Derivation

Let $n$ be the number of cities and $m = \lvert \text{roads} \rvert$.

**Time.** Building the adjacency structure costs $O(m)$, since each road appends one entry to each of
two lists. The traversal visits each city of the component at most once and scans each adjacency
entry of a visited city exactly once, so it performs $O(n + m)$ work overall. Folding a distance in
is a single comparison, and the visited test is constant-time. Since $n, m \le 10^{5}$, this is a
linear pass over the input graph, and the constant is small: roughly $2m$ adjacency entries plus $n$
visited checks. Cities outside the component are never touched, so an input with many disconnected
cities is cheaper, not more expensive.

**Auxiliary space.** The adjacency structure stores $2m$ directed entries, $O(n + m)$ total. The
visited set is one flag per city, $O(n)$, and the running minimum is a single integer, $O(1)$. A
recursive traversal additionally consumes stack space proportional to the depth of the recursion,
which in the worst case — a long chain of cities — is $O(n)$; an iterative traversal with an
explicit stack has exactly the same $O(n)$ bound on the container but avoids the interpreter's
recursion limit, which matters at $n = 10^{5}$. The input `roads` array is read but never copied.

**Total.** $O(n + m)$ time and $O(n + m)$ auxiliary space. The space is dominated by the adjacency
structure rather than by the traversal, and no ordering, sorting, or priority queue is required — a
direct consequence of the fact that the answer is a component-wide minimum rather than a sum of
distances.
