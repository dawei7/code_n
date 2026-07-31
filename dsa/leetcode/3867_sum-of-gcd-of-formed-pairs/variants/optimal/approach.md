## General

**Build the derived array with one running maximum**

The definition at index `i` depends on the maximum of the inclusive prefix ending there. Keep that maximum in `maximum`. After reading the next `value`, update `maximum = max(maximum, value)` and append `gcd(value, maximum)` to `prefix_gcd`. This produces the exact derived value for every index without revisiting any earlier element.

**Make the prescribed pairs explicit**

Sort `prefix_gcd`. Put `left` at its first index and `right` at its last. While `left < right`, add `gcd(prefix_gcd[left], prefix_gcd[right])`, then move both pointers inward. The loop runs once for every complete pair and stops before consuming a lone middle value.

Before processing index $i$, `maximum` equals the maximum through index $i-1$; incorporating `nums[i]` therefore makes it exactly $M_i$. The appended value is consequently the required $\gcd(\texttt{nums[i]},M_i)$, so the completed list contains precisely all required derived values. Sorting places the smallest unused value at `left` and the largest unused value at `right`. Each loop iteration therefore forms exactly the next prescribed pair, records its required contribution, and removes both endpoints from future consideration. After $\lfloor N/2 \rfloor$ iterations every legal pair has been counted once, and any odd middle element is untouched, making the returned total exact.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. The construction performs $N$ running-maximum updates and $N$ Euclidean GCD computations. Sorting costs $O(N\log N)$, and the pairing pass performs another $\lfloor N/2\rfloor$ GCD computations. A GCD on values at most $V$ costs $O(\log V)$, so the complete bound is $O(N\log N + N\log V)$ time. The derived array and the sorting workspace require $O(N)$ auxiliary space.

The benchmark defines size as $N$. Each tier is a descending array from $N$ to $1$, so the first element remains the prefix maximum for every later position. The accepted running-maximum implementation and an independent prefix-accumulation formulation should retain the required near-linearithmic growth. A correct slower control that recomputes `max(nums[:i + 1])` at every index scans quadratically many prefix elements and should fail only the scaling verdict.

## Alternatives and edge cases

- **Recompute every prefix maximum:** Calling `max` on each growing prefix follows the definition literally and returns the same values, but it adds $O(N^2)$ work before sorting.
- **Prefix-maximum array:** Precomputing all $M_i$ values and then deriving `prefixGcd` is correct with the same asymptotic time and space, but the running scalar is simpler because each maximum is consumed immediately.
- **Reuse the input array:** Replacing each `nums[i]` with its derived value can avoid a separate logical list, but it mutates the caller's input and Python's sort can still require linear temporary storage.
- **Sort the original values:** The pair endpoints come from `prefixGcd`, not directly from `nums`; sorting the original array can change both the elements and the answer.
- **Pair before sorting:** Original positions do not determine pairs. The smallest and largest currently unpaired derived values must be selected after the complete derived array is sorted.
- **Odd length:** The two pointers stop when they meet, leaving the sorted middle value unpaired exactly as required.
- **Singleton input:** There is no complete pair, so the loop never runs and the result is `0`.
- **Large values:** Euclid's algorithm handles values through $10^9$ without enumerating divisors.
