## General

**Sort items and queries so affordability grows monotonically**

The source sorts `items` lexicographically, making price the primary order. It also creates `(query_value, original_index)` pairs and sorts them by query value.

As query prices increase, every item affordable for an earlier query remains affordable. A single item pointer can therefore move forward without ever resetting.

**Preserve original query order with indices**

Sorting raw queries would lose their required output positions. `zip(queries, range(m))` pairs each query with its original index.

After processing sorted pair `(q,j)`, the source writes the answer into `ans[j]`. The returned array consequently matches the original query order even though computation occurs in sorted order.

**Maintain the best beauty among processed items**

Pointer `i` separates items already known affordable from items still too expensive for the current query. While `items[i][0] <= q`, the source updates

`mx = max(mx, items[i][1])`

and advances `i`.

After this loop, every item priced at most `q` has been processed, and no item with a larger price has been processed. `mx` is exactly the maximum beauty among affordable items.

**Return zero when nothing is affordable**

`mx` begins at zero. Item beauty values are positive, so it remains zero only while no item has passed the price condition.

Writing this value gives the required no-affordable-item answer without a separate branch.

**Why equal-price items are all included**

The while condition uses `<=` and continues through every item whose price equals the query.

Lexicographic sorting may order equal-price items by beauty, but `mx` examines them all before the answer is written. Their internal order cannot change the maximum.

**Trace increasing queries**

For items with price-beauty pairs `[1,2]`, `[2,4]`, and two price-three items, query one advances through only price one and records beauty two.

Query two continues from the existing pointer, adds price two, and raises the maximum to four. Query three adds every price-three item and records their combined running maximum. No cheaper item is rescanned.

**Why the sweep is correct**

Before writing a query answer, the pointer loop has included all and only items satisfying price at most `q`. The maintained maximum is therefore the required answer for that query.

Sorted processing does not change any query's affordability set. Original-index writes restore presentation order. Thus every output position receives its exact maximum.

The invariant before each sorted query is that `i` is the first item not yet processed and `mx` is the greatest beauty among all earlier items. The while loop extends that invariant until the first unprocessed item is too expensive for the current query. Because later queries are no smaller, none of the processed items ever needs to be removed.

Duplicate query values are processed consecutively. The first one advances through every item at that price; later duplicates perform no additional item work and receive the same maximum at their distinct original indices.

**Why each item is processed once**

The item pointer only increases. Although it is inside a loop over queries, its total increments across all queries are at most `n`.

This makes the sweep after sorting linear in items plus queries rather than their product.

**Exact implementation differs from the manifest description**

The manifest gives a bound consistent with sorting items and binary-searching each query. The protected source instead sorts indexed queries and performs a joint sweep.

Sorting queries costs $O(Q\log Q)$, not $O(Q\log N)$. It also materializes the sorted query-index pairs. The exact bounds must reflect this implementation.

**Mutation and allocation**

`items.sort()` changes the caller's item order in place. `queries` itself is not modified because sorting is applied to newly created zip tuples.

The answer list and sorted query tuples both have length `m`.

If original queries arrive in decreasing order, sorting reverses their computational order but not their result positions. This is precisely why the stored index is part of every tuple rather than relying on the loop position.

## Complexity detail

Let $N$ be the number of items and $Q$ the number of queries. Sorting items costs $O(N\log N)$. Sorting the query-index pairs costs $O(Q\log Q)$. The joint sweep costs $O(N+Q)$.

Total time is $O(N\log N+Q\log Q)$. The exact source materializes $O(Q)$ query tuples and an $O(Q)$ output list; Python sorting can additionally use linear temporary memory. Overall working/output storage is $O(N+Q)$ in a conservative bound, not the manifest's item-only $O(N)$ when $Q$ is independent.

## Alternatives and edge cases

- **Item prefix maxima plus binary search:** Sort items, store running beauty, and answer each query in $O(\log N)$.
- **Scan all items per query:** Costs $O(NQ)$ and repeats work.
- **No affordable item:** `mx` remains zero.
- **All items affordable:** Answer is the global maximum beauty.
- **Equal item prices:** Every tied item is consumed before answering that price.
- **Equal queries:** They receive the same `mx` and are restored to separate original positions.
- **Query between item prices:** Pointer stays at the last affordable item.
- **Positive beauty guarantee:** Makes zero an unambiguous absence result.
- **Original query order:** Restored through `ans[j]`.
- **Item mutation:** The item list is sorted in place.
- **Query preservation:** Only tuple copies are sorted.
- **Manifest mismatch:** Exact source sorts queries rather than binary-searching them.
