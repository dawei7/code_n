## General

Maintain a frequency map for the current length-`k` window. The desired mode is the value minimizing the ordered key

$$
(-\text{frequency},\ \text{value}).
$$

A min-heap over this key therefore places the highest frequency first and uses the smallest value for ties.

**Record new states lazily.** Whenever a value enters the window, increment its count and push its new `(-count, value)` state. Whenever a value leaves, decrement its count and, if it remains positive, push that new state too. Older states for the same value remain in the heap temporarily.

Before reading a window's mode, inspect the heap top. If the stored negative count no longer equals the frequency map's current count for that value, pop it as stale and repeat. Once the top matches, it is a valid current state.

Every positive-frequency value has at least one entry representing its latest count because both increments and positive decrements push states. After stale top entries are removed, the surviving top is therefore the minimum key among all current values. Its negated count and value give the contract's exact mode and frequency, so their product is the window weight.

Initialize the first window, add its weight, then slide one position at a time by removing the outgoing value and adding the incoming value. Each update preserves the frequency map, and lazy cleanup preserves the heap query invariant. Summing every queried weight covers all $n-k+1$ windows exactly once.

## Complexity detail

There are $O(n)$ additions and removals. Each pushes at most one heap entry, and every pushed entry is popped at most once. Heap operations cost $O(\log n)$, giving $O(n\log n)$ total time. The frequency map and lazy heap contain $O(n)$ entries in the worst case, so auxiliary space is $O(n)$.

The benchmark defines its size as $n$, uses distinct increasing values, and sets $k=n/2$. The accepted sliding structure updates one outgoing and one incoming value per step. A calibrated correct alternative rebuilds a frequency map and searches for the mode independently in every window, taking $O(nk)$ time.

## Alternatives and edge cases

- **Recount every window:** This is simple and correct but costs $O(nk)$ time.
- **Ordered set of current pairs:** Removing the old key and inserting the new key gives $O(n\log d)$ time for $d$ distinct window values, but requires a balanced ordered-set implementation.
- **Frequency buckets:** Buckets can support the maximum frequency, but selecting the smallest value in the winning bucket still needs ordering.
- **Frequency tie:** Compare values only after frequencies; the smallest tied value wins.
- **k equals one:** Every element is its own mode with frequency one, so the answer is the array sum.
- **k equals n:** Compute exactly one whole-array weight.
- **Outgoing mode:** A decrement may expose a different value or a smaller tied value; pushing the new state handles both.
- **Duplicate heap states:** Multiple valid identical entries are harmless because they represent the same current key.
