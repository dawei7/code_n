# Guided Example: Design Order Management System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"], "arguments": [[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]}`
- **Required output:** `[null, null, null, null, [2, 1], null, null, [2], null, null, []]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are asked to design a simple order management system for a trading platform.

The objective is to compute `[null, null, null, null, [2, 1], null, null, [2], null, null, []]` from `{"operations": ["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"], "arguments": [[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Index the same active order in two directions

Each method needs one of two access patterns.

`modifyOrder` and `cancelOrder` receive only an `orderId`, so the system must quickly recover that order's type and current price. `getOrdersAtPrice` receives a type and price, so it must quickly find all active IDs in that category.

The source maintains two synchronized dictionaries:

- `orders[orderId] = (orderType, price)` stores the authoritative current attributes of every active order;
- `t[(orderType, price)]` is a list containing the active order IDs currently assigned to that exact type-price bucket.

An order appears once in `orders` and once in exactly one bucket list while active. A canceled order appears in neither active representation. Maintaining this relationship is the central requirement behind every mutation.

The bucket key must include both fields. A buy order at price 10 cannot be returned for a sell query at price 10, and a buy order at another price cannot be returned either. The tuple `(orderType, price)` identifies the complete query category.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"], "arguments": [[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Add a globally unique order

`addOrder` writes the type and price under the new ID, then appends that ID to the corresponding bucket:

`orders[orderId] = (orderType, price)`

`t[(orderType, price)].append(orderId)`

The contract guarantees that `orderId` is globally unique, so the source does not need to check for or remove an older record. `t` is a `defaultdict(list)`; accessing a new key automatically creates an empty list before `append`.

After these two writes, lookup by ID can recover the order, and lookup by type and price can return it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Modify the price while preserving the type

`modifyOrder` is given only an ID and a new price. It first reads

`orderType, price = orders[orderId]`

to recover both the unchanged type and the old bucket location. The contract says modification changes only price, so `orderType` is carried forward.

The authoritative mapping is replaced with `(orderType, newPrice)`. The ID is removed from the old bucket using

`t[(orderType, price)].remove(orderId)`

and appended to the new bucket.

All three state changes are needed. Updating only `orders` would leave the old query bucket stale. Adding to the new bucket without removing from the old one would make the same active order appear at two prices. Removing from the old bucket without appending to the new one would make price queries unable to find an otherwise active order.

If `newPrice == price`, the old and new bucket keys are identical. The source removes the ID and appends it back to that same list. This may move the ID to the list's end, but result ordering is explicitly irrelevant, so behavior remains correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, null, [2, 1], null, null, [2], null, null, []]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["OrderManagementSystem", "addOrder", "addOrder", "addOrder", "getOrdersAtPrice", "modifyOrder", "modifyOrder", "getOrdersAtPrice", "cancelOrder", "cancelOrder", "getOrdersAtPrice"], "arguments": [[], [1, "buy", 1], [2, "buy", 1], [3, "sell", 2], ["buy", 1], [1, 3], [2, 1], ["buy", 1], [3], [2], ["buy", 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, null, [2, 1], null, null, [2], null, null, []]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use a set per bucket:** Replacing each list with a hash set gives expected $O(1)$ addition, modification removal, and cancellation. A query converts the set to a list in $O(R)$ time, matching the manifest's intended $O(Q+T)$ aggregate bound.
- **Return a defensive copy:** `list(t.get(key, ()))` prevents callers from mutating internal state and avoids creating an empty key for a missing query. It costs $O(R)$, which is already proportional to the returned data.
- **Delete empty buckets:** After removal, deleting a key whose container is empty keeps storage tied more closely to active state. Using `dict.get` for queries then avoids reintroducing empty keys.
- **Unique order IDs:** The guarantee prevents one ID from appearing as two different active orders and makes `list.remove(orderId)` unambiguous within its bucket.
- **Modify to the same price:** Removing and appending within the same list preserves membership; only irrelevant output order may change.
- **Modify preserves order type:** The source recovers `orderType` from `orders` and never accepts a replacement type parameter.
- **Cancel the last order in a bucket:** The bucket becomes an empty retained list, and subsequent queries correctly return an empty result.
- **Query an unseen type-price pair:** `defaultdict` creates an empty bucket as a side effect and returns it.
- **Many orders in one bucket:** Functional behavior remains correct, but list removal becomes linear in the number of those orders and exposes the source's worst-case complexity.
- **Returned order is unspecified:** The source can return insertion order, and same-price modification can move an ID to the end. Both are valid because the contract imposes no ordering.
- **Guaranteed active mutation targets:** Invalid repeated cancellation or modification of a canceled ID may raise an exception, but such calls are excluded by the contract.
- **Large prices:** Prices are used only as dictionary-key integers, so values up to $10^9$ require no special arithmetic handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q + T)$. Let $A$ be the maximum number of simultaneously active orders, $B$ the size of the affected old bucket, $K$ the number of distinct type-price keys ever touched or queried, and $T$ the total number of IDs contained in all query responses.
- **Auxiliary Space Complexity:** $O(A+K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
