## General

**Each smaller absolute value must claim its double**

Every pair must have the form `(x, 2x)`. The difficult part is deciding which occurrence plays the role of `x` and which plays the role of its double, especially for negative numbers.

The solution counts occurrences with `Counter` and processes distinct values in increasing order of absolute value:

`sorted(freq, key=abs)`.

For each `x`, all remaining occurrences of `x` must be paired with the same number of occurrences of `2x`. If fewer doubles remain, pairing is impossible. Otherwise, those doubles are consumed.

**Why ordinary numeric sorting is wrong for negatives**

For positive values, the base `x` is smaller than `2x`. For negative values, numeric order reverses that appearance: `-4 < -2`, but the valid pair is `(-2, -4)`.

Absolute-value order solves both cases. A nonzero value always has smaller absolute value than its double:

`abs(x) < abs(2x)`.

Therefore, when `x` is processed, it is the natural base whose required double has not been used as a base earlier.

For example, `-2` is processed before `-4`, so the algorithm consumes `-4` as its double rather than incorrectly demanding `-8` for `-4` first.

**Frequency accounting**

Suppose `freq[x] = c` at the moment value `x` is processed. Every one of those `c` copies must be the first element of a pair, so at least `c` copies of `2x` are required.

The check `freq[x << 1] < freq[x]` detects a shortage. Left shift by one multiplies an integer by two, including negative integers in Python.

If enough copies exist, the code performs:

`freq[x << 1] -= freq[x]`.

This reserves those double values and prevents them from being reused by another base.

Counter returns zero for a missing key, so absent doubles naturally fail the comparison.

**Why zero needs a separate check**

Zero is its own double. Zero values can only form pairs `(0, 0)`, so their count must be even.

Without the explicit test `freq[0] & 1`, the generic comparison would examine `freq[0] < freq[0]`, which is always false, and subtract the count from itself. An odd number of zeros would incorrectly pass.

The bitwise expression detects odd parity. Once zero count is even, all zeros can be paired among themselves.

**Trace with positive and negative values**

For `arr = [4, -2, 2, -4]`, frequencies are one for each value. Absolute order processes values of magnitude two before magnitude four.

- For `-2`, one copy of `-4` exists, so it is consumed.
- For `2`, one copy of `4` exists, so it is consumed.
- When `-4` and `4` later appear in the key order, their remaining frequencies are zero, so they require nothing.

The method returns true.

For `[3, 1, 3, 6]`, value one requires a two that does not exist, so the method immediately returns false.

**Why the greedy consumption is correct**

Take the remaining nonzero value with smallest absolute magnitude. It cannot be used as the double of another remaining nonzero value, because that other value would have half its magnitude and would have been processed earlier. Thus every remaining occurrence must serve as a base and must claim its own double.

If enough doubles exist, assigning them is forced and cannot harm a different smaller-magnitude base, which has already made its claims. If not enough exist, no reordering can succeed.

Induction through absolute-value order proves that consuming doubles greedily is correct.

**What a zero remaining frequency means**

When a value later appears in the sorted key list with frequency zero, all of its original copies were already reserved as doubles for smaller-absolute-value bases. It must not create any new pairs. The shortage test compares zero required copies with the available count of its own double, succeeds, and subtracts zero. This makes previously consumed keys harmless without deleting dictionary entries or changing the iteration order.

## Complexity detail

Let `N` be the array length.

Building the frequency map costs `O(N)`. Sorting at most `N` distinct keys costs `O(N log N)`. Each key then performs constant expected-time Counter operations, so total time is `O(N log N)`.

The frequency map and sorted key list use `O(N)` space in the worst case.

## Alternatives and edge cases

- **Sort every array occurrence by absolute value:** Pair each occurrence greedily with its double using counts. This has the same asymptotic bounds but may sort more items than distinct-key sorting.
- **Ordinary ascending sort:** It mishandles negative bases because a more negative double appears before its half.
- **Backtracking:** Trying pair assignments is exponential and unnecessary once absolute-value order reveals forced choices.
- **Odd number of zeros:** Always false because zeros pair only with zeros.
- **Even zeros:** They can all be paired and do not interact with nonzero values.
- **Duplicate bases:** The double frequency must cover the complete remaining multiplicity.
- **Values already consumed as doubles:** Their frequency becomes zero, so later processing does nothing.
- **Negative left shift:** In Python, `x << 1` equals `2x` for negative and positive integers.
- **Even input length:** It is necessary but not sufficient; factor relationships must also match.
- **Missing Counter key:** It behaves as count zero, allowing a direct shortage check.
