# Guided Example: Find Special Substring of Length K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaabaaa", "k": 3}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `k`.

The objective is to compute `true` from `{"s": "aaabaaa", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

**The boundary conditions mean the substring must be a whole run.** A maximal run is a largest consecutive block containing one repeated character. By maximality, the character immediately before and after the run, when present, is different.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaabaaa", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Any substring satisfying the problem's neighbor conditions cannot be a strict interior portion of a longer equal-character run. If it started after the run's beginning, its preceding character would be equal; if it ended before the run's end, its following character would be equal. Therefore, a valid substring exists exactly when some maximal run has length $k$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Any substring satisfying the problem's neighbor conditions c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Locate one maximal run at a time.** `l` is the first index of the current run. `r` starts at `l` and advances while it stays inside the string and `s[r] == s[l]`. When the inner loop ends, the run is half-open interval `[l,r)` and has length `r - l`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaabaaa", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every length-\(k\) window:** This works :** - **Check every length-\(k\) window:** This works in $O(nk)$ naively or with extra state, but maximal-run scanning is simpler and linear.
- **Use global character counts:** A character may have several separated runs; global frequency does not determine local validity.
- **Run longer than \(k\):** It must be rejected because any length-$k$ slice has an equal neighbor.
- **Run shorter than \(k\):** It cannot contain a qualifying substring.
- **Run exactly \(k\):** Its maximal boundaries satisfy both neighbor rules automatically.
- **Whole string one run:** It is valid exactly when `len(s) == k`.
- **\(k=1\):** Any maximal run of one isolated character qualifies.
- **First run:** No preceding character is required.
- **Last run:** No following character is required.
- **Early return:** Only existence is requested, so scanning later runs after a match is unnecessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert s\rvert$. Although there are nested loops, `r` advances across each character once, and `l` jumps directly to the next unprocessed position. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
