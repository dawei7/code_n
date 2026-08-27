# Guided Example: Check if a Parentheses String Can Be Valid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "))()))", "locked": "010100"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is valid if **any** of the following conditions is **true**:

The objective is to compute `true` from `{"s": "))()))", "locked": "010100"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reject odd length immediately

Every valid parentheses string contains one opening and one closing parenthesis per pair, so its length must be even. Editable positions cannot change the length.

The source checks `n & 1` and returns false for odd `n` before scanning. This handles the one-character example even when that character is unlocked.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "))()))", "locked": "010100"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Forward scan: every prefix needs enough possible openings

In the first pass, `x` counts parentheses that can currently act as unmatched openings:

- a locked `'('` definitely supplies an opening, so increment;
- an unlocked position can be chosen as `'('`, so also increment;
- a locked `')'` must consume one available opening.

If a locked closing parenthesis appears when `x == 0`, no earlier position can be assigned as an opening for it. A valid string can never have a prefix with more forced closings than possible openings, so the method returns false.

This pass deliberately treats every unlocked character as the most helpful choice for satisfying closing-prefix constraints. It is a feasibility count, not a final assignment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In the first pass, `x` counts parentheses that can currently... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Backward scan: every suffix needs enough possible closings

Passing the first scan is not sufficient. A string such as too many locked openings near the end may have no later positions available to close them.

The second pass moves right to left and uses the symmetric interpretation:

- a locked `')'` supplies a closing parenthesis, so increment `x`;
- an unlocked position can be chosen as `')'`, so increment;
- a locked `'('` must consume one available closing.

If no closing is available, that locked opening cannot be matched anywhere to its right, so return false.

Together, the scans enforce both directions of valid-parentheses structure.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "))()))", "locked": "010100"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit stack of positions:** Storing locked :** - **Explicit stack of positions:** Storing locked openings and unlocked positions can solve matching but uses $O(n)$ space. The two capacity scans are constant-space.
- **Low/high balance interval:** Track the minimum and maximum feasible unmatched-open counts in one forward pass. This is another $O(n)$, $O(1)$ formulation.
- **Only the forward scan:** It misses unmatched locked openings near the end. The backward symmetry is essential.
- **Odd length:** Impossible regardless of editability.
- **All positions unlocked:** Every even length is feasible.
- **All positions locked:** The scans reduce to ordinary valid-parentheses checks.
- **Locked close at the beginning:** Forward scan rejects it unless an earlier possible opening exists, which it cannot at index zero.
- **Locked open at the end:** Backward scan rejects it.
- **Unlocked original character:** Its current `s[i]` value is irrelevant because it may be changed either way.
- **Equality of counts:** Even length ensures the final assignment can contain equal numbers of opens and closes.
- **No constructed output:** The task asks only whether an assignment exists.
- **Input preservation:** Neither `s` nor `locked` is changed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
