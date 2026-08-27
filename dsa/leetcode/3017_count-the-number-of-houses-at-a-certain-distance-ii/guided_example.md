# Guided Example: Count the Number of Houses at a Certain Distance II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "x": 1, "y": 3}`
- **Required output:** `[6, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three **positive** integers `n`, `x`, and `y`.

The objective is to compute `[6, 0, 0]` from `{"n": 3, "x": 1, "y": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**See the graph hidden inside the street.** Houses $1$ through $n$ normally form a path: each house is connected to the next one. The extra street between $x$ and $y$ either changes nothing or turns part of that path into a cycle. The answer array is a distance histogram. Entry `answer[d - 1]` must contain the number of ordered pairs of distinct houses whose shortest-path distance is $d$. “Ordered” matters: if houses $a$ and $b$ are distance $d$ apart, both $(a,b)$ and $(b,a)$ contribute.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "x": 1, "y": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution constructs this histogram through closed-form pieces instead of inspecting every pair. Its arrays use zero-based indices, so index $q$ represents distance $q+1$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution constructs this histogram through closed-... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Handle a useless extra street immediately.** When $|x-y|\le 1$, the added street is either a self-loop or duplicates an existing path edge. It cannot shorten any route. In an ordinary path of $n$ houses, there are $n-d$ unordered pairs at distance $d$, hence $2(n-d)$ ordered pairs. The return value

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "x": 1, "y": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every ordered pair:** Running a shor:** - **Enumerate every ordered pair:** Running a shortest-distance formula for all $N(N-1)$ pairs is conceptually direct but costs $O(N^2)$ time, which does not meet the large input bound.
- **Breadth-first search from every house:** The graph has only $O(N)$ edges, but $N$ BFS traversals still cost $O(N^2)$ time and add considerable overhead.
- **Difference-array pair counting:** One can derive another linear solution by classifying endpoint ranges and applying range increments. That can be elegant, but it is not what this exact source implements; this source builds explicit cycle-and-tail histograms.
- **Self-loop, $x=y$:** The edge returns to the same house and cannot shorten a path. The `abs(x - y) <= 1` branch correctly returns the ordinary path counts.
- **Adjacent endpoints:** An extra edge between already adjacent houses duplicates the existing connection. This is handled by the same early branch.
- **Reversed input endpoints:** The cycle length uses an absolute difference, then the code swaps `x` and `y` when necessary before calculating tail lengths. The answer is therefore symmetric in the supplied endpoint order.
- **No left or right tail:** If the shortcut touches house 1 or house $n$, one tail length is zero. The corresponding contribution is skipped, avoiding invalid indexing and correctly leaving only the other tail.
- **Even cycle:** The opposite vertex is unique at distance $L/2$, so counts at that distance are $L$, not $2L$. The source has explicit even-parity corrections in both the cycle-only and tail interaction histograms.
- **Odd cycle:** There is no single antipodal vertex. Two directions remain distinct up to distance $\lfloor L/2\rfloor$, so the general $2L$ cycle count applies.
- **Ordered rather than unordered pairs:** Every geometric relationship contributes in both directions. The factors of two and four in the formulas encode those orientations; dividing the result by two would answer a different question.
- **Last bucket:** Distance $N$ is impossible between distinct houses in an $N$-vertex connected graph, so the last result entry is always zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=n$ and $L=|x-y|+1$. Creating the baseline list and padding it costs $O(N)$. The cycle histogram has $O(L)$ entries. Each of the two tail passes creates and edits a list whose length is $O(N)$ in the worst case, and its loops are linear in the tail length or the corresponding histogram length. Adding each temporary histogram to `res` is also linear in its size. There are only two tails, so all work sums to $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
