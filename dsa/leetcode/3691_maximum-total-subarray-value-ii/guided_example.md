# Guided Example: Maximum Total Subarray Value II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2], "k": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` and an integer `k`.

The objective is to compute `4` from `{"nums": [1, 3, 2], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One monotone sequence for each left endpoint

Fix a left endpoint $l$ and consider the subarrays:

$$
[l,l], [l,l+1], \ldots, [l,n-1].
$$

Define:

$$
V(l,r)=\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r]).
$$

When $r$ moves one position to the right, the subarray gains an element.

- Its maximum can increase or stay the same; it cannot decrease.
- Its minimum can decrease or stay the same; it cannot increase.

Therefore, $V(l,r)$ is nondecreasing as $r$ increases. For each fixed $l$, the values form one sorted sequence:

$$
V(l,l)\le V(l,l+1)\le\cdots\le V(l,n-1).
$$

Every distinct subarray belongs to exactly one such sequence, identified by its left endpoint.

The problem is now equivalent to finding the sum of the largest $k$ elements across these $n$ sorted sequences. The algorithm reads each sequence backward, beginning with its largest element at $r=n-1$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sparse-table state

To evaluate $V(l,r)$ quickly, the class `SparseTableRMQ` stores two tables:

- `f_max[i][j]` is the maximum over the length-$2^j$ interval beginning at `i`;
- `f_min[i][j]` is the minimum over the same interval.

Column zero represents intervals of length one:

`f_max[i][0] = data[i]`

`f_min[i][0] = data[i]`

For a higher level $j$, a length-$2^j$ interval is split into two adjacent halves of length $2^{j-1}$. The source combines the previously computed halves:

`f_max[i][j] = max(f_max[i][j - 1], f_max[i + 2^(j-1)][j - 1])`

and analogously uses `min` for `f_min`.

The actual code expresses the power of two with bit shifts. Only starting indices for which the complete interval fits are filled.

The table uses:

`max_log = n.bit_length() + 1`

which allocates a small number of harmless extra columns. Levels whose interval length exceeds $n$ have no valid starting positions and their construction loops are empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | To evaluate $V(l,r)$ quickly, the class `SparseTableRMQ` sto... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choosing the query block size

The array `lg` stores:

$$
\texttt{lg}[L]=\lfloor\log_2 L\rfloor.
$$

The recurrence

`lg[i] = lg[i >> 1] + 1`

works because right-shifting a positive integer by one performs floor division by two.

For query interval $[l,r]$, let its length be $L=r-l+1$ and choose $j=\lfloor\log_2L\rfloor$. A block of length $2^j$ fits inside the query. The source uses two such blocks:

- one beginning at $l$;
- one ending at $r$, beginning at $r-2^j+1$.

Together they cover the complete query interval and may overlap. Overlap is safe for minimum and maximum because repeating an element does not change either aggregate. Thus:

`query_max(l, r)`

and

`query_min(l, r)`

each need only two table lookups and one comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate and sort all subarrays:** There are :** - **Enumerate and sort all subarrays:** There are $\Theta(n^2)$ distinct subarrays, so materializing all values is infeasible at the maximum $n$.
- **Segment tree plus heap:** A segment tree uses $O(n)$ space and builds in $O(n)$ time, but each range minimum/maximum query costs $O(\log n)$. This is the manifest-described alternative, not the exact source.
- **Heapify initial candidates:** Building a list of the $n$ terminal candidates and calling `heapify` reduces heap initialization from $O(n\log n)$ to $O(n)$. The checked-in source uses repeated `heappush`.
- **Binary-search a value threshold:** One could try to count subarrays above a range threshold, but efficiently counting max-minus-min constraints is substantially more involved and still needs tie handling for the top-$k$ sum.
- **`k = 1`:** The first heap pop returns the maximum range among all subarrays, which is the global array range.
- **Maximum legal `k`:** When `k=n(n+1)/2`, every sequence is eventually exhausted and every distinct subarray is selected exactly once.
- **One-element array:** The only sequence contains one value zero. The heap pops it, performs no replacement push, and returns zero.
- **All elements equal:** Every range value is zero. Heap tie order is irrelevant, and the total remains zero for any legal $k$.
- **Equal range values:** Distinct subarrays may have identical values. The heap entries retain coordinates, so equal values are still emitted as separate legal choices.
- **Overlapping subarrays:** Different coordinate pairs may overlap freely. The sequence organization is by left endpoint, not by disjointness.
- **Sparse-table overlap:** Query blocks may overlap because minimum and maximum are idempotent. The same technique would not work unchanged for a non-idempotent aggregate such as sum.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
