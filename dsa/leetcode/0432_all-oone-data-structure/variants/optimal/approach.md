## General

**Why a hash map alone is not enough**

A map from key to count supports increment and decrement quickly, but finding the minimum or maximum count would require scanning every key. A sorted tree of counts could retrieve extremes quickly, but moving keys would cost logarithmic time. The required average $O(1)$ operations need two coordinated structures:

- a hash map `nodes` that locates the bucket containing any key; and
- a doubly linked list of count buckets kept in strictly increasing count order.

Each real bucket stores one `cnt` value and a set of every key currently having that count. Keys with equal counts share a bucket. Because updates change a count by exactly one, a key can only move to the immediately neighboring count, which can be found or created beside its current bucket in constant time.

**The central invariants**

After every public operation:

- real buckets are ordered by increasing `cnt`;
- there is at most one real bucket for each count;
- every real bucket's `keys` set is nonempty;
- every stored key appears in exactly one bucket; and
- `nodes[key]` points to that bucket.

These invariants make the first real bucket the minimum-count bucket and the last real bucket the maximum-count bucket.

**A circular sentinel removes endpoint special cases**

`root = Node()` is a sentinel whose `next` and `prev` initially point back to itself. The real bucket list lives between `root.next` and `root.prev` around this circle.

The sentinel's constructor creates `keys = {''}`. This dummy empty-string key is never placed in `nodes` and is not a real stored key. It has one useful consequence: when the structure is empty, both minimum and maximum retrieval iterate the sentinel's key set and return `""` naturally, without a branch.

Real keys are nonempty lowercase strings, so they cannot collide with this sentinel value.

**Constant-time bucket insertion and removal**

`some_node.insert(new_node)` places `new_node` immediately after `some_node`. It sets the new node's two pointers, then redirects both neighboring reciprocal pointers. It returns the inserted node, which is convenient for assigning `nodes[key]`.

`node.remove()` bypasses a bucket by connecting its predecessor directly to its successor in both directions. A real bucket is removed only after its key set becomes empty, preserving the no-empty-real-bucket invariant.

Neither helper traverses the list.

**Increment a new key**

If `key not in nodes`, its new count is one. The smallest real bucket is `root.next`.

If the list is empty or that bucket's count is greater than one, no count-one bucket exists. `root.insert(Node(key, 1))` creates it at the front. Otherwise the first bucket must already have count one, so the key is added to its set.

In both cases, `nodes[key]` is updated to the count-one bucket. The ordering invariant holds because no positive count can precede one.

**Increment an existing key**

Let `curr = nodes[key]`. The destination count is `curr.cnt + 1`, so only `curr.next` can possibly be the destination bucket.

If `curr.next` is the sentinel or its count is greater than the destination, that count bucket is absent. The code inserts a new bucket immediately after `curr`. Otherwise, sorted unique buckets imply the next count equals `curr.cnt + 1`, and the key joins its existing set.

The map is redirected to the destination. Then the key is discarded from `curr.keys`; if that set is empty, `curr.remove()` deletes the obsolete bucket.

The code chooses the destination before deleting an empty current bucket, so it always has a stable insertion position.

**Decrement a key**

The contract guarantees the key exists, so `curr = nodes[key]` is safe.

If `curr.cnt == 1`, decrementing makes the key's count zero. It is removed from `nodes` and is not placed in another bucket.

For a larger count, the destination is `curr.cnt - 1`, and only `curr.prev` can contain it. If the predecessor is the sentinel or has a smaller count than the destination, the desired bucket is missing; `prev.insert(...)` creates it immediately before `curr`. Otherwise the predecessor's count must equal the destination, so the key joins that set.

After redirecting the map, the key is removed from `curr`, and an empty current bucket is unlinked.

**Retrieve extrema without searching**

`root.prev` is the greatest-count real bucket when keys exist, and `root.next` is the least-count bucket. `next(iter(bucket.keys))` returns an arbitrary member of the appropriate set, exactly as the contract permits when several keys tie.

When empty, both neighbors are `root`; iterating `root.keys` returns the sentinel's `""`, producing the required empty result.

**Why all invariants are preserved**

New keys enter count one at the front. Existing keys move exactly one count left or right, joining the adjacent matching bucket or creating the missing bucket in the only sorted position. The key map is updated on every move/removal. Removing empty source buckets prevents duplicates of count positions and leaves no empty real nodes.

By induction over operations, the bucket order and map/set partition remain correct. Extremal retrieval is therefore correct at all times.

## Complexity detail

Hash-map lookup/update, set insertion/removal, and obtaining an arbitrary set iterator element are average $O(1)$ operations. Each update examines at most one adjacent bucket and changes a constant number of pointers. Thus `inc`, `dec`, `getMaxKey`, and `getMinKey` all run in average $O(1)$ time.

Worst-case hash behavior can degrade map/set operations, which is why the contract and manifest use average complexity.

Let $k$ be the number of currently stored distinct keys. The map stores $k$ entries, bucket key sets collectively store exactly $k$ real keys, and there can be at most $k$ nonempty real buckets. Total space is $O(k)$.

## Alternatives and edge cases

- **Map only:** Updates are constant average time, but each min/max query requires an $O(k)$ scan.
- **Balanced search tree keyed by count:** Extremes are easy, but moving a key between counts costs $O(\log k)$.
- **Heap for minimum and maximum:** Count changes leave stale heap entries or require indexed deletion; cleanup can complicate the strict per-operation goal.
- **One linked-list node per key:** Moving individual keys cannot find the correct count position in constant time. Grouping equal counts into buckets is essential.
- **First increment:** The circular list is empty, so a count-one bucket is inserted between the sentinel and itself.
- **Decrement from one:** The key disappears completely rather than entering a zero-count bucket.
- **Last key removed from a bucket:** The bucket is unlinked immediately, keeping extrema on nonempty buckets.
- **Several tied keys:** Retrieval may return any set member; deterministic ordering is neither required nor provided.
- **Completely empty structure:** Sentinel key `""` makes both retrieval methods return the required empty string without special branching.
- **Gaps between counts:** Missing adjacent counts are represented by no bucket. A move creates only the exact newly needed count.
- **Variable named `next`:** It shadows Python's built-in name only locally inside `inc`; retrieval's built-in `next(...)` is called in a different method and remains available.
