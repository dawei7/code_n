# Guided Example: Widest Vertical Area Between Two Points Containing No Points

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[8, 7], [9, 9], [7, 4], [9, 7]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given `n` `points` on a 2D plane where $\text{points}[i] = [x_{i}, y_{i}]$, Return* the **widest vertical area** between two points such that no points are inside the area.*

The objective is to compute `1` from `{"points": [[8, 7], [9, 9], [7, 4], [9, 7]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only horizontal position affects a vertical strip

A vertical area extends infinitely along the $y$-axis. Its width is determined solely by two vertical boundary lines, so point $y$-coordinates cannot change whether a point lies horizontally inside the strip.

Project every point onto its $x$-coordinate. The problem becomes finding the largest open interval between occupied $x$ positions that contains no occupied position. Points may lie on either boundary because boundary points are explicitly allowed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[8, 7], [9, 9], [7, 4], [9, 7]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort points by x-coordinate

`points.sort()` applies Python's lexicographic list ordering. It compares each point's first entry, $x$, first and uses $y$ only to order points whose $x$ values tie. Thus, after sorting, the sequence of $x$-coordinates is non-decreasing.

The call sorts the input list in place. The method does not create a separate coordinate list.

`pairwise(points)` then yields every adjacent pair `(a,b)` in that sorted order. For each pair, the generator computes `b[0] - a[0]`, the horizontal gap between their $x$ positions. `max` returns the largest such gap.

The constraint of at least two points guarantees that `pairwise` yields at least one pair, so `max` never receives an empty generator.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only adjacent sorted positions matter

Suppose two boundary points have $x$-coordinates $x_L<x_R$. If some point has $x$ strictly between them, that point lies inside the infinite vertical strip regardless of its $y$-coordinate, so the area is invalid.

After sorting by $x$, an interval contains no occupied $x$ strictly inside it exactly when its endpoints are consecutive in the sorted sequence of occupied positions. Therefore every valid candidate width appears among adjacent differences.

Conversely, between two adjacent sorted points there is no point whose $x$ lies strictly between their $x$ values. The open vertical strip between those boundary lines contains no point, while any points on the boundary lines are allowed. Every adjacent gap is therefore a valid candidate.

Taking their maximum produces the widest valid vertical area.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[8, 7], [9, 9], [7, 4], [9, 7]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Extract and sort only x-coordinates:** `xs = sorted(x for x, _ in points)` makes the relevant dimension explicit but allocates another $O(n)$ list rather than sorting the supplied points.
- **Deduplicate x-coordinates first:** Sorting a set can reduce repeated zeros, but building the set uses extra storage and is not necessary for correctness.
- **Bucket or counting sort:** Coordinates range up to $10^9$, so a direct coordinate-sized bucket array is impractical.
- **Maximum-gap linear algorithms:** With numeric bucketing, the maximum adjacent sorted gap can be found in linear expected time, but the implementation is much more complex and ordinary sorting fits $n\le10^5$.
- **Two points:** Their horizontal difference is the only adjacent gap and therefore the answer.
- **All points share one x-coordinate:** Every gap is zero, so the widest valid area has width zero.
- **Duplicate points:** They contribute zero gaps and do not alter gaps between distinct x positions.
- **Boundary points:** Points at the chosen left or right x-coordinate are allowed, so only strict interior positions invalidate a strip.
- **Arbitrary y-coordinates:** They never influence an infinitely tall vertical area's width or emptiness.
- **Input mutation:** `points.sort()` changes the original ordering. Use `sorted(points)` if caller-visible preservation were required.
- **At least two points guarantee:** Without it, `max` over `pairwise` would be empty and raise an error; the stated constraints rule that out.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of points. In-place sorting costs $O(n\log n)$ time. `pairwise` and the maximum generator then traverse $n-1$ adjacent pairs in $O(n)$ time. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
