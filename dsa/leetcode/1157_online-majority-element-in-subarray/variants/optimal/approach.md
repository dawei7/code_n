## General

**The threshold guarantee changes the problem**

Every query satisfies

`2 * threshold > right - left + 1`.

Therefore, any qualifying value occupies strictly more than half of the queried subarray. At most one value can do that. This permits a two-stage strategy:

1. obtain the only possible majority candidate quickly;
2. count that candidate's actual occurrences and verify the threshold.

The first stage uses Boyer-Moore cancellation summaries stored in a segment tree. The second uses binary search over occurrence positions.

**What a segment-tree node summarizes**

Each `Node` stores its inclusive one-based range `[l, r]`, a candidate `x`, and a residual count `cnt`.

Imagine repeatedly canceling pairs of different values in that segment. After all possible cancellations, either nothing remains or all uncanceled values are equal. The node stores that surviving value and how many unmatched copies remain.

This residual is not the candidate's true frequency. It is a cancellation balance. Its crucial property is that if some value occurs more than half the segment, it cannot be completely canceled: there are more copies of it than all other values combined, so it must be the survivor.

At a leaf, the segment contains one array value. That value is the candidate and its residual count is one.

**Merge two cancellation summaries**

`pushup` combines the left and right child summaries exactly as Boyer-Moore cancellation would combine their remaining elements.

If both candidates are equal, their unmatched copies reinforce each other, so their counts are added.

If candidates differ, unmatched copies cancel pairwise. The candidate with the larger residual survives with the difference of the two counts. If the left count is at least the right count, the left candidate is kept with `left_count - right_count`; otherwise, the right candidate survives with the opposite difference.

The same merge logic appears when a range query overlaps both children. Thus a query over several tree segments produces the cancellation summary of their concatenated array range.

Cancellation summaries can be grouped this way without changing the eventual majority survivor. Internal cancellation within a child removes equal numbers of competing elements and cannot destroy a strict majority of the combined range.

**Build over one-based tree ranges**

The tree is built for logical positions one through `n`, while Python's input array is zero-based. A leaf covering position `l` reads `self.nums[l - 1]`.

The tree array contains roughly four nodes per input position through `n << 2`, a standard safe allocation for a binary segment tree. Child indices are `u << 1` for the left child and `u << 1 | 1` for the right child.

The midpoint splits each interval until leaves are reached. After both children are built, `pushup` computes the parent summary.

**Query only the requested interval**

The public query receives zero-based inclusive bounds. It calls the segment tree with `left + 1` and `right + 1` to match the tree's one-based ranges.

If a node lies completely inside the requested interval, its stored summary is returned immediately. If the interval lies wholly on one side of the midpoint, recursion follows only that child. If it crosses the midpoint, both partial summaries are obtained and merged with the same cancellation rules.

The returned `x` is the Boyer-Moore candidate of exactly `arr[left...right]`. If a strict majority exists, `x` must be that value. If no strict majority exists, cancellation still returns some candidate, so a verification step remains mandatory.

**Store sorted occurrence positions for verification**

During construction of `MajorityChecker`, `self.d[x]` receives every zero-based index at which value `x` occurs. Indices are appended while the array is traversed from left to right, so each list is sorted.

For candidate `x`, `bisect_left(self.d[x], left)` finds the first occurrence position not before `left`. `bisect_left(self.d[x], right + 1)` finds the first position after the inclusive right boundary. Their difference is the exact number of candidate occurrences in the query range.

If that count is at least `threshold`, the candidate is returned. Otherwise, `-1` is returned. There is no need to test another value: the threshold guarantee means any qualifying value would be a strict majority and therefore would have been the cancellation candidate.

**Why the complete data structure is correct**

For every segment-tree node, the stored pair is the result of canceling different values in its segment, by induction from leaves through the merge rule. A strict majority survives every such cancellation, so querying a subarray returns its strict-majority value whenever one exists.

The position lists give the candidate's exact subarray frequency. Passing the frequency test proves it meets the requested threshold. Failing the test proves no answer exists, because any different qualifying value would be a strict majority, yet a strict majority cannot differ from the returned Boyer-Moore candidate.

Thus each query returns the qualifying element when it exists and `-1` otherwise.

## Complexity detail

Let `n` be the array length and `q` be the number of queries. Building the segment tree visits `O(n)` nodes. Building the occurrence lists also visits the array once. Initialization therefore takes `O(n)` time.

A range query visits `O(log n)` boundary paths and merges `O(log n)` canonical summaries. The two bisections in one occurrence list each take `O(log n)` time in the worst case. Thus each public query is `O(log n)`, and total time is `O(n + q log n)`.

The tree contains `O(n)` nodes, and all occurrence lists together contain exactly `n` indices. Total space is `O(n)`. Recursive build and query calls add `O(log n)` stack depth for a balanced segment tree, dominated by stored structures.

## Alternatives and edge cases

- **Count every value in each query:** Scanning `arr[left...right]` takes linear time per request and wastes the online preprocessing opportunity.
- **Use only Boyer-Moore without verification:** Cancellation always returns a candidate, even when no value reaches `threshold`. Exact frequency verification is required.
- **Use only occurrence lists:** They can verify a known candidate quickly, but trying every distinct array value per query would be too expensive. The segment tree supplies the single candidate.
- **Random sampling:** Because the threshold is more than half, repeated random picks can find the majority with high probability, followed by bisection verification. The exact solution is deterministic.
- **Threshold equals the subarray length:** Only a completely uniform range qualifies. The candidate verification returns it exactly in that case.
- **One-element range:** Its leaf value is the candidate, its frequency is one, and it meets every legal threshold for that range.
- **No qualifying value:** The candidate fails the bisection count and the method returns `-1`.
- **Several values tied after cancellation:** The merge may choose one based on residual comparison, but verification prevents a false answer.
- **Why only one answer is possible:** The strict threshold condition prevents two different values from each occupying more than half the same range.
- **Inclusive right endpoint:** Searching for `right + 1` converts the inclusive interval to a half-open position range for subtraction.
- **Repeated queries:** Precomputed tree summaries and occurrence lists are reused; the original array is never modified.
- **One-based versus zero-based indices:** The public bounds are shifted only for the tree. Occurrence lists remain zero-based and use the original query bounds.
