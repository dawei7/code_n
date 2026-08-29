# Guided Example: Minimum Cost to Hire K Workers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2}`
- **Required output:** `105`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` workers. You are given two integer arrays `quality` and `wage` where $\text{quality}[i]$ is the quality of the $i^{\text{th}}$ worker and $\text{wage}[i]$ is the minimum wage expectation for the $i^{\text{th}}$ worker.

The objective is to compute `105` from `{"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid group uses one common pay-per-quality rate

Payment must be proportional to quality. Therefore, for a chosen group there is one rate `R` such that worker `i` is paid:

$$
R\cdot quality[i].
$$

To meet that worker's minimum wage:

$$
R\cdot quality[i]\ge wage[i],
$$

so:

$$
R\ge\frac{wage[i]}{quality[i]}.
$$

For a fixed group, the smallest legal common rate is the maximum wage-to-quality ratio among its members.

The group's minimum total cost is consequently:

$$
\left(\max_{i\text{ in group}}\frac{wage[i]}{quality[i]}\right)
\cdot\left(\sum_{i\text{ in group}}quality[i]\right).
$$

This formula separates the problem into choosing a maximum rate and minimizing total quality under that rate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort workers by required rate

The list `t` contains `(quality,wage)` pairs sorted by `w/q` increasingly.

When processing current worker `(q,w)`, all workers seen so far have required ratio no greater than current:

$$
R=\frac{w}{q}.
$$

Any `k`-worker group drawn from this prefix and including a worker with this maximum ratio can legally be paid at rate `R`.

For this fixed rate, minimizing total cost means choosing the `k` smallest qualities available, because `R` is positive and cost is `R\cdot\sum quality`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the smallest qualities with a max-heap

Python's heap is a min-heap, so the source pushes `-q`. The smallest negative value represents the largest positive quality.

`tot` stores the sum of qualities currently in the heap.

For each sorted worker:

1. add their quality to `tot`;
2. push `-q`;
3. when heap size reaches `k`, evaluate this group;
4. remove the largest quality to leave the best `k-1` qualities for future rates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `105` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `105` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every group:** There are $\binom{n}{k}$ possibilities, which is infeasible.
- **Choose workers with smallest wages:** Minimum wage alone ignores proportionality; required ratios and qualities jointly determine cost.
- **Choose smallest qualities globally:** A low-quality worker may require a very high pay rate that makes the group expensive.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the number of workers. Sorting by ratio takes `O(n\log n)` time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
