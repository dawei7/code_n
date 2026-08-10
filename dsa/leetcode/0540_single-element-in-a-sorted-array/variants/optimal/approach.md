## General

Before the single element, duplicate pairs occupy index positions `(0, 1)`, `(2, 3)`, and so on: each pair begins at an even index. The single element shifts every later pair by one position, so after it, pairs begin at odd indices.

This change in pairing alignment creates a monotone boundary that binary search can locate.

The search interval is inclusive, initialized as `l = 0` and `r = len(nums) - 1`. The invariant is that the unique element lies somewhere from `l` through `r`.

**Use `mid ^ 1` to select the expected partner.** Bitwise XOR with one flips only the lowest bit of a nonnegative integer:

- if `mid` is even, `mid ^ 1` equals `mid + 1`;
- if `mid` is odd, `mid ^ 1` equals `mid - 1`.

Thus `nums[mid ^ 1]` is the element paired with `nums[mid]` under the normal “even index followed by odd index” alignment that exists before the singleton.

This compact expression avoids separate even/odd branches while comparing the exact neighbor relevant to the alignment test.

**Matching the expected partner means the singleton is later.** If:

`nums[mid] == nums[mid ^ 1]`,

then `mid` belongs to a correctly aligned pair. All elements through the later index of that pair lie before the alignment break, so the singleton must be to the right. The code assigns:

`l = mid + 1`.

When `mid` is even, this moves to the odd partner index rather than explicitly skipping both positions. That may look surprising, but the next interval still excludes `mid` and retains the singleton; subsequent midpoint tests continue shrinking it correctly. When `mid` is odd, the matching partner is `mid - 1` and `mid + 1` moves past the complete pair.

**A mismatch means the break is at or before `mid`.** If `nums[mid] != nums[mid ^ 1]`, the expected pre-singleton pairing has failed. Either `mid` is the singleton or the singleton occurred earlier and shifted this position's real partner to the opposite alignment. The method keeps `mid` by assigning:

`r = mid`.

It must not use `mid - 1` because `mid` itself may be the answer.

For `[1, 1, 2, 3, 3, 4, 4, 8, 8]`, suppose a midpoint comparison finds four aligned with its expected partner in the suffix or finds a mismatch after the singleton shift. Each result discards the half whose pair structure proves it cannot contain the single two. Repetition narrows the interval to index two.

For `[3, 3, 7, 7, 10, 11, 11]`, pairs at indices zero through three are normally aligned. Index four contains ten and does not match its expected index-five value eleven, locating the boundary at or before four. The remaining search returns ten.

**Why the array length is odd.** There is one singleton plus an even number of paired occurrences, so the total length is odd. The final valid index can stand alone when all earlier pairs are aligned.

**Why `mid ^ 1` stays in bounds.** While `l < r`, the interval contains at least two indices. The overall odd-length structure and the search updates prevent an unpaired out-of-range comparison at termination; the loop stops before comparing when one index remains. For an even `mid` at the current nontrivial range, its next index is available, and for an odd `mid`, its previous index exists.

**Why the loop terminates.** On a match, `l` becomes at least `mid + 1`, strictly shrinking from the left. On a mismatch, `r` becomes `mid`, strictly shrinking from the right because `mid < r` when `l < r` under floor midpoint calculation. Eventually `l == r`.

At termination, the invariant says the singleton lies in the one-index interval, so `nums[l]` is returned.

**Why numeric sorting matters indirectly.** Equal occurrences are adjacent because the array is sorted. The binary search uses pair adjacency and alignment rather than comparing magnitudes. Once those adjacent-pair guarantees hold, the alignment transition is what drives the search.

The solution uses no frequency map and never modifies the array.

## Complexity detail

Let $n$ be the array length. Each iteration reduces the search interval to at most roughly half its previous size, so there are $O(\log n)$ iterations. Each performs constant arithmetic and at most one value comparison, giving $O(\log n)$ time.

The variables `l`, `r`, and `mid` use constant storage. There is no recursion or auxiliary container, so space is $O(1)$. These bounds match the manifest and the explicit problem requirement.

## Alternatives and edge cases

- **Linear pair scan:** Examine indices zero, two, four, and so on until a pair fails. It uses constant space but takes $O(n)$ time.
- **XOR all values:** Duplicate values cancel and reveal the singleton in $O(n)$ time and $O(1)$ space, but do not meet the logarithmic requirement.
- **Frequency map:** It works for unsorted input but costs linear time and space.
- **Force `mid` even:** Comparing `nums[mid]` with `nums[mid + 1]` after adjusting parity is an equivalent, more explicit binary-search formulation.
- **Singleton at index zero:** The first expected pair mismatches, repeatedly moving `r` left until zero remains.
- **Singleton at the last index:** Every preceding expected pair matches, moving `l` right to the final position.
- **Array of length one:** The loop never runs and that sole value is returned.
- **Large repeated values:** Only equality and indices matter; numeric magnitude does not.
- **No out-of-bounds partner at termination:** The loop stops as soon as one candidate remains.
- **Distinct singleton guarantee:** It ensures exactly one alignment break and makes the predicate monotone.
