## General

**Store only what future numbers need to know**

Every constructed subsequence is consecutive, so after processing some prefix of the sorted input, a future value needs only two facts about a subsequence:

- the value at which it currently ends;
- its current length.

The earlier members are determined implicitly by those facts and are not needed to decide whether the next number can extend it.

The exact solution uses `d[end_value]` as a min-heap of the lengths of all subsequences currently ending at that value.

**Why heaps are grouped by ending value**

A current number `v` can extend only a subsequence ending at `v - 1`. It cannot extend one ending at `v` because the next value must be exactly one larger, and it cannot extend a smaller ending value because that would create a gap.

Looking directly at `d[v - 1]` therefore finds exactly the eligible chains. Grouping by ending value avoids searching through unrelated subsequences.

**Extend the shortest eligible chain**

If `d[v - 1]` is nonempty, the solution removes its smallest length with `heappop`, adds one, and pushes the new length into `d[v]`. This moves that subsequence's endpoint from `v - 1` to `v`.

Choosing the shortest eligible chain is the critical greedy rule. A short chain is in greater danger of ending below the required length three. A longer chain that is already valid, or closer to validity, can more safely be left unchanged.

For example, suppose chains of lengths two and three both end at two, and the current value is three. Extending the length-three chain would leave the length-two chain invalid if no more threes appear. Extending the length-two chain makes both lengths three.

**Start a new chain only when extension is impossible**

If no subsequence ends at `v - 1`, the current occurrence cannot legally join any existing chain. The only possible use of that array element is to begin a new subsequence of length one ending at `v`.

The code pushes one into `d[v]`.

It does not immediately demand that `v + 1` and `v + 2` exist. Instead, later input elements will extend this new chain if possible, and the final validation will reject it if it remains too short.

**Understanding the assignment expression**

The condition `if h := d[v - 1]` retrieves the heap for the previous value and assigns it to `h`. A nonempty list is truthy, so that branch extends a chain. An empty list is false, so the `else` branch starts a new one.

Because `d` is a `defaultdict(list)`, accessing a missing key creates an empty list for it. These extra empty heaps do not affect correctness; final validation explicitly accepts empty lists.

**Walk through a successful example**

For `[1, 2, 3, 3, 4, 5]`:

- one has no predecessor chain, so start length one at one;
- two extends that chain to length two ending at two;
- the first three extends it to length three ending at three;
- the second three has no remaining chain ending at two, so it starts a new length-one chain at three;
- four extends the shortest chain ending at three, namely length one, to length two;
- five extends that chain to length three.

The final chain lengths are three and three, so the array can be split as `[1, 2, 3]` and `[3, 4, 5]`.

**Walk through a failing example**

For `[1, 2, 3, 4, 4, 5]`, the first four extends `[1, 2, 3]` to length four. The second four must start a new chain because no additional chain ends at three. Five extends that new chain only to length two. At the end, one heap contains a chain shorter than three, so the answer is `False`.

**Why the shortest-chain greedy rule is safe**

Suppose two eligible chains end at `v - 1` with lengths `a <= b`. Consider any plan that assigns current `v` to the longer chain. Swap this occurrence to the shorter chain instead. The lengths change from `a` and `b + 1` to `a + 1` and `b`.

Both chains still end with valid consecutive values, and no input occurrence is lost. The smaller length has improved, while the larger chain is no shorter than the original smaller one. This swap cannot create a new below-three failure that was not already present, and future equal values can be reassigned between chains ending at the same value. Repeating the exchange transforms an optimal feasible assignment into one that always extends the shortest eligible chain.

Therefore, if any valid partition exists, the greedy choices can lead to one. If the greedy result contains a short chain at the end, no alternative choice could have saved all chains.

**Why scanning sorted input preserves subsequences**

The array is non-decreasing. Processing occurrences from left to right ensures every newly appended value comes from a later input position. Consequently, each constructed chain is a subsequence, not merely a multiset of values.

Sorted order also means once processing has moved beyond a value, no smaller future element can repair a gap. The algorithm's forward-only endpoint updates rely on this guarantee.

**Validate all remaining chains through heap minima**

At the end, every input occurrence belongs to exactly one stored chain. For each heap:

- an empty heap represents no active chain and is harmless;
- a nonempty min-heap has its smallest length at index zero.

If the smallest length is greater than two, every other length in that heap is also at least three. If it is one or two, at least one invalid chain exists.

The final `all` expression checks exactly this condition for every ending value. It need not pop every heap entry.

## Complexity detail

Let `N` be the number of input elements.

Each element causes one heap push. If it extends a chain, it also causes one heap pop. A heap for one ending value can contain `O(N)` lengths, so an operation can cost `O(log N)`. The literal worst-case running time is `O(N log N)`.

The final validation examines each dictionary heap once and reads only its minimum, taking `O(N)` across at most `O(N)` keys. It does not change the dominant bound.

Every input occurrence is represented by exactly one chain length across all nonempty heaps, so heap entries total `O(N)`. The dictionary and empty lists created by predecessor lookups also use `O(N)` space.

The manifest advertises `O(N)` time and `O(N)` space. The linear-time bound belongs to the frequency-map and tail-count greedy alternative, where each update is expected constant time. The exact per-end min-heap implementation has the `O(N log N)` worst-case time described above.

## Alternatives and edge cases

- **Remaining-frequency and tails maps:** First count unused values. For each number, extend an existing chain ending at the previous value if possible; otherwise reserve the next two values to start a valid length-three chain. This gives expected `O(N)` time and matches the manifest.

- **Global heap of start/end pairs:** Store all subsequences ordered by endpoint and length. It works but is more complicated than separate heaps keyed directly by endpoint.

- **Store complete subsequence lists:** This uses unnecessary memory and copying. Endpoint plus length is sufficient metadata for decisions and validation.

- **Extend an arbitrary eligible chain:** Choosing a longer chain while a shorter one exists can strand the shorter chain below length three.

- **Start a new chain despite an eligible old chain:** This creates another short obligation unnecessarily and can turn a feasible input into a failure.

- **All values consecutive with no duplicates:** One chain grows to length `N` and is valid exactly when `N >= 3`.

- **Many duplicates:** Separate heap entries represent separate subsequences ending at the same value. Each occurrence is consumed exactly once.

- **Gap in values:** Chains before the gap can no longer be extended. The final minimum-length check determines whether they were already valid.

- **Negative values:** Dictionary keys and the `v - 1` lookup work unchanged.

- **One or two total elements:** Every possible chain is too short, so the minimum heap length causes `False`.

- **Empty predecessor heap created by `defaultdict`:** It is accepted by the final `not v` condition and does not represent a real subsequence.

- **Unsorted input:** The greedy scan relies on non-decreasing order to preserve subsequence positions and future availability. Sorting an arbitrary input would change which original-order subsequences are legal.

- **Checking only one heap:** Invalid chains may end at different values. Every nonempty heap must have minimum length at least three.

- **Heap minimum:** Because the heap is ordered by length, `v[0] > 2` proves every chain in that heap is valid; inspecting all entries would be redundant.
