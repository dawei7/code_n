## General

**Grow each part until it can no longer remain valid**

The greatest common divisor of a group can stay the same or decrease when another number is appended; it can never increase. Once the running GCD becomes 1, adding still more numbers cannot make it greater than 1 again because `gcd(1, x) = 1` for every `x`. This monotonic behavior is what makes a greedy split possible.

The solution maintains `g`, the GCD of the current subarray, and `ans`, the number of subarrays started so far. It initializes `ans = 1` because the non-empty input must contain at least one part. It initializes `g = 0` because `gcd(0, x) = x`, allowing the first loop iteration to start the first part without a special case.

For each value `x`, the assignment `g = gcd(g, x)` tentatively appends `x` to the current part. If the new `g` remains greater than 1, the enlarged part is valid, so the algorithm keeps extending it. Using fewer splits is the goal, and there is no reason to close a still-valid part early.

If the new GCD is 1, `x` cannot belong to the current part. The solution increments `ans` to start a new part and sets `g = x`. Every input value is at least 2, so this singleton new part always has GCD greater than 1.

**What boundary is chosen**

Suppose the current part begins at index $L$, and processing index $R$ changes the running GCD from a value greater than 1 to 1. Then

$$
\gcd(\texttt{nums}[L],\ldots,\texttt{nums}[R-1]) > 1
$$

but

$$
\gcd(\texttt{nums}[L],\ldots,\texttt{nums}[R]) = 1.
$$

The greedy split places the boundary between $R-1$ and $R$. In other words, it takes the longest valid prefix beginning at $L$ and makes `nums[R]` the first value of the next part.

No valid partition whose current part starts at $L$ can extend that part through index $R$, because its GCD would already be 1. It must put a boundary somewhere before $R$. Ending earlier only leaves more elements for the remaining parts; it cannot allow the first part to absorb more.

**Why the longest valid prefix is optimal**

Consider an optimal partition of the suffix beginning at $L$. Its first part must end no later than the greedy part, because the greedy part stops at the first element that would make its GCD 1. If the optimal first part ends earlier, move its boundary right until it reaches the greedy boundary. Every intermediate prefix is valid by the definition of the first failure. This change does not increase the number of parts and only removes elements from the suffix that later parts must cover.

Therefore there exists an optimal partition whose first boundary equals the greedy boundary. The same argument applies to the remaining suffix after that boundary. Repeating it proves that every greedy boundary is compatible with an optimal solution, so the final number of parts is minimal.

Another way to see the forced nature of a split is through prime factors. A subarray has GCD greater than 1 exactly when all its values share at least one prime factor. The running GCD represents the common factors still available. When it reaches 1, no common prime survives across the full tentative part, so a boundary is unavoidable.

**Trace an example**

For `nums = [12, 6, 3, 14, 8]`:

- Start with `gcd(0,12)=12`.
- Appending 6 changes the GCD to 6.
- Appending 3 changes it to 3, still valid.
- Tentatively appending 14 changes it to 1. The first part must stop at `[12,6,3]`, `ans` becomes 2, and the new running GCD is 14.
- Appending 8 changes the new part's GCD to 2, so `[14,8]` is valid.

The algorithm returns 2. For `[4,12,6,14]`, the running GCD evolves as 4, 4, 2, 2 and never reaches 1, so the whole array remains one valid part.

**Why resetting to `x` does not lose information**

The failing value `x` has not been placed in the completed previous part. It becomes the first value of the new part, whose GCD must therefore be exactly `x`. Resetting to `x` models this placement. Resetting to zero would forget that `x` is already in the new part, while keeping the failed GCD of 1 would prevent every later extension.

Each element is processed once and belongs to exactly one resulting interval: successful updates keep it in the current part, and a failure closes the prior part before it and immediately starts the next part with it.

## Complexity detail

Let $n$ be the array length and $V$ the largest value. Euclid's algorithm computes one GCD in $O(\log V)$ worst-case time. The loop performs exactly one GCD update per element, so total time is $O(n\log V)$.

Only `ans`, `g`, `x`, and the internal scalar state of the GCD operation are needed. No partition list is constructed, so auxiliary space is $O(1)$.

In practice, running GCD values often shrink quickly and Euclid's algorithm is fast. The asymptotic bound nevertheless accounts for every call independently.

## Alternatives and edge cases

- **Dynamic programming over split positions:** Let a state store the minimum parts for every prefix and test every possible last subarray. This can require $O(n^2\log V)$ time and repeats GCD work that monotonicity makes unnecessary.
- **Prime-factor set intersections:** Factor every value and maintain the intersection of prime factors in the current segment. This expresses the same idea but factorization is more expensive and complicated than updating one GCD.
- **Split every singleton:** This is always valid because each value is at least 2, but it produces $n$ parts and is generally far from minimal.
- **Whole array has GCD greater than one:** The running GCD never reaches 1, so the answer remains 1.
- **Adjacent coprime values:** Their joint GCD is 1, forcing a boundary before the second value.
- **Running GCD becomes one:** It can never recover through further extension, which is why the split can be made immediately.
- **Every value is the same:** The GCD stays at that value and the complete array is one part.
- **First element:** `gcd(0,x)=x` starts the first segment cleanly, and $x\ge2$ guarantees validity.
- **Failing element ownership:** The value that causes GCD 1 begins the next part; it is not discarded and is not included in both parts.
- **No output partition required:** The counter and current GCD are sufficient because the problem asks only for the minimum number of parts.
