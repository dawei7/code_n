## General

**Express the array total in terms of the three roles.** Let $P$ be the sum of the $n-2$ special numbers, and let $x$ be a candidate outlier. The array also contains a separate element whose value equals $P$. Therefore the total sum `s` satisfies

$$
s=P+P+x=2P+x.
$$

If `x` is chosen as the outlier, the only possible sum-element value is

$$
P=\frac{s-x}{2}.
$$

This identity removes any need to guess which $n-2$ indices are special.

**Count values so index multiplicity can be checked.** `Counter(nums)` records how many indices carry each value. Roles must occupy distinct indices even though their numeric values may coincide. A set would lose the information needed when the outlier value equals the sum-element value.

The source iterates once over each distinct candidate `x` with frequency `v`. Testing distinct values is sufficient because all indices holding the same numeric outlier produce the same returned value, and frequency is already known.

**Reject candidates whose remaining sum is odd.** Set `t = s - x`. It should equal `2P`. If `t % 2` is nonzero, no integer sum element can satisfy the equation, so this `x` is impossible.

Python's modulo test works for negative totals too: an odd negative integer still has nonzero remainder modulo two.

**Require the computed sum element to exist.** When `t` is even, candidate sum value is `t // 2`. `cnt[t // 2] == 0` means no array index can play that role, so the candidate is rejected.

If the value exists and differs from `x`, the roles automatically use different values and therefore different indices.

**Handle equal-valued roles with the frequency guard.** When `x == t // 2`, one occurrence must serve as outlier and another as the sum element. Condition `v > 1` requires at least two indices. This is why example `[1,1,1,1,1,5,5]` can use one 5 as the sum and the other 5 as the outlier.

The test

`if x != t // 2 or v > 1`

accepts exactly the distinct-index possibilities.

**Why the remaining indices automatically form the special set.** After removing one candidate-outlier index and one sum-element index, the remaining values sum to

$$
s-x-P=(2P+x)-x-P=P.
$$

There are exactly $n-2$ remaining indices. Their sum equals the selected sum element, so they satisfy the definition of the special numbers. No additional per-number property is required.

**Keep the largest accepted value.** `ans` begins at negative infinity so every legal integer candidate can replace it, including negative outliers. Each accepted `x` updates `max(ans,x)`. The input guarantee says at least one potential outlier exists, so negative infinity cannot be returned under the contract.

**Trace a negative-valued case.** For `[-2,-1,-3,-6,4]`, total is $-8$. Trying outlier 4 leaves `t=-12` and computes $P=-6$, which exists as a distinct array value. Removing 4 and -6 leaves values summing to -6, so 4 is valid.

**Why every valid outlier is found.** Any genuine outlier obeys `s=2P+x`, so its iteration computes the actual sum-element value and passes parity, presence, and index-multiplicity checks. Conversely, every candidate passing those checks leaves exactly $n-2$ indices summing to the chosen sum element. The algebraic test is therefore both necessary and sufficient.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values. Computing `s` and `cnt` takes $O(n)$ time. Iterating over `u <= n` counter items takes $O(u)$ expected time, for total expected $O(n)$.

The counter stores $O(u)$ entries, giving $O(n)$ worst-case auxiliary space. `Counter` lookups are expected $O(1)$. The source also requires `inf` and `List` imports.

## Alternatives and edge cases

- **Try every pair of excluded indices:** It directly assigns outlier and sum roles but costs $O(n^2)$ before even checking remaining sums.
- **Sort and use two pointers:** Value bounds permit alternatives, but frequency counting makes the algebraic condition direct and linear.
- **Candidate equals sum value:** At least two occurrences are mandatory.
- **Candidate differs from sum value:** One occurrence of each is enough.
- **All roles share values:** Special numbers may also equal the role values; only the outlier and sum indices must be separately available.
- **Negative total:** Parity and integer division remain valid in Python.
- **Odd remainder:** It cannot equal twice an integer special sum.
- **Duplicate candidate indices:** Iterating distinct values once is sufficient because the answer asks for the numeric outlier.
- **All-negative array:** Initializing with zero would be wrong; negative infinity correctly permits a negative largest answer.
- **At least one solution:** The contract prevents the sentinel from escaping.
- **Zero as a role value:** Counter presence and multiplicity rules handle it normally.
- **Largest potential outlier:** The method considers every valid value rather than returning the first.
- **Distinct indices, not distinct values:** The frequency condition captures this crucial distinction.
- **No reconstruction needed:** Once the sum identity holds, all remaining indices are necessarily the special set.
- **Input preservation:** Summation and counting do not modify `nums`.
