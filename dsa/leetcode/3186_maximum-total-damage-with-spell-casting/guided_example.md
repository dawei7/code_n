# Guided Example: Maximum Total Damage With Spell Casting

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"power": [1, 1, 3, 4]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A magician has various spells.

The objective is to compute `6` from `{"power": [1, 1, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn individual spells into damage-value groups.** The restriction is based on a spell's damage value, not on its position in the input. If damage $v$ is selected, every spell of damage $v-2$, $v-1$, $v+1$, or $v+2$ becomes forbidden. Spells whose damage is also $v$ do not forbid one another. Because every damage value in this problem is positive, selecting one copy of $v$ while leaving another copy unused can never help: the extra copy adds $v$ damage and creates no new restriction. Therefore every optimal answer either selects all copies of a value or selects none of them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"power": [1, 1, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution records the multiplicity of every value in `cnt = Counter(power)`. A group with value $v$ and frequency $\texttt{cnt}[v]$ is consequently worth

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution records the multiplicity of every value i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

For example, four spells with damage $7$ form one decision worth $28$. Thinking in groups removes a misleading distinction between duplicate array elements.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"power": [1, 1, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative dynamic programming on unique values:** - **Iterative dynamic programming on unique values:** Build sorted pairs `(value, frequency)` and compute the best prefix value iteratively, using a pointer or binary search for the last compatible group. This expresses the same recurrence without duplicate `nxt` entries and avoids recursion-depth failure. It is the safer production formulation, but it is not the exact source implemented here.
- **Monotonic-pointer transition:** The editorial keeps the best compatible prior state while scanning unique values. Because the pointer only moves forward, the DP after sorting is linear in the number of unique values. The overall bound remains $O(n\log n)$ because sorting dominates.
- **Quadratic comparison with every earlier group:** A direct DP can test all earlier values for compatibility. It is easy to derive but costs $O(u^2)$ after grouping and is unnecessary when sorted order permits a pointer or binary search.
- **Greedy choice of the largest immediate group:** Choosing the greatest group weight first is not reliable. A moderately valuable group can block two compatible groups whose combined damage is larger, so the skip/take future must be compared by dynamic programming.
- **Duplicate values:** All duplicates are deliberately taken or skipped together. The skip index `i + cnt[power[i]]` is correct only because sorting makes every copy consecutive and reachable states begin at group boundaries.
- **Gap of exactly two:** Values differing by one or two conflict. `bisect_right(..., v + 2)` correctly skips both boundaries; using a search for `v + 2` with the wrong inclusive/exclusive rule would allow an illegal pair.
- **Gap of exactly three:** Such values are compatible. The first value greater than $v+2$ may be $v+3$, so the take branch must be allowed to continue there.
- **One damage group:** The take branch receives the full positive group value and jumps to `n`, while the skip branch returns zero, so all copies are selected.
- **Large numeric values:** The total can exceed a 32-bit signed integer. Python integers grow automatically, so multiplication and addition remain exact for the stated constraints.
- **Input mutation:** `power.sort()` changes the order of the caller's list. LeetCode permits this because only the returned integer matters, but code that needs the original order must sort a copy.
- **Recursion-depth limitation:** The mathematical algorithm supports $u$ up to $10^5$, but the exact recursive Python source can raise `RecursionError` on a valid input with many distinct values. Memoization prevents repeated work; it does not reduce the longest chain of nested calls. An iterative DP is required to remove this implementation defect robustly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $n$ be the number of spells and $u$ the number of distinct damage values, where $1 \le u \le n$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
