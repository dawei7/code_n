# Guided Example: Number of Equivalent Domino Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of `dominoes`, $\text{dominoes}[i] = [a, b]$ is **equivalent to** $\text{dominoes}[j] = [c, d]$ if and only if either ($a = c$ and $b = d$), or ($a = d$ and $b = c$) - that is, one domino can be rotated to be equal to another domino.

The objective is to compute `1` from `{"dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rotation means endpoint order should not matter

Domino `[a,b]` is equivalent to both `[a,b]` and `[b,a]`. To count efficiently, every equivalent orientation needs one canonical identity.

The solution places the smaller endpoint first and the larger endpoint second. It encodes that ordered canonical pair as a two-digit integer.

If `a < b`, key `a * 10 + b` already has the smaller value first. Otherwise, key `b * 10 + a` reverses the endpoints. Equal endpoints follow the second branch but produce the same value either way.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why decimal encoding is collision-free

Every endpoint lies from one through nine. In key `10 * small + large`, integer division by ten recovers the smaller digit and remainder modulo ten recovers the larger digit.

Therefore, different canonical endpoint pairs cannot share a key. The bound of one decimal digit per endpoint is essential; for arbitrary larger values, a tuple would be safer.

Examples `[1,2]` and `[2,1]` both map to twelve. Domino `[1,3]` maps to thirteen and cannot collide. Double `[2,2]` maps to twenty-two.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every endpoint lies from one through nine.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count earlier equivalent dominoes online

`cnt[key]` is the number of previously processed dominoes with this canonical identity.

When the current domino arrives, every earlier domino in that count forms exactly one valid pair with it. Adding `cnt[key]` to `ans` counts all pairs whose later index is the current position.

Only after counting does the code increment `cnt[key]`. This prevents pairing the domino with itself and prepares it as an earlier partner for future positions.

For three copies of `[1,2]` in mixed orientations, the first sees count zero, the second sees one, and the third sees two. Their total contribution is three pairs: first with second, first with third, and second with third. The counter never needs to remember the actual indices because only how many earlier partners exist affects the new contribution.

At the beginning of each loop iteration, `ans` equals the number of equivalent pairs entirely inside the processed prefix, and `cnt` stores exact canonical frequencies for that prefix. The add-then-increment steps extend both facts to include the current index, which is a direct loop invariant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Tuple key:** Use `(min(a,b), max(a,b))`. It ge:** - **Tuple key:** Use `(min(a,b), max(a,b))`. It generalizes beyond one-digit endpoints and makes canonicalization visually explicit.
- **Sort each domino:** Sorting a two-element list creates the same identity but adds avoidable allocation or mutation.
- **Compare every pair:** Directly test equivalence in $O(n^2)$ time.
- **Count frequencies then combine:** Build all canonical counts, then sum `q * (q - 1) // 2`. It is equally correct but needs a second pass over keys.
- **One domino:** No earlier partner exists, so the answer is zero.
- **All equivalent:** Contributions grow from zero through $n-1$, yielding every index pair.
- **No equivalent keys:** Every lookup is zero and the answer remains zero.
- **Repeated double:** Dominoes such as `[3,3]` canonicalize normally and pair with each other.
- **Rotation:** `[1,9]` and `[9,1]` share key nineteen.
- **Different unordered pairs:** The decimal encoding cannot collide under digits one through nine.
- **Self-pair prevention:** Incrementing after adding ensures an index never pairs with itself.
- **Index order:** Each unordered pair is counted once at its later index, satisfying `i < j`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of dominoes. The loop performs constant arithmetic and expected constant-time Counter operations per domino, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
