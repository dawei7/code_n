# Guided Example: Rearranging Fruits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"basket1": [4, 2, 2, 2], "basket2": [1, 4, 1, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have two fruit baskets containing `n` fruits each. You are given two **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit in each basket. You want to make both baskets **equal**. To do so, you can use the following operation as many times as you want:

The objective is to compute `1` from `{"basket1": [4, 2, 2, 2], "basket2": [1, 4, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only multiplicities matter

The baskets are considered equal after sorting, so original positions have no importance. For each fruit cost $x$, both baskets must end with the same number of copies of $x$.

The counter `cnt` stores

$$
\texttt{cnt[x]}=
\text{count of }x\text{ in basket1}
-
\text{count of }x\text{ in basket2}.
$$

The code builds this difference by adding one for each first-basket value and subtracting one for the paired second-basket value. Using `zip` does not claim the values at matching positions must correspond; it is simply a convenient way to visit one item from each equally sized array per iteration. The final counter is an aggregate frequency difference.

A positive difference means basket1 has surplus copies that must move to basket2. A negative difference means basket2 has the surplus.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"basket1": [4, 2, 2, 2], "basket2": [1, 4, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Detect when equalization is impossible

Across both baskets, the total number of copies of every cost must be split equally between the final baskets. If the combined count of a value is odd, such a split is impossible.

The parity of the combined count and the parity of `cnt[x]` are the same, because

$$
(c_1+c_2)-(c_1-c_2)=2c_2.
$$

Their difference is even. Therefore, `v % 2` being nonzero proves that the total count is odd, and the function immediately returns $-1$.

If the difference is even, `abs(v) // 2` is the number of copies of cost $x$ that are on the wrong side. For example, if basket1 has four more copies than basket2, two copies must cross from basket1, reducing the difference by four: basket1 loses two and basket2 gains two.

The list `nums` stores every misplaced copy from both sides with exactly this required multiplicity. Its length is even. Half of its entries belong to surpluses from basket1 and half to surpluses from basket2, because the baskets have equal sizes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Pair small misplaced values with large ones

Every correcting exchange pairs one surplus item from one basket with one surplus item from the other. A direct swap of costs $x$ and $y$ costs $\min(x,y)$. To minimize the sum of these minima, small misplaced values should serve as the cheaper side of exchanges with large misplaced values.

After sorting `nums`, let `m = len(nums) // 2`. The first half contains exactly the $m$ globally smallest misplaced values. These are the only values that need to be priced as the smaller member of a pairing; the second-half values can be paired with them from the large end.

An exchange argument explains this. If two pairs have their cheaper members $a\le b$ and their larger partners are arranged so that a smaller partner is wasted with $a$ while a larger partner is paired with $b$, swapping the partners cannot increase either minimum. Pairing extremes ensures every globally small value pays once, while globally large values do not become unnecessarily expensive minima.

The implementation does not need to construct the actual pairs or track which basket contributed each entry. The balanced surplus counts guarantee compatible cross-basket partners, and the minimum-cost total depends on the $m$ smaller representatives.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"basket1": [4, 2, 2, 2], "basket2": [1, 4, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate arbitrary swaps:** Local choices can be suboptimal because an expensive direct swap may be cheaper through the global minimum. Frequency balancing exposes the real structure.
- **Use two frequency maps:** Separate basket counters are conceptually clear, but one signed counter stores the same information more compactly.
- **Already equal baskets:** Every difference is zero, `nums` is empty, `m=0`, and the sum correctly returns zero.
- **Odd total frequency:** An odd `cnt` difference means an odd combined multiplicity, so no sequence of swaps can split that value equally.
- **Duplicate costs:** Multiplicity is the entire point of the counter; every required surplus copy is repeated in `nums`.
- **Global minimum already balanced:** It can still be used as an intermediary. A physical minimum fruit exists in a basket even when it is not itself in the mismatch list.
- **Direct route cheaper:** When $x\le2\cdot\texttt{mi}$, one direct swap costs no more than using two intermediary swaps.
- **Indirect route cheaper:** When $x>2\cdot\texttt{mi}$, routing through the minimum saves cost.
- **Meaning of `min(cnt)`:** Python iterates the counter's keys for `min`, so this produces the smallest fruit value. It does not inspect signed counts.
- **Large answer:** Python integers avoid overflow; fixed-width languages should accumulate the total in a 64-bit type.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the size of each basket. Building the counter takes $O(n)$ time. The mismatch list contains at most $2n$ entries but in fact remains $O(n)$. Sorting it dominates with $O(n\log n)$ time, and the final sum is linear.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
