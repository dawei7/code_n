# Guided Example: Minimum Time to Build Blocks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"blocks": [1], "split": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a list of blocks, where $\text{blocks}[i] = t$ means that the `i`-th block needs `t` units of time to be built. A block can only be built by exactly one worker.

The objective is to compute `1` from `{"blocks": [1], "split": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compress two sibling jobs into one effective job

Suppose two block or subtree completion requirements are $x$ and $y$, with $x\leq y$. If one worker splits and its two children handle those branches in parallel, their parent subtree finishes after

$$
\texttt{split}+\max(x,y)=\texttt{split}+y.
$$

From the perspective of everything above that parent, the entire two-branch subtree behaves like one abstract job whose required time is `y + split`. The internal details no longer matter for higher merges.

The code performs exactly this contraction:

- pop the smallest time and discard its scalar value,
- pop the next-smallest time,
- push that second value plus `split`.

The first popped value does affect the tree—it is the sibling with no larger completion requirement—but it does not appear in the parent formula because the maximum is the second value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"blocks": [1], "split": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the two smallest requirements should become siblings

Long build times should receive fewer split delays, while short build times can tolerate deeper placement. In an optimal tree, consider a pair of sibling leaves at maximum depth. If a deeper leaf had a larger build time than some shallower leaf, swapping their assigned blocks would not increase the maximum completion time: moving the larger time shallower helps, and moving the smaller time deeper is no worse than the old larger deep completion.

By repeated exchanges, two of the smallest current requirements can occupy a deepest sibling pair in some optimal tree. Contracting that pair replaces their parent by an effective requirement `max(x, y) + split`. What remains above the parent is the same problem on one fewer requirement.

This gives optimal substructure. Choose the two smallest, combine them, then optimally combine the resulting abstract job with the remaining jobs. Repeating the argument justifies every greedy heap step.

It is important that the heap contains both original block times and previously abstracted subtree times. After two small blocks combine, their parent may no longer be among the smallest requirements. The new effective value is pushed back so the next choice compares it fairly with untouched blocks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Long build times should receive fewer split delays, while sh... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Follow the three-block example

For blocks `[1, 2, 3]` and `split = 1`, the heap first removes one and two. Their abstract parent takes `2 + 1 = 3`, so the heap now contains three and three. Combining those produces `3 + 1 = 4`.

The corresponding schedule splits once at the root. One child builds the original three-time block. The other child splits again and its children build the one- and two-time blocks. The root-to-finish time is four, matching the example.

For blocks `[1, 2]` with split five, their only merge gives `2 + 5 = 7`. Both blocks then build in parallel after the one required split.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"blocks": [1], "split": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming over worker counts:** One :** - **Dynamic programming over worker counts:** One can model how many blocks or workers are handled, but the greedy optimal-merge structure gives a simpler $O(n\log n)$ solution.
- **Repeatedly sort the remaining values:** It finds the same two minima but can cost $O(n^2\log n)$ across all contractions.
- **Linear search for two minima:** This avoids a heap but costs $O(n^2)$ total time.
- **Binary search on the answer:** Test whether a proposed time permits enough worker splits and block assignments. This is possible but substantially harder to implement and prove.
- **One block:** No split occurs, and the sole build time is returned.
- **Very expensive split:** The number of leaves still must reach the number of blocks, but the optimal tree places longer jobs shallower to limit accumulated split delays.
- **Equal block times:** Any two equal minima can be siblings; heap tie order does not affect the optimal completion value.
- **New abstract value becomes large:** Pushing it back rather than immediately merging it again lets smaller untouched requirements pair first when beneficial.
- **Parallel versus additive time:** A sibling combination uses `split + max(x, y)`, not `split + x + y`, because the two child branches execute concurrently.
- **Input mutation:** `heapify` and subsequent pops destroy the original block list. Copy before heapifying if caller-visible preservation is required.
- **Positive split and build times:** These guarantees support placing longer work shallower and ensure no unusual benefit from unnecessary extra splitting.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of blocks.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
