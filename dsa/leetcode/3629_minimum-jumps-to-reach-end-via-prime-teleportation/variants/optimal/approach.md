## General

**Model every permitted jump as an unweighted edge.** Each array index is a graph vertex. Adjacent indices share edges in both directions. When `nums[i]` is a prime $p$, index `i` also has an outgoing edge to every other index whose value is divisible by $p$. Because every operation costs one jump, breadth-first search discovers the minimum distance from index 0.

**Find teleport destinations without scanning the array repeatedly.** First use a sieve through $M$ to identify primes, and group indices by their exact array value. When breadth-first search processes a prime value $p$, enumerate the multiples $p, 2p, 3p, \ldots$ through $M$. Looking up each multiple in the value-to-indices map yields exactly the indices whose values are divisible by $p$.

**Expand each prime only once.** All indices carrying the same prime $p$ have the identical teleport destination set. The first such index removed from the breadth-first queue has the smallest possible distance among them, so its expansion assigns the earliest possible distance to every unvisited destination. Marking $p$ as used prevents later copies from repeating that work without suppressing any shorter route.

Adjacent neighbors and teleport destinations are enqueued only when first visited. Standard breadth-first ordering therefore ensures that the first discovery of the final index uses the minimum number of jumps.

## Complexity detail

Let $n$ be the array length and $M = \max(\texttt{nums})$. The sieve costs $O(M \log \log M)$ time. Across all expanded primes, enumerating numeric multiples costs $O(M \log \log M)$ in the worst case, while visiting indices through the prime factors of their values costs $O(n \log M)$. Total time is $O(M \log \log M + n \log M)$.

The primality table, distance array, queue, value-to-indices map, and stored indices use $O(M+n)$ auxiliary space.

The benchmark uses a cutoff $S$ and includes every prime at most $S$. The accepted lazy expansion follows the stated near-linear bound, while a correct breadth-first baseline that rescans all $n$ indices for each processed prime requires $O(n^2)$ time.

## Alternatives and edge cases

- **Scan all destinations from every prime index:** This constructs the right implicit edges but repeats an $O(n)$ divisibility scan and becomes quadratic.
- **Materialize every teleport adjacency list:** Precomputing explicit edges can consume unnecessary memory; lazy multiple expansion creates only the work reached by breadth-first search.
- **Factor every value first:** Associating indices with their distinct prime factors can achieve a similar bound, but only prime values present at a reached source can initiate teleportation.
- **Single element:** The start already equals the destination, so the answer is zero.
- **Composite current value:** It cannot initiate teleportation even when one of its prime factors divides another array value.
- **Repeated prime values:** Their outgoing teleport sets are identical and must be expanded only once.
- **Backward adjacent step:** It remains a valid graph edge and can participate in an optimal route after a teleport.
- **No useful teleport:** Adjacent steps always connect the array, so the destination is reachable.
