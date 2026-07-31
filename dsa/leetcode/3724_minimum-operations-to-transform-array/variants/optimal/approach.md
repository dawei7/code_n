## General

Ignoring the extra final element for a moment, position $i$ must change from `nums1[i]` to `nums2[i]`, which unavoidably costs `abs(nums1[i] - nums2[i])`. Sum those independent costs. Exactly one append is also necessary because the target is one element longer.

Suppose index $i$ supplies the appended copy. While its original value moves from $a = \texttt{nums1[i]}$ to $b = \texttt{nums2[i]}$, an optimal monotone path visits every integer in the closed interval $[\min(a,b),\max(a,b)]$. Copying at any visited value adds no work to the original position. If the final target value $x = \texttt{nums2[-1]}$ lies inside that interval, append when the original equals $x$ and pay no adjustment beyond the append itself.

If $x$ is outside the interval, the cheapest copy value is the nearest endpoint, and the appended element needs exactly the distance from $x$ to that interval in further increments or decrements. Compute this distance for every original index and keep the minimum.

The base position costs and one append are unavoidable. The selected interval distance is both necessary for its copied value to reach $x$ and achievable by appending at the closest point along the original's transformation. Their sum is therefore optimal.

## Complexity detail

Let $n$ be `nums1.length`. One pass computes the base cost and the best append interval, so time is $O(n)$. Only scalar accumulators are used, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Append only before all adjustments:** The copy may be taken at any moment, including while an original element moves toward its target; ignoring that can overcount.
- **Try every source and recompute the base:** This is correct but repeats the same $O(n)$ position cost for all $n$ choices, producing $O(n^2)$ time.
- **Appended target inside an interval:** Its extra adjustment cost is zero, though the append still costs one operation.
- **Original already equals its target:** Its interval is one point and can still be the best copy source.
- **Target outside every interval:** Choose the globally nearest interval endpoint.
- **Large answer:** The operation total can exceed 32-bit range across $10^5$ positions, so fixed-width implementations need a 64-bit result.
