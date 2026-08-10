## General

**Sort lengths so the best candidate is local**

For positive side lengths `a <= b <= c`, a non-degenerate triangle exists exactly when:

`a + b > c`.

The other triangle inequalities hold automatically because positive `c` is at least each smaller side. Equality would form a flat, zero-area shape, so the comparison must be strict.

After sorting `nums` in ascending order, the solution scans possible largest sides from right to left and tests the two immediately preceding lengths.

**Why use the two largest smaller sides**

Fix largest candidate `c = nums[i]`.

Among every pair selected from indices below `i`, the largest possible sum is `nums[i - 1] + nums[i - 2]`. If even this pair does not exceed `c`, no smaller pair can satisfy the triangle inequality.

Therefore, for a fixed largest side, checking only its two immediate predecessors is sufficient.

If they do satisfy the inequality, they also give the largest possible perimeter among triangles whose largest side is `c`, because replacing either with a smaller length can only reduce the sum.

**Why the first valid triple is globally best**

The scan starts with the largest array value and moves left.

The first valid triple uses consecutive sorted values `nums[i - 2], nums[i - 1], nums[i]`. Any candidate considered later has largest side at most `nums[i - 1]` and its other sides no larger than the corresponding already-considered high values.

More directly, any triple whose largest index is below `i` uses three values drawn from a smaller sorted prefix. Its perimeter cannot exceed the sum of the three consecutive values at the first successful index.

Thus the method can return immediately rather than collecting every valid triangle.

**The walrus assignment**

Expression:

`(c := nums[i - 1] + nums[i - 2]) > nums[i]`

computes the sum of two smaller sides once and stores it in `c`.

If valid, the perimeter is `c + nums[i]`. Here variable `c` is a partial sum, not the conventional largest-side label used in the mathematical explanation.

**Trace**

For `[2, 1, 2]`, sorting gives `[1, 2, 2]`. The two smaller sides sum to three, which exceeds two, so perimeter five is returned.

For `[1, 2, 1, 10]`, sorted array is `[1, 1, 2, 10]`.

- For largest ten, two plus one is not greater than ten.
- For largest two, one plus one equals two, forming zero area and failing strict inequality.

No triple works, so zero is returned.

**Why no non-consecutive triple can be missed**

Suppose a valid triple uses sorted indices `p < q < r`. For largest side at `r`, replacing its smaller sides by the two largest preceding values cannot decrease their sum. Hence the consecutive triple ending at `r` is also valid and has at least as large a perimeter.

This dominance argument means every non-consecutive valid triangle has an equal-or-better consecutive representative.


Each returned triple satisfies strict triangle inequality and positive lengths, so it forms a nonzero-area triangle.

For each potential largest side, immediate predecessors are the maximum-sum companions. Scanning largest sides downward and returning the first valid companions produces a perimeter no smaller than any later or non-consecutive candidate.

If every consecutive test fails, dominance proves no triple can form a triangle.

**A sharper maximality argument**

Let the first successful descending endpoint be `i`. Any candidate using an endpoint greater than `i` was already tested with the largest possible two companions and failed, so no triangle with that larger side exists.

Any candidate whose largest endpoint is below `i` uses three elements from indices at most `i - 1`. Its three sides are componentwise no larger than the successful consecutive high triple after suitable ordering, so its perimeter cannot exceed the returned sum.

This separates impossibility for earlier scanned endpoints from perimeter dominance for later endpoints.

**Why sorting cost is worthwhile**

Without order, identifying the best two companions for every potential largest side is expensive. Sorting performs one global organization step, after which each candidate largest side needs one constant-time inequality test.

The scan then exploits information shared by all triples instead of rebuilding it repeatedly.

## Complexity detail

Let `N` be length count.

Sorting takes `O(N log N)`. The reverse scan checks at most `N - 2` triples, adding `O(N)`. Total time is `O(N log N)`.

Python's in-place sort may use `O(N)` temporary memory in the worst case, matching the manifest. The scan itself uses `O(1)` state and mutates input order.

## Alternatives and edge cases

- **Check every triple:** `O(N^3)` and ignores sorted dominance.
- **Check every pair for each largest side:** `O(N^2)`; the two largest smaller values are always best.
- **Equality case:** `a + b = c` is degenerate and must fail.
- **Exactly three lengths:** Perform one triangle test.
- **Duplicate lengths:** They are separate usable sides and sorting handles them.
- **Very large side:** If the next two largest cannot exceed it, no pair for that side can.
- **No valid triangle:** Return zero.
- **First valid early return:** Safe because the scan is in descending perimeter opportunity.
- **Positive-length guarantee:** Avoids separate checks for zero or negative sides.
- **Input mutation:** `nums.sort()` changes original order.
