# Guided Example: Number of Students Unable to Eat Lunch

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"students": [1, 1, 0, 0], "sandwiches": [0, 1, 0, 1]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The objective is to compute `0` from `{"students": [1, 1, 0, 0], "sandwiches": [0, 1, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace queue rotations with preference counts

The literal process appears to require a queue: if the front student dislikes the current sandwich, move that student to the back and try again. However, the question only asks how many students remain, not their final order. Before the process becomes stuck, queue rotations do not change how many students prefer each type.

For a fixed top sandwich of type `v`, there are only two possibilities:

- At least one remaining student prefers `v`. Repeatedly rotating the queue will eventually bring such a student to the front. That student takes the sandwich, so one `v`-preferring student and that sandwich leave.
- No remaining student prefers `v`. Every student can rotate past the front, but no one will take the sandwich. Since the sandwich stack cannot skip its top item, the process stops permanently and every remaining student is unable to eat.

This observation makes the students' exact queue positions irrelevant. The source records only the counts of preferences with `cnt = Counter(students)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"students": [1, 1, 0, 0], "sandwiches": [0, 1, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the sandwich array can be scanned from left to right

The description says index zero is the top of the sandwich stack. Sandwiches can only be removed from that top, so their serving order is exactly `sandwiches[0]`, then `sandwiches[1]`, and so on. A normal left-to-right loop therefore represents popping the stack in the required order; no Python stack object is needed.

For each sandwich value `v`, `cnt[v]` is the number of still-waiting students who want that type. Python's `Counter` returns zero for a missing key, which makes the same check work even if the original student list contained only one preference.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The description says index zero is the top of the sandwich s... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Serve when the required preference still exists

If `cnt[v] > 0`, some remaining student wants the current sandwich. That student may not presently be at the queue's front, but all students ahead can rotate to the back. Because the queue is finite, the matching student eventually reaches the front without changing the sandwich.

The statement `cnt[v] -= 1` represents that eventual service. It removes exactly one student of the matching type. There is no need to count how many rotations occurred because rotations are not included in the requested answer and do not affect future preference counts.

This abstraction preserves everything that matters: which sandwich is next, and how many students of each type remain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"students": [1, 1, 0, 0], "sandwiches": [0, 1, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Literal deque simulation:** Rotate mismatching:** - **Literal deque simulation:** Rotate mismatching students and track how many consecutive failures have occurred. It mirrors the story but can perform $O(n^2)$ rotations in a direct implementation.
- **Two scalar counters:** Because there are only two types, count zeros and derive or separately count ones. This achieves the same $O(n)$ time and $O(1)$ space without `Counter`.
- **Sorting preferences:** It loses the useful simplicity of direct counting and does not remove the need to respect sandwich order.
- **One student:** Equal array lengths do not guarantee matching types. If the only preference differs from the top sandwich, the check immediately returns one; if they match, the loop ends and returns zero.
- **All students share one preference:** The first opposite-type top sandwich immediately blocks everyone who remains.
- **All sandwiches are served:** Each iteration decrements an available preference, and the final return is zero.
- **Block occurs late:** Counts already decremented represent students who ate; only the unserved opposite count is returned.
- **Duplicate preferences:** They are intentionally aggregated because students with the same preference are interchangeable for deciding whether the top sandwich can be taken.
- **Top-of-stack convention:** The scan is correct specifically because index zero is defined as the top; reversing `sandwiches` would model a different process.
- **Binary-type assumption:** The expression `v ^ 1` is valid only because every type is exactly zero or one.
- **Counter missing key:** It evaluates to zero, so an absent preference type triggers the stopping rule without a key error.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of students; the sandwich array has the same length. Building the `Counter` scans all students in $O(n)$ time. The loop examines at most all $n$ sandwiches, doing constant work for each, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
