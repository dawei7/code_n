## General
**Map every key to one bucket**

Allocate `B` list buckets and use `key % B` as the hash function. All operations on a key inspect only that bucket, and different keys with the same remainder coexist in its collision chain.

**Preserve set semantics inside a chain**

Before adding, scan the bucket and append only if the key is absent. Membership performs the same scan and returns whether it finds equality. Removal locates the key's position and deletes exactly that entry; finding nothing leaves the structure unchanged.

**Adapt the native design interface locally**

The native platform constructs `MyHashSet` and calls one method at a time. The app-local `solve` function drives the same object behavior over the authored operation list and records only membership-query results.

**Why each operation is correct**

The modulo function always sends a given key to the same bucket. No other bucket can hold that key, while the duplicate check ensures its own bucket contains at most one copy. Therefore the bucket scan exactly represents membership, and add or remove changes that truth value as specified.

## Complexity detail
With a well-distributed hash function, the expected chain length is constant, so `q` operations take expected $O(q)$ time. The `B` bucket headers and `U` stored unique keys use $O(U + B)$ space. A deliberately adversarial collision pattern can make one operation $O(U)$.

## Alternatives and edge cases
- **Direct-address table:** one Boolean slot per possible key gives worst-case $O(1)$ operations but reserves memory for the complete key domain.
- **Resizable chaining table:** grow and rehash when the load factor rises; it improves distribution for unbounded workloads at the cost of more implementation detail.
- **Flat list:** store every key together and scan it for each operation; it is correct but can take $O(q^2)$ total time.
- Adding an existing key must not create a duplicate.
- Removing an absent key must leave every stored key unchanged.
- Distinct keys that hash to the same bucket must remain independently addressable.
- Boundary keys such as zero use the same hash and chain rules.
