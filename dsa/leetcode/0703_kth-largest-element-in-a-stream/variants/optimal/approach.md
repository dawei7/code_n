## General
**Keep only values that can affect rank k**

Maintain a min-heap containing the largest `k` values seen so far. Any value outside this set is no larger than the heap minimum and cannot become the `k`th largest while all retained values remain present.

**Build the bounded heap**

Offer each initial value to the heap. Push while fewer than `k` values are retained. Once full, replace the minimum only when the new value is larger.

**Process each addition identically**

Apply the same offer rule to every streamed value. After the operation, the heap contains the largest `k` values among the enlarged history, so its root is their smallest value and therefore the overall `k`th largest.

**Why discarding a value is safe forever**

When a value is rejected or removed, at least `k` seen values are no smaller. Future additions never delete those values; they can only add more competition. The discarded value can therefore never enter the largest-`k` set later.

## Complexity detail
For `m` initial values and `s` additions, each offer costs at most $O(\log k)$, giving $O((m + s) \log k)$ total time. The heap never stores more than `k` values, so it uses $O(k)$ space beyond the returned results.

## Alternatives and edge cases
- **Rebuild a bounded heap after each addition:** it returns the right rank but repeatedly processes the complete history, taking $O(s(m + s) \log k)$ time.
- **Sort the complete history after each addition:** it is simple and correct but can take up to $O(s(m + s) \log(m + s))$ time.
- **Balanced search tree with subtree sizes:** insert each value and select rank `k`; it supports logarithmic operations but requires an augmented ordered multiset.
- **Sorted list of the largest k values:** binary search finds an insertion point, but shifting elements can cost $O(k)$ per addition.
- When $k = 1$, the heap root is the running maximum.
- Duplicate values occupy separate rank positions and must remain separate heap entries.
- Negative values follow the same ordering rules as positive values.
- The operation contract guarantees enough total values exist whenever an answer is requested.
