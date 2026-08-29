# Guided Example: Find Champion I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1], [0, 0]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` teams numbered from `0` to $n - 1$ in a tournament.

The objective is to compute `0` from `{"grid": [[0, 1], [0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why an all-one off-diagonal row identifies the champion

If candidate $i$ has a one against every $j\ne i$, then $i$ is stronger than every other team. In particular, none of those teams is stronger than $i$, because the input guarantees opposite comparison results for each pair. Hence $i$ is a champion.

Conversely, suppose $i$ is the champion. For every other team $j$, exactly one of $i$ or $j$ is stronger. Since no $j$ may be stronger than the champion, $i$ must be stronger than $j$, so `grid[i][j]` is one. The champion's row therefore passes the test.

This proves the predicate is necessary and sufficient.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1], [0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why returning the first match is safe

Two different rows cannot both contain ones against every opponent. If teams $a$ and $b$ both passed, the first row would require `grid[a][b] == 1`, while the second would require `grid[b][a] == 1`. The contract says these two entries differ, making that impossible.

The transitive-order guarantee also ensures a strongest team exists. Therefore the loop will encounter exactly one passing row for legal input. Although Python would implicitly return `null` if no row passed, that path is unreachable under the reference contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How `all` evaluates

`all` starts conceptually true and consumes generated comparisons until one is false. A candidate may therefore be rejected early after its first loss. In the worst case, however, many rows can have their zero near the end, and the champion's entire row must be checked.

The source does not use the candidate-elimination algorithm described by the Optimal manifest summary. It directly verifies rows in the matrix.

For `[[0,0,1],[1,0,1],[0,0,0]]`:

- row $0$ fails because it loses to team $1$;
- row $1$ has ones against teams $0$ and $2$, so it passes and returns $1$;
- later rows need not be examined.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1], [0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Candidate elimination:** Compare a current candidate with each next team and replace the loser, then optionally verify. Under the strong tournament guarantees this can run in $O(n)$ time and $O(1)$ space.
- **Column indegree count:** Count losses for every team from the matrix in $O(n^2)$ time and $O(n)$ space; the champion has zero losses.
- **Do not include the diagonal:** `grid[i][i]` is zero by definition. Testing it would reject every candidate.
- **Two apparent champions:** Impossible because their mutual pair cannot point in both directions.
- **Cycle without transitivity:** Every team might lose to someone, and the source would fall through with `null`. Legal inputs exclude this.
- **Early short-circuit:** `all` stops at the first zero, improving common-case constants but not worst-case asymptotics.
- **Single champion guarantee:** It follows from the complete transitive tournament even though the method has no explicit `-1` branch.
- **Manifest mismatch:** The summary's elimination language and $O(n)$ time do not describe this source. Faithful analysis is $O(n^2)$ for row verification.
- **Why a loss is decisive:** Once row $i$ contains zero against some different team $j$, the pairwise guarantee means $j$ is stronger than $i$. No comparisons with other teams can restore $i$ as champion.
- **Row order:** Returning the first passing row does not prefer a smaller label over another valid champion; uniqueness proves no second passing row exists.
- **Matrix storage:** The input already occupies $O(n^2)$ space, but the method allocates no additional structure proportional to it.
- **Worst-case short-circuit example:** If each rejected row's first zero appears near its last checked column, almost every off-diagonal entry is inspected before the champion is found.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n$ rows and up to $n-1$ off-diagonal entries checked per row. Worst-case running time is $O(n^2)$, not the $O(n)$ stated in the manifest. Short-circuiting `all` may reduce work on particular inputs but does not improve the worst-case bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
