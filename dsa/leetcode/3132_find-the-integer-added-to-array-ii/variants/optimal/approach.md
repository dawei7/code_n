## General

Sort copies of both arrays into non-decreasing order. Let the sorted arrays be `a` and `b`. The smallest value `b[0]` must come from one of `a[0]`, `a[1]`, or `a[2]`: if its source were any later element, more than two smaller elements of `a` would have to be removed.

Consequently, every possible answer is among `b[0] - a[i]` for $i \in \{0,1,2\}$. Because `a` is non-decreasing, these differences become smaller as $i$ increases. Test indices `2`, `1`, and `0` in that order so the first valid shift is the minimum possible one.

For a candidate $x$, scan `a` from left to right while pointing at the next unmatched value of `b`. When `a[i] + x` equals that target, match the pair and advance both sides; otherwise, treat `a[i]` as one of the removed values. This greedy match is safe because both transformed `a` and `b` are sorted: bypassing an equal value is never useful, and a smaller unmatched source cannot match a later, smaller target. If every value of `b` is matched, exactly two values of `a` remain unmatched because the lengths differ by two, so the candidate is valid.

The problem guarantees that at least one candidate succeeds. Testing candidates from smallest to largest therefore returns precisely the required minimum $x$.

## Complexity detail

Let $n = \lvert\texttt{nums1}\rvert$. Sorting dominates the three linear verification scans, giving $O(n \log n)$ time. The app-local implementation sorts copies of the inputs, so it uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate removal pairs:** Try every pair of removed indices and compare the shifted remainder with `nums2`. This is straightforward but can require at least quadratic enumeration and substantially more comparison work.
- **Frequency maps per candidate:** Count both multisets and validate each of the three shifts through frequencies. This remains linear after candidate generation but uses $O(n)$ additional storage and is less direct than the sorted two-pointer match.
- **Minimum rather than any valid shift:** Several removal pairs may work. Testing candidates in arbitrary order can return a valid but non-minimal value; index order `2, 1, 0` is deliberate.
- **Duplicate values:** Equal elements are separate occurrences. Greedy matching consumes one occurrence at a time, while the two unmatched occurrences represent the removals.
- **Negative and zero shifts:** Array elements are nonnegative, but the returned shift may be negative or zero.
- **Three-element source:** `nums2` then has one element, and all three alignments must still be considered to find the minimum shift.
