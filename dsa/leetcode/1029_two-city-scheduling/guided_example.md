# Guided Example: Two City Scheduling

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"costs": [[10, 20], [30, 200], [400, 50], [30, 20]]}`
- **Required output:** `110`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A company is planning to interview `2n` people. Given the array `costs` where $\text{costs}[i] = [\text{aCost}_{i}, \text{bCost}_{i}]$, the cost of flying the $$i^{\text{th}}$$ person to city `a` is $\text{aCost}_{i}$, and the cost of flying the $$i^{\text{th}}$$ person to city `b` is $\text{bCost}_{i}$.

The objective is to compute `110` from `{"costs": [[10, 20], [30, 200], [400, 50], [30, 20]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare the extra cost of choosing city A

Every person must go to exactly one city, and exactly half must go to each. Looking only at the cheaper ticket for each person can violate that quota. The useful quantity is not either ticket price alone, but the relative change caused by assigning that person to city A instead of city B.

For costs `[a, b]`, define

$$
\Delta = a-b.
$$

If `\Delta` is negative, city A is cheaper by `-\Delta`. If it is positive, city A is more expensive by `\Delta`. A smaller difference means that choosing A is more favorable relative to choosing B.

The code sorts `costs` by `x[0] - x[1]` in ascending order. It then sends the first half to A and the second half to B.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"costs": [[10, 20], [30, 200], [400, 50], [30, 20]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive the rule from a baseline

Imagine initially sending everyone to city B. The baseline total is

$$
\sum_i b_i.
$$

Moving person `i` from B to A changes that total by `a_i - b_i = \Delta_i`. The quota requires moving exactly `n` of the `2n` people to A. Therefore, the final total is

$$
\sum_i b_i + \sum_{i\ \text{chosen for A}} \Delta_i.
$$

The baseline is fixed regardless of the assignment. Minimizing total cost is therefore exactly the same as choosing `n` differences with the smallest possible sum. Those are the first `n` entries after sorting differences ascending.

This derivation explains why sorting by `a` alone, `b` alone, or the cheaper absolute ticket is not sufficient. The quota decision depends on the cost of switching between cities for the same person.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Imagine initially sending everyone to city B.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: An exchange proof

Suppose an assignment sends person `p` to A and person `q` to B, but `\Delta_p > \Delta_q`. Swap their destinations. The number assigned to each city remains unchanged.

The original contribution is `a_p + b_q`. The swapped contribution is `b_p + a_q`. Subtracting gives

$$
(a_p+b_q)-(b_p+a_q)=\Delta_p-\Delta_q>0.
$$

So the swap makes the schedule cheaper. Consequently, an optimal assignment cannot place a larger difference in A while a smaller difference remains in B. All A-assigned differences must be no larger than all B-assigned differences, which is exactly the sorted first-half rule.

Tied differences can appear on either side without changing the total. Python's stable tie order is irrelevant to correctness.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `110` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"costs": [[10, 20], [30, 200], [400, 50], [30, 20]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `110` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Start with everyone in A:** Use B-minus-A diff:** - **Start with everyone in A:** Use B-minus-A differences and switch exactly half to B. This is algebraically symmetric and produces the same assignments.
- **Dynamic programming by person and A quota:** A state can track minimum cost after assigning a certain number to A. It is correct but uses `O(P^2)` time in the straightforward form, while the difference structure gives a greedy solution.
- **Heap selection:** Keep the `n` smallest differences in a heap. This can avoid fully ordering the data but is more complex and has similar `O(P \log n)` time.
- **Quickselect:** Partition around the `n`-th difference for expected `O(P)` time, then sum the two groups. Worst-case guarantees and tie handling are more involved than sorting for at most 100 people.
- **Choose each person's cheaper city:** This can send the wrong number of people to each city and does not satisfy the central constraint.
- **Sort by A cost only:** A low A cost may still be a poor A assignment if that person's B cost is much lower. Relative difference is the correct opportunity cost.
- **Equal differences:** Swapping tied people between cities leaves total cost unchanged, so any tie order is valid.
- **All differences negative:** A is cheaper for everyone, but only half may go there. The algorithm gives A to the half with the largest relative savings.
- **All differences positive:** B is cheaper for everyone, yet the quota forces half to A. The smallest penalties are selected.
- **Exactly two people:** The smaller difference goes to A and the other person goes to B, which directly minimizes the two possible valid schedules.
- **Even-length guarantee:** `len(costs) >> 1` is exact only because the number of people is guaranteed even.
- **Input mutation:** `costs.sort(...)` changes row order. If the original order is needed afterward, sort a copy instead at the cost of additional explicit space.
- **Large individual prices:** Only subtraction and addition are used, and the stated price bounds keep totals comfortably within ordinary integer ranges.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P \log P)$. Let `P = len(costs)` be the total number of people. Computing comparison keys and sorting takes `O(P \log P)` time. The final generator visits `P / 2` paired positions and performs `O(P)` work. Sorting dominates, so total time is `O(P \log P)`, which is the manifest's `O(N \log N)` bound with `N` denoting input size.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
