# Guided Example: Final Element After Subarray Deletions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 5, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [1, 5, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A player may end the game immediately

When the current array has length `m`, a legal move may remove any nonempty contiguous subarray of length strictly less than `m`. In particular, removing `m - 1` elements is legal.

There are two especially important such moves:

- remove every element except the current first element;
- remove every element except the current last element.

The removed elements form a contiguous suffix or prefix, respectively. Either move leaves one element and ends the game immediately.

This means the full minimax game tree is unnecessary. Alice can choose an endpoint on her first turn, and Bob can choose an endpoint on his first turn if Alice does not already finish.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 5, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Alice can guarantee the larger original endpoint

Let

$$
M=\max(\texttt{nums}[0],\texttt{nums}[N-1]).
$$

If the first element equals `M`, Alice removes the suffix `nums[1..N-1]`. If the last element equals `M`, she removes the prefix `nums[0..N-2]`.

Both removed blocks have length $N-1<N$, so they are legal whenever $N>1$. The selected endpoint is left alone, the game ends before Bob moves, and the final value is `M`.

For a one-element array, no move is needed and both endpoints refer to that same value. Thus Alice can always ensure a result of at least `M`.

This already proves why an interior maximum does not automatically decide the game. Alice cannot keep an arbitrary interior element by deleting everything else in one move: the elements on both sides of an interior position form two separated blocks, not one contiguous subarray.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Bob can prevent any value above the larger original endpoint

To establish the exact minimax result, it is not enough to show what Alice can obtain. We must also show that she cannot force anything larger than `M`.

Consider any first move by Alice. She removes one proper contiguous block `[l,r]`.

Because the removed block is not the entire array, at least one element survives. More specifically, Alice cannot remove both original endpoints unless she removes the whole array: a contiguous block containing index 0 and index $N-1$ contains every index between them. Therefore at least one of the two original endpoints survives.

Any surviving original first element remains the first element of the concatenated array. Any surviving original last element remains its last element. Deleting a middle block changes adjacency but does not move an outside element past another surviving element.

If Alice's move already leaves one element, that survivor can only be an original endpoint. Removing $N-1$ contiguous elements leaves either index 0 or index $N-1$, never a strict interior index. Its value is at most `M`.

If at least two elements remain, Bob can end the game on his turn. He compares the current first and last values and keeps the smaller one by deleting the other `m-1` elements as one prefix or suffix. Since at least one current endpoint is a surviving original endpoint, the smaller current endpoint is no greater than that surviving endpoint, which is itself at most `M`.

Thus, regardless of Alice's first deletion, Bob has a response ensuring the final value is at most `M`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 5, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive minimax:** Enumerating every removable subarray at every state creates an explosive game tree and repeats many array states. It is useful only as a tiny-input verification model.
- **Dynamic programming over intervals:** Surviving arrays after middle deletion can concatenate separated original pieces, so an interval DP is not even a natural complete state; the endpoint theorem eliminates the need.
- **Choose the global maximum:** This is wrong when the maximum is strictly interior. Alice cannot isolate an interior element by deleting one contiguous proper block.
- **One element:** No move is possible or necessary, and `nums[0]` equals `nums[-1]`.
- **Two elements:** Alice can remove either one, so she directly chooses the larger.
- **Equal endpoints:** Their common value is the minimax result, regardless of all interior values.
- **Very large interior value:** It does not exceed Bob's endpoint-based cap unless it is itself an original endpoint.
- **Alice ends immediately:** Removing a prefix or suffix of length $N-1$ is legal because the condition is strictly less than the current length, not at most $N-2$.
- **Bob's cap after a middle deletion:** At least one original endpoint survives as a current endpoint, and Bob keeps the smaller current endpoint.
- **Positive-value constraint:** The proof uses only ordering and would remain valid for arbitrary integers; positivity is not needed by the source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The source reads `nums[0]` and `nums[-1]` and computes one maximum. Running time is $O(1)$, independent of $N$. It does not need to scan interior elements because the minimax proof establishes that they cannot change the game value.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
