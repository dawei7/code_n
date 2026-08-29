## General

**Translate the subset wording into integer coefficients**

The task permits selecting some array elements, multiplying each selected value by an integer, and summing the products. Not selecting a value is equivalent to assigning it coefficient zero. Therefore, the question is whether integers \(c_1,c_2,\ldots,c_n\) exist such that

\[
c_1a_1+c_2a_2+\cdots+c_na_n=1.
\]

Coefficients may be negative, as the examples show. This is exactly the setting of Bézout’s identity.

**Bézout’s identity**

For integers \(a_1,\ldots,a_n\), the set of all integer linear combinations is precisely the set of multiples of

\[
g=\gcd(a_1,a_2,\ldots,a_n).
\]

In particular, some integer combination equals \(g\). Every integer combination is divisible by \(g\), because \(g\) divides every input.

Consequently, a combination can equal one if and only if the GCD of the whole array is one.

**Necessity**

Suppose the array is good, so a combination equals one. Any common divisor of all array values divides every product \(c_i a_i\), and therefore divides their sum. The greatest common divisor must divide one. Since the inputs are positive and GCD is positive, it must be one.

This proves no array with GCD greater than one can be good. For `[3,6]`, every integer combination is divisible by three, so one is impossible.

**Sufficiency**

If the full GCD is one, the extended Euclidean algorithm guarantees integer coefficients whose combination equals one. The task does not ask for those coefficients, only whether they exist, so computing the GCD is enough.

For `[12,5,7,23]`, the full GCD is one. One explicit witness uses only 5 and 7: \(3\cdot5-2\cdot7=1\). Zero coefficients can be assigned to 12 and 23, matching the subset interpretation.

**How `reduce(gcd, nums)` works**

`reduce` combines the list from left to right:

\[
\gcd(\gcd(\gcd(a_1,a_2),a_3),\ldots,a_n).
\]

GCD is associative, so this folded value equals the GCD of all elements regardless of grouping.

The exact return compares the result with one. No coefficient construction, subset enumeration, or dynamic programming is necessary.

**Why subset enumeration would be misguided**

There are \(2^n\) possible subsets, and each selected number could have infinitely many integer multipliers. The number-theoretic characterization collapses that enormous search to a deterministic fold.

The ability to use negative coefficients is crucial. If multipliers had to be nonnegative, GCD one would not by itself guarantee that one is representable from values greater than one. The source problem explicitly demonstrates negative multipliers.

**Intermediate GCD behavior**

As values are folded, the running GCD can only stay the same or decrease to a divisor. Once it becomes one, it remains one for all remaining elements because \(\gcd(1,x)=1\).

The exact `reduce` still processes the remaining input; it does not implement early exit. An explicit loop could return immediately when the running GCD reaches one, improving best-case work but not worst-case complexity.

**One-element input**

For a single value \(a\), the fold returns \(a\). The array is good only when \(a=1\), because integer multiples of a positive \(a>1\) cannot equal one.


Let \(g\) be the value computed by the fold. Associativity of GCD makes it the common GCD of all input values. If \(g>1\), it divides every permitted sum, so no sum equals one. If \(g=1\), Bézout’s identity supplies integer multipliers producing one. Therefore, the Boolean comparison returns true exactly for good arrays.

**Required imports**

Standalone Python code needs `reduce` from `functools` and `gcd` from `math`. The nonempty-input guarantee means `reduce` does not need an initializer.

## Complexity detail

Let \(n\) be the array length and \(M\) its maximum value. Euclid’s algorithm computes a GCD in \(O(\log M)\) arithmetic steps in the conventional bound. Folding across \(n\) values therefore takes \(O(n\log M)\) time.

`reduce` keeps only the running result and current value, so auxiliary space is \(O(1)\). Python integer sizes are bounded here by the input magnitude.

## Alternatives and edge cases

- **Explicit GCD loop with early exit:** Return true as soon as the running GCD reaches one. It preserves the worst-case bound and can be faster in practice.
- **Extended Euclidean algorithm:** Also produce the actual integer coefficients witnessing the sum. It is unnecessary because the contract asks only for a Boolean.
- **Subset enumeration:** Exponential and conceptually incomplete because coefficients are unbounded integers.
- **Array contains one:** The full GCD is immediately one, so the array is good.
- **Single element greater than one:** Only its multiples are obtainable, so the result is false.
- **All values even:** Their GCD is at least two, making one impossible.
- **Pairwise GCDs greater than one:** The full array can still have GCD one; for example, several numbers may collectively remove all common factors.
- **Negative coefficients:** They are essential to Bézout’s identity and permitted by the examples.
- **Nonempty list:** The contract guarantees at least one value, so `reduce` without an initializer is safe.
- **Required imports:** Missing `reduce` or `gcd` would be an environment error, not an algorithmic issue.
