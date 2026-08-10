## General

**Ask how wide each value can remain the minimum**

Instead of evaluating every window length separately, the solution considers each element `nums[i]` and finds the largest contiguous interval in which that element can serve as a minimum. If that interval has length $m$, then `nums[i]` is an achievable window minimum for length $m$ and for smaller contained windows that include it.

The interval stops immediately before the nearest strictly smaller value on each side. Values equal to `nums[i]` do not stop it because `nums[i]` is still a minimum when equals are present.

**Find nearest strictly smaller boundaries with monotonic stacks**

The left scan maintains indices whose values are strictly increasing on the stack. Before assigning `left[i]`, it pops while the top value is greater than or equal to the current value. After those pops, the remaining top, if any, is the nearest index to the left with a strictly smaller value. If none exists, the sentinel remains `-1`.

The right-to-left scan applies the same rule and stores the nearest strictly smaller index to the right, or sentinel `n`.

For index $i$, every value between these boundaries is at least `nums[i]`, while crossing either boundary would include a smaller value. Therefore the maximum interval length for this minimum is

`m = right[i] - left[i] - 1`.

The code records `nums[i]` as a candidate for answer index `m - 1`, because result index $m-1$ corresponds to window size $m$. Multiple elements may have the same span length, so `max` keeps the best minimum value.

**Why equal values are handled**

Both scans pop equal values. This may let several equal elements claim overlapping wide intervals, but it cannot inflate the answer because they contribute the same value. More importantly, at least one representative of a plateau can claim every window span where that plateau value is the minimum. Strictly smaller values, not equals, are the true limiting boundaries.

**Fill lengths that received no direct candidate**

An element is written only at its largest span length. Some shorter lengths may remain zero even though valid windows exist. The final right-to-left pass applies

`ans[i] = max(ans[i], ans[i + 1])`.

The true maximum-of-minimum answer is nonincreasing as window length grows. Any window of length $L+1$ contains a length-$L$ subwindow whose minimum is at least the larger window's minimum. Hence the best value for length $L$ is at least the best value for length $L+1$.

Propagating larger-length candidates toward shorter lengths implements this fact. If value $v$ is a minimum over a maximal interval of length $m$, then for every length below $m$ there is a contained subarray including its position whose minimum is at least $v$. The propagation makes that lower bound available, while direct candidates and maxima choose the greatest one.

**Why the final answers are exact**

Every direct candidate `nums[i]` is the actual minimum of its maximal boundary interval, so it is achievable. Propagated candidates are also achievable at smaller lengths by taking a contained window.

Conversely, consider an optimal window of some length $L$ and one occurrence of its minimum at index $i$. No strictly smaller value lies inside that window, so the nearest-strictly-smaller span for $i$ has length at least $L$. The value is recorded at that span or is represented by an equal occurrence, then propagated down to length $L$. Thus the computed answer is at least the optimal value. Since all candidates are achievable, it cannot exceed the optimum. Equality follows.

## Complexity detail

Let $N$ be the array length.

Each index is pushed once and popped at most once in the left scan, and the same is true in the right scan. Both scans are $O(N)$ amortized. Computing span candidates and propagating answers are two more linear passes, so total time is $O(N)$.

The `left`, `right`, `ans`, and stack arrays each use $O(N)$ space. Reusing storage could reduce constants, but the asymptotic auxiliary bound remains $O(N)$.

Initializing `ans` with zero is safe because all input values are nonnegative.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintaining minima for all $O(N^2)$ windows is too slow.
- **Sliding minimum for each length:** A deque can solve one fixed length in $O(N)$, but repeating it for all $N$ lengths is quadratic.
- **Use one strict and one non-strict boundary:** This is a common way to assign duplicate spans uniquely. The exact source uses non-strict popping on both sides; overlapping equal claims remain harmless for maximum values.
- **Single element:** Both sentinels bound a span of one, and the result is that element.
- **All equal values:** Every answer should equal that value. Wide spans are recorded and backward propagation fills all lengths.
- **Strictly increasing array:** Each value's right reach extends to the end until a left smaller boundary; the formula derives the expected decreasing answers.
- **Strictly decreasing array:** Symmetric boundary behavior handles minima extending leftward.
- **Zeros:** Zero is a valid minimum and also the initialization value; propagation still works because no true answer is negative.
- **Missing direct length:** The backward monotonicity pass supplies it from a longer achievable span.
- **Nearest strictly smaller:** Equal values must not terminate the region where the current value remains a minimum.
