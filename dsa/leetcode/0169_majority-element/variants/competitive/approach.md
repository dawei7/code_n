## General

**Vote for a candidate with a running balance**

The competitive solution wraps Boyer–Moore voting in a local helper. `result`
is the active candidate, and `cnt` is the number of its unmatched votes after
pairing it against different values.

For each `x`, if the balance is zero, the source chooses `x` as the new
candidate. It then increments the balance because `x == result`. If an active
candidate already exists, an equal `x` increments the balance and a different
`x` decrements it.

The condition `if not cnt` is equivalent to `cnt == 0` here. The update rules
never make the counter negative: a value that would decrement one to zero ends
that segment, and the next iteration establishes a fresh candidate.

**Interpret a decrement as removing a pair**

Whenever `x != result`, reducing `cnt` pairs this occurrence with one previously
unpaired occurrence of `result`. The pair contains two different values, so
neither member can gain an advantage from keeping it.

When the balance reaches zero, the complete current segment can be partitioned
into different-value pairs. It contributes no surviving candidate vote and can
be ignored while processing the suffix.

This interpretation is more useful than treating `cnt` as a literal frequency.
The candidate may have occurred many times in discarded segments even though
the current balance is small.

**Why balanced prefixes may be forgotten**

Suppose the true majority is `M`. In any balanced segment removed by the
algorithm, the number of removed `M` occurrences is no greater than the number
of removed non-`M` occurrences. If `M` is the segment candidate, they are
paired one-for-one with other values. If another value is the candidate, an
`M` occurrence is one of the votes canceling it.

Since globally there are more `M` values than all non-`M` values combined,
discarding such pairs leaves at least one unmatched `M` and preserves its
overall advantage. Eventually the final unresolved segment must have `M` as
its surviving candidate.

**Trace candidate resets**

For `[2,2,1,1,1,2,2]`, the first two selects candidate two and raises the
balance to two. Two one values cancel that balance. The next one starts a new
candidate with balance one. A following two cancels it, and the final two
starts the last segment. Two is returned.

For `[3,2,3]`, candidate three is canceled by two, then selected again at the
final position.

These examples show that selecting a non-majority candidate temporarily is
safe. The algorithm does not claim every intermediate `result` is correct.

**Prove the returned candidate under the guarantee**

Let the majority occur more than $\lfloor n/2\rfloor$ times. Equivalently, it
occurs more often than all other values together.

Every decrement corresponds to deleting one pair of unequal elements.
Deleting such pairs cannot remove all majority occurrences, because there are
not enough non-majority elements to pair with them all. Therefore the value
that survives the online cancellation process is the majority.

The method returns the helper's final `result`. The nonempty-input guarantee
ensures some first value replaces the initial `None`.

**Understand when verification would be needed**

Boyer–Moore always proposes a candidate for a nonempty array, even if no value
appears more than half the time. Without the guarantee, a second pass would
need to count `result` and compare its occurrence total with `len(nums) // 2`.

This package promises existence, so omitting verification preserves correctness
and keeps one linear pass.

**Source organization details**

The file imports `collections`, but the selected `Solution` does not use it.
Later unselected classes use `Counter`; that import has no effect on the
voting helper's complexity.

The nested helper closes over `nums`. It is called once and uses only scalar
local variables. Creating the function object is constant overhead.

## Complexity detail

The helper visits each of the $n$ values once and performs equality plus one
counter update. Time is $O(n)$.

`result`, `cnt`, and `x` are scalar state. The closure and unused module import
do not grow with input size, so auxiliary space is $O(1)$. These bounds match
the manifest.

## Alternatives and edge cases

- **`collections.Counter`:** The later source alternative counts all values in $O(n)$ time and $O(n)$ space.
- **Sort and take the middle:** Correct under the majority guarantee, but costs $O(n\log n)$ time.
- **Random sampling with verification:** Has expected linear time but unbounded worst-case sampling attempts.
- **One value:** `None` is replaced immediately, and that value is returned.
- **Balance reaches zero:** The next number begins a fresh independent voting segment.
- **Repeated majority run:** Each equal occurrence raises the unmatched balance.
- **Arbitrary integer range:** Only equality is used, so no overflow or ordering issue arises.
- **No-majority input outside the contract:** The candidate must be verified in a second pass.
- **Unused import:** `collections` belongs to other classes and is irrelevant to the selected algorithm.
- **Nonempty guarantee:** It ensures the final candidate is not `None`.
