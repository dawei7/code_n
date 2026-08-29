## General

**Fix the middle index and optimize both sides independently.** For middle $j$, a valid triplet needs:

$$
i<j<k,\qquad
\texttt{nums}[i]<\texttt{nums}[j]<\texttt{nums}[k].
$$

Its value is

$$
\texttt{nums}[i]-\texttt{nums}[j]+\texttt{nums}[k].
$$

With $j$ fixed, the best left choice is the largest earlier value strictly below `nums[j]`, and the best right choice is the largest later value strictly above it. Those choices maximize the positive left and right terms independently.

**Precompute the best value to the right.** Array `right` is built backward. `right[i]` equals the maximum of `nums[i:]`. The recurrence

`right[i] = max(nums[i], right[i + 1])`

establishes this by induction.

For middle $j$, `right[j + 1]` is the largest value at a strictly later index. If it is not greater than `nums[j]`, no valid right endpoint exists. If it is greater, it is automatically the optimal $k$ because a larger right value only increases the expression.

**Maintain earlier values in sorted order.** `sl` begins with `nums[0]`. Before processing middle $j$, it contains exactly `nums[0..j-1]`.

`sl.bisect_left(nums[j])` gives the insertion position before all values equal to the middle. Subtracting one reaches the largest stored value strictly smaller than `nums[j]`. If the result is negative, no legal left endpoint exists.

When both sides exist, the source evaluates:

`sl[i] - nums[j] + right[j + 1]`.

Afterward, it inserts `nums[j]` so that the next middle can use it as an earlier value.

**Strict inequalities are correctly enforced.** The right condition uses `>`. The left lookup uses `bisect_left` rather than `bisect_right`, so equal left values are excluded. This matches the strictly increasing triplet definition.

**A trace.** For `[1,5,3,6]`, the right suffix maxima are `[6,6,6,6]`. At middle 5, largest smaller left is 1 and best right is 6, producing 2. After inserting 5, middle 3 sees largest smaller left 1 and right 6, producing 4. The answer is 4.
Every valid triplet has one middle $j$, which the loop visits. The suffix maximum selects the best valid right value for that middle, and the sorted predecessor selects the best valid left value. Therefore the candidate is at least as large as every triplet with that middle. Maximizing across all middles gives the global optimum.

**Manifest mismatch.** The manifest describes coordinate compression and a Fenwick prefix-maximum tree. The protected source uses `SortedList` plus a suffix-maximum array. Its time and space classes are similar, but its data flow and dependencies are different.

## Complexity detail

Building `right` costs $O(N)$ time and space. Each of $N-2$ middle positions performs logarithmic binary search and insertion in `SortedList` under the library's advertised ordered-container behavior. Total time is conventionally $O(N\log N)$.

`right` and `sl` each store $O(N)$ values, so auxiliary space is $O(N)$. The input list is not modified.

Actual `SortedList` implementation uses block-based storage; the standard solution analysis treats its search and amortized insertion as efficient logarithmic-style ordered-multiset operations.

## Alternatives and edge cases

- **Fenwick prefix maximum:** Compress values and query the best earlier value below the current rank. This is the algorithm described by the manifest, not the exact source.
- **Balanced search tree:** Any ordered multiset supporting predecessor and insertion can replace `SortedList`.
- **Brute-force triplets:** It costs $O(N^3)$ and ignores separable left/right optimization.
- **Prefix minimum instead of predecessor maximum:** It is wrong because the expression benefits from the largest legal left value, not the smallest.
- **Duplicate middle values:** Equal earlier values are excluded by `bisect_left`.
- **No valid side for a middle:** The source skips it without changing the answer.
- **Guaranteed valid triplet:** It makes initializing `ans=0` safe because valid triplet values are positive under positive strictly increasing values.
- **Best right endpoint:** The suffix maximum is used only after verifying it is strictly greater.
- **Input preservation:** `SortedList` is separate and `nums` remains unchanged.
- **Manifest mismatch:** No Fenwick tree or coordinate-compressed rank array appears in the protected implementation.
- **Why the maximum left value is best:** The middle and right terms are fixed while selecting $i$, so increasing `nums[i]` increases the objective one-for-one as long as strict inequality remains satisfied.
- **Why the maximum right value is best:** The left and middle terms are fixed while selecting $k$, and the right value has positive coefficient one.
- **Middle index bounds:** The loop starts at 1 and ends before $N-1$, guaranteeing at least one physical position on both sides even though value constraints may still fail.
- **Sorted multiset retains duplicates:** Multiple equal earlier values occupy separate entries, but predecessor lookup chooses one value; their identities are irrelevant because only the maximum numeric contribution is needed.
- **Suffix array includes current position generally:** The query deliberately uses `right[j+1]`, not `right[j]`, so the middle node can never be reused as the right endpoint.
