## General

**Search without reading individual values**

Every hidden array entry has one common value except for one strictly larger entry. The API does not reveal values, but it can compare sums of two inclusive subarrays in constant time. If two compared groups have the same number of elements, their ordinary equal entries contribute the same baseline sum. The only possible difference then comes from whether one group contains the unique larger entry.

The stored solution maintains an inclusive candidate interval `[left, right]`. Its invariant is that the unique larger value lies somewhere in this interval. Initially the interval covers the entire array.

**Construct two equal comparison groups**

During each iteration, the source computes:

- `t1 = left`.
- `t2 = left + (right - left) // 3`.
- `t3 = left + ((right - left) // 3) * 2 + 1`.

The first compared subarray is `[t1, t2]`. The second is `[t2 + 1, t3]`. If `d = (right - left) // 3`, each group contains exactly $d+1$ elements. Equal sizes are essential: unequal groups could have unequal sums merely because one contains more copies of the common value.

Any remaining positions form a third region `[t3 + 1, right]`. Depending on the current length, that region may be smaller than the compared regions or empty.

**Interpret the API result**

If `compareSub` returns one, the first equal-sized group has the larger sum. Because all baseline values cancel conceptually, the unique larger entry must be in that first group. Assigning `right = t2` preserves exactly that region.

If it returns negative one, the larger entry must be in the second group. The assignment `left, right = t2 + 1, t3` discards both the first group and any remainder.

If it returns zero, neither compared group contains the special entry. If either contained it, that group's sum would be strictly larger. Therefore the answer must be in the unexamined remainder, and `left = t3 + 1` keeps that region while `right` stays unchanged.

An equal result cannot lead to an empty candidate interval on a valid input. For example, when the compared groups cover the whole current interval, one of them must contain the larger value, so their sums cannot tie.

**Why one comparison discards most candidates**

The two compared groups have equal length and the possible remainder is no larger than roughly one third of the interval. Whichever outcome occurs, the next candidate interval is at most about one third of the current size, with only constant rounding differences.

For a length-three interval, the algorithm compares the first singleton with the second singleton. A tie proves that the third position is the answer. A nonzero result selects the larger singleton immediately.

For a length-two interval, it compares the two individual values. Equality is impossible under the unique-larger guarantee, and the larger side becomes the one-element interval.

**Termination and returned index**

The loop continues while `left < right`, meaning at least two candidates remain. Every legal update strictly shrinks the candidate interval. Eventually `left == right`.

The invariant says the answer is still inside the interval, and a one-position interval contains only `left`. Returning that index is therefore correct.

**Why the 20-call limit is respected**

Reducing the candidate count by a factor close to three gives logarithmic query growth. With at most $5\cdot10^5$ positions, only about twelve base-three reductions are needed, comfortably below twenty. Rounding can alter individual interval sizes but does not threaten the limit.

This is more query-efficient than comparing individual positions. A linear scan could require hundreds of thousands of API calls and violate the contract even though its ordinary CPU work is simple.

**A complete correctness argument**

Assume before an iteration that the unique larger entry is in `[left, right]`. The algorithm compares disjoint equal-length groups. If one sum is larger, exactly that group contains the larger entry; choosing it preserves the invariant. If sums are equal, both groups contain only the common value, so the larger entry lies in the remainder; choosing the remainder also preserves the invariant.

The chosen region is strictly smaller whenever the loop condition holds. Thus termination is guaranteed. At termination, the preserved region is one position, and the invariant proves that position is the required index.

## Complexity detail

Let $N$ be the array length. Each iteration calls `compareSub` once and performs constant arithmetic and assignments. The candidate interval shrinks to roughly one third, so there are $O(\log N)$ iterations and API calls. Each API operation is guaranteed to be $O(1)$, giving $O(\log N)$ total time.

The algorithm stores only a fixed number of indices and the comparison result. It uses $O(1)$ auxiliary space and does not copy or materialize the hidden array.

The logarithm's base is irrelevant in asymptotic notation, although the exact source is closer to ternary reduction than the editorial's equal-halves presentation. For the maximum legal $N$, the call count remains below the explicit limit of twenty.

## Alternatives and edge cases

- **Equal-halves binary search:** Compare two equal halves and leave one extra element aside for odd lengths. It is also logarithmic, but it is not the exact split used by this stored solution.
- **Compare individual entries:** Singleton comparisons are valid but a linear tournament can exceed twenty API calls.
- **Unequal-size sums:** They are not comparable for locating the outlier because different counts of the common value distort the result.
- **Length two:** Two singleton groups are compared and equality is impossible.
- **Length three:** Equal singleton sums identify the unexamined third position.
- **Empty remainder:** A zero comparison is impossible because the unique larger entry must be in one compared group.
- **All values equal:** The logic relies on exactly one strictly larger value; an all-equal array would violate the contract.
- **Multiple large values:** Equal-sum reasoning would no longer identify a single region reliably, which is why the follow-up is a different problem.
- **One larger and one smaller value:** Their effects could cancel across sums, invalidating the central inference.
- **Inclusive endpoints:** Every argument passed to `compareSub` is inclusive, so the arithmetic deliberately makes the first group end at `t2` and the second begin at `t2 + 1`.
- **Read-only access:** No step attempts indexing or mutation; all information comes from the two permitted API methods.
- **Quoted type annotation:** `'ArrayReader'` allows the platform-provided interface name to be used without implementing that helper class.
