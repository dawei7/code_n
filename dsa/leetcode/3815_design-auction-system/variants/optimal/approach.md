## General

**Maintain the same active bid in two complementary indexes**

The system must support two different kinds of access:

- addition, replacement, update, and removal identify one bid by `(userId, itemId)`;
- a highest-bidder query must rank every active bid for one `itemId`.

One data structure is not naturally optimal for both. The source therefore stores each active bid in two synchronized views.

`self.users` is a regular dictionary whose outer key is `userId`. Each value is another dictionary mapping `itemId` to the current `bidAmount`. Thus `self.users[userId][itemId]` is the authoritative amount for one exact bid and can be found in expected $O(1)$ time.

`self.items` maps each `itemId` to a `SortedList` of tuples `(bidAmount, userId)`. This view groups all bids competing for the same item and keeps them ordered. Python tuple ordering compares the amount first and, when amounts tie, compares the user identifier. Therefore, the last tuple in the list has the greatest bid amount and, among equal greatest amounts, the greatest user ID—exactly the query's priority.

The central consistency rule is:

> For every active bid `self.users[u][item] = amount`, `self.items[item]` contains exactly one tuple `(amount, u)`, and there are no other tuples representing that user-item pair.

Every mutating method preserves this rule.

**Adding a new bid or replacing an old one**

`addBid` first ensures that the user has an inner dictionary. If `userId` has never appeared, `self.users[userId] = {}` creates it.

The method then checks whether `itemId` is already in that user's dictionary. The contract says another `addBid` for the same user-item pair replaces the old amount; it does not create a second bid. The source implements replacement by calling `removeBid(userId, itemId)` first. That removes both the old sorted tuple and the old dictionary entry.

After any old version is gone, the new amount is written into the user lookup and `(bidAmount, userId)` is inserted into the item's ordered list. The two indexes again describe exactly the same active bid.

The order of these steps prevents stale duplicates. If user 5 changes an item-9 bid from 100 to 130 through `addBid`, the list does not retain both `(100, 5)` and `(130, 5)`. Only the latter remains eligible to win.

**Updating an existing bid eagerly**

`updateBid` is guaranteed to receive an existing pair. It reads `oldAmount` directly from `self.users[userId][itemId]`. That amount identifies the exact tuple `(oldAmount, userId)` stored for the item.

The old tuple is removed from `self.items[itemId]`, the new tuple `(newAmount, userId)` is added, and the dictionary amount is replaced. Removing before adding is important even when the amount changes downward: the ordered item view must reflect current bids only. If `newAmount` equals `oldAmount`, removing and reinserting the same tuple is unnecessary work but remains correct.

This is an eager-update design. There are no stale heap records and no version timestamps to validate during a query. At all times, the ordered list itself is an exact representation of the live auction.

**Removing an existing bid**

`removeBid` also uses the authoritative user lookup to recover the old amount. It removes `(oldAmount, userId)` from the corresponding ordered list and then removes `itemId` from the user's inner dictionary with `pop`.

The source does not delete an outer user key after that user's last bid disappears, and it does not delete an item key after its list becomes empty. Those empty containers do not affect behavior. They can occupy space for previously seen users and items, but there are at most as many such keys as operations.

Because removal is guaranteed valid, direct indexing and `SortedList.remove` are appropriate. There is no need for a missing-bid branch; calling the method outside the contract could raise an exception.

**Answer the priority query from the ordered endpoint**

`getHighestBidder` obtains `ls = self.items[itemId]`. Since `items` is a `defaultdict(SortedList)`, querying an unseen item creates and stores an empty ordered list. If `ls` is empty, the method returns -1.

Otherwise, `ls[-1]` is the lexicographically greatest `(bidAmount, userId)` tuple. Its second component, `ls[-1][1]`, is the requested user ID.

Suppose an item has bids `(80, 4)`, `(100, 2)`, and `(100, 9)`. Sorted order places `(100, 9)` last: amount 100 beats 80, and user 9 beats user 2 within the amount tie. The method returns 9 without scanning the item or writing an explicit tie branch.

**Follow the example as synchronized state changes**

After users 1 and 2 bid 5 and 6 on item 7, the user view contains amounts under both users, while `self.items[7]` contains `[(5, 1), (6, 2)]`. Its final tuple selects user 2.

Updating user 1 to amount 8 removes `(5, 1)` and inserts `(8, 1)`. The list becomes `[(6, 2), (8, 1)]`, so user 1 wins. Removing user 2 deletes `(6, 2)` from the item view and item 7 from user 2's inner mapping. The remaining final tuple still selects user 1. Querying item 3 creates an empty list and returns -1.

**The exact source is not the lazy-heap method named by the manifest**

The manifest summary says the solution uses an authoritative hash map and “one lazy max-heap per item.” That description does not match this implementation. There is no heap, no negated priority, no stale record, and no cleanup loop during `getHighestBidder`.

The source uses `SortedList` and eagerly deletes every superseded or removed tuple. The nested user dictionaries are used to locate exact old amounts, while item lists remain fully current. The documented approach must describe this actual ordered-multiset design. The manifest's $O(Q\log Q)$ total-time and $O(Q)$ space bounds still fit the source, even though its data-structure summary is wrong.

## Complexity detail

Let $B_i$ be the number of active bids on the item involved in a call, and let $Q$ be the total number of calls after construction. Expected dictionary access is $O(1)$.

`SortedList.add`, `remove`, and `discard` are treated as $O(\log B_i)$ ordered-container operations. A new `addBid` performs one insertion; a replacing `addBid` performs one removal and one insertion. `updateBid` also performs one removal and one insertion. `removeBid` performs one ordered removal. Each is therefore $O(\log B_i)$, bounded by $O(\log Q)$.

`getHighestBidder` checks emptiness and reads the final list element, so it is $O(1)$ after the dictionary access. Construction is $O(1)$. Across $Q$ arbitrary calls, the worst-case total is $O(Q\log Q)$.

There is one user-dictionary entry and one ordered tuple per active bid. Empty outer user dictionaries and empty item lists may remain for previously used identifiers, including unseen items queried through the `defaultdict`. Across $Q$ calls, all active records and retained keys occupy $O(Q)$ space.

The source assumes `defaultdict` and `SortedList` are available from the execution environment. `SortedList` is not part of Python's built-in collection types.

## Alternatives and edge cases

- **Hash map plus lazy max-heap:** Push `(-amount, -userId, version)` records and keep current amounts in a dictionary. Updates avoid arbitrary heap deletion, but queries must discard stale records until the top matches current state. This is the method described by the manifest, not by the exact source.
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
