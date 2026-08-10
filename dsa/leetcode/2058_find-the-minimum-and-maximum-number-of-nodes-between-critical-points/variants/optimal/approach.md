## General

**A critical point needs a three-node window**

The current candidate must have both a previous and a next node. The source keeps `head` at the left node of a moving triple and assigns

`a, b, c = head.val, head.next.val, head.next.next.val`.

The middle value `b` is critical when either `a > b < c` or `a < b > c`. Python chained comparisons express the required strict local minimum or strict local maximum directly.

Equal neighboring values make both chains false, as required by the strict definition.

**Stop before the final node becomes the middle**

The loop condition is `while head.next.next`. It runs only while the current triple has a real third node.

The first node is never tested as the middle because the initial middle is `head.next`. The last node is never tested because it cannot have a next neighbor. A two-node list performs zero iterations and correctly has no critical point.

**Track only the first and most recent critical positions**

`first` stores the position assigned to the first critical point found. `last` stores the most recent critical position.

On the first critical point, both become the current scan counter `i`. On each later one:

- `i - last` is the distance to the previous critical point;
- `last` is replaced with `i`;
- `last - first` is the distance from the first through the newest critical point.

No list of all critical positions is necessary.

**The scan counter has a harmless offset**

At `i=0`, the code is testing the linked-list node at actual zero-based index one, because `b=head.next.val`. Every critical node is therefore recorded one position smaller than its actual zero-based index.

Only differences between critical positions are returned. Subtracting the same one-position offset from both endpoints does not change any distance:

$$
(q-1)-(p-1)=q-p.
$$

The unusual indexing is exact-source behavior, but it does not affect correctness.

**Why minimum distance needs only consecutive critical points**

List critical positions in increasing order as

$$
p_1<p_2<\cdots<p_k.
$$

For any nonconsecutive pair `p_a,p_b` with `b>a+1`, its distance is a sum of at least two positive consecutive gaps. It cannot be smaller than every gap inside that sum.

Therefore the minimum over all critical-point pairs is attained by some consecutive pair. Updating `ans[0]` with `i-last` at each discovery examines exactly those gaps.

**Why maximum distance uses the first and last**

Among ordered positions, the farthest pair is the smallest and largest position. Any other left endpoint is no smaller than `first`, and any other right endpoint is no larger than `last`.

The source updates `ans[1]` with `last-first` after every later critical point. This quantity never decreases, and after traversal it equals the distance between the first and final critical points.

**Trace the three-critical-point example**

For values `[5,3,1,2,5,1,2]`, the critical nodes have actual indices two, four, and five. The source records offset indices one, three, and four.

The consecutive gaps are two and one, so the minimum becomes one. The first-to-last difference is `4-1=3`. These equal the distances from the actual indices because of the uniform offset.

**Recognize fewer than two critical points**

Initially `first=last=-1`. With no critical point, they remain equal. With exactly one, both are set to the same scan index and remain equal.

The return expression checks `first == last` and produces `[-1,-1]` in both cases. With two or more critical points, `last` is strictly greater than `first`, and both entries of `ans` have been replaced by finite distances.

**Why the one-pass state is correct**

After each processed middle node, `first` and `last` identify the earliest and latest critical points seen. `ans[0]` is the smallest gap between consecutive seen critical points, and `ans[1]` is their current outer span.

Discovering a noncritical node changes none of these facts. Discovering a critical node performs exactly the updates needed to extend them. At loop termination, the state describes every critical point in the list, proving the returned distances.

**The list structure is not modified**

Assigning `head = head.next` advances the method's local pointer. It does not change any `next` field, node value, or caller-visible link.

## Complexity detail

Let $N$ be the number of nodes. Each loop iteration advances one link, so the list is traversed once in $O(N)$ time.

The method stores a constant number of node references, values, indices, and the two-element result list. Auxiliary space is $O(1)$. The returned two-element list is also constant size.

## Alternatives and edge cases

- **Store all critical indices:** Makes the final calculations easy but uses $O(N)$ space unnecessarily.
- **Two passes:** One pass could collect or count points and another compute distances, but the rolling state already suffices.
- **Two-node list:** No middle node exists, so return `[-1,-1]`.
- **Exactly one critical point:** `first==last` and the failure pair is returned.
- **Exactly two critical points:** Minimum and maximum distances are equal.
- **Equal adjacent value:** Cannot participate in a strict extremum on that side.
- **First or last node:** Never eligible because one neighbor is missing.
- **Adjacent critical points:** Produce minimum distance one.
- **Offset scan index:** Harmless because all reported quantities are differences.
- **Long monotone list:** Contains no critical points.
- **Alternating highs and lows:** Every eligible middle may be critical; adjacent-gap tracking remains linear.
- **Input preservation:** The local traversal pointer moves, but links are untouched.
