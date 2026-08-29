# Guided Example: Most Visited Sector in  a Circular Track

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "rounds": [1, 3, 1, 2]}`
- **Required output:** `[1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n` and an integer array `rounds`. We have a circular track which consists of `n` sectors labeled from `1` to `n`. A marathon will be held on this track, the marathon consists of `m` rounds. The $i^{\text{th}}$ round starts at sector $rounds[i - 1]$ and ends at sector $\text{rounds}[i]$. For example, round 1 starts at sector $\text{rounds}[0]$ and ends at sector $\text{rounds}[1]$

The objective is to compute `[1, 2]` from `{"n": 4, "rounds": [1, 3, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Collapse the whole marathon into its start and finish

Movement always follows increasing sector labels, wrapping from sector `n` back to sector one. The round boundaries do not change that direction; they merely identify checkpoints along one continuous traversal.

Imagine writing the entire visited sequence from `rounds[0]` to `rounds[-1]`. Every complete lap visits every sector exactly once. Complete laps therefore add the same count to all sectors and cannot affect which sectors are most visited.

After removing all complete laps, only the final partial traversal matters. It starts at the marathon's first sector and ends at its final sector, including both endpoints.

The exact source consequently reads only `rounds[0]` and `rounds[-1]`. Intermediate round endpoints determine how many full laps occurred, but those equal contributions do not change the winners.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "rounds": [1, 3, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the residual arc receives one extra visit

The starting sector is visited before any movement. As the runner proceeds, each crossed sector is visited in ascending circular order.

Whenever a full lap is completed, every sector gains one visit. At the end, sectors along the residual arc from the initial sector through the final sector have been encountered one additional time compared with sectors outside that arc.

Those residual-arc sectors are therefore exactly the most visited sectors.

This conclusion remains true when several rounds stop and restart conceptually at the same checkpoint: the marathon's path is continuous, so a round endpoint that is also the next round's start represents the same visit rather than an extra stationary visit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: the residual arc does not wrap

If `rounds[0] <= rounds[-1]`, the final partial traversal runs directly through:

`rounds[0], rounds[0] + 1, ..., rounds[-1]`.

The source returns `list(range(rounds[0], rounds[-1] + 1))`. Python's range excludes its upper endpoint, so adding one includes the final sector.

This list is already in ascending numeric order, exactly as required.

If start and finish are equal, this branch returns just that one sector. It has one extra visit after an integer number of complete laps.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "rounds": [1, 3, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Visit-count simulation:** Follow every round and count sectors. It is correct but does unnecessary work compared with the endpoint invariant.
- **Difference array on the circle:** It can count interval coverage efficiently for more general movement, but is excessive here.
- **Start below finish:** Return one contiguous inclusive numeric interval.
- **Start above finish:** Return the low-label interval followed by the high-label interval to preserve ascending output.
- **Start equals finish:** Exactly that sector has the residual extra visit.
- **Many complete laps:** They add equally to every sector and do not change the answer.
- **All sectors most visited:** This occurs when the residual arc covers the entire circle, as in a start of one and finish of `n`.
- **Two-sector track:** The same endpoint branches remain valid.
- **Round endpoints:** Intermediate values affect total laps but not which sectors receive the final extra visit.
- **Inclusive finish:** The upper range bound adds one so the ending sector is present.
- **Traversal order versus output order:** Wrapped traversal starts with high labels, but output must be numerically ascending.
- **Output space:** The returned list can contain all $N$ sectors even though auxiliary computation is constant.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K)$. Let $K$ be the number of returned sectors. Creating the output lists takes $O(K)$ time and $O(K)$ output space. Since $K \le N$, the manifest summarizes time as $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
