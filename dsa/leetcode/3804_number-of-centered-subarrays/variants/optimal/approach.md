## General

**Enumerate each contiguous interval by its endpoints**

The outer loop fixes left endpoint `i`. The inner loop advances right endpoint `j` from `i` through the final index.

For this fixed left endpoint, `s` is the running sum of `nums[i..j]` and `st` contains all values appearing in that same interval.

After adding `nums[j]` to both structures, `s in st` is exactly the centered-subarray condition.

**Reuse state while extending right**

Moving `j` one step adds one element. The new sum is the previous sum plus that value, and the new contained-value set is the previous set plus that value.

This makes each interval check expected constant time after its extension. Recomputing `sum(nums[i:j+1])` and rebuilding a set for every pair would introduce another linear factor.

**Reset for each new left endpoint**

When `i` increases, earlier elements must no longer belong to the candidate intervals. The source creates a fresh empty set and zero sum inside the outer loop.

It does not attempt a sliding-window optimization because values may be negative and the centered property is not monotone when boundaries move.

**Trace the first example**

For left endpoint zero in `[-1,1,0]`:

- interval `[-1]` has sum -1, present in its set;
- `[-1,1]` has sum zero, absent from set `{-1,1}`;
- `[-1,1,0]` has sum zero, now present.

For left endpoint one, `[1]` and `[1,0]` are centered. The final singleton `[0]` is centered, totaling five.

**Every singleton is centered**

A one-element interval has sum equal to its sole value, so it always qualifies. The source naturally counts this when `j==i`.

This supplies at least $N$ centered subarrays and provides a useful sanity check.

**Why membership, not frequency, is enough**

The condition asks whether at least one element equals the sum. A set answers existence. Duplicate occurrences do not make one interval count multiple times; the endpoints define a single subarray.

**Why all and only valid intervals are counted**

Every contiguous nonempty subarray has one unique pair $(i,j)$ with $i\le j$, and the nested loops visit every such pair exactly once.

At that moment, the maintained sum and set describe exactly its elements. Membership is true precisely when the sum equals at least one contained value. Incrementing once counts the interval regardless of how many matching occurrences it contains.

**Why validity is not monotone**

Adding a value can create or destroy centered status. Starting from `[2]`, adding `-2` changes the sum from two to zero while the set becomes `{2,-2}`, so validity disappears. Adding zero makes the sum zero present again. Negative values rule out a conventional monotone sliding window.

For each fixed left endpoint, the state progresses only through contiguous intervals `[i,i]`, `[i,i+1]`, and onward. A fresh set and sum are created for the next left endpoint so earlier elements do not leak into its intervals.

If an interval sum occurs several times inside the interval, it still contributes one. The set intentionally stores existence rather than frequency.

For example, `[0,0]` has sum zero and two matching elements, but it is one centered interval. Its two singleton intervals are separate because they have different endpoint pairs, giving three centered subarrays total.

There are exactly $N-i$ right endpoints for left endpoint `i`. Summing over `i` gives $N(N+1)/2$ checks, matching the number of nonempty subarrays.

Python's integer sum may lie far beyond the range of individual values; membership simply fails unless that exact total occurs as an element.

The source inserts the newly extended value before membership testing, so the rightmost element is eligible to witness the current interval's sum.

## Complexity detail

There are $N(N+1)/2=O(N^2)$ intervals. Each extension performs constant arithmetic and expected $O(1)$ set operations, so expected total time is $O(N^2)$.

For one left endpoint, `st` may hold $O(N)$ distinct values. It is discarded before the next left endpoint, giving $O(N)$ peak auxiliary space.

## Alternatives and edge cases

- **Recompute sum and set per interval:** This raises time toward $O(N^3)$.
- **Prefix sums only:** They give interval sums quickly but do not answer whether that sum appears inside the interval.
- **Sliding window:** Negative values and nonmonotone membership provide no safe one-direction shrink rule.
- **Count each matching occurrence:** A centered interval counts once even if its sum appears several times.
- **Singleton:** Always centered.
- **All zeros:** Every interval has sum zero and contains zero, so all intervals count.
- **Negative sums:** Set membership handles them normally.
- **Duplicate values:** The set preserves existence semantics.
- **No qualifying longer intervals:** Singletons still contribute $N$.
- **Input preservation:** Only local sums and sets are changed.
- **Several matching occurrences:** The interval still counts once.
- **Nonmonotone validity:** Extension may destroy or restore the property.
- **Fresh outer state:** Each left endpoint resets sum and membership.
- **Right endpoint witness:** Add it to the set before testing the extended interval.
