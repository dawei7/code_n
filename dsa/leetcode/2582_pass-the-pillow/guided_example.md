# Guided Example: Pass the Pillow

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "time": 5}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` people standing in a line labeled from `1` to `n`. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

The objective is to compute `2` from `{"n": 4, "time": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent position and direction explicitly

The exact solution simulates one pass per second with two scalars:

- `ans` is the current person's one-based label;
- `k` is the direction, $+1$ toward person $n$ and $-1$ toward person $1$.

Both start at one: person one initially holds the pillow, and the first pass goes toward person two.

For each elapsed second, `ans += k` moves exactly one position. If the new position is either endpoint, `k *= -1` reverses the direction for the next second.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "time": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why reversal occurs after moving

At an endpoint, the holder has just received the pillow. The pass that reached the endpoint used the old direction. Only the subsequent pass must go back inward.

For example, with $n=4$, positions evolve as:

$$
1\to2\to3\to4\to3\to2.
$$

When the update reaches $4$, direction changes from $+1$ to $-1$. The position remains $4$ at that instant; the next loop iteration moves it to $3$.

Reversing before movement whenever currently at an endpoint could also be made correct with a different loop structure, but mixing the conventions would cause an off-by-one pass.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At an endpoint, the holder has just received the pillow.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A loop invariant

After exactly $t$ loop iterations, `ans` is the person holding the pillow after $t$ seconds, and `k` is the direction of the next legal pass.

The invariant holds before the loop at time zero: person one holds the pillow and the next direction is right. One iteration adds the direction, reaching the adjacent legal person after one second. If that person is an endpoint, the direction reverses; otherwise it remains. In either case, `k` is correct for the following pass.

By induction, the state after `time` iterations is the required answer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "time": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Endpoint traversal formula:** Divide time by $:** - **Endpoint traversal formula:** Divide time by $n-1$, use traversal parity for direction, and compute the remaining offset in $O(1)$ time.
- **Full-period modulo:** Reduce time modulo $2(n-1)$ and reflect positions in the second half of the period.
- **Queue simulation:** Storing people or pillow passes is unnecessary; position and direction are sufficient state.
- **Exactly at person `n`:** Direction flips after arrival, but the returned holder remains $n$ if time ends there.
- **Exactly back at person one:** Direction flips to positive for a possible next second.
- **Two people:** The pillow alternates every second, and the same loop works without special cases.
- **One complete traversal:** At `time = n - 1`, person $n$ holds the pillow.
- **One complete period:** At `time = 2(n - 1)`, the pillow is back at person one.
- **Manifest distinction:** The source is a linear simulation; the mathematical $O(1)$ method is an alternative.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop runs exactly `time` iterations, each with constant work. The exact implementation takes $O(\texttt{time})$ time and $O(1)$ auxiliary space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
