# Guided Example: Find Time Required to Eliminate Bacterial Strains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"timeReq": [10, 4, 5], "splitTime": 2}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `timeReq` and an integer `splitTime`.

The objective is to compute `12` from `{"timeReq": [10, 4, 5], "splitTime": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Model the strategy as a binary split tree.** Each bacterial strain is assigned to one final WBC, so it is a leaf. Every time a WBC splits, it creates the two child branches of an internal node and costs `splitTime` before either child can continue.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"timeReq": [10, 4, 5], "splitTime": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If two child subplans need times $a$ and $b$ after their WBCs become available, creating both from one parent requires

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

because the children execute in parallel after the split. The slower child determines completion.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"timeReq": [10, 4, 5], "splitTime": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Split until one WBC per strain immediately:** A balanced tree ignores different elimination times and can make a long strain unnecessarily deep.
- **Assign largest requirements deepest:** Extra split delays on large leaves can only worsen the maximum.
- **Merge two largest first:** This creates a parent even larger than necessary and contradicts the deepest-smallest exchange.
- **Sum child requirements:** Children operate in parallel, so their parent uses a maximum.
- **Add split time to both children separately:** One split event delays both branches by the same single interval.
- **Two strains:** One merge returns `max(a,b)+splitTime`.
- **Equal strain times:** Many split trees may tie; the heap chooses one optimal merge order.
- **Very large split time:** The greedy tree tends to keep larger requirements shallow, limiting added split depth.
- **One subtree value in the heap:** It is treated exactly like a raw leaf requirement during later merges.
- **Input order:** Strains may be eliminated in any order, so heap reordering is legal.
- **Input mutation:** The source consumes `timeReq` as its heap; copy it first if preservation is required.
- **Positive durations:** Every split and elimination adds real delay, supporting the depth exchange argument.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Heap construction costs $O(n)$. There are $n-1$ merges, each with two pops and one push, each $O(\log n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
