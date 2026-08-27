# Guided Example: Design Auction System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"], "arguments": [[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]}`
- **Required output:** `[null, null, null, 2, null, 1, null, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are asked to design an auction system that manages bids from multiple users in real time.

The objective is to compute `[null, null, null, 2, null, 1, null, 1, -1]` from `{"operations": ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"], "arguments": [[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain the same active bid in two complementary indexes

The system must support two different kinds of access:

- addition, replacement, update, and removal identify one bid by `(userId, itemId)`;
- a highest-bidder query must rank every active bid for one `itemId`.

One data structure is not naturally optimal for both. The source therefore stores each active bid in two synchronized views.

`users` is a regular dictionary whose outer key is `userId`. Each value is another dictionary mapping `itemId` to the current `bidAmount`. Thus `users[userId][itemId]` is the authoritative amount for one exact bid and can be found in expected $O(1)$ time.

`items` maps each `itemId` to a `SortedList` of tuples `(bidAmount, userId)`. This view groups all bids competing for the same item and keeps them ordered. Python tuple ordering compares the amount first and, when amounts tie, compares the user identifier. Therefore, the last tuple in the list has the greatest bid amount and, among equal greatest amounts, the greatest user ID—exactly the query's priority.

The central consistency rule is:

> For every active bid `users[u][item] = amount`, `items[item]` contains exactly one tuple `(amount, u)`, and there are no other tuples representing that user-item pair.

Every mutating method preserves this rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"], "arguments": [[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Adding a new bid or replacing an old one

`addBid` first ensures that the user has an inner dictionary. If `userId` has never appeared, `users[userId] = {}` creates it.

The method then checks whether `itemId` is already in that user's dictionary. The contract says another `addBid` for the same user-item pair replaces the old amount; it does not create a second bid. The source implements replacement by calling `removeBid(userId, itemId)` first. That removes both the old sorted tuple and the old dictionary entry.

After any old version is gone, the new amount is written into the user lookup and `(bidAmount, userId)` is inserted into the item's ordered list. The two indexes again describe exactly the same active bid.

The order of these steps prevents stale duplicates. If user 5 changes an item-9 bid from 100 to 130 through `addBid`, the list does not retain both `(100, 5)` and `(130, 5)`. Only the latter remains eligible to win.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `addBid` first ensures that the user has an inner dictionary... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Updating an existing bid eagerly

`updateBid` is guaranteed to receive an existing pair. It reads `oldAmount` directly from `users[userId][itemId]`. That amount identifies the exact tuple `(oldAmount, userId)` stored for the item.

The old tuple is removed from `items[itemId]`, the new tuple `(newAmount, userId)` is added, and the dictionary amount is replaced. Removing before adding is important even when the amount changes downward: the ordered item view must reflect current bids only. If `newAmount` equals `oldAmount`, removing and reinserting the same tuple is unnecessary work but remains correct.

This is an eager-update design. There are no stale heap records and no version timestamps to validate during a query. At all times, the ordered list itself is an exact representation of the live auction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, 2, null, 1, null, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"], "arguments": [[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, 2, null, 1, null, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash map plus lazy max-heap:** Push `(-amount,:** - **Hash map plus lazy max-heap:** Push `(-amount, -userId, version)` records and keep current amounts in a dictionary. Updates avoid arbitrary heap deletion, but queries must discard stale records until the top matches current state. This is the method described by the manifest, not by the exact source.
- **Balanced search tree per item:** Any ordered multiset keyed by `(amount, userId)` supports the same eager insert, delete, and maximum operations. `SortedList` is the concrete Python choice here.
- **Scan all bids at query time:** Keeping only the nested dictionaries makes mutations expected $O(1)$, but finding one item's winner could take $O(Q)$. The ordered item index pays logarithmic mutation cost to make queries constant-time.
- **Replacing through addBid:** The old tuple must be removed before the new one is inserted; otherwise one user could have multiple active tuples for one item and a stale amount might win.
- **Equal highest amounts:** Tuple ordering places the larger `userId` later, so the required tie-break is automatic.
- **A user bidding on many items:** The inner user dictionary isolates each `itemId`. Updating one bid cannot disturb the same user's bids elsewhere.
- **Many users with identical amounts:** `(amount, userId)` tuples remain unique because a user can have only one active bid per item and user IDs distinguish the records.
- **Removing the final bid on an item:** Its `SortedList` becomes empty and later queries return -1, even though the empty item key remains stored.
- **Querying an unseen item:** `defaultdict` creates an empty list as a side effect, then the method returns -1. Repeated unseen-item queries can retain empty entries, but total retained entries remain $O(Q)$.
- **Updating to the same amount:** The source removes and reinserts the identical tuple. State remains correct, with logarithmic work.
- **Guaranteed-valid update and removal:** The source intentionally does not guard against missing pairs. The contract makes direct lookup and exact removal safe.
- **Largest numeric values:** Amounts up to $10^9$ compare exactly as Python integers; no arithmetic beyond ordering is needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q log Q)$. Let $B_i$ be the number of active bids on the item involved in a call, and let $Q$ be the total number of calls after construction. Expected dictionary access is $O(1)$.
- **Auxiliary Space Complexity:** $O(Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
