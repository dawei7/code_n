## General

Checking every subarray would be quadratic, and checking each candidate for palindromicity could make it cubic. The source instead adapts Manacher's algorithm from strings to an integer array. Equality between array values plays exactly the same role as equality between characters.

Manacher's algorithm finds the longest odd palindrome and the longest even palindrome around every possible center in total linear time. Prefix sums then evaluate each chosen palindrome's element sum in constant time.

**Why only the longest palindrome at each center matters**

Every shorter palindrome with a fixed center is nested inside the longest palindrome for that center. Extending an odd or even palindrome by one radius adds two array values.

All `nums[i]` are positive, so adding those outer values strictly increases the sum. Therefore, among palindromes sharing a center, the longest one always has the greatest sum.

This positivity fact is essential. With negative values, a shorter inner palindrome could have a larger sum, and scoring only the maximum radius would be insufficient.

Every palindromic subarray has either an odd center at an element or an even center between two elements. Evaluating the longest palindrome for every center therefore includes a palindrome whose sum is at least that of every possible candidate.

**Prefix sums for constant-time range totals**

The source builds:

```python
prefix[0] = 0
prefix[i + 1] = prefix[i] + nums[i]
```

For a half-open range `[a,b)`, its sum is:

$$
\texttt{prefix}[b]-\texttt{prefix}[a].
$$

This avoids walking across a palindrome after its boundaries have been found.

**Odd-radius definition**

For an odd palindrome centered at index `c`, define radius `R` so the palindrome covers:

$$
[c-R+1,\ c+R-1].
$$

Radius one is the single element `nums[c]`. A radius-two palindrome contains three elements, and so on.

The array `odd[c]` stores the maximum such radius.

**The rightmost known odd palindrome**

While scanning centers from left to right, `[left,right]` stores the inclusive boundaries of the palindrome reaching farthest right among those already found.

If the new `center` lies beyond `right`, no previously known symmetry helps, so expansion starts with radius one.

If `center\le right`, reflect it across the midpoint of `[left,right]`:

$$
\texttt{mirror}=left+right-center.
$$

The palindrome at `mirror` tells how far symmetry is already guaranteed around `center`. However, that copied radius cannot extend beyond the known right boundary. The safe initial value is:

```python
min(
    odd[left + right - center],
    right - center + 1,
)
```

This skips comparisons already implied by the larger palindrome.

**Expanding an odd center**

With current radius `R`, the next possible pair lies at:

$$
center-R
\qquad\text{and}\qquad
center+R.
$$

The source expands while both indices are inside the array and their values are equal. Each successful pair increases `radius` by one.

After expansion, the longest odd palindrome begins at:

$$
start=center-radius+1
$$

and ends inclusively at `center+radius-1`. The half-open end for prefix sums is:

$$
end=center+radius.
$$

That explains:

```python
prefix[end] - prefix[start]
```

If this palindrome extends beyond the current `right`, the source replaces `left` and `right` with its boundaries.

**Even-radius definition**

An even palindrome uses a center position `c` representing the gap between indices `c-1` and `c`. Radius `R` covers:

$$
[c-R,\ c+R-1].
$$

Radius zero means there is no nonempty even palindrome at that gap. Radius one covers the equal pair `nums[c-1],nums[c]`.

The source stores maximum values in `even[c]`.

**Reusing even symmetry**

The even scan maintains another rightmost inclusive palindrome `[left,right]`.

If `center>right`, it starts at radius zero. Otherwise the mirrored even center is:

$$
left+right-center+1.
$$

The extra one comes from reflecting a boundary between elements rather than an element index. The safe radius is:

```python
min(
    even[left + right - center + 1],
    right - center + 1,
)
```

The next pair to test lies at:

$$
center-radius-1
\qquad\text{and}\qquad
center+radius.
$$

After expansion, the half-open palindrome interval is:

$$
[center-radius,\ center+radius),
$$

so its sum is:

```python
prefix[center + radius]
- prefix[center - radius]
```

Radius-zero entries are not scored because they represent an empty interval. Nonempty single-element palindromes are already covered by the odd scan.

**Why mirror reuse is valid**

Within a known palindrome `[left,right]`, positions symmetric around its center have equal surrounding values as long as both sides remain inside the known boundary. A palindrome already measured at the mirror center therefore transfers to the new center up to either:

- the mirror's full known radius; or
- the distance to `right`.

Only comparisons beyond that guaranteed portion must be performed directly.

If expansion crosses the old right boundary, the newly discovered palindrome becomes the new rightmost one. This is the mechanism that makes total expansion linear rather than quadratic.

**Why every palindrome is represented**

Every odd-length palindrome has one element center and is contained in the maximum `odd` palindrome at that center. Every even-length palindrome has one gap center and is contained in the corresponding maximum `even` palindrome.

Because values are positive, containment also means no larger sum than the maximum-radius palindrome at that center. Taking `best` across both scans therefore yields the global maximum palindromic-subarray sum.

The odd radius is always at least one, so every single element is evaluated. This guarantees a valid nonempty result even when no adjacent values form a longer palindrome.

**A simple odd example**

For `[1,2,3,2,1]` centered at index two:

- radius one covers `[3]`;
- matching twos extend to radius two;
- matching ones extend to radius three;
- boundaries stop further expansion.

The interval is `[0,5)` and its prefix-sum difference is nine.

For `[10,10]`, the odd scan sees two singletons, while the even center one expands to radius one and scores the full sum twenty.

## Complexity detail

Let `n` be the array length.

Building prefix sums takes `O(n)` time. The odd and even Manacher scans each take `O(n)` time. Although each contains a `while` expansion, mirror initialization skips already known interior comparisons, and successful expansion beyond the current right boundary can advance that boundary at most `n` times per scan. Failed boundary comparisons also occur only a constant number per center.

Total time complexity is `O(n)`.

The prefix array, odd-radius array, and even-radius array each contain `O(n)` integers. All other state is scalar, so auxiliary space complexity is `O(n)`.

The source does not modify `nums`.

The result may exceed 32-bit range, but Python integers preserve the exact prefix sums and answer.

## Alternatives and edge cases

- **Enumerate all subarrays:** There are `O(n^2)` candidates before palindrome checking. This is too slow for `n=10^5`.

- **Expand independently around every center:** This is simple and correct but can take `O(n^2)` time on an array whose values are all equal. Manacher reuses symmetry.

- **String conversion:** Joining integer values into text can confuse multi-digit value boundaries and is unnecessary. Manacher operates directly on array equality.

- **Rolling hashes:** Hashes can test palindrome candidates quickly, but finding the maximum sum would still need careful candidate search and collision handling. Exact Manacher comparisons are linear.

- **Score every smaller radius:** Positivity makes nested extensions strictly increase sum, so only the longest radius per center matters.

- **Negative values outside the contract:** With negatives, the longest palindrome at a center may not have the largest sum. This source relies on all values being positive.

- **One element:** Odd radius one scores that element, which is the answer.

- **No equal adjacent values:** Even radii remain zero, but every singleton odd palindrome remains valid; the largest value wins.

- **All values equal:** Every possible centered expansion succeeds as far as the boundary. Manacher still runs in linear time, and the full array is the maximum-sum palindrome.

- **Odd palindrome boundaries:** Radius `R` maps to inclusive endpoints `center-R+1` and `center+R-1`; prefix end is one farther.

- **Even center interpretation:** `center` is the gap before `center`, so radius `R` maps to `[center-R,center+R)`.

- **Radius-zero even state:** It is empty and must not update `best`.

- **Best initialized to zero:** Every array value is positive and at least one odd singleton is processed, so `best` becomes a valid positive sum.

- **Mirror clipping:** Copying a mirror radius without limiting it to `right-center+1` could claim equality beyond the known palindrome and skip necessary checks.

- **Separate odd and even scans:** One radius convention cannot directly represent both center types without transformed separators. The source keeps two explicit arrays.
