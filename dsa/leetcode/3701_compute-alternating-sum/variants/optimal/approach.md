## General

The sign of each element is determined entirely by its zero-based index: even indices contribute positively and odd indices contribute negatively. Traverse `nums` once while maintaining the sum of all contributions processed so far.

At index `i`, add `nums[i]` when `i` is even and subtract it when `i` is odd. After processing the prefix through `i`, the accumulator therefore equals

$$
\sum_{j=0}^{i}(-1)^j\texttt{nums[j]}.
$$

The next update appends precisely the sign required for index $i+1$, so the same statement continues to hold for the longer prefix. Once the traversal covers the full array, the accumulator is exactly the requested alternating sum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan visits each element once, taking $O(n)$ time. The accumulator and loop variables use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Separate even and odd slices:** Summing `nums[::2]` and `nums[1::2]` is concise, but the slices allocate $O(n)$ additional space.
- **Two independent index loops:** One loop can add even positions and another subtract odd positions; it remains $O(n)$ but is less direct than one traversal.
- **Single element:** Index `0` is even, so the result is the sole value.
- **Odd array length:** The final index is even and its value is added; no special case is required.
- **Negative result:** Although every input value is positive, the total may be negative because odd-indexed values can outweigh even-indexed ones.
