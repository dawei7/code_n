## General

Let $n$ be the array length, $M$ the initial maximum, and $P = 10^9 + 7$.

**Handle the identity multiplier**

If `multiplier` is 1, no operation changes a value. Return the entries modulo $P$ immediately; attempting to wait for heap values to grow would never make progress.

**Simulate only the unbalanced prefix**

Build a min-heap of `(value, index)`, which implements both minimum selection and the earliest-index tie rule. While operations remain and the heap minimum is below $M$, multiply that root and replace it in the heap using its exact, unreduced value.

For a multiplier greater than one, each value can be selected only logarithmically many times before reaching $M$. When the loop ends, every heap value is at least $M$. Any value created by the loop was multiplied while below $M$, so it is less than `M * multiplier`; untouched values are at most $M$. All values therefore lie in one multiplicative band.

**Batch complete cycles**

Sort the remaining `(value, index)` pairs. Multiplying the first pair moves it to the end of the order, and repeating does the same for each successive pair. Thus every complete group of $n$ operations multiplies every value once. If `k = q * n + r` operations remain, every pair receives exponent $q$, and the first $r$ sorted pairs receive one additional multiplication.

Use modular exponentiation for those exponents and place each reduced result at its saved original index. Exact values were retained through every ordering decision, so modulo arithmetic cannot corrupt selection order. The heap phase matches the original operations directly, and the one-band invariant proves that the batched phase reproduces the same cyclic sequence.

## Complexity detail

For `multiplier > 1`, each of the $n$ values needs at most $O(\log M)$ warm-up multiplications, each costing $O(\log n)$ in the heap. Sorting costs $O(n \log n)$, and $n$ modular powers cost $O(n \log k)$. The total is $O(n \log M \log n + n \log k)$ time and $O(n)$ space. The identity-multiplier branch takes $O(n)$ time.

## Alternatives and edge cases

- **Simulate all `k` operations:** A heap makes each step efficient but still takes $O(k \log n)$ time, which is infeasible for $k = 10^9$.
- **Apply modulo after every multiplication:** Reduced values can become artificially small and change which index should be selected next.
- **Batch before values are balanced:** The selection order is not yet cyclic while some values remain below the initial maximum.
- **Ignore indices in heap ordering:** Equal minima must choose the smallest original index.
- When `multiplier` is 1, the answer is just the original values modulo $P$.
- A one-element array receives all `k` multiplications, handled directly by its batched exponent.
- A remainder of zero means every value receives exactly the same number of batched multiplications.
- Equal balanced values use ascending index order when assigning the extra remainder operations.
- Final output order is the original index order, not the heap's sorted order.
