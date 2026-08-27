# Guided Example: Minimum Number of Chairs in a Waiting Room

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "EEEEEEE"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. Simulate events at each second `i`:

The objective is to compute `7` from `{"s": "EEEEEEE"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track purchased chairs and currently free chairs

The exact source uses two counters:

- `cnt` is the total number of chairs that have ever been needed and therefore must be available initially;
- `left` is the number of those chairs currently free.

The room starts empty with no purchased capacity, so both are zero.

When a person enters:

- if `left > 0`, one free chair is reused and `left` decreases;
- otherwise, every existing chair is occupied, so one additional chair is necessary and `cnt` increases.

When a person leaves, their chair becomes free, so `left` increases.

`cnt` never decreases. It records the maximum capacity required over the whole event sequence, which is the minimum number that must have been supplied from the beginning.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "EEEEEEE"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Connection to maximum occupancy

At every prefix,

$$
\text{current occupants}=\texttt{cnt}-\texttt{left}.
$$

Whenever occupancy rises without exceeding earlier maximum, a free chair is consumed. Whenever it would exceed all prior occupancy, no free chair exists and `cnt` grows by one. Therefore, final `cnt` equals maximum simultaneous occupancy.

The manifest describes explicitly simulating occupancy and recording its maximum. The exact code implements the equivalent resource-reuse viewpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At every prefix,

$$
\text{current occupants}=\texttt{cnt}-\... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Example

For `"ELELEEL"`:

- first E finds no free chair, so `cnt=1`;
- L makes `left=1`;
- next E consumes it;
- alternating events repeat;
- the second consecutive E eventually finds no free chair and raises `cnt` to 2.

No later prefix needs more, so two chairs suffice.

For seven E events, no chair is ever freed. Every entry increments `cnt` and the result is 7.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "EEEEEEE"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Occupancy plus maximum:** Add one on E, subtra:** - **Occupancy plus maximum:** Add one on E, subtract one on L, and update a peak variable. It matches the manifest and is algebraically equivalent.
- **Stack of chairs:** Explicitly store free chair identifiers, but identities never matter and would use unnecessary space.
- **Count E minus L prefixes:** Maximum prefix balance directly gives the answer.
- **All entries:** Every event needs a new chair, so result is string length.
- **Perfect alternation starting with E:** One chair is repeatedly reused.
- **Consecutive entries:** Each beyond currently free capacity raises `cnt`.
- **Consecutive valid leaves:** They accumulate several reusable chairs.
- **Room empty at end:** Final occupancy may be zero while `cnt` retains peak capacity.
- **Valid-sequence guarantee:** It prevents `left` from representing nonexistent chairs.
- **Single event E:** One chair is necessary.
- **Only E/L alphabet:** It makes the source's `else` branch safe.
- **No early return:** A later burst of entries may exceed every earlier capacity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the event-string length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
