# Guided Example: Design a File Sharing System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 3, "operations": [["join", [[2]]], ["request", [1, 2]], ["request", [1, 3]]]}`
- **Required output:** `[1, [1], []]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We will use a file-sharing system to share a very large file which consists of `m` small **chunks** with IDs from `1` to `m`.

The objective is to compute `[1, [1], []]` from `{"m": 3, "operations": [["join", [[2]]], ["request", [1, 2]], ["request", [1, 3]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The state maintained by the object

The class must remember active users across many method calls. The stored implementation keeps four fields:

- `cur` is the largest fresh user ID issued so far.
- `chunks` stores the valid upper chunk ID `m`.
- `reused` is a min-heap of IDs belonging to users who have left.
- `user_chunks` maps each active user ID to a set of chunks currently owned by that user.

The sets make membership tests and adding a newly received chunk efficient on average. The heap makes the smallest reusable ID available at its root.

There is deliberately no map from a chunk to its owners. A request discovers owners by scanning all active users. This keeps joining and leaving structurally simple but makes requests depend on the active-user count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 3, "operations": [["join", [[2]]], ["request", [1, 2]], ["request", [1, 3]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Assigning the smallest available ID

When `join` is called, every reusable ID came from an earlier active user and is therefore at most `cur`. If `reused` is nonempty, `heappop` returns its smallest element. That value is smaller than the next never-issued ID `cur + 1`, so it is the globally smallest available positive ID.

If no departed ID is available, all IDs from one through `cur` are active. The method increments `cur` and assigns that next consecutive integer.

It then converts `ownedChunks` to a set and stores it at `user_chunks[userID]`. The contract says the initial list contains unique chunk IDs, but using a set also establishes the representation needed for later membership and insertion.

`cur` does not decrease when a high-numbered user leaves. It represents the frontier of IDs ever issued, not the number of active users. Reuse is handled exclusively by the heap.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Removing a user

`leave(userID)` pushes the ID into `reused` and removes its mapping with `user_chunks.pop(userID)`. Once the mapping disappears, future requests cannot find any chunk through that user.

The contract guarantees that the user is active and every leave matches a join. Therefore, the same ID is not pushed twice without being popped by another join, and `pop` is not asked to remove a missing key. Those guarantees preserve the one-copy-per-free-ID heap invariant.

The user's set is discarded as a whole. Because ownership is stored only by user, the method does not need to visit every chunk to update a reverse index.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, [1], []]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 3, "operations": [["join", [[2]]], ["request", [1, 2]], ["request", [1, 3]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, [1], []]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Chunk-to-owners reverse index:** Maintain an ordered owner set for each chunk. Requests become proportional to owner count, but join, leave, and successful request must update both directions consistently.
- **Unordered reverse sets plus sorting:** Owner lookup is direct, and sorting still costs $O(p \log p)$ when returning a request.
- **Scanning for a free ID:** Testing IDs from one upward on every join can be slow after frequent churn. The min-heap returns the smallest reusable ID efficiently.
- **User joins with no chunks:** An empty set is stored, and the user can acquire chunks through later successful requests.
- **No owner for a requested chunk:** The method returns an empty list and does not grant the chunk.
- **Requester already owns the chunk:** The requester appears among current owners, and adding the chunk again leaves the set unchanged.
- **Departed owner:** Removing the user's entire map entry ensures none of that user's chunks are offered afterward.
- **Frequent join and leave:** Heap size can grow with inactive reusable IDs, so space is not described solely by active-user count.
- **Out-of-range chunk:** The source returns an empty list even though valid calls are guaranteed by the contract.
- **Sorted output:** Dictionary iteration order is irrelevant because `sorted` establishes ascending IDs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log F)$. Let $U$ be the number of active users, $F$ the number of reusable IDs, $k$ the number of initially owned chunks in one join, $p$ the number of current owners of a requested chunk, and $H$ the total number of active user-chunk ownership entries.
- **Auxiliary Space Complexity:** $O(U + H)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
