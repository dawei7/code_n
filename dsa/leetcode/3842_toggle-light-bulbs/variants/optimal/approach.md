## General

**A toggle keeps only occurrence parity**

Each bulb starts off. Its first occurrence turns it on, its second turns it off, and every later pair of occurrences cancels in the same way. The final state of a bulb therefore depends only on whether its total occurrence count is odd or even.

Create a boolean array indexed by bulb number. For each value in `bulbs`, negate the boolean at that index. After processing any prefix, `is_on[b]` is true exactly when bulb `b` has occurred an odd number of times in that prefix: this holds initially because every count is zero, and one negation changes both the occurrence parity and the stored state together. Thus it remains true after the complete array.

**The numbered state array provides the required ordering**

Inspect the fixed bulb indices from `1` through `100` and append precisely those whose state is true. The scan is already in ascending numeric order, so it needs no later sorting. By the parity property, these and only these indices identify bulbs that finish on; if every boolean is false, the same scan naturally returns the required empty list.

## Complexity detail

Let $N$ be the length of `bulbs` and let $B=100$ be the fixed number of bulbs. Toggling the operations and scanning all bulb numbers takes $O(N+B)$ time, which is $O(N)$ because $B$ is a source constant. The state array uses $O(B)=O(1)$ auxiliary space. The returned list is output space and can contain at most 100 numbers.

The complete legal domain stops at $N=100$ and uses only 100 bulb states. Calibration across legal lengths could not reliably distinguish the accepted scan from a correct $O(N^2)$ repeated-count implementation: both passed the scaling gate. The package therefore uses a reviewed `bounded_domain` certificate instead of presenting those timings as asymptotic evidence. Its replacement regression checks exhaustive small arrays, every legal length, and the value boundaries against an independent odd-frequency oracle.

## Alternatives and edge cases

- **Toggle a set:** Remove a bulb number when already present and add it otherwise, then sort the set at the end. This is correct but adds a needless $O(D\log D)$ sort for $D$ bulbs left on.
- **Count frequencies:** Increment one of 101 counters and return indices with odd counts. It has the same $O(N)$ time and fixed auxiliary space but stores more state than a boolean toggle.
- **Sort and group:** Sorting `bulbs` makes equal values contiguous and exposes odd group sizes, but costs $O(N\log N)$ time.
- **Repeated whole-array counting:** For every distinct bulb, calling `bulbs.count(b)` determines the correct parity but can require $O(N^2)$ time.
- **One occurrence:** A bulb seen exactly once must finish on.
- **Even repetitions:** Any bulb toggled an even number of times returns to off, including the only bulb in an otherwise nonempty input.
- **Boundary numbers:** Bulbs `1` and `100` are both valid and require an indexed state large enough to include the upper endpoint.
- **Ascending result:** Operation order controls toggling, but the final returned numbers must be numerically sorted rather than kept in first-occurrence order.
- **Empty result:** The input array is never empty, yet every final state may be off when all occurrence counts are even.
