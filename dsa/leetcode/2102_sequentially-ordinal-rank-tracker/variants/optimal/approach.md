## General
**Partitioning around the current query rank**

After $q$ calls to `get`, maintain two heaps. The first contains exactly the best $q$ locations and exposes the worst member of that prefix. The second contains every remaining location and exposes its best member.

The ranking key is higher score first and, for equal scores, smaller name first. The two heap roots deliberately use opposite orientations: “worst of the best” means lower score or lexicographically larger name, while “best of the rest” means higher score or lexicographically smaller name.

**Adding while preserving the partition**

Insert a new location into the remaining heap. If no query has occurred, nothing else is needed. Otherwise compare the best remaining location with the worst prefix location. When the remaining candidate ranks better, exchange the two heap roots.

Only one exchange can be necessary: before the addition, every prefix member ranked ahead of every remaining member. A single new element is the only possible violation, and swapping it across the boundary restores the ordered partition without changing the prefix size.

**Advancing the sequential rank**

On `get`, remove the best location from the remaining heap and insert it into the prefix heap. The prefix size grows from $q$ to $q+1$, so its worst member is now precisely the $(q+1)$th best location. Return that root's name.

The invariant proves each answer. The prefix always consists of exactly the globally best locations whose count equals the number of queries. Its worst member therefore has the requested ordinal rank, even when additions between queries change which locations belong to the prefix.

## Complexity detail
Each `add` performs a constant number of heap pushes and pops, and each `get` performs one pop and one push. With $m$ stored locations, every operation takes $O(\log m)$ time. The two heaps contain each location exactly once and therefore use $O(m)$ space.

## Alternatives and edge cases
- **Balanced ordered set with an iterator:** In languages with order-statistic-friendly tree containers, maintain the ranking and move an iterator one step on each query. Insertions and queries can be handled in $O(\log m)$ time.
- **Sort on every query:** Store all locations and re-sort whenever `get` is called. This is correct but can require quadratic-logarithmic total work over a long stream.
- **Single heap:** One heap exposes only one extreme and cannot directly track an ordinal that advances while better items may be inserted; the two-sided partition supplies the movable boundary.
- Equal scores are resolved solely by lexicographic name order.
- Names are unique, so ranking keys never tie completely.
- Several `get` calls may occur consecutively; each moves one more location into the requested prefix.
- A high-scoring location added after earlier queries may cross into the prefix and displace its previous worst member.
- The prefix guarantee on operation counts ensures the remaining heap is nonempty whenever `get` is called.
