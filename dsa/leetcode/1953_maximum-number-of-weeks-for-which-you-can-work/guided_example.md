# Guided Example: Maximum Number of Weeks for Which You Can Work

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"milestones": [1, 2, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` projects numbered from `0` to $n - 1$. You are given an integer array `milestones` where each $\text{milestones}[i]$ denotes the number of milestones the $$i^{\text{th}}$$ project has.

The objective is to compute `6` from `{"milestones": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the largest project can create a scheduling bottleneck

Let `mx` be the largest milestone count and let `rest` be the total milestones in all other projects. Milestones belonging to different nonlargest projects can be arranged among one another as needed; the only possible impossible surplus comes from one project appearing too many times to separate its own milestones.

The code computes `s = sum(milestones)` and `rest = s - mx`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"milestones": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count separator slots

Arrange the `rest` other-project milestones in some valid order. They create `rest + 1` slots around them: before the first, between consecutive milestones, and after the last. Placing at most one largest-project milestone in each slot prevents two milestones from that project from becoming consecutive.

If

$$
mx\le rest+1,
$$

all largest-project milestones fit into these slots. With appropriate interleaving, every milestone can be completed, so the answer is the total `s`.

If

$$
mx>rest+1,
$$

some largest-project milestones cannot be separated. The best schedule alternates:

largest project, other project, largest project, other project, and so on.

All `rest` other milestones separate `rest+1` largest-project milestones, producing

$$
2\cdot rest+1
$$

working weeks. Any additional largest-project milestone would immediately follow another from the same project, so work must stop.

That is the exact conditional:

`rest * 2 + 1 if mx > rest + 1 else s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Arrange the `rest` other-project milestones in some valid or... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why projects among “rest” can supply the separators

It may seem necessary to examine the distribution inside `rest`. However, `mx` is the maximum individual count. No other project exceeds it, and the objective is only to avoid equal adjacent project IDs. In the balanced case, the standard rearrangement condition for a multiset—largest count at most all others plus one—is sufficient to arrange all milestones.

In the imbalanced case, the upper bound is already forced solely by the dominant project: each pair of its consecutive used milestones needs a distinct non-dominant separator. How the separators are divided among projects cannot create a lower upper bound, because they can be placed one per gap while the dominant milestones keep them separated from equal neighbors when necessary through ordering.


When `mx > rest + 1`, suppose $k$ largest-project milestones are used. They require at least $k-1$ milestones from other projects between them. Since only `rest` such milestones exist, $k\le rest+1$. Total used milestones are at most $(rest+1)+rest=2rest+1$. Alternation attains this upper bound, so it is optimal.

When `mx <= rest + 1`, the largest multiplicity satisfies the necessary and sufficient condition for rearranging all project labels without equal adjacent labels. Place the largest project in distinct separator slots and distribute the remaining labels so their own copies are also separated. Therefore all `s` milestones can be completed.

For `[5,2,1]`, `mx=5` and `rest=3`. Only four dominant milestones can be separated, so the answer is $2\cdot3+1=7$. For `[1,2,3]`, `mx=3` and `rest=3`; all six milestones fit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"milestones": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Max-heap simulation:** Repeatedly choose the t:** - **Max-heap simulation:** Repeatedly choose the two projects with most remaining milestones. It constructs a valid schedule but costs $O(S\log N)$ for total milestones $S$, which may be enormous.
- **Sort counts:** Sorting can expose the largest count but costs $O(N\log N)$ when a linear maximum suffices.
- **One project:** `rest=0`, so only one milestone can be worked before consecutive work would be required.
- **Perfect balance:** When `mx = rest`, all milestones alternate or interleave and the answer is `s`.
- **Boundary `mx = rest + 1`:** All milestones still fit, starting and ending with the largest project.
- **Strict imbalance:** Only `rest+1` dominant milestones can be used; remaining ones are unfinished.
- **Several projects tied for maximum:** null can dominate the sum of all others excessively, so the balanced branch handles them.
- **Two projects:** The counts can alternate completely when they differ by at most one; otherwise the answer is twice the smaller count plus one.
- **All counts one:** Every project can be used exactly once in any order, and the returned total is the number of projects.
- **Large counts:** The formula avoids iterating once per week and depends only on the number of projects.
- **No schedule output:** Only the maximum length is requested, so the constructive interleaving need not be materialized.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of projects.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
