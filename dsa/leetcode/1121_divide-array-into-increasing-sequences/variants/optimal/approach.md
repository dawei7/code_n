## General
**Duplicates impose a minimum sequence count:** One strictly increasing subsequence can contain at most one copy of any value. If the greatest frequency of one value is $f$, every valid division therefore needs at least $f$ subsequences.

**Length requirements impose the decisive capacity bound:** If there are at least $f$ subsequences and each has length at least `k`, the array needs at least $fk$ elements. Thus `n < f * k` is impossible.

**Why the same bound is sufficient:** Because `nums` is non-decreasing and no equal-value run exceeds $f$, elements `f` positions apart are strictly increasing. Form up to $f$ subsequences by grouping indices with the same remainder modulo $f$: sequence `r` receives `nums[r]`, `nums[r + f]`, and so on. Every sequence is strictly increasing. Their lengths are either $\lfloor n/f \rfloor$ or $\lceil n/f \rceil$; when $n \ge fk$, even the shorter length is at least `k`. This constructs a valid division, so the test `n >= f * k` is both necessary and sufficient.

**Find $f$ in one sorted scan:** Track the length of the current equal-value run and the maximum run length seen. Sorting is guaranteed by the contract, so equal copies are contiguous and no frequency map is needed.

## Complexity detail
The run-length scan visits all $n$ values once, for $O(n)$ time. It stores only the current and maximum counts plus the previous value, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Frequency map:** Counting every value also finds $f$ in $O(n)$ expected time but uses $O(n)$ space unnecessarily for sorted input.
- **Repeated `count` calls:** It is correct but rescans the array for many values and can take $O(n^2)$ time.
- **Explicit greedy construction:** Maintaining sequence tails can build a partition, but the Boolean question needs only the maximum multiplicity bound.
- **All values distinct:** Then $f = 1$, so the whole sorted array is one strictly increasing subsequence and succeeds exactly when `n >= k`.
- **All values equal:** Then $f = n$; every sequence can contain only one element, so success requires `k = 1`.
- **Exact boundary:** When `n = f * k`, the residue construction creates exactly $f$ sequences of length `k`.
- **Strictly increasing:** Equal adjacent values cannot share a subsequence; interpreting the target as non-decreasing would change the problem.
- **Subsequence rather than subarray:** Elements assigned together need not be contiguous, which makes the residue construction legal.
