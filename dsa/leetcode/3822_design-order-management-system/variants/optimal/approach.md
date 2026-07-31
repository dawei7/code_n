## General

The system must support two directions of access. Modification and cancellation start from an `orderId`, while a lookup starts from an `(orderType, price)` pair. Keeping only one of those views would make the other operation scan all active orders.

Maintain two synchronized hash-based indexes:

- an order map from each active `orderId` to its `(orderType, price)` attributes;
- a bucket map from each `(orderType, price)` pair to the set of active IDs with exactly those attributes.

Adding an order inserts the same information into both indexes. To modify a price, use the order map to locate the old bucket, remove the ID from it, update the stored price, and insert the ID into the new bucket. If the price is unchanged, both indexes are already correct. Cancellation removes the order from its bucket and from the order map. Empty buckets can be deleted so storage continues to represent active orders only.

A lookup reads the requested bucket directly and materializes its IDs as a list. If the pair has no bucket, the result is empty. Because an ID is inserted into the bucket matching its current attributes, moved out of its former bucket on every real price change, and removed on cancellation, each bucket contains exactly the active orders with that type and price. The direct bucket lookup therefore returns all and only the required IDs.

## Complexity detail

Hash-map and hash-set operations take expected $O(1)$ time. Construction is $O(1)$. Each addition, modification, or cancellation therefore takes expected $O(1)$ time. A lookup returning $R$ IDs takes expected $O(R)$ time because the result list itself must contain those IDs.

Across $Q$ method calls whose lookup results contain $T$ IDs in total, the expected running time is $O(Q + T)$. The order map stores one record per active order, and the bucket sets collectively store each active ID exactly once, so space usage is $O(A)$.

The benchmark defines size as both the number of active orders inserted and the number of subsequent empty-result lookups. Direct bucket access keeps the trace linear in size, while scanning every active order for every lookup is quadratic.

## Alternatives and edge cases

- **Scan all active orders per lookup:** A single `orderId` map makes updates simple, but a lookup costs $O(A)$ and a query-heavy trace costs $O(QA)$.
- **Nested maps by type and price:** This is equivalent to a hash map keyed by `(orderType, price)`; either representation is valid when it retains a set of IDs at the final bucket.
- **Price modification:** Remove the ID from its old bucket before adding it to the new one, or a later lookup can return the same active order at two prices.
- **Unchanged price:** Leaving both indexes untouched is valid and avoids deleting and recreating the same bucket.
- **Order type is immutable:** `modifyOrder` changes only the price, so the order must remain under its original `"buy"` or `"sell"` type.
- **Cancellation:** Remove the ID from both indexes; deleting it only from the order map would leave a canceled order visible in bucket queries.
- **Last ID in a bucket:** Removing the empty bucket is optional for correctness, but prevents stale empty keys from accumulating.
- **No matching pair:** Read without creating a new bucket and return `[]`.
- **Arbitrary result order:** A set naturally has no required output order, which agrees with the source contract.
