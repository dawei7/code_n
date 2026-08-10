## General

**The contract makes the first duplicate decisive**

The array contains exactly one value that occurs more than once: it appears `n` times. Every other distinct value occurs exactly once.

Therefore, as soon as a left-to-right scan encounters a value already seen, that value must be the required repeated element. No other value can produce a duplicate encounter.

The solution uses set `s` to remember values from earlier positions.

**Step-by-step scan**

For each value `x`:

1. Check whether `x in s`.
2. If it is present, return `x` immediately.
3. Otherwise, add `x` to the set and continue.

The membership check must happen before insertion. Inserting first would make every value appear present and incorrectly return the first element.

**Why a duplicate must eventually appear**

The repeated value occurs `n` times and the constraints give `n >= 2`. Its second occurrence therefore exists.

By the time that second occurrence is scanned, the first is already in `s`, so the method returns no later than that position.

This is why the exact function has no explicit return after the loop. Under the promised input contract, control can never fall through.

**Why the first repeated encounter is the answer**

Suppose the scan returns value `x`. Set membership proves an earlier occurrence of `x` exists, so `x` occurs at least twice.

The contract says `n` other values each occur exactly once and only one value is repeated. Hence `x` can only be the value occurring `n` times.

Conversely, the true repeated value necessarily causes the first or only duplicate encounter, while singleton values never do. The returned value is exact.

**Trace**

For `[2, 1, 2, 5, 3, 2]`:

- Read two and add it.
- Read one and add it.
- Read two again. It is already present, so return two.

The remaining values do not need examination because no later evidence can change the unique repeated identity.

For `[1, 2, 3, 3]`, the first three values are inserted, and the final three triggers the return.

**Why frequencies are unnecessary**

A full frequency table could count every occurrence and then search for count `n`. That works but continues after the answer is already logically known.

The special promise that all other values are singletons means merely detecting count two is sufficient. The set stores only the distinction between unseen and seen-at-least-once.


Maintain the invariant that before processing each position, `s` contains exactly the distinct values in the already-scanned prefix.

If current `x` is absent, adding it preserves the invariant. If it is present, the prefix plus current position contains two occurrences. By the uniqueness condition on repeated values, `x` is the target and immediate return is correct.

Because the target has at least two occurrences, the return eventually happens.

**How the size promise reinforces the argument**

The array has `2n` positions. The repeated value occupies `n` of them, while the remaining `n` positions contain the `n` singleton values. For `n >= 2`, at least two positions necessarily hold the repeated value.

The scan does not need to know the numeric value of `n` or count how many copies remain. The size and multiplicity promises are used logically: they prove that a duplicate encounter must occur and that there is only one possible identity for it.

If the contract were weakened so that several values could repeat, this early-return algorithm would answer “first duplicate encountered,” which might not be the most frequent value. Its simplicity comes directly from the unusually strong distribution guarantee.

**Why hash collisions do not change logical correctness**

A Python set resolves internal hash collisions by equality checks. Two different integers that happen to interact at the hashing level are still stored and queried as different values. The expected-time complexity depends on hashing behavior, but the semantic membership result remains exact.

## Complexity detail

Let `N` be the array length, which equals `2n` in the statement.

Each value is visited at most once. Hash-set membership and insertion take expected `O(1)` time, so expected total time is `O(N)`. Early return may inspect only a prefix.

The set can contain `O(N)` distinct values before the duplicate is encountered, so auxiliary space is `O(N)`.

## Alternatives and edge cases

- **Frequency counter:** Count all values and return the one with count `n`. It has the same asymptotic bounds but may scan more than necessary.
- **Fixed value-range array:** Values are at most ten thousand, so a Boolean array can replace the hash set at the cost of range-sized storage.
- **Constant-space distance observation:** The frequent element must repeat within a small index gap; comparing nearby positions can yield `O(1)` space, but its proof is less direct.
- **Sort the array:** Equal copies become adjacent, but sorting costs `O(N log N)` and may mutate input.
- **Second element is duplicate:** The method returns immediately after one insertion.
- **Duplicate appears late:** Singleton values accumulate in the set until the second target occurrence.
- **Value zero:** It is an ordinary hashable integer and needs no sentinel handling.
- **No explicit fallback return:** Safe only because the input guarantees a repeated value with at least two copies.
- **Other values unique:** This promise is essential. Without it, the first duplicate need not be the most frequent value.
- **Input preservation:** The set-based scan does not modify `nums`.
