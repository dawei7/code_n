## General

**Use membership for the successor test.** Build a set from `arr`, then scan the original array. For each occurrence `value`, add one exactly when `value + 1` belongs to the set. The set turns each successor lookup into expected constant time.

**Keep the original array for multiplicity.** The set deliberately discards duplicate keys because the contract asks only whether a successor exists. The scan deliberately retains every array position, so all copies of a qualifying value are counted. Successor occurrences are never consumed or paired: one copy of `value + 1` is sufficient for any number of copies of `value`.

For each position, the membership test is true precisely when that position satisfies the problem condition. Summing those Boolean results therefore adds one for every qualifying occurrence and zero for every other occurrence, which yields exactly the requested count.

## Complexity detail

Let $n$ be the length of `arr`. Constructing the set and scanning the array take expected $O(n)$ time. The set contains at most $n$ distinct values and uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Frequency map:** Count each value, then add the frequency of every key whose successor is present. This has the same expected $O(n)$ time and $O(n)$ space but stores counts that the direct scan does not need.
- **Repeated list membership:** Evaluating `value + 1 in arr` for every position is functionally correct but can rescan the array each time and take $O(n^2)$ time.
- **Sorting:** After sorting, runs of equal values can be compared with later runs, but the method takes $O(n\log n)$ time and requires more careful multiplicity bookkeeping.
- **Duplicate qualifying values:** Every copy of `x` counts when `x + 1` exists, even if the successor occurs only once.
- **Duplicate successors:** Extra copies of `x + 1` do not cause one occurrence of `x` to count more than once.
- **Singleton array:** Its only value has no different successor in the array, so the answer is zero.
- **Boundary values:** `0` can qualify when `1` occurs. A value of `1000` cannot qualify because the constraints exclude `1001`, while `999` can still qualify when `1000` is present.
