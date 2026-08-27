# Guided Example: Check Array Formation Through Concatenation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [15, 88], "pieces": [[88], [15]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of **distinct** integers `arr` and an array of integer arrays `pieces`, where the integers in `pieces` are **distinct**. Your goal is to form `arr` by concatenating the arrays in `pieces` **in any order**. However, you are **not** allowed to reorder the integers in each array $\text{pieces}[i]$.

The objective is to compute `true` from `{"arr": [15, 88], "pieces": [[88], [15]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Match the next piece from the current target position

The order inside each piece is fixed, but the pieces themselves may be permuted. Therefore, when the unmatched suffix of `arr` begins at index `i`, any piece placed next must begin with `arr[i]`.

The source uses `i` as the first unmatched target index. Its inner search starts `k` at zero and scans `pieces` until it finds a piece whose first value equals `arr[i]`. If the scan reaches the end, no piece can begin this portion of the target, so it returns false.

The global distinctness guarantee makes the starting value decisive: flattened `pieces` contains no repeated integer, so at most one piece can have `arr[i]` as its first element. There is no need to branch over several candidate pieces.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [15, 88], "pieces": [[88], [15]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Consume matching values in that piece

After locating `pieces[k]`, `j` starts at zero. While `j` is still inside the piece and `arr[i] == pieces[k][j]`, both indices advance.

This compares the piece's values in their given order. It never rearranges them. If the complete piece matches, `j` reaches its length and the outer loop resumes with `i` at the next unmatched position of `arr`.

For `arr = [91,4,64,78]` and pieces `[[78],[4,64],[91]]`, the searches find:

- `[91]` at `i=0`,
- `[4,64]` at `i=1`,
- `[78]` at `i=3`.

Every piece is consumed in order and `i` reaches the target length, so the method returns true.

For `arr = [49,18,16]` and piece `[16,18,49]`, no piece begins with 49, so it returns false immediately. Having the same values is insufficient when their required internal order differs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After locating `pieces[k]`, `j` starts at zero.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the distinctness and total-length guarantees help

In an intended successful execution, every chosen piece is determined uniquely by its first value and must match completely. Because the total length of all pieces equals `len(arr)`, consuming enough complete, non-repeated pieces to cover all of `arr` also consumes all available piece values. No separate “used piece” set is necessary for a valid formation.

The distinct values in `arr` also mean the scan cannot encounter the same target starting value twice, so a piece cannot be selected twice along a successful match.

The intended invariant is: before an outer iteration, `arr[:i]` equals the concatenation of the fully consumed pieces selected so far. Finding and completely matching the unique next piece extends that invariant. When `i == len(arr)`, those pieces form the whole target.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [15, 88], "pieces": [[88], [15]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **First-value hash map:** Build `{piece[0]: piec:** - **First-value hash map:** Build `{piece[0]: piece}` once, then find each next piece in expected $O(1)$ time. Comparing all piece entries gives $O(n)$ total time and $O(p)$ space, matching the manifest.
- **Sort pieces and binary search first values:** This gives $O(p\log p+n\log p)$ time and mutates or copies the piece order. It is slower than hashing but faster than repeated full scans.
- **Explicit full-piece validation:** After the inner loop, immediately return false unless `j == len(piece)`. Also check `i < len(arr)` before each target access. This makes failure behavior direct and bounds-safe.
- **No piece begins with the next target value:** The source returns false through `k == len(pieces)`.
- **A piece has the right values in the wrong order:** Matching stops because piece order cannot be changed, and formation is impossible.
- **Single-element pieces:** They can be concatenated in the unique order dictated by `arr`.
- **One piece contains the whole target:** It succeeds only when every value matches in order.
- **Distinctness:** It guarantees at most one candidate piece for a starting value and prevents valid reuse of a piece.
- **Equal total length:** A successful full target match necessarily accounts for every available piece entry; this is central to the no-used-set reasoning.
- **Exact-source complexity:** Calling this variant “Optimal” does not change the fact that it linearly rescans `pieces` at every boundary.
- **Defensive indexing:** The matching condition should normally include `i < len(arr)` even when global constraints make an overrun difficult or impossible on conforming data.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(bp+n)$. Let $n=\lvert arr\rvert$ and $p=\lvert pieces\rvert$. Suppose $b$ piece boundaries are attempted. At each boundary, the source scans from the beginning of `pieces` and can inspect all $p$ first values. Across the run, this costs $O(bp)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
