# Guided Example: Last Remaining Integer After Alternating Deletion Operations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 8}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `3` from `{"n": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track indices instead of materializing the sequence

The initial list may contain up to $10^{15}$ integers, so simulation is impossible. Every sweep keeps roughly half the current entries, and the survivors follow a simple arithmetic mapping back to their positions before the sweep.

The recursive helper `survivor(length, from_left)` returns the one-based position, within a conceptual sequence of `length` consecutive slots, of the eventual survivor when the next sweep begins from the indicated side.

The values in the original list equal their one-based positions, so the top-level returned position is also the required integer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A sweep keeps the first visited item

The contract says to start from one side, keep the first encountered number, delete the second, and alternate.

From the left, survivors occupy old positions

$$
1,3,5,\ldots.
$$

Their count is $\lceil L/2\rceil=(L+1)//2$. Reduced survivor position $r$ maps back to old position

$$
2r-1.
$$

This mapping is the same for both even and odd $L$ when sweeping from the left.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A right sweep depends on parity

From the right, the rightmost item is kept and the next one to its left is deleted.

If $L$ is odd, the kept positions in normal left-to-right order are again

$$
1,3,5,\ldots,L,
$$

so reduced position $r$ maps to $2r-1$.

If $L$ is even, the kept positions are

$$
2,4,6,\ldots,L,
$$

so reduced position $r$ maps to $2r$.

This is why the source uses the odd-position formula when

`from_left or length % 2 == 1`

and uses the even-position formula only for a right-to-left sweep of an even-length sequence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal list simulation:** It needs $O(N)$ initial memory and work, impossible for $N$ up to $10^{15}$.
- **Iterative affine tracking:** One can maintain the first value, spacing, count, and direction without recursion; the source instead maps survivor indices recursively.
- **Always map with `2r-1`:** This fails for an even-length right sweep, whose survivors occupy even old positions.
- **Always map with `2r` from the right:** This fails for odd lengths, where the leftmost position is retained.
- **Use `length//2` survivors:** Odd lengths keep one extra element, so the correct size is `(length+1)//2`.
- **Forget to alternate direction:** Every recursive level must negate `from_left`.
- **`n=1`:** The base case returns one without performing a sweep.
- **`n=2`:** The left sweep keeps one and deletes two, returning one.
- **Odd current length:** Both sweep directions retain odd-indexed positions when written left to right.
- **Even current length:** Left keeps odd positions while right keeps even positions.
- **Large input:** Recursion depth is logarithmic and safely small for the stated bound.
- **One-based mapping:** Formulas use positions 1 through `length`, matching the original values `[1,2,...,n]`.
- **No input mutation:** Only integer lengths, directions, and mapped indices are used.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$. Each recursive call replaces `length` with $\lceil\texttt{length}/2\rceil$. The number of calls is therefore $O(\log N)$; for $N\le10^{15}$ it is only about fifty levels.
- **Auxiliary Space Complexity:** $O(log N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
