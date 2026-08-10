## General

**Subtract the removal interval from each disjoint input interval**

The input intervals are already sorted and mutually disjoint, so there is no need to merge or reorder them. The algorithm processes each interval `[a, b)` independently against the removal interval `[x, y)` and appends whatever portion remains.

Half-open boundaries matter. Two half-open intervals overlap only when `a < y` and `b > x`. Equivalently, they do not overlap when `a >= y` or `b <= x`. The exact source uses that non-overlap test.

If `a >= y`, the input begins at or after the removal interval's excluded right endpoint. If `b <= x`, it ends at or before the removal interval's included left endpoint. In either case the sets share no real number, so `[a, b)` is appended unchanged.

Equality belongs in the non-overlap condition. For example, `[0, 2)` and `[2, 5)` merely touch at two. The first excludes two while the second includes it, so their intersection is empty.

**An overlapping interval leaves at most two pieces**

When overlap exists, removing one contiguous interval can leave a portion to its left, a portion to its right, both portions, or nothing.

If `a < x`, values from `a` up to but excluding `x` remain, so the code appends `[a, x)`. The strict inequality guarantees this piece is nonempty.

If `b > y`, values from `y` up to but excluding `b` remain, so the code appends `[y, b)`. Again, strict inequality prevents an empty interval.

Both tests can succeed when the removal interval lies strictly inside the input interval. For `[0, 5)` minus `[2, 3)`, the output is `[0, 2)` followed by `[3, 5)`. If removal covers the entire input interval, neither condition succeeds and that interval contributes nothing.

For the first example, `[0, 2)` overlaps `[1, 6)` and leaves `[0, 1)`. Interval `[3, 4)` lies completely inside the removal range and disappears. Interval `[5, 7)` leaves `[6, 7)`.

**Why output order and disjointness are preserved**

Input intervals are visited from left to right. Any surviving left piece begins at the original `a`, and any right piece begins at `y` within that same original interval. The left piece is appended before the right piece. Therefore pieces from one interval are ordered, and all pieces from an earlier input interval remain before pieces from a later one.

Subtraction can only remove points; it cannot create an overlap between originally disjoint intervals. The two pieces from one split are separated by the removed interval. Consequently the output remains sorted and disjoint without a final sort or merge.

For correctness, consider any real value in an appended piece. It was inside the original interval, and the endpoint tests place it outside `[x, y)`, so it belongs in the required set difference. Conversely, any original value not in the removal interval lies either in a completely non-overlapping input interval, to the left of `x` in an overlapping interval, or at or to the right of `y` in that interval. One of the append rules retains it. Thus the result contains every and only required value.

**Why intervals can be handled independently**

The removed set is fixed for the entire loop, and original intervals share no points. Subtracting `[x, y)` from one interval cannot change which points belong to another interval. There is therefore no evolving sweep state and no need to remember whether an earlier interval overlapped. Even when the removal interval spans many inputs, each middle interval simply contributes nothing while the first and last overlaps independently contribute their possible boundary pieces. This local reasoning is what makes the one-pass implementation both simple and complete.

## Complexity detail

Let $n$ be the number of input intervals and $r$ the number of returned intervals. The loop examines each input once and performs constant work, so time is $O(n)$. This is optimal because the output may contain information from every input interval.

The result contains at most two pieces per input interval, so $r\le2n$ and output space is $O(n)$. Aside from that required output, the code uses only endpoint and loop variables, giving $O(1)$ auxiliary working space. The manifest's $O(n)$ space includes the returned list.

No cost depends on coordinate magnitude. All work consists of comparisons and copying endpoints.

## Alternatives and edge cases

- **Four explicit overlap cases:** Fully covered, left overlap, right overlap, and internal removal can be handled separately. The two surviving-piece tests express all cases more compactly.
- **General sweep-line events:** Sorting all endpoints works but is unnecessary because input intervals are already sorted and only one interval is removed.
- **Removal completely outside:** Every interval passes the non-overlap test and is copied unchanged.
- **Removal covers an interval:** Neither residual condition succeeds, so the interval disappears.
- **Removal strictly inside one interval:** Both residual pieces are emitted in left-to-right order.
- **Touching endpoints:** `b == x` or `a == y` means no intersection for half-open intervals, so the original interval remains intact.
- **Removal shares a left endpoint:** There is no empty left piece because `a < x` is false.
- **Removal shares a right endpoint:** There is no empty right piece because `b > y` is false.
- **Negative coordinates:** Only ordering matters, so signs have no effect.
- **Do not use closed-interval logic:** Treating touching endpoints as overlap can create unnecessary or empty fragments.
