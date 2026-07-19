## General
**Map each possible value to one marker position**

Value `v` corresponds to array index $v - 1$ because all values lie in `[1, n]`. Reuse the sign at that index to record whether `v` appears, avoiding a separate presence table.

**Mark every encountered value negative**

For each current element, take its absolute value because its position may already have been negated by another value. Set `nums[value - 1]` to the negative of its absolute value. Repeated occurrences simply leave the same marker negative.

**Read unmarked positions as missing values**

After marking, a positive value at index `i` proves no input element ever mapped to that position, so $i + 1$ is missing. A negative marker proves at least one occurrence. Scanning indices from left to right naturally returns missing values in increasing order.

**Why duplicates do not disturb the encoding**

Every occurrence of the same value targets the same index, and idempotent negative marking preserves the fact of presence regardless of repetition. Taking absolute values prevents earlier markers from changing the numeric identity of later elements.

## Complexity detail
One pass marks presence and one pass collects missing values, giving $O(n)$ time. The input array stores all markers, so auxiliary space is $O(1)$ beyond the required output.

## Alternatives and edge cases
- **Cyclic placement:** swap values toward index `value - 1`, then report mismatched positions; this also takes $O(n)$ time and $O(1)$ space.
- **Hash set:** makes the final membership checks simple but uses $O(n)$ extra space.
- **Scan the full array for every candidate:** is correct but takes $O(n^2)$ time.
- **All values present:** every marker is negative and the result is empty.
- **One repeated value:** every other value is missing.
- **Duplicate occurrences:** mark the same position repeatedly without changing the result.
