## General
**Group keys into ordered count buckets**

Maintain a doubly linked list of buckets in strictly increasing count order. Each bucket stores a set of keys sharing its count. Two sentinels represent the positions before the minimum and after the maximum, so retrieval reads any key from `head.next` or `tail.prev` directly.

**Find a key and its neighboring count in constant time**

A hash map sends each key to its current bucket. Incrementing needs only the next bucket, whose count must be current count plus one; decrementing needs only the previous bucket. If that adjacent count bucket is absent, create it between the two known neighbors.

**Move the key and remove empty buckets**

Insert the key into its destination set, update the hash map, and remove it from the old set. If the old bucket becomes empty, unlink it immediately. A decrement from count one deletes the key instead of creating a zero-count bucket.

**Why the endpoints always answer correctly**

Buckets are created only between consecutive neighbors at the moved key's new count, so their order remains strictly increasing. Empty buckets never remain. Therefore the first real bucket contains exactly all minimum-count keys and the last contains exactly all maximum-count keys; choosing any member satisfies the tie-permitting contract.

## Complexity detail
Hash lookups, set updates, adjacent-bucket insertion or removal, and endpoint access are average $O(1)$ for every operation. With `k` live keys, the key map, bucket memberships, and at most `k` nonempty buckets use $O(k)$ space.

## Alternatives and edge cases
- **Hash map plus full scan:** updates are constant time, but each minimum or maximum query takes $O(k)$.
- **Two heaps with lazy deletion:** supports extrema in $O(\log k)$ amortized time rather than the required constant time.
- **New key:** incrementing inserts it into count one, creating that bucket only when absent.
- **Count drops to zero:** remove the key entirely.
- **Tied extrema:** any member of the endpoint bucket is correct.
- **Empty structure:** both retrieval methods return the empty string.
