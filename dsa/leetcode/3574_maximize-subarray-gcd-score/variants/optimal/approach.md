## General

Write every positive integer as $2^e q$, where $q$ is odd. Doubling an element increases only its exponent $e$ by one; it cannot introduce any new odd factor. For a fixed subarray, its GCD's exponent of two is the minimum exponent among its elements.

Suppose that minimum exponent occurs $c$ times. The GCD gains a factor of two exactly when all $c$ minimum-exponent elements are doubled. If even one remains unchanged, the minimum exponent and therefore the GCD remain unchanged. Doubling elements with larger exponents has no effect on the GCD. Consequently, the best modified GCD for this subarray is twice its original GCD when $c\le k$, and its original GCD otherwise.

Enumerate every left endpoint and extend the right endpoint one element at a time. Maintain the running GCD, the smallest power-of-two exponent seen, and how many elements attain that exponent. A smaller exponent resets the count to one; an equal exponent increments it. These three values determine the best score for the current subarray immediately.

Every non-empty subarray is visited once. For each one, the exponent argument proves that the computed multiplier is both achievable—double exactly the minimum-exponent elements when allowed—and maximal, since operations cannot change odd factors or raise the minimum exponent in any other way. The maximum recorded score is therefore globally optimal.

## Complexity detail

Let $n$ be the array length and $M=\max(\texttt{nums})$. There are $O(n^2)$ subarrays. Each extension performs one Euclidean GCD operation in $O(\log M)$ time plus constant-time exponent bookkeeping, for total time $O(n^2\log M)$. Only scalar running state is stored, so auxiliary space is $O(1)$.

The benchmark uses array length $S=n$ and a repeated pattern whose GCD and minimum exponent remain relevant at every extension. The accepted incremental enumeration is $O(S^2\log M)$. The calibrated alternative rescans every current subarray to recompute its GCD and exponent count, requiring $O(S^3\log M)$ time.

## Alternatives and edge cases

- **Recompute every subarray from scratch:** This reaches the same number-theoretic decision but adds an inner scan, increasing time to $O(n^3\log M)$.
- **Enumerate operation subsets:** Trying which indices to double is exponential and ignores that only minimum power-of-two exponents can affect a subarray's GCD.
- **Double the largest values:** Magnitude is irrelevant to whether the GCD improves; the deciding property is the minimum exponent of two.
- **Insufficient operations:** When more than `k` elements attain the minimum exponent, the subarray's GCD cannot increase at all.
- **Singleton subarray:** Its one element can always be doubled because $k\ge1$, so twice the maximum array value is a useful baseline.
- **Odd values:** Their exponent of two is zero, and every odd element attaining that minimum must be doubled to make the subarray GCD even.
- **Large scores:** A score can exceed a 32-bit signed integer, so fixed-width implementations require a 64-bit type.
