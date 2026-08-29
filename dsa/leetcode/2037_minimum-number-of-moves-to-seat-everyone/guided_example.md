# Guided Example: Minimum Number of Moves to Seat Everyone

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"seats": [3, 1, 5], "students": [2, 7, 4]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` **availabe **seats and `n` students **standing** in a room. You are given an array `seats` of length `n`, where $\text{seats}[i]$ is the position of the $i^{\text{th}}$ seat. You are also given the array `students` of length `n`, where $\text{students}[j]$ is the position of the $j^{\text{th}}$ student.

The objective is to compute `4` from `{"seats": [3, 1, 5], "students": [2, 7, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The movement cost is absolute distance

Moving a student from position `b` to seat position `a` requires one operation per unit of distance. The exact cost of that assignment is therefore `abs(a - b)`.

The task is to choose a one-to-one matching between all students and all seats that minimizes the sum of these distances. Seats at the same numerical position are still separate available seats, and students at the same position are still separate people.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"seats": [3, 1, 5], "students": [2, 7, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort both sides and match by rank

The source sorts `seats` and `students` in ascending order. It then pairs the smallest student position with the smallest seat position, the second smallest with the second smallest, and so forth.

The final generator

`abs(a - b) for a, b in zip(seats, students)`

computes the movement cost of every rank-matched pair, and `sum` returns their total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why crossed assignments can be uncrossed

Consider two student positions `p <= q` and two seat positions `a <= b`. A crossed matching sends `p` to `b` and `q` to `a`. The ordered matching sends `p` to `a` and `q` to `b`.

On a line, the ordered cost satisfies

$$
\lvert p-a\rvert+\lvert q-b\rvert
\le
\lvert p-b\rvert+\lvert q-a\rvert.
$$

Intuitively, crossed travel contains overlapping distance traveled in opposite directions. Swapping the two destinations removes that crossing without increasing total movement.

This inequality holds regardless of the relative placement of the four coordinates. If both seats lie to one side, the totals may tie; if their intervals interleave, uncrossing strictly removes duplicated travel.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"seats": [3, 1, 5], "students": [2, 7, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Counting by coordinate:** Positions are bounded by one hundred, so frequency differences can compute the cost in $O(N+U)$ time with $U=100$.
- **Minimum-cost bipartite matching:** General but far more expensive; one-dimensional absolute distance has the uncrossing property.
- **Nearest free seat per student:** Can be suboptimal because early choices may force later crossings.
- **Already matched sorted positions:** Every absolute difference is zero.
- **Duplicate seats:** Equal coordinates still represent distinct seat entries and remain separately paired.
- **Duplicate students:** Each occurrence is assigned to one distinct seat.
- **One student and one seat:** The answer is their absolute distance.
- **Students entirely left of seats:** Ordered matching remains optimal and sums all rightward distances.
- **Students entirely right of seats:** The same proof handles all leftward moves.
- **Tied optimal assignments:** The method returns the minimum cost without needing to reconstruct a unique assignment.
- **Equal input lengths:** This guarantee makes `zip` cover all entries.
- **Input mutation:** Both arrays are sorted in place.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the common number of seats and students. Sorting each list takes $O(N\log N)$ time. Pairing and summing takes $O(N)$, so total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
