# Guided Example: Minimum Amount of Time to Collect Garbage

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"garbage": ["G", "P", "GP", "GG"], "travel": [2, 4, 3]}`
- **Required output:** `21`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of strings `garbage` where $\text{garbage}[i]$ represents the assortment of garbage at the $i^{\text{th}}$ house. $\text{garbage}[i]$ consists only of the characters `'M'`, `'P'` and `'G'` representing one unit of metal, paper and glass garbage respectively. Picking up **one** unit of any type of garbage takes `1` minute.

The objective is to compute `21` from `{"garbage": ["G", "P", "GP", "GG"], "travel": [2, 4, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate unavoidable pickup time from necessary travel

Every character across all `garbage` strings represents one garbage unit, and picking up each unit takes one minute. All units must be collected, so total pickup time is fixed:

$$
S=\sum_i\lvert\texttt{garbage}[i]\rvert.
$$

The only travel decision is how far each of the three type-specific trucks must go. A truck responsible for type `c` must reach the last house containing `c` and never benefits from traveling farther.

Because only one truck can operate at a time, truck times cannot overlap. The minimum total elapsed time is therefore the sum of all pickup minutes plus the necessary travel minutes of each used truck.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"garbage": ["G", "P", "GP", "GG"], "travel": [2, 4, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count pickups and record last occurrences together

The first loop adds `len(s)` for each house string to `ans`. This counts every metal, paper, and glass unit exactly once regardless of type.

For every character `c` at house `i`, it assigns:



Later occurrences overwrite earlier ones. After the scan, `last['M']`, `last['P']`, or `last['G']` exists exactly when that type occurs and stores its farthest required house.

The dictionary contains at most three entries. Repeated units of the same type at one house update the same value harmlessly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute prefix travel time to each house

`travel[t]` is the time from house `t` to `t+1`. The second loop enumerates it starting with house index one:



After adding `t`, `ts` is the travel time from house zero through consecutive roads to house `i`. A truck whose last required house is `i` must incur exactly this prefix cost.

The query:



adds `ts` once for each garbage type whose final house is `i`. At most three values are checked. If two trucks both end at that house, both must traverse the same roads at different times because trucks cannot operate simultaneously, so adding the prefix twice is correct.

A type found only at house zero has last index zero. The travel loop begins at house one, so it adds no travel for that truck.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `21` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"garbage": ["G", "P", "GP", "GG"], "travel": [2, 4, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `21` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix travel array:** Precompute travel time to every house, then add the entries at the three last positions. It is clear but uses $O(n)$ extra space.
- **Separate scan per garbage type:** Find each last occurrence and count pickups independently. With only three types it remains linear but repeats work.
- **Simulate truck movements house by house:** Correct if stopped at each final occurrence, but explicit scheduling is unnecessary because times simply add.
- **Type absent entirely:** It has no `last` entry, so neither pickup nor travel time is added for its truck.
- **Type only at house zero:** Its last index is zero and requires no road travel.
- **Several types end at the same house:** The prefix time is added once per truck because their work cannot overlap.
- **Many units at one house:** Each character contributes one pickup minute, while travel to the house is paid once for that truck.
- **No return trip:** Trucks stop after their last collection, so prefix travel is not doubled.
- **Houses beyond a truck's last type occurrence:** That truck never visits them.
- **Serialized operation rule:** It justifies adding all truck pickup and travel durations rather than taking a maximum across trucks.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+S)$. Let $n$ be the number of houses and $S$ the total number of garbage characters. The first loop examines each house and each unit, taking $O(n+S)$ time. The travel loop has $n-1$ iterations and checks at most three dictionary values each, so it takes $O(n)$ time. Total time is $O(n+S)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
