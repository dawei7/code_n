## General
**Use each value as an array index**

Because every value `v` lies in `[1, n]`, index $v - 1$ can store whether `v` has been seen. This reuses the input array instead of allocating a hash set.

**Encode visitation in the target sign**

For each element, take its absolute value because earlier visits may have negated it. Inspect `nums[v - 1]`: if it is positive, negate it to mark the first occurrence; if it is already negative, this is the second occurrence and `v` belongs in the output.

**Why every duplicate is reported once**

The first occurrence of each value changes its unique marker position from positive to negative. The second finds that marker negative and is reported. The contract forbids a third occurrence, so no value can be appended more than once. Values appearing once only perform the initial mark.

## Complexity detail
The algorithm performs constant work for each of `n` elements, giving $O(n)$ time. It modifies the input and uses only scalar variables beyond the required output, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Cyclic placement:** swap values toward index `value - 1`, then collect mismatches; this also takes $O(n)$ time and $O(1)$ auxiliary space.
- **Hash set:** gives $O(n)$ expected time but uses $O(n)$ additional space.
- **Count each value by rescanning:** is correct but takes $O(n^2)$ time.
- **No duplicates:** every marker changes sign once and the output stays empty.
- **All values paired:** every distinct value is reported on its second occurrence.
- **Already negative markers:** always take the absolute value of the current element before deriving its index.
