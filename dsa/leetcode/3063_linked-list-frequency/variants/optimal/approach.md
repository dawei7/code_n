## General

**Count occurrences in one traversal.** `Counter()` maps each node value to the number of times it has appeared. The while-loop visits every node, increments `cnt[head.val]`, and follows `head.next`.

When traversal ends, the counter has exactly one entry for each distinct input value and its stored number is the required output node value.

**Build a fresh output list from frequencies.** The task does not require preserving any particular order. The source creates a dummy node, then loops through `cnt.values()`. For each frequency `val`, it creates:

`ListNode(val, dummy.next)`

and assigns it as the new `dummy.next`. This prepends the node to the list built so far.

If counter values are encountered as 3, 2, 1, the output construction becomes:

- `3`;
- `2 -> 3`;
- `1 -> 2 -> 3`.

The final order is the reverse of counter value iteration. Since any order is valid, no sorting or tail pointer is necessary.

**Understand counter iteration order without depending on it.** Modern Python counters preserve first-insertion order of distinct keys. Therefore `cnt.values()` follows the order in which distinct input values first appeared, and prepending reverses it. Correctness does not rely on that language detail because every permutation of frequencies is accepted.

**Why output length is exactly the distinct count.** The counter contains $K$ entries for $K$ distinct values. The construction creates one node per entry and no others besides the temporary dummy, which is not returned. Therefore the returned list contains exactly $K$ nodes.

**A trace.** For input `1 -> 1 -> 2 -> 1 -> 2 -> 3`, the counter becomes `{1:3, 2:2, 3:1}`. Iterating values produces 3, 2, 1; prepending yields `1 -> 2 -> 3`. These are the frequencies in a permitted order.

For six distinct input values, every counter value is one, so the output has six nodes all containing one.

**Why the input nodes cannot simply be reused safely.** The output needs one node per distinct value, not one per input node, and values must become frequencies. Reusing selected input nodes would require choosing representatives and rewiring links, mutating the caller's structure. The exact source allocates new nodes and leaves the original list intact.

**Dummy-node role.** The dummy provides a stable object whose `next` always points at the current output head. It avoids a special case for the first created node. Since only `dummy.next` is returned, the extra node does not appear in the answer.
The first pass establishes exact frequency for every distinct value by adding one per occurrence. The second pass maps each counter entry to exactly one new node containing that frequency. No entry is omitted or duplicated. Since ordering is unrestricted, the returned list satisfies the complete contract.

## Complexity detail

Let $N$ be input node count and $K$ distinct values. Counting takes $O(N)$ expected time. Building $K$ output nodes takes $O(K)$. Total expected time is $O(N)$ because $K\le N$.

The counter uses $O(K)$ auxiliary space. The returned list necessarily uses $O(K)$ output space. If output storage is excluded, the counter remains $O(K)$.

Traversal and construction are iterative, so there is no recursion stack. The input nodes are not altered.

## Alternatives and edge cases

- **Fixed frequency array:** Values are at most $10^5$, so a dense array works but uses space for the whole domain rather than only observed values.
- **Sort collected values:** Sorting would permit run counting but requires $O(N)$ storage and $O(N\log N)$ time.
- **Append with a tail pointer:** It preserves counter iteration order and remains linear. Prepending is shorter because output order is unrestricted.
- **One input node:** Counter has one frequency of one, producing a one-node output.
- **All nodes equal:** One counter entry produces one node containing $N$.
- **All values distinct:** Output length is $N$ and every value is one.
- **Repeated frequencies:** They remain separate nodes because they correspond to different distinct input values.
- **Output order:** Reversal caused by prepending is valid under “any order.”
- **Input preservation:** Local traversal changes only the `head` reference; newly allocated nodes form a separate list.
- **Expected dictionary time:** Counter operations rely on normal hash-table behavior for integer keys.
- **Frequency nodes lose original labels intentionally:** The output node contains a count, not the distinct value it describes. Since order is unrestricted and no mapping is requested, values and frequencies do not need to remain paired in the returned structure.
- **Dummy node value:** The default value stored in `dummy` is irrelevant because the dummy itself is skipped. Only its `next` field is used as a convenient mutable head holder.
- **Maximum counter value:** A frequency can be as large as $N$, which fits the node value type used by the platform even though input values themselves have a separate bound.
- **Fresh ownership:** Every returned node was allocated during the second pass, so later edits to the output cannot corrupt the original linked list and vice versa.
