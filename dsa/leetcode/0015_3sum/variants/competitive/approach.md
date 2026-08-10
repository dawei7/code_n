## General

**Fix the largest triplet value, then search the prefix**

This variant sorts `nums` but scans pivot index `i` from right to left:

```python
for i in reversed(range(2, len(nums))):
```

`nums[i]` is the largest value in the candidate triplet. The two remaining values must lie in `nums[0:i]` and sum to

$$
\texttt{target}=-\texttt{nums[i]}.
$$

Pointers `left = 0` and `right = i - 1` search that sorted prefix. This is the mirror image of fixing the smallest value and searching its suffix.

**Skip duplicate largest values**

Because `i` decreases, a duplicate pivot immediately to its right has already been processed:

```python
if i + 1 < len(nums) and nums[i] == nums[i + 1]:
    continue
```

The earlier search used the same pivot value with an equal or larger prefix of available indices, so repeating it could add only duplicate value triplets.

**Use monotonic pair sums**

Compare `nums[left] + nums[right]` with `target`.

- A smaller sum requires `left += 1`; moving `right` left would only decrease it.
- A larger sum requires `right -= 1`; moving `left` right would only increase it.
- Equality yields `[nums[left], nums[right], nums[i]]`, already sorted by value.

After equality, both pointers move inward. Repeated values are then skipped relative to the just-used values:

```python
while left < right and nums[left] == nums[left - 1]:
    left += 1
while left < right and nums[right] == nums[right + 1]:
    right -= 1
```

This prevents the same pair values from being emitted again for the pivot. The pivot duplicate check prevents repetition across outer iterations.

**Why pointer elimination is safe**

If the current pair sum is below `target`, every pair using the same `left` and a right index no greater than the current `right` is also too small. Discarding that left endpoint loses no solution. The symmetric statement proves the right move when the sum is too large.

Thus the pointers visit or safely dominate every possible pair in the prefix. Any pair meeting the target is found before one of its endpoints can be eliminated.

**Trace `[-1,0,1,2,-1,-4]`**

The sorted array is `[-4,-1,-1,0,1,2]`.

- With pivot `2`, the target is `-2`. The prefix search finds `-1 + -1`, producing `[-1,-1,2]`.
- With pivot `1`, the target is `-1`. It finds `-1 + 0`, producing `[-1,0,1]`.
- Subsequent pivots and pointer comparisons produce no new value triplet; duplicate pivots are skipped.

Unlike the forward variant, this code has no `pivot > 0` early break because positive largest values are often necessary to balance negative values. Reverse orientation changes which sign-based pruning is valid.

**Why fixing the largest value still covers triples with duplicates**

Sorting gives every value triplet a nondecreasing representation `(a, b, c)`. The reverse outer loop chooses `c`; the inner pointers search positions strictly before its selected occurrence for `a` and `b`. If `b == c`, there must be two distinct occurrences in the array, and choosing the rightmost copy as pivot leaves the other copy available before `i`. Similarly, `a == b` is allowed because `left` and `right` are distinct indices even when their values match.

The algorithm therefore deduplicates **value combinations**, not input values. It never removes all copies before they have a chance to occupy separate triplet positions. Duplicate skipping occurs only after one representative combination has been emitted or after an equal pivot's complete search has already happened.

**Why both pointers move after equality**

Once `nums[left] + nums[right] == target`, keeping the same left value while decreasing `right` can only reduce the pair sum, and keeping the same right value while increasing `left` can only increase it. Neither can create a different pair with the same target until a value changes on both relevant sides. Moving both pointers, then skipping repeats, advances directly to the next possible distinct value combination.

**Why output uniqueness and completeness coexist**

Every sorted triplet has one largest value occurrence. The first processed occurrence of that value searches all earlier indices using safe monotonic elimination. Duplicate skipping happens only after a value combination has been recorded or after the same pivot value has already had a complete search. It therefore removes redundant representations without removing the first path to any distinct triplet.

## Complexity detail

Let $n$ be the input length.

- **Time complexity: $O(n^2)$.** Sorting is $O(n\log n)$. Each pivot performs one linear two-pointer pass over its prefix, for a quadratic total.
- **Space complexity: $O(n)$ using the manifest's conservative accounting for sorting.** The two-pointer work itself is $O(1)$ auxiliary space. The source comment's $O(1)$ convention excludes output and assumes in-place sorting without counting its implementation workspace.

The output may contain $O(n^2)$ triplets and is separate from auxiliary-space analysis.

## Alternatives and edge cases

- **Forward pivot orientation:** Fix the smallest value and search its suffix; it supports an early break when the pivot becomes positive and is often the more familiar presentation.
- **`Solution2` in the same file:** Implements that forward orientation on a sorted copy rather than sorting the caller's list in place.
- **Hash-set pair search:** Retains $O(n^2)$ time but introduces $O(n)$ explicit storage per pivot or reusable marker logic.
- **All zeros:** The largest-zero pivot produces one triplet, and duplicate checks suppress repetitions.
- **Repeated pivot values:** Only the rightmost occurrence is processed in the reverse scan.
- **Repeated pair values:** Both left and right duplicate loops run after a successful match.
- **No solution:** Pointers cross without appending, and the result remains empty.
- **Distinct indices:** `left < right < i` is maintained for every emitted triplet.
- **Input mutation:** The selected `Solution` sorts `nums` in place; `Solution2` would avoid that by using `sorted(nums)`.
- **Equal largest values:** The rightmost copy is processed as pivot first, leaving earlier copies available as pair elements when a valid triplet needs them.
- **Both-pointer movement:** After a match, changing only one endpoint cannot preserve the target with the other fixed sorted value; moving both begins the search for a genuinely new pair.
