## General

Interpret a bowl as a pair of endpoints that can see each other over strictly lower interior values. Process possible right endpoints from left to right while maintaining a stack of `(value, index)` pairs whose values decrease from bottom to top.

For a new value `nums[r]`, repeatedly pop every smaller stack top. A popped index $l$ has survived on the stack until $r$, which means no value between $l$ and $r$ reached or exceeded `nums[l]`; otherwise that value would already have popped it. Since `nums[r]` is larger, the smaller endpoint is `nums[l]`, and `(l,r)` is a bowl whenever the gap is at least two.

After those pops, at most one additional left endpoint can form a bowl: the current stack top, if one exists. It is the nearest surviving value greater than `nums[r]`, and every value between it and $r$ is smaller than `nums[r]`. Deeper stack entries are blocked by that top value, which is already greater than the smaller endpoint `nums[r]`. Thus counting only the top is both sufficient and necessary.

Push the current value and index after counting. Every index is pushed once and popped at most once, and each qualifying endpoint pair is counted exactly when its right endpoint arrives. Explicitly require `r - l >= 2` so visible adjacent pairs are not mistaken for length-three bowls.

## Complexity detail

Each of the $n$ indices enters and leaves the monotonic stack at most once, so the total time is $O(n)$. The stack may contain all indices of a decreasing array and therefore uses $O(n)$ space.

The benchmark defines its size as $n$ and uses strictly decreasing arrays. This forces the accepted implementation to retain the full stack while a correct enumeration strategy examines every endpoint pair, providing a calibrated quadratic contrast.

## Alternatives and edge cases

- **Enumerate all endpoint pairs:** Maintaining an interior maximum makes this correct in $O(n^2)$ time, but it cannot handle the largest arrays efficiently.
- **Range-maximum queries:** A sparse table can test a chosen pair quickly, yet there are still quadratically many pairs unless visibility is exploited.
- **Adjacent visible endpoints:** They must not be counted because a bowl requires at least one interior element.
- **Strictly increasing or decreasing arrays:** Every nonadjacent pair is blocked by an interior value closer to the smaller endpoint, so the count is zero.
- **Popped smaller endpoint:** Its pair with the current value is valid because its survival proves all intervening values are smaller.
- **Surviving greater endpoint:** Only the nearest survivor can pair with the current value; deeper candidates are blocked.
- **Distinctness:** Equal-height handling is unnecessary because the contract guarantees all values are distinct.
