## General

**Use the minimum and maximum to determine the only possible spacing**

For one query, let the inclusive subarray length be

$$
k=r-l+1.
$$

If its values can be rearranged into an arithmetic sequence, sorting that sequence would place its minimum value first and its maximum value last. A length-$k$ arithmetic sequence has $k-1$ equal gaps. Therefore its common difference is forced to be

$$
d=\frac{\textit{maximum}-\textit{minimum}}{k-1}.
$$

There is no need to try several possible differences. The two extremes and the number of elements leave exactly one candidate.

The helper `check(nums, l, r)` computes `n = r - l + 1` for this query. Here `n` is the query length, not necessarily the length of the original array.

It builds `s` as a set of the values in `nums[l:l+n]`. Since `l + n = r + 1`, this Python slice contains exactly indices $l$ through $r$. The helper separately obtains `a1` and `an` as the minimum and maximum of the same inclusive range.

**Reject a fractional common difference**

All input values are integers, so every member of any rearranged arithmetic sequence must remain an integer. `divmod(an - a1, n - 1)` returns both the integer quotient `d` and remainder `mod`.

If `mod != 0`, the distance between the extremes cannot be split evenly among the $n-1$ gaps. No rearrangement can repair this numerical impossibility, and the helper returns false through the leading condition `mod == 0`.

Using `divmod` avoids floating-point arithmetic. A division such as $2/3$ must be rejected, not approximated and rounded. Integer quotient and remainder express the divisibility test exactly, including when input values are negative, because `an - a1` is always non-negative.

**Check that every required value is present**

When the difference is integral, the only possible sorted sequence is

$$
a_1,\ a_1+d,\ a_1+2d,\ \ldots,\ a_1+(n-1)d=a_n.
$$

The generator tests

`(a1 + (i - 1) * d) in s for i in range(1, n)`.

Because `i` runs from 1 through $n-1$, `i-1` runs from 0 through $n-2$. Thus it checks the minimum and every expected interior value. It does not explicitly test the final maximum, because `an` was obtained from the subarray and is necessarily present in its set.

`all` returns true only if every generated membership test is true. It also short-circuits: as soon as one required value is absent, later expected values are not checked.

**Why a set is sufficient even though duplicates disappear**

At first, discarding multiplicities may seem dangerous. Consider the two cases.

If $d>0$, the $n$ expected arithmetic values from $a_1$ through $a_n$ are all distinct. The generator verifies the first $n-1$, and the known maximum supplies the last. Therefore the input set contains at least $n$ distinct required values. But the queried subarray has only $n$ elements, so it cannot contain an extra duplicate or an unwanted value. Its multiset must be exactly the desired sequence.

If $d=0$, then $a_n-a_1=0$, so the subarray's minimum equals its maximum. Every input value lies between those equal extremes, which means every value is the same. Repeated membership checks for `a1` correctly accept this constant arithmetic sequence.

Thus the minimum, maximum, element count, and membership tests together recover all necessary multiplicity information.

**A successful query**

For subarray `[5, 9, 3, 7]`, the length is 4, the minimum is 3, and the maximum is 9. `divmod(9 - 3, 4 - 1)` gives difference 2 and remainder 0. The required values are 3, 5, 7, and 9. The generator checks 3, 5, and 7 in the set, while 9 is already known to be the maximum. The query returns true, corresponding to rearrangement `[3, 5, 7, 9]`.

For `[4, 6, 5, 9]`, the extreme distance is 5 and there are three gaps. The remainder from `divmod(5, 3)` is nonzero, so it is rejected immediately.

**Why the per-query decision is correct**

If `check` returns true, the difference is integral and every member of the uniquely determined arithmetic progression occurs in the subarray, with the duplicate reasoning above covering both positive and zero differences. Rearranging the subarray into increasing order therefore produces an arithmetic sequence.

Conversely, if the subarray is rearrangeable, its sorted form starts at `a1`, ends at `an`, and has exactly $n-1$ equal integer gaps. The remainder must be zero, and every expected progression value must occur in the set. Hence every condition tested by `check` succeeds.

The outer list comprehension pairs each `left` with its corresponding `right` through `zip(l, r)` and calls the helper in query order. The input contract gives equal lengths for `l` and `r`, so one Boolean is produced for every query in the original order.

## Complexity detail

For query $i$, let

$$
k_i=r[i]-l[i]+1,
$$

and let $S=\sum_i k_i$ be the total number of array positions covered across all queries, counting repeated coverage separately.

The exact source creates the query slice three times: once to build the set, once for `min`, and once for `max`. Each copy and scan is $O(k_i)$. The membership generator performs at most $k_i-1$ expected-value checks, each expected $O(1)$ in the hash set. Therefore one query is $O(k_i)$ time despite the repeated constant number of passes, and all queries take expected $O(S)$ time, matching the manifest.

For one active query, the set and temporary slice data require $O(k_i)$ memory. Python can release each temporary min/max slice after that call finishes, while the set remains until `check` returns. If $K=\max_i k_i$, peak helper space is $O(K)$, which is $O(n)$ relative to the original array length. The returned Boolean list uses $O(m)$ required output space for $m$ queries.

Hash-set membership gives expected constant time. A pathological collision model can degrade hash operations, but integer hashing under ordinary analysis supports the stated expected bound.

## Alternatives and edge cases

- **Sort every queried subarray:** After sorting, compare adjacent differences. This is straightforward but costs $O(k_i\log k_i)$ per query instead of expected linear time.
- **Boolean placement array:** Map each value to its expected progression index and mark occupied slots. This avoids hashing but still needs $O(k_i)$ storage and careful range and duplicate checks.
- **Reuse one query slice:** Store `arr = nums[l:r+1]` once, then pass it to `set`, `min`, and `max`. It has the same asymptotic bounds with fewer slice copies than the exact source.
- **Length two:** Any two numbers form an arithmetic sequence. The computed gap has denominator one, the remainder is zero, and the membership test succeeds.
- **All values equal:** `d = 0`. Minimum equals maximum, and the repeated expected value is present, so the query correctly returns true.
- **Negative values:** Only differences from the minimum are used. `an - a1` is non-negative, and set membership works identically for negative integers.
- **Fractional required gap:** A nonzero remainder rejects the query before membership checks.
- **Duplicate with positive gap:** A duplicate consumes one of the $n$ positions and forces some distinct expected value to be absent; the set checks expose that absence.
- **The maximum is not generated by `range(1, n)`:** It need not be checked because `an` came directly from the subarray. The generator covers the other $n-1$ required values.
- **Inclusive right endpoint:** Python slicing excludes its stop, so the slice ends at `l + n = r + 1` to include index `r`.
- **Parallel query arrays:** `zip` is safe because the contract guarantees equal lengths. Without that guarantee, it would silently stop at the shorter input.
