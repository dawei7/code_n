## General

**Eligibility depends on total frequency**

A number is eligible only if it appears exactly once in the entire array. It is not enough to be different from its immediate neighbors or unique within a prefix.

`Counter(nums)` performs one complete frequency pass and maps each distinct value to its total occurrence count.

As Counter reads the array, every occurrence increments exactly one entry. After the scan, `cnt[x]` equals the number of indices whose value is `x`. It contains no positional information because position is irrelevant once total frequency is known.

**Filter the frequency map**

The generator:

`x for x, v in cnt.items() if v == 1`

yields exactly those values whose frequency is one. Values occurring twice or more are skipped, regardless of how large they are.

The generator is lazy, so it does not first allocate a list of all unique candidates. `max` consumes candidates one at a time while retaining the greatest.

Dictionary iteration order does not matter. `max` compares numeric values and produces the same result whether a large unique value is encountered early or late.

**Use a safe default**

If no value has frequency one, the generator is empty. Calling `max` without a default would raise an exception.

`default=-1` supplies the required failure result. Input values are between zero and one thousand, so negative one cannot be confused with a legitimate answer. Zero remains a valid unique maximum when it is the only eligible value.

The default is consulted only when the generator yields nothing. It is not inserted as an artificial candidate alongside legal values, so it cannot influence a nonempty maximum.

**Why maximum must be taken after filtering**

The largest array value may be repeated. For `[5,7,3,9,4,9,8,3,1]`, nine is globally largest but has frequency two. Filtering removes it, and the maximum among remaining one-frequency values is eight.

Taking the array maximum first and returning failure when it repeats would be wrong because a smaller value may still be unique.

For `[9,9,8,8]`, the frequency map contains nine mapped to two and eight mapped to two. The filter yields no values and default negative one is used. For `[0,1,1]`, only zero is yielded, so max correctly returns zero.

**Complete correctness argument**

Counter records exact total frequency for every value. The generator includes a value if and only if that frequency equals one, so its produced set is precisely the eligible set defined by the problem.

When the set is nonempty, `max` returns its greatest member. When empty, the safe sentinel is returned. These are exactly the two contract cases.

**A bounded-value perspective**

The source values lie in a small range, but the hash-map method does not depend on that bound for correctness. It stores only values actually present.

A fixed counting array could use the range directly and scan from one thousand down to zero. The protected code instead uses general-purpose counting and maximum selection.

This sparse representation can use less storage when only a few different values occur, even though the asymptotic bounded-domain maximum is still proportional to the value range.

## Complexity detail

Let $n$ be array length and $u$ the number of distinct values. Counter construction takes expected $O(n)$ time. Scanning its items takes $O(u)$, so exact expected time is $O(n+u)$, which fits the manifest’s $O(n+V)$ bound because $u\le V$.

Counter stores $u$ entries, giving $O(u)$ space and at most $O(V)$ under the fixed value range. The generator itself uses constant iteration state.

The returned scalar and running maximum require constant storage.

Any correct algorithm must inspect all $n$ occurrences in the worst case. A duplicate of the current best candidate could appear at the final index, so stopping early could return an ineligible value. The linear input scan is therefore asymptotically necessary.

Counter lookup and increment use expected constant hash-table time. With integer keys in this bounded range, those operations are straightforward and deterministic in value equality.

## Alternatives and edge cases

- **Fixed frequency array:** Count indices zero through one thousand, then scan backward for count one. This realizes $O(n+V)$ time and $O(V)$ space directly.
- **Sorting:** Sort values, identify runs of length one, and retain the largest. It costs $O(n\log n)$ and may mutate input.
- **Repeated list count:** Calling `nums.count(x)` for many values can cost $O(n^2)$.
- **One element:** Its frequency is one, so it is returned.
- **No unique values:** The generator is empty and default negative one is returned.
- **Unique zero:** Zero is returned, not confused with failure.
- **Largest value repeated:** It is skipped and the next greatest eligible value wins.
- **Several unique values:** `max` selects the greatest numeric value, independent of input order.
- **All values distinct:** The ordinary array maximum is returned.
- **Nonempty input:** Counter always has at least one entry, though the candidate generator may be empty.
- **Sentinel safety:** Negative one lies outside the legal nonnegative domain.
- **Input preservation:** Counter reads the array without changing it.
