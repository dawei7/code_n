## General

**For each value, only its most recent index can matter**

When scanning the array from left to right at current index `i`, every prior
occurrence of the same value has a smaller index. The closest such occurrence
is the one with the largest prior index. If that closest occurrence is more
than `k` positions away, every older occurrence is even farther away and also
fails. If it is within `k`, the required pair has already been found.

This observation means the method does not need a list of all positions for
each value. The dictionary `d` stores one entry per value: the greatest index
at which that value has appeared so far.

At the start of the iteration for `(i, x)`, the condition `x in d` asks whether
there is any earlier occurrence. If so, `d[x]` is its most recent index, and
`i - d[x]` is positive because the scan moves strictly left to right. The
absolute value from the problem is unnecessary: for a prior index `j`,
$i > j$, so $\lvert i-j\rvert = i-j$.

If the distance is at most `k`, the method immediately returns `True`. If no
prior occurrence exists or the nearest one is too far away, it assigns
`d[x] = i`. This either creates the first record for `x` or replaces an older
index with the newer, more useful one.

**Why the membership test must happen before the update**

The two indices in a valid pair must be distinct. If the code first wrote
`d[x] = i` and then checked the distance, it would compare index `i` with
itself, obtain distance zero, and incorrectly return true for every element
when `k >= 0`.

Checking first means `d[x]`, when present, can only refer to an earlier loop
iteration. Updating afterward prepares the closest possible partner for future
occurrences.

**Trace a value appearing several times**

For `nums = [1, 0, 1, 1]` and `k = 1`, the first 1 is recorded at index 0 and
0 is recorded at index 1. At index 2, value 1 was last seen at 0, but the
distance is 2, which exceeds `k`. The method does not return; it updates the
stored index for 1 from 0 to 2. At index 3, the nearest prior 1 is now at index
2, giving distance 1, so the method returns true.

Keeping index 0 instead of refreshing the entry would miss this valid pair.
Keeping both indices would be unnecessary because index 2 dominates index 0
for every future position: it is always at least as close.

For `nums = [1, 2, 3, 1, 2, 3]` and `k = 2`, each repeated value is encountered
three positions after its previous occurrence. None passes the distance test,
and after the final element the method returns false.

**Why returning true is always justified**

The method returns true only when `x` is already a dictionary key and
`i - d[x] <= k`. The key match gives
`nums[i] == nums[d[x]]`. Because the stored index came from an earlier
iteration, the indices are distinct. Their difference is positive and at most
`k`, so all conditions in the contract hold.

**Why returning false cannot overlook a pair**

After processing index `i` without returning, `d[x]` is set to `i`, and every
other dictionary entry remains the latest occurrence of its own value. Thus,
before each new iteration, the dictionary accurately stores the nearest prior
candidate for every value seen.

Suppose a valid pair existed but the scan completed without finding it. At the
later index of that pair, the dictionary contained an occurrence of the same
value at least as recent as the pair's earlier index. Its distance from the
current index was therefore no larger than the valid pair's distance and also
at most `k`. The condition would have returned true, a contradiction. Hence
finishing the loop means no valid nearby duplicate exists.

**This exact source is not the sliding-set implementation in the manifest**

The manifest describes a set containing exactly the previous `k` values. The
exact solution instead retains a last-index dictionary and never removes old
keys. Both achieve expected linear time, but their space bounds differ. A
sliding set holds at most `min(n, k)` relevant values. This dictionary can hold
every distinct value ever seen, even when `k` is small, so its exact worst-case
auxiliary space is $O(n)$.

The dictionary method has a useful conceptual advantage: it directly records
the nearest equal index and needs no eviction calculation. The document follows
that actual data flow and reports its real storage cost rather than attributing
the set implementation's bound to it. The source also assumes `List` is
available for its annotation.

## Complexity detail

Let $n$ be `len(nums)`. The loop examines each element once. Python dictionary
membership, lookup, and assignment take expected $O(1)$ time, so expected total
time is $O(n)$. Hash tables can have worse behavior under pathological
collision conditions, but expected linear time is the standard bound for
integer keys.

The dictionary holds one entry for each distinct value encountered before an
early return. There may be $n$ distinct values, so exact worst-case auxiliary
space is $O(n)$. It is not bounded by `k` because entries older than the window
are updated or retained rather than deleted. The input list is read only.

## Alternatives and edge cases

- **Sliding set of the previous `k` values:** Check membership, insert the current value, and evict the value leaving the window. This matches the manifest and uses $O(\min(n,k))$ space, but eviction order must be implemented carefully so the current comparison covers distances 1 through `k`.
- **Map each value to all indices:** Binary-search or inspect stored positions. It retains unnecessary history because the most recent occurrence always dominates older ones for a left-to-right scan.
- **Sort value-index pairs:** Equal values become grouped, after which adjacent indices within each value group can be compared. It costs $O(n\log n)$ time and $O(n)$ space and loses the simple streaming behavior.
- **Nested window scan:** Compare each element with the preceding `k` positions. It uses constant extra space but takes $O(n\min(n,k))$ time in the worst case.
- **`k = 0`:** Distinct indices always differ by at least 1, so no valid pair exists. The code may find prior equal values, but `i - d[x] <= 0` is never true and it returns false.
- **`k` at least `n - 1`:** Any duplicate anywhere in the array is close enough, so the method behaves like an ordinary duplicate detector while still storing latest indices.
- **Adjacent duplicates:** Their distance is 1 and they are reported exactly when `k >= 1`.
- **A distant duplicate followed by a nearby one:** The failed distant comparison still refreshes the index, enabling the later nearby pair to be detected.
- **Negative and large values:** Integers are valid dictionary keys, so sign and magnitude do not alter the method.
- **All values distinct:** The dictionary grows to $n$ entries, no membership condition succeeds, and the method returns false; this is the worst storage case.
- **Input preservation:** Only the dictionary changes. `nums`, its values, and their order remain untouched.
