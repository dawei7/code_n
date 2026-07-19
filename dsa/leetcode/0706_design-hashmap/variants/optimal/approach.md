## General
**Hash each key to one collision chain**

Allocate `B` list buckets and select `key % B`. Store each mapping as a two-item `[key, value]` entry in that bucket, allowing different keys with the same hash to coexist.

**Make put update or append**

Scan the chosen bucket for the key. If found, replace that entry's value and return; otherwise append a new mapping. This maintains exactly one current value per stored key.

**Share the same lookup for get and remove**

Getting returns the matching entry's value or `-1` after the bucket is exhausted. Removing deletes the matching entry if present and otherwise changes nothing.

**Why bucket-local search is complete**

The deterministic modulo function always maps the same key to the same bucket, so its mapping cannot legally reside elsewhere. The uniqueness rule within that bucket makes a found entry authoritative, and exhausting the chain proves absence.

## Complexity detail
With well-distributed keys, a bucket has expected constant length, so `q` operations take expected $O(q)$ time. The bucket headers and `U` stored mappings use $O(U + B)$ space. If adversarial keys all collide, one operation can take $O(U)$.

## Alternatives and edge cases
- **Direct-address array:** store a value at every possible key index and reserve `-1` for absence; operations are worst-case $O(1)$ but memory covers the full domain.
- **Resizable chaining table:** rehash into more buckets as the load factor grows; it controls expected chain length for unbounded use.
- **Flat association list:** keep all key/value pairs together and scan for every operation; it is correct but can take $O(q^2)$ total time.
- Putting an existing key changes its value without creating another entry.
- Values may be zero, so absence must use the specified `-1` result.
- Removing an absent key leaves all mappings unchanged.
- Colliding keys must retain independent values and removal behavior.
