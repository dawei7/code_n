# Guided Example: Count Square Sum Triples

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **square triple** `(a,b,c)` is a triple where `a`, `b`, and `c` are **integers** and $a^{2} + b^{2} = c^{2}$.

The objective is to compute `2` from `{"n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate the two ordered legs

A valid triple satisfies $a^2+b^2=c^2$, with all three values between $1$ and $n$. The exact solution chooses every ordered pair $(a,b)$ with two nested loops, computes $x=a^2+b^2$, and asks whether $x$ is the square of an allowed integer $c$.

The word ordered matters. The triples $(3,4,5)$ and $(4,3,5)$ are counted separately by the examples. Iterating every value of `a` in the outer loop and every value of `b` in the inner loop naturally visits both orders. The code should not divide its result by two.

Both loops use `range(1, n)` rather than `range(1, n + 1)`. At first this may look as though it omits a legal leg equal to $n$, but no valid triple is lost. If $a=n$ and $b\ge1$, then

$$
c=\sqrt{n^2+b^2}>n,
$$

which violates $c\le n$. The same reasoning applies when $b=n$. Therefore every valid leg is at most $n-1$, while the hypotenuse may equal $n$ and is retained by the later `c <= n` check.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test for an integer hypotenuse

For each pair, the code calculates:

`x = a * a + b * b`

and then

`c = int(sqrt(x))`.

For positive `x`, converting its nonnegative square root to an integer truncates toward zero, which is the same as taking the floor. If `x` is a perfect square, that floor is its exact integer square root. If it is between two consecutive squares, the floor is the smaller candidate.

The decisive test is `c * c == x`. Merely computing a square root is not enough: most sums of two squares are not perfect squares. Squaring the integer candidate again makes the perfect-square decision exact after the candidate has been selected. The additional condition `c <= n` enforces the upper bound on the hypotenuse. The lower bound needs no separate test because positive `a` and `b` imply `c > 0`.

For $n=5$, the loops encounter $(a,b)=(3,4)$ and calculate $x=9+16=25$, then `c = 5`. Both conditions succeed. They also encounter $(4,3)$ and count it independently. A pair such as $(1,2)$ gives $x=5$ and `c = 2`, but $2^2\ne5$, so it is rejected.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every count is correct

Whenever the algorithm increments `ans`, it has an integer `c` satisfying `c * c == a * a + b * b` and `c <= n`. The loops already guarantee $1\le a,b<n$, and positivity guarantees $c\ge1$. Thus every increment corresponds to a legal square triple.

Conversely, take any legal square triple $(a,b,c)$. Because $c\le n$ and both legs are positive, each leg is strictly smaller than $c$, so $a<n$ and $b<n$. The nested loops therefore visit that exact ordered pair. At that iteration `x=c^2`, `sqrt(x)` yields $c$ under these small constraints, the squared candidate equals `x`, and the upper-bound check succeeds. Thus every legal ordered triple is counted. Since a positive square has only one positive square root, an ordered pair cannot be counted with two different values of $c$.

The maximum possible `x` in the loops is below $2\cdot250^2$. Such small integers and their roots are represented accurately by ordinary double-precision floating point, so the exact solution's `sqrt` candidate is safe for the stated domain. For unrestricted much larger integers, an integer square-root function would be more robust.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precomputed square set:** Store `c * c` for every $1\le c\le n$, then test whether `a * a + b * b` belongs to the set. This keeps $O(n^2)$ time but uses $O(n)$ space and avoids floating-point square roots.
- **Integer square root:** Python's `isqrt` can compute the floor square root exactly with integer arithmetic. It gives the same asymptotic bounds and is safer if constraints become much larger.
- **Three nested loops:** Enumerating `a`, `b`, and `c` directly is easy to understand but takes $O(n^3)$ time even though $c$ is determined by the first two values.
- **Generate primitive Pythagorean triples:** Euclid's formula plus scaling can enumerate triples more selectively, but avoiding duplicates and counting ordered legs correctly adds complexity unnecessary for $n\le250$.
- **Do not divide by two:** The problem counts $(a,b,c)$ and $(b,a,c)$ separately when $a\ne b$. The nested loops already implement that ordered interpretation.
- **A leg equal to $n$:** It cannot occur in a valid triple with positive other leg and hypotenuse at most $n$, so the half-open loop range is correct.
- **Small bounds:** For $n<5$, no positive integer Pythagorean triple fits, and the counter remains zero.
- **Hypotenuse exactly $n$:** The condition is `c <= n`, so triples such as $(6,8,10)$ are correctly included when $n=10$.
- **Non-square sum:** Flooring the square root does not itself validate a pair. The exact equality `c * c == x` is what rejects it.
- **Floating-point scope:** The given upper bound keeps all values tiny enough for reliable `sqrt` conversion. With huge integers, replace `sqrt` with an integer square root rather than trusting rounding.
- **Repeated triples:** Each ordered pair appears exactly once in the nested loops, so the same ordered triple is never counted twice.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The outer loop has $n-1$ iterations and the inner loop has $n-1$ iterations for each outer value. Each pair performs a constant number of multiplications, additions, comparisons, and one square-root operation. Under the standard fixed-width arithmetic model, total time is $(n-1)^2\cdot O(1)=O(n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
