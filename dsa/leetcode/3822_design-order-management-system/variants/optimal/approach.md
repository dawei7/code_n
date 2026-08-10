## General

**Index the same active order in two directions**

Each method needs one of two access patterns.

`modifyOrder` and `cancelOrder` receive only an `orderId`, so the system must quickly recover that order's type and current price. `getOrdersAtPrice` receives a type and price, so it must quickly find all active IDs in that category.

The source maintains two synchronized dictionaries:

- `self.orders[orderId] = (orderType, price)` stores the authoritative current attributes of every active order;
- `self.t[(orderType, price)]` is a list containing the active order IDs currently assigned to that exact type-price bucket.

An order appears once in `self.orders` and once in exactly one bucket list while active. A canceled order appears in neither active representation. Maintaining this relationship is the central requirement behind every mutation.

The bucket key must include both fields. A buy order at price 10 cannot be returned for a sell query at price 10, and a buy order at another price cannot be returned either. The tuple `(orderType, price)` identifies the complete query category.

**Add a globally unique order**

`addOrder` writes the type and price under the new ID, then appends that ID to the corresponding bucket:

`self.orders[orderId] = (orderType, price)`

`self.t[(orderType, price)].append(orderId)`

The contract guarantees that `orderId` is globally unique, so the source does not need to check for or remove an older record. `self.t` is a `defaultdict(list)`; accessing a new key automatically creates an empty list before `append`.

After these two writes, lookup by ID can recover the order, and lookup by type and price can return it.

**Modify the price while preserving the type**

`modifyOrder` is given only an ID and a new price. It first reads

`orderType, price = self.orders[orderId]`

to recover both the unchanged type and the old bucket location. The contract says modification changes only price, so `orderType` is carried forward.

The authoritative mapping is replaced with `(orderType, newPrice)`. The ID is removed from the old bucket using

`self.t[(orderType, price)].remove(orderId)`

and appended to the new bucket.

All three state changes are needed. Updating only `self.orders` would leave the old query bucket stale. Adding to the new bucket without removing from the old one would make the same active order appear at two prices. Removing from the old bucket without appending to the new one would make price queries unable to find an otherwise active order.

If `newPrice == price`, the old and new bucket keys are identical. The source removes the ID and appends it back to that same list. This may move the ID to the list's end, but result ordering is explicitly irrelevant, so behavior remains correct.

**Cancel an active order**

`cancelOrder` again uses `self.orders[orderId]` to find the current type and price. It deletes the authoritative entry and removes the ID from that exact bucket list.

The operation is guaranteed to refer to an existing active order. Therefore direct dictionary access and `list.remove` are safe under valid input; no missing-order branch is needed.

The source leaves an empty list in `self.t` when the canceled order was the bucket's last member. That empty bucket correctly produces an empty query result later, although retaining it affects the precise space analysis.

**Return the matching bucket**

`getOrdersAtPrice` directly returns

`self.t[(orderType, price)]`.

If the key already exists, this is the current list of active matching IDs. If the key has never appeared, `defaultdict` creates an empty list and returns it. Thus a missing category naturally produces `[]`.

The list's order is insertion history, possibly altered by remove-and-append modifications. The contract says order does not matter, so no sorting is required.

For the example, adding orders 1 and 2 as buys at price 1 creates a bucket containing both IDs. Modifying order 1 to price 3 removes it from the price-1 list and appends it under price 3. Modifying order 2 to the same price removes and re-appends it to price 1, leaving it as that bucket's sole member. Canceling order 2 removes the final ID, so the next price-1 query returns the retained empty list.

**Why the two structures remain synchronized**

Construction begins with no active orders in either structure. Addition inserts the new order into both views. Modification removes its one old bucket occurrence, changes the authoritative attributes, and inserts one new bucket occurrence. Cancellation removes its records from both views.

By induction over the operation sequence, every active order is found under its current type and price, every listed bucket ID has a matching authoritative order, and no canceled ID remains in a nonempty bucket. A query therefore returns precisely the active orders matching its key.

**The exact source uses lists, not the sets claimed by the manifest**

The manifest summary says the method maintains “a set of active IDs for every order-type/price pair.” The executable source instead uses `defaultdict(list)`. This difference materially changes complexity.

Appending to a list is amortized constant time, but `list.remove(orderId)` scans from the beginning until it finds the ID. Removing from a bucket of size $B$ can take $O(B)$ time. The manifest's aggregate $O(Q+T)$ time would fit hash sets with expected constant-time removal, but it does not describe the exact list-based implementation.

There is another source-level detail: `getOrdersAtPrice` returns the internal mutable list itself, not a copy. The platform adapter reads the result and does not mutate it, so standard operation sequences remain correct. In a general-purpose API, a caller could modify the returned list and corrupt internal state; returning `list(bucket)` would provide defensive isolation at the unavoidable $O(R)$ cost for $R$ returned IDs.

## Complexity detail

Let $A$ be the maximum number of simultaneously active orders, $B$ the size of the affected old bucket, $K$ the number of distinct type-price keys ever touched or queried, and $T$ the total number of IDs contained in all query responses.

`addOrder` uses expected $O(1)$ dictionary work and amortized $O(1)$ append time. `modifyOrder` and `cancelOrder` each call `list.remove`, costing $O(B)$ in the worst case, followed by expected or amortized constant-time dictionary and append operations. Since $B\le A$, either mutation can cost $O(A)$.

The method body of `getOrdersAtPrice` returns a list reference in expected $O(1)$ time. Producing or serializing the observable response still requires $O(R)$ work for its $R$ IDs, contributing $O(T)$ across queries.

Across $Q$ calls, a faithful worst-case end-to-end bound is $O(QA+T)$, or more precisely $O(Q+T+\sum B_r)$ over all list removals. This contradicts the manifest's $O(Q+T)$ claim for the exact source. With the stated maximum of 2000 calls, the implementation may still be practically accepted, but it is not the claimed set-based asymptotic design.

Active entries in `self.orders` and across all nonempty bucket lists total $O(A)$. However, empty bucket lists are never deleted, and querying an unseen key creates another empty entry. Hence dictionary-key storage is $O(K)$, where $K\le Q$. Exact source space is $O(A+K)$ and can be $O(Q)$ even when $A$ stays small. The manifest's $O(A)$ bound would require deleting empty keys and avoiding creation on missing queries.

## Alternatives and edge cases

- **Use a set per bucket:** Replacing each list with a hash set gives expected $O(1)$ addition, modification removal, and cancellation. A query converts the set to a list in $O(R)$ time, matching the manifest's intended $O(Q+T)$ aggregate bound.
- **Return a defensive copy:** `list(self.t.get(key, ()))` prevents callers from mutating internal state and avoids creating an empty key for a missing query. It costs $O(R)$, which is already proportional to the returned data.
- **Delete empty buckets:** After removal, deleting a key whose container is empty keeps storage tied more closely to active state. Using `dict.get` for queries then avoids reintroducing empty keys.
- **Unique order IDs:** The guarantee prevents one ID from appearing as two different active orders and makes `list.remove(orderId)` unambiguous within its bucket.
- **Modify to the same price:** Removing and appending within the same list preserves membership; only irrelevant output order may change.
- **Modify preserves order type:** The source recovers `orderType` from `self.orders` and never accepts a replacement type parameter.
- **Cancel the last order in a bucket:** The bucket becomes an empty retained list, and subsequent queries correctly return an empty result.
- **Query an unseen type-price pair:** `defaultdict` creates an empty bucket as a side effect and returns it.
- **Many orders in one bucket:** Functional behavior remains correct, but list removal becomes linear in the number of those orders and exposes the source's worst-case complexity.
- **Returned order is unspecified:** The source can return insertion order, and same-price modification can move an ID to the end. Both are valid because the contract imposes no ordering.
- **Guaranteed active mutation targets:** Invalid repeated cancellation or modification of a canceled ID may raise an exception, but such calls are excluded by the contract.
- **Large prices:** Prices are used only as dictionary-key integers, so values up to $10^9$ require no special arithmetic handling.
