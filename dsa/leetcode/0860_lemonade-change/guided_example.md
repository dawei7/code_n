# Guided Example: Lemonade Change

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bills": [5, 5, 5, 10, 20]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

The objective is to compute `true` from `{"bills": [5, 5, 5, 10, 20]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process customers in their fixed queue order

Change collected from a later customer cannot help an earlier transaction. The simulation must therefore process `bills` from left to right, maintaining only bills already received and not returned as change.

Only five- and ten-dollar bills are useful for future change:

- a five-dollar bill can help change a ten or twenty;
- a ten-dollar bill can help change a twenty;
- a twenty-dollar bill is larger than every required change and is never useful.

Variables `five` and `ten` track available counts. Twenty-dollar bills need not be stored.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bills": [5, 5, 5, 10, 20]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Customer pays five

A five-dollar payment requires no change. The stand keeps it:

`five += 1`.

These bills are especially valuable because every ten-dollar customer requires one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Customer pays ten

The customer needs five dollars change. The only possible bill is one five.

The source:

- increments `ten` because it receives the ten;
- decrements `five` for the change.

If no five was available, `five` becomes negative and the common failure check returns false.

The received ten cannot be used as change in the same transaction because the customer needs only five.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bills": [5, 5, 5, 10, 20]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Backtracking over change choices:** Only twenty-dollar payments offer two combinations, but the greedy exchange proof makes branching unnecessary.
- **Use three fives before a ten:** This can strand future ten-dollar customers and is never better.
- **First customer pays ten or twenty:** No five exists, the count becomes negative, and false is returned.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(bills)`. The loop visits each customer once and performs constant arithmetic and comparisons, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
