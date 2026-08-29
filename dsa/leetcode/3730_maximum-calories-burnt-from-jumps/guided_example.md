# Guided Example: Maximum Calories Burnt from Jumps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [1, 7, 9]}`
- **Required output:** `181`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `heights` of size `n`, where $\text{heights}[i]$ represents the height of the $i^{\text{th}}$ block in an exercise routine.

The objective is to compute `181` from `{"heights": [1, 7, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Squared distance rewards jumps between opposite extremes

All block heights are positive and the start is fixed at zero, below every block. A jump contributes the square of its height difference. Because squaring is convex, one large difference is more valuable than splitting that separation into smaller differences. An optimal route therefore repeatedly crosses between the largest and smallest unvisited heights instead of visiting nearby heights consecutively.

The exact source sorts the heights and keeps two indices:

- `l` points to the smallest unvisited height.
- `r` points to the largest unvisited height.

It begins with `pre = 0`. While at least two heights remain, it jumps first to `heights[r]`, then to `heights[l]`, removes both extremes by moving the pointers inward, and records the low height as the new `pre`.

The resulting order is

$$
\text{largest},\ \text{smallest},\ \text{second largest},\ \text{second smallest},\ldots
$$

If one middle height remains, the final statement jumps to it from `pre`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [1, 7, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first block is the maximum

The ground is zero and all heights are positive. Among possible first jumps, the largest height gives the greatest initial square. It also places the route at the high extreme, ready for a maximum-span jump to the smallest remaining height.

Starting from a smaller height would spend that block without gaining the full ground-to-maximum distance. The standard extreme-exchange argument for convex distance shows that moving the largest remaining height into this first position and relocating the displaced height to the later neighbor of the maximum cannot reduce the two affected squared differences. The fixed endpoint outside the height range breaks the symmetry in favor of starting high.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why alternating extremes is optimal

For ordered values `a <= b <= c <= d`, pairing across the range is at least as valuable as pairing nearby values. Expanding squares gives the Monge-style inequality

$$
(d-a)^2+(c-b)^2
\ge
(b-a)^2+(d-c)^2.
$$

The left side uses cross-extreme gaps; the right side uses gaps within the low and high groups. Repeated exchange of adjacent route portions removes any situation in which two still-available extremes are bypassed in favor of closer internal transitions. The route can therefore be transformed, without lowering its score, into one that alternates the high and low ends of the sorted remaining set.

Once the route is at a low chosen extreme, the farthest unvisited point is the current maximum. Once it reaches that maximum, the farthest unvisited point is the current minimum. Choosing those in alternation realizes the cross-extreme form at every layer. With the ground fixed below all values, the high-first version is the maximizing orientation.

This exchange view is important: “choose the farthest next block” is not being used as an unsupported generic greedy rule. On arbitrary metrics it could fail. It works here because points lie on one ordered line and squared distance has the convex cross-extreme inequality.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `181` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [1, 7, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `181` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every visiting order:** This requires $n!$ permutations. Sorting plus the convex extreme exchange determines an optimal order directly.
- **Visit heights in sorted order:** Consecutive gaps are small and waste the benefit of squaring. Alternating extremes maximizes large cross-range jumps.
- **Start at the smallest height:** Because the fixed ground is below all blocks, this sacrifices the largest possible initial square. The high-first extreme orientation is superior.
- **Alternate extremes but begin low:** This may be optimal for a different free endpoint, but not with the fixed zero start and positive heights.
- **Single block:** The loop is skipped, and the final statement returns its height squared.
- **Two blocks:** The route is maximum then minimum. The bookkeeping's final zero term does not change the correct two-jump score.
- **Odd number of blocks:** One middle height remains after paired extremes and receives the final jump.
- **Duplicate heights:** Sorting retains all positions. Equal-height jumps contribute zero, and every duplicate is still visited exactly once.
- **All heights equal:** The first jump contributes `h²` and every later jump contributes zero.
- **Input mutation:** `heights.sort()` changes the list order. The problem permits arbitrary rearrangement and does not require preserving the input.
- **Ground cannot be revisited:** The sequence includes zero only as `pre` before the first jump; no later transition uses it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the number of blocks. Sorting takes $O(n\log n)$ time. The two pointers move inward across the array once, so the jump accumulation takes $O(n)$ time. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
