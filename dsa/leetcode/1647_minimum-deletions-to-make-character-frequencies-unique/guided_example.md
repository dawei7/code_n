# Guided Example: Minimum Deletions to Make Character Frequencies Unique

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aab"}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A string `s` is called **good** if there are no two different characters in `s` that have the same **frequency**.

The objective is to compute `0` from `{"s": "aab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the problem to assigning distinct frequencies

`Counter(s)` obtains one positive frequency for every character present. Deleting characters can only decrease a frequency; it cannot increase one. The goal is to keep as many characters as possible while making the remaining positive frequencies distinct. A zero frequency means deleting that character completely and is ignored by the goodness rule.

The source sorts the positive frequencies in descending order. Processing large counts first is useful because a smaller count can never be increased to get out of a larger count's way. The best response is to keep each frequency as large as possible below the previous assigned one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Interpret `pre` as the strict upper boundary

`pre` records the final frequency assigned to the previously processed character. The current final frequency must be strictly less than `pre`.

Initially `pre = inf`, so the largest frequency can remain unchanged.

For each original frequency `v`, three cases apply.

If `pre == 0`, no positive frequency smaller than the previous assignment exists. The current character must be deleted completely, so all `v` occurrences are added to `ans`.

If `v >= pre`, keeping `v` would duplicate or exceed the previous assigned frequency. The largest legal choice is `pre - 1`. The deletions are

$$
v-(pre-1)=v-pre+1.
$$

The source adds that amount and decrements `pre`.

If `v < pre`, the frequency is already strictly smaller, so no deletion is needed and `pre` becomes `v`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pre` records the final frequency assigned to the previously... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why zero is treated specially

Once `pre` reaches zero, later positive counts cannot receive a distinct non-negative frequency below it. All must become zero. Multiple characters may have frequency zero because absent characters do not count when deciding whether the string is good.

The dedicated first branch prevents setting `pre` negative and counts complete deletion directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Used-frequency set:** For each count, decremen:** - **Used-frequency set:** For each count, decrement until it reaches an unused positive value or zero. It is simple and still effectively linear with 26 letters, but may perform more individual decrement steps.
- **Max-heap:** Repeatedly reduce duplicate largest counts. It works but adds heap operations for a constant-sized alphabet.
- **All frequencies already distinct:** Every `v < pre` after the first, so the answer remains zero.
- **Several equal frequencies:** The sorted greedy assigns consecutive smaller values while possible.
- **Frequency reaches zero:** That character disappears and zero may be reused by any later character.
- **Single distinct character:** Its frequency is retained unchanged.
- **Lowercase-only constraint:** It is what makes Counter storage and sorting constant space relative to $n$.
- **Do not require zero frequencies to be unique:** Only characters remaining in the string participate in the rule.
- **Infinite initial boundary:** It lets the largest original frequency stay unchanged without a special first-iteration branch.
- **Frequency one collision:** One character may keep frequency 1; any later colliding character must fall to zero and disappear.
- **Deletion count formula:** In the collision branch, `v - pre + 1` is exactly `v - (pre - 1)`, the cost of lowering to the greatest permitted frequency.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length and $K$ the number of distinct lowercase letters. Counting takes $O(n)$ time. Sorting takes $O(K\log K)$, and the loop takes $O(K)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
