# Guided Example: Minimum Cost to Move Between Indices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-5, -2, 3], "queries": [[0, 2], [2, 0], [1, 2]]}`
- **Required output:** `[6, 2, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` where `nums` is **strictly increasing**.

The objective is to compute `[6, 2, 5]` from `{"nums": [-5, -2, 3], "queries": [[0, 2], [2, 0], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Adjacent value gaps

For edge between indices $i-1$ and $i$, define

$$
d_i=\texttt{nums}[i]-\texttt{nums}[i-1].
$$

Strict increase guarantees $d_i>0$. A normal move across this edge in either direction costs $d_i$.

The special closest-neighbor move may reduce one direction to cost 1. Because closest choice belongs to the departure index, the cost from $i-1$ to $i$ can differ from the cost from $i$ to $i-1$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-5, -2, 3], "queries": [[0, 2], [2, 0], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cost of moving right across one edge

Consider departure index $i-1$ and destination $i$.

If $i-1=0$, the departure has only one adjacent neighbor, so index $i$ is automatically closest and the cost is 1.

For an interior departure, compare:

- left gap $d_{i-1}=\texttt{nums}[i-1]-\texttt{nums}[i-2]$;
- right gap $d_i=\texttt{nums}[i]-\texttt{nums}[i-1]$.

The right neighbor is closest only when

$$
d_i<d_{i-1}.
$$

If the gaps tie, the problem chooses the smaller index, which is the left neighbor, so moving right does not receive the special cost.

The source's `c1` is:

$$
c_i^{\rightarrow}
=
\begin{cases}
d_i,&i>1\text{ and }d_{i-1}\le d_i,\\
1,&\text{otherwise}.
\end{cases}
$$

The first branch means the left neighbor is closer or wins the tie, so the best rightward edge move is the ordinary gap cost. The second means the right neighbor is uniquely closest, or the departure is the left endpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider departure index $i-1$ and destination $i$.

If $i-1... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cost of moving left across one edge

Now depart from index $i$ toward $i-1$.

If $i=n-1$, the departure is the right endpoint and has only the left neighbor, so cost is 1.

At an interior index $i$, compare left gap $d_i$ with right gap $d_{i+1}$. The left neighbor is closest when

$$
d_i\le d_{i+1}.
$$

Equality chooses the smaller index $i-1$, so unlike the rightward case, the tie does receive the special cost.

The source's `c2` is:

$$
c_i^{\leftarrow}
=
\begin{cases}
d_i,&i<n-1\text{ and }d_i>d_{i+1},\\
1,&\text{otherwise}.
\end{cases}
$$

This exactly encodes the asymmetric tie rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 2, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-5, -2, 3], "queries": [[0, 2], [2, 0], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 2, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dijkstra per query:** Model every allowed move:** - **Dijkstra per query:** Model every allowed move explicitly, but the complete direct-jump graph is dense and repeated shortest-path searches are unnecessary on the ordered line.
- **Use only absolute differences:** This misses closest-neighbor moves whose cost 1 is cheaper than the adjacent gap.
- **One undirected edge cost:** Incorrect because closest status belongs to the departure index; the two directions may have different costs.
- **Tie at an interior index:** The smaller adjacent index wins, making a left move special and a right move ordinary.
- **Left endpoint:** Its only neighbor is closest, so the first rightward edge costs 1.
- **Right endpoint:** Its only neighbor is closest, so the last leftward edge costs 1.
- **Adjacent gap equal to one:** Normal and special moves both cost 1, so either interpretation yields the same edge weight.
- **Same query endpoints:** No movement is needed, and prefix subtraction returns zero.
- **Negative values:** Strict ordering keeps every adjacent gap positive; absolute move costs depend on differences, not signs.
- **Direct long jump:** Its cost decomposes into adjacent gaps and can always be matched or improved by adjacent traversal.
- **Input preservation:** The source only reads `nums` and `queries` while constructing separate prefixes and output.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+Q)$. Let $N=\lvert\texttt{nums}\rvert$ and $Q=\lvert\texttt{queries}\rvert$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
