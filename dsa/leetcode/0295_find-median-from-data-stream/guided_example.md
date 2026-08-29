# Guided Example: Find Median from Data Stream

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stream": [1, 2, 3, 4, 5]}`
- **Required output:** `[1.0, 1.5, 2.0, 2.5, 3.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

The objective is to compute `[1.0, 1.5, 2.0, 2.5, 3.0]` from `{"stream": [1, 2, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The two invariants

After every call to `addNum`, the data structure maintains two properties.

First, the heaps form an ordered partition:

$$
\text{every lower-half value} \le \text{every upper-half value}.
$$

Second, their sizes are balanced so that `minq`, the upper half, either has the same number of elements as `maxq` or has exactly one more:

$$
\lvert\texttt{minq}\rvert = \lvert\texttt{maxq}\rvert
$$

or

$$
\lvert\texttt{minq}\rvert = \lvert\texttt{maxq}\rvert + 1.
$$

Giving the extra element to `minq` is a design choice. A symmetric implementation could give it to the lower heap, but the insertion and query formulas would then need to follow that opposite convention consistently.

Together, these invariants expose the median at the two roots. If the total count is even, the two heaps have equal sizes, and the sorted middle pair consists of the largest lower value and the smallest upper value. If the total count is odd, `minq` has one extra value, and its smallest element is the single middle value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stream": [1, 2, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Routing a new number to the proper side

The compact line

`heappush(minq, -heappushpop(maxq, -num))`

does several carefully ordered operations.

Conceptually, treat `num` as a candidate for the lower half. Because `maxq` stores negated values, the code pushes `-num` into it. It then immediately pops the smallest stored negative value. The smallest negative represents the largest original value among the old lower half plus the new candidate. Negating that popped value converts it back to its original sign, and the outer `heappush` inserts it into `minq`.

In plain language: temporarily place the new value with the lower values, remove the largest value from that candidate group, and send that largest value to the upper heap.

This operation restores the ordering invariant regardless of how small or large `num` is:

- If `num` is very large, it becomes the largest candidate and moves directly to `minq`; the old lower half stays unchanged.
- If `num` belongs in the lower half, some previous lower-half maximum is displaced into `minq`, leaving `num` among the lower values.
- If `num` equals boundary values, either copy may cross the boundary. Since equal values satisfy the non-strict ordering relation, the partition remains valid.

After this routing step, every value left in `maxq` is no larger than every value in `minq`. However, `minq` has just received one element and may now exceed `maxq` by two elements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Restoring the size invariant

The condition `len(minq) - len(maxq) > 1` detects the only possible size violation. If it holds, the source removes `heappop(minq)`, the smallest upper-half value, negates it, and pushes it into `maxq`.

Moving the smallest upper value down is exactly the safe rebalance. It is no larger than the values remaining in `minq`, and it is at least as large as the existing lower values because the ordering invariant already held. Thus, it becomes the new boundary maximum of the lower half without mixing the two ordered groups.

No opposite rebalance is required. The first routing line always sends one candidate to `minq`, and the previous valid size relation ensures `maxq` cannot become larger than `minq` afterward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1.0, 1.5, 2.0, 2.5, 3.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stream": [1, 2, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1.0, 1.5, 2.0, 2.5, 3.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort on every median query:** Appending is cheap, but each query can cost $O(n\log n)$. It repeats ordering work and is poor when medians are requested frequently.
- **Keep one sorted list:** Binary search finds an insertion index in $O(\log n)$ time, but inserting into a Python list can shift $O(n)$ elements. Median lookup is then $O(1)$, with slower updates than the two-heap method.
- **Balanced search tree with order statistics:** Such a tree can support logarithmic insertion and median selection, but Python has no built-in order-statistic tree, and implementing one is substantially more complex.
- **Frequency buckets for values in `[0, 100]`:** Under the first follow-up's narrow value range, store 101 counts and scan the buckets for the middle rank. Updates become $O(1)$ and queries take $O(101)$, which is constant with respect to stream length.
- **Buckets plus outlier structures:** If 99 percent of values lie in `[0, 100]`, counts can cover the dense range while separate ordered structures track values below 0 and above 100. Rank counts determine whether the median lies in the dense range or an outlier side, but the bookkeeping is more specialized.
- **Reservoir sampling:** It can estimate a median with bounded storage, but the contract requires an exact answer within numerical tolerance, not a statistical approximation.
- **Putting the extra element in the wrong heap:** This source gives the extra value to `minq`. If `maxq` had the extra element, returning `minq[0]` for odd sizes would be wrong.
- **Forgetting negation:** `maxq[0]` is a stored negative number. The logical lower maximum is `-maxq[0]`, which explains the subtraction in the even-size formula.
- **Negative stream values:** Negation still reverses their ordering correctly. For example, original values `-5` and `-2` are represented as 5 and 2 in the lower max-heap mechanism; Python's min-heap root still corresponds to the largest original lower value after the sign conversion.
- **Duplicate values:** Equal elements may reside on either side of the partition. The invariant uses `<=`, so duplicates do not affect correctness or require unique keys.
- **One inserted value:** It resides in `minq`, which has one extra element. `findMedian` returns that value directly.
- **Two inserted values:** The heaps have equal sizes. Their roots are the lower and upper values, and the formula returns their arithmetic mean.
- **Odd number of values:** `minq` has exactly one extra element, making its root the unique median.
- **Even number of values:** Both heaps have equal sizes, so the mean of their boundary roots is required even when that result is fractional.
- **Large positive and negative bounds:** The inputs lie between $-10^5$ and $10^5$. Their sum and negation are safe in Python integers, and `/ 2` produces a floating-point result as the return contract expects.
- **Query before insertion:** The source does not guard against empty roots because the problem explicitly guarantees at least one stored element before `findMedian` is called.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Suppose $k$ values have already been inserted. Heap insertion, removal, and combined push-pop each take $O(\log k)$ time in the worst case. `addNum` performs one `heappushpop`, one push into `minq`, and, when needed, one pop and one push for rebalancing. The number of heap operations per insertion is constant, so a single insertion costs $O(\log k)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
