## General

**Maintain the order needed by each read operation.** `search(movie)` needs available copies of one movie ordered by price then shop. `report()` needs all rented copies ordered by price, shop, then movie. The system keeps two ordered indexes matching these two query shapes so neither operation must sort the entire inventory on demand.

**Store immutable prices separately.** `price_map` maps a combined shop/movie key to the fixed rental price. Method `f(shop, movie)` computes `shop << 30 | movie`. Shifting reserves 30 low bits for movie; constraints keep movie far below $2^{30}$, so different permitted pairs cannot collide. Rent and drop can recover price in constant expected map time without searching an ordered collection.

The constructor parameter `n` is not otherwise needed because entries explicitly describe every carried copy and shops are already validated by the contract.

**Index available copies per movie.** `available` is a `defaultdict` whose values are `SortedList` objects. Each entry `(price, shop)` sorts lexicographically: cheaper price first, then smaller shop for ties. During construction, every copy begins unrented and is added to its movie's list.

`search(movie)` takes slice `[:5]` from that ordered list and extracts shops. If fewer than five exist, slicing returns all; if none exist, accessing the default dictionary creates an empty sorted list and returns an empty answer. The slice is already in required order.

**Index rented copies globally.** `rented` is one `SortedList` of triples `(price, shop, movie)`. Lexicographic tuple order exactly matches report priority: price, then shop, then movie. `report()` reads its first five triples and returns only `[shop, movie]` from each.

**Move one copy between indexes on rent.** The contract guarantees `rent` is called only for an available copy. Price lookup identifies exact tuple `(price, shop)`, which is removed from that movie's available list. Triple `(price, shop, movie)` is added to the rented list. The copy now appears in exactly one availability state.

**Reverse the move on drop.** Valid calls guarantee the triple is rented. `drop` removes it from the global rented list and adds its pair back to the appropriate available movie list. Price never changes, so restored search ordering is automatic.

**Maintain a partition invariant.** After construction, every catalog copy is in its per-movie available list and none is rented. Rent and drop each remove one exact tuple from one side before adding it to the other. Therefore each copy is represented exactly once across the availability states, and price-map identity remains permanent.

**Trace the example's ordering.** Movie one copies include price four at shop one and price five at shops zero and two. Their tuples sort as `(4,1), (5,0), (5,2)`, so search returns `[1,0,2]`. Renting shop zero removes `(5,0)` from that list and adds `(5,0,1)` globally. Renting movie two at shop one adds `(7,1,2)`. Report orders price five before seven and returns `[[0,1],[1,2]]`.

**Why exact tuple removal is safe.** Each shop carries at most one copy of a given movie, and price is fixed. Thus `(price, shop)` uniquely represents a copy within a movie list, while `(price, shop,movie)` uniquely represents it globally. The validity guarantees mean `SortedList.remove` always finds its target.

**Library behavior is part of this source.** `SortedList` is not a built-in list. It maintains sorted order during insertion and deletion, supporting ordered prefix reads without resorting. A normal list would not provide the same operation costs.

## Complexity detail

Let $E$ be the number of entries and $Q$ the number of calls. Each constructor insertion into a movie's ordered list costs logarithmic time in that list's size, giving $O(E\log E)$ as a broad bound. Each rent or drop performs ordered removal and insertion in $O(\log E)$ plus expected $O(1)$ price lookup.

Search and report copy at most five tuples, so their result work is $O(1)$ after locating the relevant list; dictionary lookup is expected constant and ordered slicing of five elements is bounded. The manifest summarizes the full sequence as $O(E\log E+Q\log(E+Q))$, a safe broad bound.

Catalog tuples and price entries use $O(E)$ storage. Searching previously unseen movie IDs through the `defaultdict` can create empty lists, adding up to $O(Q)$ keys over many calls. Thus exact long-lived space can be $O(E+Q)$, matching the manifest.

## Alternatives and edge cases

- **Heaps with lazy deletion:** Per-movie and global heaps can return cheapest entries, but rent/drop state changes require stale-entry filtering and careful synchronization.
- **Sort on every search/report:** Correct but can repeatedly cost $O(E\log E)$ rather than maintaining order incrementally.
- **Ordinary sets:** Support membership changes but not cheapest-five ordering.
- **Fewer than five matches:** Slicing naturally returns the available count without padding.
- **No available or rented copies:** Empty sorted-list slices produce empty results.
- **Equal prices:** Tuple fields apply the exact shop and then movie tie breakers.
- **Repeated state changes:** A dropped copy re-enters with its original price and correct sorted position.
- **Search for unknown movie:** The default dictionary returns an empty list but also stores that empty key, explaining possible $O(Q)$ extra space.
- **Composite-key safety:** The low 30 bits are sufficient for every allowed movie ID; changing constraints beyond that range would require tuple keys or a wider reservation.
- **Valid-operation guarantee:** The source uses strict `remove` rather than defensive discard. Invalid rent/drop calls would raise, but tests exclude them.
