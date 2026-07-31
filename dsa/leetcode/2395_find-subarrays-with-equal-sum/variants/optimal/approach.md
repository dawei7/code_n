## General

**Reduce each subarray to the value relevant to the question.** There are
exactly $n-1$ length-2 subarrays, one beginning at every index from 0 through
$n-2$. The contents themselves need not be stored; whether two subarrays
qualify depends only on whether their two-element sums are equal.

**Remember sums from earlier starting indices.** Scan those starts from left
to right and keep a set of adjacent-pair sums already encountered. Before
inserting the current sum, test whether it is present. A hit proves that the
current start and an earlier start are different indices with equal sums, so
the answer can immediately be `True`. If the scan ends without a hit, every
pair sum was unique and the answer is `False`.

The set contains exactly the sums of subarrays beginning before the current
index. Therefore a membership hit is sufficient: it supplies the required
earlier, distinct start. It is also necessary for returning `True`, because
any two equal sums cause the later one to find the earlier one's stored value.
Overlapping pairs require no special handling; their starts are still
different.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. The scan evaluates $n-1$ adjacent pairs,
so it takes expected $O(n)$ time under standard hash-set behavior. At most
$n-1$ distinct sums are stored, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Compare every pair of subarrays:** This uses $O(1)$ extra space but tests
  up to quadratically many pairs of starting indices and takes $O(n^2)$ time.
- **Sort all pair sums:** Materializing and sorting the $n-1$ sums makes equal
  values adjacent, but costs $O(n\log n)$ time and $O(n)$ space.
- **Minimum length:** When $n=2$, only one length-2 subarray exists, so the
  result must be `False`.
- **Overlapping subarrays:** Starts $i$ and $i+1$ are distinct even though the
  two subarrays share one array element.
- **Identical contents:** Equal subarray contents are allowed; their positions,
  rather than their values, determine whether the subarrays are distinct.
- **Negative and extreme values:** Pair sums may be negative or outside the
  input element range, but Python integers and hash-set keys preserve them
  exactly.
