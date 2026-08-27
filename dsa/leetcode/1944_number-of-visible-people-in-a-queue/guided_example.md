# Guided Example: Number of Visible People in a Queue

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [10, 6, 8, 5, 11, 9]}`
- **Required output:** `[3, 1, 2, 1, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` people standing in a queue, and they numbered from `0` to $n - 1$ in **left to right** order. You are given an array `heights` of **distinct** integers where $\text{heights}[i]$ represents the height of the $$i^{\text{th}}$$ person.

The objective is to compute `[3, 1, 2, 1, 1, 0]` from `{"heights": [10, 6, 8, 5, 11, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Scan from the direction people are looking

Every person looks to the right. Scanning the queue from right to left means that when processing person $i$, all possible people they might see have already been incorporated into a stack.

The stack stores heights that remain relevant as visible blockers for people farther left. From bottom to top, these heights are strictly decreasing. The top is the nearest surviving candidate.

For current height `heights[i]`, the algorithm repeatedly pops a stack top that is shorter. Each popped person is visible to the current person, so `ans[i]` increases.

After all shorter tops are removed, one of two things is true:

- the stack is empty, so nobody taller remains to block the view;
- the stack top is taller than the current person. That person is also visible, and then blocks every person farther behind it.

Accordingly, the code adds one more when `stk` remains nonempty, then pushes the current height for people farther left.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [10, 6, 8, 5, 11, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every popped shorter person is visible

Consider a shorter height at the stack top. The stack invariant means no already processed person between it and the current position remains as an equal-or-taller obstruction to it. Any people removed earlier were shorter than some nearer survivor and do not invalidate the top's visibility from the new, taller current person.

More intuitively, as the current person looks right, they can see a sequence of record-high silhouettes. Every time the stack pops a shorter height, that height rises above all people between it and the current viewer but remains below the viewer. Therefore everyone between is shorter than both endpoints, satisfying the visibility definition.

Distinct heights remove equality complications: each comparison is strictly shorter or strictly taller.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider a shorter height at the stack top.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only one taller person is visible

Once the shorter visible people have been popped, the remaining top is the first surviving person taller than the current viewer. Everyone between is shorter than the current viewer, so this taller person is visible.

Any person behind that taller top is blocked by it. The blocking person's height is greater than the current viewer, so it is not shorter than the minimum of the two endpoint heights for any farther target. Thus the current viewer can see at most that one taller person beyond all popped shorter people.

This explains the two contributions exactly: all popped shorter heights, plus at most one unpopped taller height.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 2, 1, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [10, 6, 8, 5, 11, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 2, 1, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every pair:** For each viewer, scan righ:** - **Check every pair:** For each viewer, scan rightward while tracking intervening maxima. This can take $O(N^2)$ time.
- **Next-greater links:** One can precompute blocking relationships and follow visibility chains, but the monotonic stack computes counts directly in one pass.
- **Strictly increasing heights left to right:** Each person sees every person until the first taller sequence behavior permits; the stack repeatedly pops shorter suffix heights, producing the correct growing counts.
- **Strictly decreasing heights left to right:** Each person sees only the immediate next person, because that nearer person blocks all shorter people behind.
- **Last person:** The stack is empty when processed, so their answer remains zero.
- **Single person:** It is also the last person and correctly sees nobody.
- **One shorter then one taller:** Both can be visible: the shorter is popped and counted, and the taller survivor is counted once.
- **Distinct-height guarantee:** The exact comparisons rely on no equal heights. With duplicates, equality visibility and stack handling would need explicit policy.
- **Amortized loop:** A person may pop many heights in one iteration, but those heights never reenter, keeping the full scan linear.
- **Stack stores heights only:** Indices are unnecessary because the result is assigned to the current index and only height comparisons determine blocking.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of people.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
