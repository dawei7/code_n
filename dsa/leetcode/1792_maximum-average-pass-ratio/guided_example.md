# Guided Example: Maximum Average Pass Ratio

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"classes": [[1, 2], [3, 5], [2, 2]], "extraStudents": 2}`
- **Required output:** `0.7833333333333333`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where $\text{classes}[i] = [\text{pass}_{i}, \text{total}_{i}]$. You know beforehand that in the $i^{\text{th}}$ class, there are $\text{total}_{i}$ total students, but only $\text{pass}_{i}$ number of students will pass the exam.

The objective is to compute `0.7833333333333333` from `{"classes": [[1, 2], [3, 5], [2, 2]], "extraStudents": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Optimize the improvement, not the current ratio

For a class with $p$ passing students out of $t$ total students, its current pass ratio is $p/t$. Assigning one guaranteed-to-pass student changes both counts, producing $(p+1)/(t+1)$.

The useful quantity for deciding where that student should go is the marginal gain

$$
\Delta(p,t)
=
\frac{p+1}{t+1}-\frac{p}{t}
=
\frac{t-p}{t(t+1)}.
$$

A class with the lowest current ratio does not necessarily have the greatest gain. Class size matters: changing one student has more influence on a small class than on a very large class. The algorithm must compare $\Delta$, not merely $p/t$, $p$, or $t$.

Because the number of classes is fixed, maximizing the average pass ratio is equivalent to maximizing the sum of class ratios. Dividing the final sum by the number of classes does not affect which assignment is optimal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"classes": [[1, 2], [3, 5], [2, 2]], "extraStudents": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Each class has diminishing returns

Suppose a class has already received $x$ extra students. Its next gain is

$$
\Delta_x
=
\frac{p+x+1}{t+x+1}-\frac{p+x}{t+x}
=
\frac{t-p}{(t+x)(t+x+1)}.
$$

The numerator $t-p$ remains constant because every added student increases both passing and total counts by one. The denominator grows with $x$, so the next gain never increases. A class may deserve several students, but after each assignment its priority must be recalculated.

This diminishing-return property is what makes a greedy decision valid. At any moment, every class exposes its next available gain. Choose the largest one. If an allegedly optimal allocation used a smaller currently available gain instead, exchange that assigned student for the larger gain. The total cannot decrease. Later gains from the chosen class are no larger than its current gain, so respecting the per-class order does not create a hidden advantage that invalidates the exchange. Repeating this exchange transforms an optimal allocation into the greedy sequence.

Another view is that each class offers a descending list of marginal gains. Assigning $x$ students to that class takes the first $x$ entries of its list. The goal is to select `extraStudents` gains across all lists while respecting those prefixes. Since each list is descending, repeatedly selecting the greatest exposed head produces the greatest possible total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Represent a max-priority rule with Python's min-heap

Python's heap removes the smallest key, but the desired class has the largest positive gain. The protected solution stores

`a / b - (a + 1) / (b + 1)`,

which is exactly $-\Delta(a,b)$. The largest gain becomes the most negative key, so it rises to the top of the min-heap.

Each heap entry is a tuple containing that negative gain, the current passing count `a`, and the current total `b`. The list comprehension creates one entry per class, and `heapify` organizes all entries in linear time.

For each extra student, the solution removes the top entry, increments both `a` and `b`, recomputes the class's new negative marginal gain, and pushes the updated tuple back. The heap always contains exactly one current entry for every class.

The extra tuple fields also provide deterministic tie-breaking when two floating-point gain keys compare equal. Either tied class is an optimal choice because their immediate improvements are equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0.7833333333333333` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"classes": [[1, 2], [3, 5], [2, 2]], "extraStudents": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0.7833333333333333` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rescan every class per student:** It makes the same greedy choice but costs $O(en)$ time, which is too slow at the maximum constraints.
- **Choose the smallest current ratio:** This ignores class size and may select a class with a smaller marginal improvement.
- **Assign all students at once to one class:** Marginal gains decrease after every assignment, so another class can become better partway through.
- **Binary search on a gain threshold:** More advanced resource-allocation methods are possible, but the heap directly implements the discrete choices within the constraints.
- **Exact fraction comparison:** Compare $(t-p)/(t(t+1))$ values by cross multiplication to avoid floating-point heap keys; integer products must use sufficient width.
- **Already perfect class:** When $p=t$, its gain is zero because adding another passing student keeps the ratio at one.
- **All classes perfect:** Every assignment has zero gain and the returned average remains exactly one.
- **One class:** Every extra student necessarily goes there; repeated pop-update-push operations produce its final ratio.
- **Repeated assignment to one class:** Its tuple is updated after each student, so the next decision uses its smaller new gain.
- **Equal gains:** Either class can be chosen without changing the best possible total.
- **Large `extraStudents`:** The loop performs exactly one allocation per student, and each maintains the heap invariant.
- **Tuple tie-breaking:** Passing and total counts may decide heap order after equal keys, but this cannot harm optimality.
- **Accepted precision:** The answer is a float and is judged with tolerance rather than exact textual equality.
- **Input preservation:** The original `classes` rows are not modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+e\log n)$. Let $n$ be the number of classes and $e$ be `extraStudents`. Creating the $n$ entries and calling `heapify` costs $O(n)$. Each of the $e$ assignments performs one heap removal and one insertion, each $O(\log n)$, for $O(e\log n)$ total. The final ratio sum scans $n$ entries in $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
