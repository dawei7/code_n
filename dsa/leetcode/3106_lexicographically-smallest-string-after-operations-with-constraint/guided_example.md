# Guided Example: Lexicographically Smallest String After Operations With Constraint

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "zbbz", "k": 3}`
- **Required output:** `"aaaz"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `k`.

The objective is to compute `"aaaz"` from `{"s": "zbbz", "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

**Lexicographic order makes the leftmost position decisive.** Two equal-length strings are compared at their first differing character. A smaller character at position zero is better than any improvement at later positions; if position zero ties, position one becomes decisive, and so on. This priority justifies processing `s` from left to right and spending as much of the distance budget as needed to make the current character as small as possible.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "zbbz", "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source converts `s` to `cs = list(s)` because Python strings are immutable. It enumerates the original string, so each decision uses the untouched source character `c1` and writes the chosen result into `cs[i]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Cyclic distance between two letters.** Let the alphabet positions be 0 through 25. For a candidate `c2 < c1`, moving backward directly costs:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aaaz"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "zbbz", "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aaaz"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compute the target directly:** First test the cyclic distance to `a`. If affordable, choose `a`; otherwise direct backward movement by the remaining budget gives the smallest reachable lower letter. This can avoid the 26-character scan.
- **Dynamic programming over position and budget:** It is correct but unnecessary because lexicographic prefix priority makes the greedy choice decisive.
- **`k = 0`:** No strictly smaller character has distance zero, so the original string is returned.
- **Character `a`:** The inner loop stops immediately at equality, correctly leaving it unchanged.
- **Character `z`:** `a` is only one cyclic step away.
- **Unused budget:** Allowed because the distance constraint is `<= k`.
- **Original-character candidate:** It is represented by doing nothing; the loop does not need to assign it explicitly.
- **Larger replacement:** It can never help lexicographic minimality at the first changed position.
- **Wraparound route:** The second distance expression is essential for letters near `z`.
- **Direct route:** For ordinary lower letters far from the wrap boundary, subtraction may be cheaper.
- **First affordable candidate:** Since candidates are tested from `a` upward, affordability immediately proves lexicographic optimality for that position.
- **Budget subtraction:** Only an actual replacement consumes `d`; failed candidates cost nothing.
- **Input immutability:** The original string remains unchanged while `cs` stores the result.
- **Fixed alphabet:** The linear time claim treats 26 as a constant; a generalized alphabet of size $A$ would give $O(nA)$.
- **Prefix proof:** A smaller current character outweighs every possible suffix, which is why saving budget for later cannot beat the greedy choice.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For each of $n$ characters, the inner loop examines at most 26 lowercase letters. Every distance calculation is constant time. The total is $O(26n)=O(n)$ under the fixed English alphabet.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
