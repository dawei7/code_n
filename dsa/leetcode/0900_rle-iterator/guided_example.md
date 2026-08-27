# Guided Example: RLE Iterator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"encoding": [1, 4], "operations": [["next", 1]]}`
- **Required output:** `[4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We can use run-length encoding (i.e., **RLE**) to encode a sequence of integers. In a run-length encoded array of even length `encoding` (**0-indexed**), for all even `i`, $\text{encoding}[i]$ tells us the number of times that the non-negative integer value $encoding[i + 1]$ is repeated in the sequence.

The objective is to compute `[4]` from `{"encoding": [1, 4], "operations": [["next", 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

The iterator must consume a potentially enormous decoded sequence without expanding it. The encoded array already groups equal consecutive values into runs, so the state needs only a run position and an offset inside that run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"encoding": [1, 4], "operations": [["next", 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

- `i`: the index of the current run's count in `encoding`. Its value is always even.
- `j`: how many elements of the current run have already been consumed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - `i`: the index of the current run's count in `encoding`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

For current pair `encoding[i], encoding[i + 1]`, the number of remaining copies is

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"encoding": [1, 4], "operations": [["next", 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Expand the sequence:** Counts may be as large :** - **Expand the sequence:** Counts may be as large as $10^9$, making materialization impossible.
- **Subtract directly from encoded counts:** This can work in place but mutates caller data. The offset field preserves the input.
- **Prefix sums plus binary search:** Record cumulative run lengths and locate each cumulative consumed position. It gives $O(\log m)$ per call and uses $O(m)$ extra space, unnecessary for forward-only iteration.
- **Zero-count run:** It is skipped automatically without reducing the request.
- **Request exactly remaining run length:** Return that run's value, then skip it on the next call.
- **Request spanning several runs:** The loop subtracts each exhausted run until the final requested element is located.
- **Request exceeds all remaining elements:** Existing elements are still exhausted and `-1` is returned.
- **Repeated values in adjacent runs:** They may remain separate in the encoding; processing them separately gives the same decoded behavior.
- **Large counts and requests:** Only integer subtraction and comparison are used, so Python handles the range exactly.
- **Nonempty request:** `n >= 1` ensures zero runs always advance rather than return.
- **Even encoding length:** Every count at `i` has a corresponding value at `i + 1`.
- **No rewind:** The design is a forward iterator; exhausted state is permanent across calls.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+q)$. Let $m$ be the number of encoded count-value pairs and $q$ the number of calls to `next`. Each run is advanced past at most once over the object's lifetime. Each call also performs at least one constant amount of work.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
