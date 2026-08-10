## General

**Count presence by array, not occurrences inside an array**

The requirement asks whether a value appears in at least two of the three arrays. Repeating a value several times inside `nums1` must still contribute only one array-presence vote.

The source enforces this distinction immediately by converting each input to a set:

`s1, s2, s3 = set(nums1), set(nums2), set(nums3)`.

A set records whether a value occurs, not how many times it occurs. For example, `[1,1,1]` becomes `{1}`, so it gives value one exactly one presence vote.

**Use the small value domain to enumerate candidates**

Every input value is between one and one hundred inclusive. Instead of building another union set, the source simply iterates `i` through `range(1, 101)`. This visits every value that could possibly appear and no irrelevant value outside the contract.

For a candidate `i`, each expression `i in s1`, `i in s2`, and `i in s3` produces a Boolean. Python Booleans behave like integers in addition: true contributes one and false contributes zero. Thus

`(i in s1) + (i in s2) + (i in s3)`

is exactly the number of distinct input arrays containing `i`.

The list comprehension retains `i` only when that count is greater than one. “Greater than one” means two or three, precisely matching “at least two.”

**Why the output is distinct automatically**

The comprehension considers each integer from one through one hundred once. A qualifying value can therefore be appended only once, regardless of how many times it appeared in an input array or whether it appeared in all three arrays.

No later `distinct` operation is necessary. Uniqueness comes from both the single candidate iteration and the membership-only sets.

**Trace the first example**

For `nums1 = [1,1,3,2]`, `nums2 = [2,3]`, and `nums3 = [3]`, the sets are `{1,2,3}`, `{2,3}`, and `{3}`.

Candidate one has membership count one, so it is excluded. Candidate two has count two, so it is included. Candidate three has count three, so it is included. Every other candidate has count zero.

The exact source returns `[2,3]` because it scans in ascending order. The example may display another order, but the contract explicitly permits any order.

**Why duplicates cannot create a false positive**

Suppose value five occurs ten times in `nums1` and nowhere else. `s1` contains five once, while `s2` and `s3` do not contain it. Its Boolean sum is one, so it is correctly rejected.

By contrast, if five occurs once in `nums1` and once in `nums3`, its count is two and it is accepted. The method responds to how many arrays contain a value, exactly as required.

**Why every returned value is correct**

Take any value in the returned list. It passed the condition that its three membership indicators sum to more than one. Therefore it belongs to at least two input sets, and set membership means it appears in those corresponding arrays. The value satisfies the requested property.

Conversely, take any value that appears in at least two arrays. The constraints place it between one and one hundred, so the range iteration reaches it. Its membership sum is at least two, making the filter true, so it is returned.

These two directions show that the list contains all and only qualifying values. Since each candidate is visited once, the distinctness requirement is also satisfied.

**Why a fixed-domain scan is appropriate here**

The candidate loop always performs one hundred iterations, which is independent of the input lengths. This is efficient specifically because the value range is tightly bounded by the constraints.

If values could be arbitrary 64-bit integers, scanning the entire numeric interval would be impossible. In that setting, iterating over `s1 | s2 | s3` would preserve the same membership logic. Here the direct one-to-one-hundred scan is simpler and additionally returns a deterministic ascending order.

**Input and output ordering**

Converting to sets discards input order, but input order has no role in the definition. The output may use any order. The range scan happens to choose ascending numeric order, making the result stable across runs without requiring a separate sort.

None of the original lists is modified. Set construction creates independent containers.

## Complexity detail

Let $S$ be the total number of elements across the three input arrays. Constructing the three sets takes expected $O(S)$ time. The candidate loop performs exactly one hundred iterations with three expected-$O(1)$ hash lookups each, which is $O(1)$ under the fixed value bound. Total expected time is $O(S)$.

The sets contain at most the number of distinct input values, bounded by both $S$ and one hundred, and the result contains at most one hundred values. In input-sensitive notation, space is $O(S)$; under the stated fixed domain it is also bounded by a constant. The manifest's $O(S)$ space is a valid general upper bound.

## Alternatives and edge cases

- **Union-set iteration:** Iterate over `s1 | s2 | s3` and apply the same membership sum; useful when the value domain is not bounded.
- **Bitmask per value:** Record one bit for each input array and select masks with at least two set bits; also linear and easily generalized.
- **Raw occurrence counter:** Incorrect unless each input is deduplicated first, because duplicates in one array must not count as several arrays.
- **Pairwise set intersections:** Return `(s1 & s2) | (s1 & s3) | (s2 & s3)`; concise and logically equivalent.
- **Value present in all three arrays:** Its membership count is three, so it is included once.
- **Value present twice in one array only:** Its set membership count is one, so it is excluded.
- **No qualifying values:** The comprehension returns an empty list.
- **Every value qualifies:** Each is emitted once in ascending order.
- **Boundary values one and one hundred:** Both are included in `range(1, 101)`.
- **Arbitrary input order:** Set membership and the final candidate scan are unaffected.
- **Allowed output order:** Ascending output is valid even when examples show a different order.
- **Input preservation:** New sets are built without changing any input list.
