# Guided Example: Minimum Distance Between Three Equal Elements II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 1, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `6` from `{"nums": [1, 2, 1, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the distance to an outer-occurrence span

Place the three distinct selected indices in increasing order `i<j<k`. The absolute values then simplify:

$$
|i-j|+|j-k|+|k-i|
=(j-i)+(k-j)+(k-i)
=2(k-i).
$$

The middle occurrence establishes that three copies exist, but its exact position disappears from the final expression. Minimizing distance means finding three equal-value occurrences whose first-to-third span is smallest.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collect sorted positions for each value

During one left-to-right scan, `g[x]` receives every index where value `x` occurs. Appending in enumeration order makes each occurrence list sorted automatically, with no separate sorting cost.

This grouping prevents comparisons between unequal values. Every three positions from one list form a good tuple, while positions from different lists never do.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | During one left-to-right scan, `g[x]` receives every index w... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why consecutive occurrence windows suffice

Let one value's positions be

$$
p_0<p_1<\cdots<p_{t-1}.
$$

Suppose a selected triple uses list positions `a<b<c`. Because three positions are required, `c>=a+2`. For the same first occurrence `p_a`, the earliest possible third occurrence is `p_{a+2}`, and

$$
p_{a+2}-p_a\le p_c-p_a.
$$

Thus the consecutive triple beginning at `a` has no larger distance than the arbitrary triple. If a global optimum skipped an occurrence, a consecutive window exists that matches or improves it.

The source checks every `h` from zero through `len(ls)-3` and evaluates the outer positions `ls[h]` and `ls[h+2]`. It need not read `ls[h+1]` because list ordering guarantees it is the distinct middle occurrence.

For example, occurrences `[1,4,5,9,12]` create windows with outer spans four, five, and seven: `(1,4,5)`, `(4,5,9)`, and `(5,9,12)`. A skipped triple such as `(1,5,9)` has span eight and cannot beat the window starting at one. The smallest window distance is twice four, or eight.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Cubic triplet enumeration:** It directly tests:** - **Cubic triplet enumeration:** It directly tests the definition but is infeasible at `n=10^5`.
- **Successor array:** Linking each occurrence to its next occurrence also permits checking the next two positions in $O(n)$ time. The exact source uses grouped lists instead.
- **Keep only the latest two positions online:** On seeing a third occurrence, evaluate its span with the occurrence two steps back. This reduces stored history per value but is not the shown implementation.
- **Evaluate nonconsecutive triples:** They cannot beat a consecutive window because moving the third occurrence earlier or first later shrinks the span.
- **Value appears fewer than three times:** It contributes no candidate.
- **Value appears exactly three times:** Its sole triple is checked.
- **Dense equal run:** Three adjacent indices yield distance four, the smallest possible for distinct integer indices.
- **Ties between values:** Only the distance is returned, so equal minima need no tie-breaking.
- **Order of tuple components:** Absolute pairwise distance is symmetric; sorting indices for analysis changes nothing.
- **Large answer:** The maximum finite distance is below `2n`, but the infinity sentinel cleanly handles absence.
- **Hash behavior:** Dictionary grouping gives expected linear time; values themselves need no bounded-array indexing.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The first scan performs one expected constant-time dictionary lookup and one append per index, totaling expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
