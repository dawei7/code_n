## General

The condition “equal numbers of zeroes and ones” becomes easier to track after assigning opposite contributions to the two values:

- treat each `1` as `+1`;
- treat each `0` as `-1`.

Under this transformation, a subarray has equal counts exactly when its transformed sum is zero. Every one contributes one positive unit and every zero contributes one negative unit, so the units cancel precisely when the two counts match.

Variable `s` is the transformed prefix sum while scanning `nums`. The update:

`s += 1 if x else -1`

uses the source guarantee that every `x` is either zero or one. A one takes the true branch and adds one; a zero is false in Python and subtracts one.

Let `S(i)` denote the transformed sum from index zero through `i`. A subarray from `a + 1` through `b` has transformed sum:

$$
S(b)-S(a).
$$

This difference is zero exactly when `S(b) == S(a)`. Therefore, whenever the same running balance appears at two indices, the elements between those indices contain equal numbers of zeroes and ones.

The dictionary `d` maps each balance to the earliest index at which it occurred. It begins with:

`d = {0: -1}`.

The synthetic index `-1` represents the empty prefix before the array, whose transformed balance is zero. It makes a balanced subarray beginning at index zero look like any other pair of equal prefix balances. If `s` becomes zero at index `i`, the computed length is `i - (-1) = i + 1`.

**When a balance appears for the first time.** If `s` is absent from `d`, the code records `d[s] = i`. There is not yet an earlier equal balance to form a zero-sum interval, but this index may become the left boundary for a later one.

**When a balance repeats.** If `s` is already stored at index `p`, the subarray from `p + 1` through `i` has transformed sum zero. Its length is `i - p`, and:

`ans = max(ans, i - d[s])`

keeps the longest balanced interval found so far.

The code never overwrites an existing balance index. This is essential for maximizing length. For a fixed right endpoint `i` and balance `s`, the earliest prior occurrence produces the largest distance. Replacing it with a later index could only shorten current and future candidates.

For `nums = [0, 1]`, the balances are minus one at index zero and zero at index one. The repeated zero uses the sentinel index `-1` and yields length two.

For `[0, 1, 0]`, balance minus one first appears at index zero, balance zero repeats at index one and gives length two, and balance minus one repeats at index two and also gives length two. The maximum remains two.

In `[0, 0, 1, 0, 0, 0, 1, 1]`, a negative balance can appear multiple times. The widest pair of equal-balance positions encloses the longest interval whose extra zeroes and ones cancel. The numerical value of the balance itself does not need to be zero; only equality at the two boundaries matters.

**Why every candidate found by the dictionary is valid.** Repeated balance values make the transformed subarray sum zero. Since the only transformed values are positive one for original one and negative one for original zero, zero sum means the counts are equal. The distance formula counts exactly the contiguous indices between the two prefix endpoints.

**Why the maximum valid subarray cannot be missed.** Take any balanced subarray from `l` through `r`. Its boundary prefix balances, at `l - 1` and `r`, are equal. When the scan reaches `r`, the dictionary contains the first occurrence of that balance at an index no later than `l - 1`. The candidate distance considered is therefore at least `r - l + 1`. It is a real balanced interval and cannot be longer than the true optimum, so the running maximum reaches the optimal length.

Variable `ans` starts at zero because an array may contain no nonempty balanced subarray, such as `[1, 1, 1]`. If no balance repeats at a positive distance that improves the result, zero is returned.

The algorithm solves contiguity automatically through prefix differences. It does not merely count the total zeroes and ones in the whole array; each repeated balance identifies exact interval boundaries.

## Complexity detail

Let $n$ be the array length. The solution visits every element once. Each iteration performs constant arithmetic and an expected-$O(1)$ dictionary operation, so expected running time is $O(n)$.

The balance starts at zero and changes by one per element, so at most $2n+1$ mathematical balance values are possible, and at most $n+1$ are observed prefix values. The dictionary therefore uses $O(n)$ auxiliary space, matching the manifest.

The returned integer and running variables use constant space. Python dictionary operations use the usual expected-time hashing model.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining counts while extending each start avoids a third loop but still takes $O(n^2)$ time.
- **Build an explicit transformed array:** It makes the plus-one/minus-one model visible but costs an unnecessary additional $O(n)$ array; the implementation transforms values during the scan.
- **Overwrite a repeated balance:** This loses the farthest-left boundary and can produce a shorter answer.
- **Subarray starting at index zero:** The `0: -1` sentinel gives its full length without special handling.
- **All zeroes:** The balance strictly decreases, never repeats, and the answer remains zero.
- **All ones:** The balance strictly increases with the same result.
- **Two opposite values:** Either `[0, 1]` or `[1, 0]` returns two.
- **Odd-length interval:** It cannot contain equal integer counts of two symbols, and the balance method never reports one.
- **Several maximum intervals:** Only their common maximum length is requested.
- **Boolean conditional:** It is safe here because the input domain contains only zero and one.
- **Negative balances:** Dictionary keys may be negative; they carry the same prefix-state meaning as positive balances.
