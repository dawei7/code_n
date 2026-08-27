# Guided Example: Shortest Matching Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abaacbaecebce", "p": "ba*c*ce"}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and a pattern string `p`, where `p` contains **exactly two** `'*'` characters.

The objective is to compute `8` from `{"s": "abaacbaecebce", "p": "ba*c*ce"}` while avoiding redundant calculations and unnecessary overhead.

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

**Split the pattern into three fixed pieces.** With exactly two stars,

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abaacbaecebce", "p": "ba*c*ce"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

A matching substring must contain an occurrence of $A$, followed without overlap by an occurrence of $B$, followed without overlap by an occurrence of $C$. The stars consume any intervening characters, including none. Any fixed piece may be empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A matching substring must contain an occurrence of $A$, foll... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

The source first finds every start position of each fixed piece in `s`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abaacbaecebce", "p": "ba*c*ce"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every substring:** There are $O(n^2)$ cand:** - **Try every substring:** There are $O(n^2)$ candidates before pattern checking.
- **Repeated `str.find` calls:** They can be concise but worst-case behavior and overlapping-occurrence management are less explicit than KMP.
- **Binary search occurrence lists:** It gives $O(n\log n)$ combination time; monotone pointers exploit ordered middle starts for linear time.
- **Empty fixed piece:** It occurs at all $n+1$ boundaries, not only character positions.
- **Overlapping fixed pieces:** They are not allowed to overlap in one match; end/start inequalities enforce sequence order.
- **Stars matching empty:** Equality at boundaries is accepted, allowing adjacent fixed pieces.
- **Overlapping occurrences within one list:** KMP prefix fallback records them all.
- **No last occurrence:** Breaking is safe because later middle endings only move right.
- **Pattern `"**"`:** The empty substring is found with length zero.
- **No match:** The untouched sentinel maps to `-1`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n=\lvert s\rvert$ and $m=\lvert p\rvert$. Building KMP data and scanning for all three pieces costs $O(n+m)$ total; three source scans are a constant factor. Occurrence lists can each contain $O(n)$ starts.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
