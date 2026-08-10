## General

**Sort to expose which values can correspond**

Two elements are removed from `nums1`, and then every remaining value is shifted by the same integer $x$. Sorting both arrays is useful because a uniform shift preserves order. After the removals, the surviving values of sorted `nums1` must match sorted `nums2` in order after adding $x$.

The smallest value `nums2[0]` must come from one of the first three values of sorted `nums1`. It cannot come from a later index: if it came from index 3 or beyond, at least the three earlier values would all need to be removed, but exactly two removals are available.

Therefore, there are only three possible shifts:

$$
x=\texttt{nums2[0]}-\texttt{nums1[i]},\qquad i\in\{0,1,2\}.
$$

The outer loop tests precisely these candidates and keeps the minimum valid one.

**Greedily validate one candidate**

For a fixed $x$, helper `f(x)` uses two pointers:

- `i` scans every value of sorted `nums1`;
- `j` points to the next unmatched value of sorted `nums2`;
- `cnt` counts scanned `nums1` values treated as removed.

If `nums1[i] + x` equals `nums2[j]`—written in the code as `nums2[j] - nums1[i] == x`—the values can correspond, so `j` advances. Otherwise, the current `nums1[i]` cannot match the next required target value, and `cnt` increases. In both cases, `i` advances.

Because the arrays are sorted, rejecting a mismatch greedily is safe. If the shifted current source is smaller than the next target, it cannot match any later, even larger target, so it must be removed. If it is larger, it cannot match the current target or repair a target missed by skipping it; a valid candidate can only exist if earlier removals and subsequent equal values permit the ordered matching. More generally, the standard subsequence matching rule—match the earliest possible equal source—leaves the most source values available for all later targets and never uses more removals than an alternative.

The helper accepts when `cnt <= 2`. The length relation makes this sufficient even though the loop can stop as soon as `j == len(nums2)`. If all target values have matched early, any unscanned source values are simply the remaining removals. Since `len(nums1) = len(nums2) + 2`, total unmatched source values are exactly two. If the loop instead exhausts `nums1`, having at most two mismatches implies at least `len(nums2)` matches, so `j` must also have reached the end.

**Why checking three candidates is complete**

Take any valid solution and view the sorted source after deleting its two chosen elements. Its first surviving value must be at original sorted index 0, 1, or 2. That value becomes the smallest target under the uniform shift. The outer loop constructs exactly the valid solution's $x$ when it considers that index.

For that candidate, the greedy scan finds the target as a shifted subsequence because those valid surviving elements occur in sorted order. Thus `f(x)` returns true. Every possible valid shift is included among the three tests, and `ans = min(ans, x)` selects the minimum as required.

**Concrete trace**

For sorted `nums1 = [4,8,12,16,20]` and sorted `nums2 = [10,14,18]`, the candidates from the first three source values are 6, 2, and -2.

For $x=-2$, shifted values are 2, 6, 10, 14, 18. The first two do not match target 10, so `cnt` becomes 2. The remaining three match in order, so the candidate is valid. It is smaller than the other valid possibilities and becomes the answer.

Duplicates cause no special difficulty. The two-pointer scan consumes target copies one at a time, preserving their frequencies.

## Complexity detail

Let $n=\lvert\texttt{nums1}\rvert$; then `nums2` has $n-2$ elements.

Sorting `nums1` and `nums2` costs $O(n\log n)$ time. The helper scans at most $n$ source elements, so one call is $O(n)$. It is called exactly three times, which remains $O(n)$. Total time is therefore $O(n\log n)$.

Python's list `sort()` mutates the input arrays. Its implementation uses temporary memory whose strict worst-case size is $O(n)$, so the manifest's $O(n)$ auxiliary-space bound is appropriate. If language-level in-place sorting were counted as $O(\log n)$ stack or $O(1)$ workspace, the accounting could differ, but Python's sorting implementation is not a constant-workspace sort.

The helper itself uses only `i`, `j`, and `cnt`, so it adds $O(1)$ space. No shifted array is constructed.

Only three candidates are checked regardless of $n$, which is why validation does not add another logarithmic or linear factor beyond sorting.

## Alternatives and edge cases

- **Try every source-target difference:** Testing $O(n^2)$ candidates and scanning for each is unnecessary; only the first three sorted source values can become the smallest target.
- **Remove every pair explicitly:** There are $O(n^2)$ removal pairs, and comparing the remaining arrays would make the approach at least quadratic, usually cubic without care.
- **Frequency maps per candidate:** Frequencies can validate shifts, but ordered two-pointer matching is simpler after sorting and handles duplicates naturally.
- **Backtracking over removals:** Branching between “remove” and “match” is exponential without memoization. Sorted greedy matching always preserves the best chance for later values.
- **Both removed values are smallest:** Then `nums2[0]` corresponds to `nums1[2]`, which is why the loop must include index 2.
- **Neither removed value is smallest:** The valid shift comes from `nums1[0]`.
- **Duplicate values:** Matching one copy advances only one target position. Extra copies can be among the two removals.
- **Negative shift:** Candidate differences are ordinary signed integers, and `min` correctly favors a more negative valid value.
- **Targets matched before source ends:** The unscanned suffix consists of the remaining removals; the fixed length difference makes the helper's early termination correct.
- **Invalid candidate with too many mismatches:** `cnt > 2` means more source values would have to be deleted than allowed, so that shift cannot work.
- **Guaranteed existence:** `ans` begins at positive infinity, but the problem guarantee ensures at least one candidate is accepted and a finite integer is returned.
- **Input mutation:** Both arrays are sorted in place. This is acceptable for the judge method but would matter to a caller that expected its lists to remain in original order.
