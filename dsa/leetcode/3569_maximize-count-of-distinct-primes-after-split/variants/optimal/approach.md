## General

For one split, each distinct prime value can contribute either one or two to the sum:

- if it appears anywhere in the array, it contributes at least one because it belongs to the prefix, the suffix, or both;
- it contributes one additional count exactly when it appears on **both** sides of the split.

This separates every answer into:

$$
\text{number of distinct primes in the whole array}
+ \text{number of prime values spanning the chosen split}.
$$

The source maintains the first term as a scalar and the second term as interval overlap over all `n-1` split positions. A lazy segment tree reports the maximum overlap after every point update.

**Turning one prime’s occurrences into a split interval**

Index split positions by `s=0,\ldots,n-2`, where `s` means the prefix ends at index `s` and the suffix starts at `s+1`.

For a prime value `p`, let `first(p)` and `last(p)` be its smallest and largest current occurrence indices.

The prime appears in both parts exactly when

$$
first(p) \le s < last(p).
$$

So `p` contributes its extra one to every split in inclusive interval

`[first(p), last(p)-1]`.

If `p` occurs only once, first equals last and this interval is empty. The prime still contributes the global baseline one, but it can never be counted in both sides.

Adding one over every prime’s spanning interval creates an overlap count for each split. The best split has the maximum overlap.

**Why the answer formula is exact**

Let `D` be the number of distinct prime values currently present. At a fixed split, take any such prime:

- occurrences only in the prefix give `1+0=1` across the two distinct-counts;
- occurrences only in the suffix give `0+1=1`;
- occurrences on both sides give `1+1=2`.

Starting with one for every present prime gives `D`. Exactly the spanning primes need one extra, and their count is the interval overlap at that split.

Therefore the maximum possible result is

`distinct_prime_count + maximum_overlap[1]`,

where segment-tree root `maximum_overlap[1]` stores the largest overlap over all split indices.

**Precomputing primality**

The source first copies `nums` because query updates must persist locally without mutating the caller’s original list.

`value_limit` is the largest value appearing either initially or as a future query replacement. A sieve byte array marks all prime values through this limit. Zero and one are cleared. For each still-prime `value` up to `\sqrt{U}`, all multiples starting at `value^2` are cleared with a stepped slice.

Beginning at `value^2` is safe because smaller multiples already have a smaller prime factor and were handled earlier.

After the sieve, primality of any old or new query value is a constant-time array lookup.

**Tracking current occurrence extremes**

For every prime that has appeared, `occurrences[value]` stores three structures:

1. an `active` set of current indices;
2. a min-heap of inserted indices;
3. a max-heap represented by negative inserted indices.

The set is the source of truth. When an index stops containing that prime, it is removed from `active` but not searched out of either heap. Heap deletion from the middle would be expensive.

`extreme_indices` performs lazy deletion. It repeatedly pops a heap top while that index is not active. The first valid min-heap top is the smallest active index, and the negated max-heap top is the largest.

Stale entries may remain below the top, but they do not affect the current extreme. Across all updates, each inserted heap entry is pushed once and eventually popped at most once, giving good amortized behavior.

If a prime’s active set becomes empty, no extremes are requested. If that prime later reappears, new indices are pushed into its retained heaps; lazy validation removes obsolete tops as needed.

**The range-add, range-maximum segment tree**

The tree represents the `n-1` legal split indices. `range_add(left,right,delta)` adds `delta` to every overlap count in a split interval.

For a fully covered tree node, both its stored maximum and lazy tag increase. For partial coverage, affected children recurse, then the parent maximum is rebuilt as its own pending lazy value plus the larger child maximum.

This supports:

- adding or removing a prime’s whole spanning interval in `O(\log n)` time;
- reading the maximum overlap across every split from the root in `O(1)` time.

`add_prime_interval(value,delta)` does nothing for an empty active set. Otherwise it obtains current extremes and updates `[first,last-1]`. If a prime has only one occurrence, query-left exceeds query-right and `range_add` returns without changing anything.

**Initializing the dynamic state**

The source gathers current indices for every prime in `nums`, builds the two heaps for each active set, and adds one to its spanning interval.

`distinct_prime_count = len(occurrences)` at this point because the dictionary initially contains exactly the prime values currently present.

After initialization:

- the scalar is the global distinct-prime baseline;
- every segment-tree leaf counts how many prime occurrence ranges cross that split.

**Updating an old prime value**

For query `[index,value]`, let `old_value = nums[index]`. If the value actually changes and the old value is prime:

1. subtract its old interval with `add_prime_interval(old_value,-1)`;
2. remove `index` from its active set;
3. if the set becomes empty, decrement the distinct-prime count;
4. add its new interval with `add_prime_interval(old_value,1)`.

Removing the old interval before changing the set is essential. After removal, the first or last occurrence may move inward, so the new interval can be different or empty.

**Updating a new prime value**

If the replacement is prime, the dictionary entry is created if this prime has never appeared.

Then the source:

1. subtracts the prime’s current interval, if it is active;
2. increments the distinct-prime count if it was absent;
3. inserts `index` into the active set and both heaps;
4. adds the new interval based on updated extremes.

Again, removing then re-adding changes only the coverage that actually differs, while keeping the segment tree consistent.

If old and new values are identical, no structures change. The answer is still appended because every query requires an output.

Finally, `nums[index] = value` makes the update persistent for later queries.

**Why only the extremes matter**

A prime spans a split if it has at least one occurrence on each side. That depends solely on whether the split lies between its first and last occurrences. Internal occurrences do not change the spanning interval.

The active set and lazy heaps maintain exactly those extremes under point updates; there is no need to store the full occurrence order in a balanced tree.

## Complexity detail

Let `U` be the maximum numeric value in the initial array or any query, `n` the array length, and `q` the number of updates.

The sieve takes `O(U\log\log U)` time and `O(U)` space. Initial occurrence construction and heapification are linear in `n`, while initial interval additions cost at most `O(n\log n)` over distinct primes.

Each query changes at most two prime values. It performs a constant number of segment-tree range updates, each `O(\log n)`. Heap pushes and lazily deleted pops cost `O(\log(n+q))` amortized per entry; across all queries there are only `O(n+q)` inserted entries.

A faithful aggregate bound is

$$
O(U\log\log U + (n+q)\log(n+q)),
$$

which includes the segment-tree and heap logarithms and matches the manifest.

Space includes the `O(U)` sieve, `O(n)` segment tree, active occurrence sets, and heaps. Stale heap entries are retained until they reach a top, so total heap entries across execution can grow to `O(n+q)`. The answer list uses `O(q)`. Total space is `O(U+n+q)`.

## Alternatives and edge cases

- **Recompute every split after each query:** Counting distinct primes independently in every prefix and suffix would cost at least linear time per query and can become quadratic overall.
- **Fenwick tree alone:** Range addition and point query are easy, but the task needs the maximum across all split positions after each update. A lazy segment tree maintains that global maximum directly.
- **Balanced sorted occurrence sets:** They provide exact first and last indices with `O(\log n)` insertion and deletion. Python lacks a built-in balanced tree, so active sets plus lazy min/max heaps implement the required extremes.
- **One occurrence of a prime:** It raises `distinct_prime_count` by one but contributes no overlap interval, so it can be counted on only one side of any split.
- **Occurrences at both endpoints:** A prime at indices zero and `n-1` spans every legal split and adds one to the entire segment tree.
- **Removing an extreme:** Its old interval is subtracted before lazy heaps reveal the new first or last occurrence.
- **Removing the final occurrence:** The baseline distinct count decreases and no new interval is added.
- **Adding the first occurrence:** The baseline count increases, but its spanning interval remains empty.
- **Changing a value to itself:** The source skips all mutations and returns the unchanged maximum.
- **Composite and value one:** The sieve marks them nonprime, so they affect neither baseline nor overlap.
- **Persistent queries:** Updating the copied `nums` array ensures the next query observes all prior replacements.
- **Stale heap entries:** Membership in the active set distinguishes valid tops. Duplicate heap entries for an index can be harmless while that index is active and are eventually discarded after removal.
- **At least one split:** The constraint `n\ge2` guarantees `split_count=n-1\ge1`, so the segment-tree root represents a real split domain.
- **Why internal occurrences do not matter:** Any split between first and last automatically has at least one occurrence on each side; splits outside cannot be rescued by internal points.
- **Value limit selection:** Including all future query values ensures every replacement has a valid sieve lookup without extending the sieve online.
