## General

**The challenge is maintaining a changing maximum.** A hash map can update the frequency of one ID in expected constant time, but it cannot by itself answer “what is the largest current frequency?” without scanning every ID after every update. Such repeated scans could take quadratic time.

The exact source combines three structures:

- `cnt[x]` stores the current frequency of ID `x`;
- `pq` is a min-heap of negated frequency values, which acts as a max-heap;
- `lazy[v]` records how many heap entries with frequency value `v` have become stale.

The heap stores frequency values rather than pairs of frequency and ID because the output needs only the maximum count, not which ID owns it.

**Why old heap entries become stale.** Python's heap supports efficient insertion and removal of the top element, but not efficient deletion of an arbitrary value buried inside it. When ID `x` changes from old count `old` to new count `new`, an old heap entry for `old` should no longer represent that ID. Searching the heap to remove it would be expensive.

Instead, the source executes:

`lazy[cnt[x]] += 1`.

This schedules one occurrence of the old count for deletion. It then changes the authoritative map value with `cnt[x] += f` and pushes `-cnt[x]` into the heap. The new count now has a fresh candidate entry.

The heap may contain many historical values, but `cnt` remains the source of current ID frequencies and `lazy` tells the cleanup process how many historical occurrences of each numeric count must be ignored.

**Negation turns a min-heap into a max-heap.** If current counts are 7, 4, and 2, the heap stores -7, -4, and -2. Python's smallest stored value is -7, and negating `pq[0]` recovers 7, the largest frequency. Every push and pop remains a standard `heapq` operation.

**Lazy cleanup needs to inspect only the top.** After the new value is pushed, the code repeatedly examines `-pq[0]`. If `lazy[-pq[0]] > 0`, one heap occurrence with that count is obsolete. The source decrements the lazy multiplicity and pops the entry.

It is unnecessary to remove stale entries that are deeper in the heap. They cannot affect the answer while a larger valid value remains above them. If one later rises to the top, the same loop removes it then. Once the loop stops, the top value has no outstanding stale occurrence and represents the maximum current count in the multiset model maintained by the code.

**Why lazy counts are stored by frequency, not ID.** Suppose several IDs once had count five. The heap contains indistinguishable `-5` entries, and the answer also does not care which ID supplies a five. If one of those IDs changes, marking one occurrence of numeric value five stale is sufficient. Cleanup may conceptually remove a different ID's identical heap occurrence, but the remaining multiplicity of value five is still correct. Only the number of valid entries at each frequency matters.

**Handling the implicit initial zero.** `Counter` returns zero for an unseen ID. The source marks that old zero stale even though an explicit zero may not yet have been pushed for the ID. This creates a lazy zero token. It is harmless because zero can never outrank a positive frequency. If a zero entry later reaches the top, the pending token can remove it; an empty heap and a heap whose maximum is zero both lead to answer zero. The input guarantee prevents negative current frequencies, so no negative count can interfere with this behavior.

**Producing one answer per update.** After cleanup, `-pq[0]` is appended when the heap is nonempty. If cleanup empties the heap, the source appends zero. This matches an empty collection. IDs whose current count becomes zero need not be physically deleted from `cnt`; their zero value does not increase the maximum.

For the first example, ID 2 changes from zero to three, so three is pushed and reported. ID 3 then changes to two; the maximum stays three. When ID 2 loses three, its old three is marked stale and zero is pushed. Cleanup removes the stale three, leaving two at the top. The returned sequence follows the maximum current multiplicity after every step.

**Why the algorithm is correct.** After processing an update, `cnt` contains every current ID count. For the updated ID, the previous count has received one stale token and the new count has received one heap entry; other IDs retain their representations. Thus the heap plus lazy multiplicities represents the multiset of current counts, possibly mixed with historical entries that are marked for future removal. The cleanup loop discards every marked occurrence encountered above the answer. When it stops, no stale occurrence is allowed to occupy the top, so the recovered value is the maximum in the current multiset. Appending that value satisfies the contract for this step, and the argument repeats for all steps.

## Complexity detail

Let $n$ be the number of updates. Each update performs one heap push, costing $O(\log n)$. It may perform several pops, but every heap entry is pushed once and can be popped at most once. Across the whole run there are only $O(n)$ pops, each costing $O(\log n)$. The total time is therefore $O(n\log n)$.

The counters hold at most $O(n)$ distinct IDs or frequency values, and the heap can hold $O(n)$ historical entries awaiting cleanup. The answer list also contains $n$ values. Auxiliary working space, excluding or including the required output, is $O(n)$ either way because the heap dominates.

Hash-map operations are expected $O(1)$. The logarithmic factor comes from heap maintenance, and lazy deletion avoids any linear search inside the heap.

## Alternatives and edge cases

- **Balanced ordered map of frequency multiplicities:** Update old and new frequencies and read the largest key. This also gives $O(\log n)$ per step but Python has no built-in ordered multiset.
- **Heap with an ID in every entry:** Push each updated `(count, ID)` pair and pop while the pair's count differs from `cnt[id]`. This is often simpler conceptually and has the same asymptotic bounds.
- **Scan all IDs after each update:** The map update is easy, but repeated maximum scans can cost $O(n^2)$ overall.
- **Frequency becomes zero:** Zero may remain in both counters and the heap; the reported maximum is still zero when no positive occurrence exists.
- **Collection becomes empty:** Cleanup may empty `pq`, and the explicit conditional appends zero.
- **Repeated updates to one ID:** Each old count is marked stale and each new count is pushed; amortized cleanup still applies.
- **Several IDs share the maximum:** The answer is only the count, so one valid heap occurrence is enough.
- **Negative update:** It decreases `cnt[x]`, and the input guarantee ensures the result never drops below zero.
- **Positive update:** It may create a new maximum immediately because its negated value rises toward the heap top.
- **Stale value below the top:** Leaving it in place is safe until all larger candidates disappear.
- **Many stale entries at one value:** `lazy[value]` is a multiplicity, so cleanup removes the correct number one by one.
- **Implicit zero debt:** Marking an unseen ID's old zero is harmless for this nonnegative-maximum problem, as described above.
- **Why not delete zero keys:** Deleting them is optional bookkeeping and would not improve the asymptotic bound.
- **Large counts:** Frequencies can accumulate beyond one update's magnitude, but Python integers do not overflow.
- **Output ownership:** The heap identifies only the maximum frequency, exactly what the result requests; it deliberately cannot identify a winning ID.
