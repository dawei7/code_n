## General

Let $S_i$ be the sum of the circular length-`k` subarray beginning at index $i$. Moving the window one position removes `arr[i]` and adds `arr[(i + k) % n]`. Therefore $S_i=S_{i+1}$ exactly when

$$
\texttt{arr[i]}=\texttt{arr[(i+k)\bmod n]}.
$$

Applying this equality repeatedly links indices by jumps of $k$ modulo $n$. Those jumps partition the array into $gcd(n,k)$ disjoint cycles, equivalently the residue classes modulo $g=\gcd(n,k)$. All length-`k` sums are equal if and only if every value within each cycle is equal; different cycles may choose different final values.

For one cycle with values $x_1,\ldots,x_r$, changing them all to $t$ costs $\sum_j\lvert x_j-t\rvert$. This absolute-deviation sum is minimized by any median. Sort the values in each cycle, select its middle value, and add every distance to that median. Because cycles are independent, the sum of their individual minima is the global minimum.

Using `arr[start::g]` collects a residue class directly. It represents the same set of indices as repeatedly adding $k$ modulo $n$, even when the visitation order differs.

## Complexity detail

Let $n=\lvert\texttt{arr}\rvert$. The cycle lengths sum to $n$. Sorting all cycles costs at most $O(n\log n)$ time in total, and summing distances costs $O(n)$ time.

The extracted cycle arrays contain $n$ values altogether, so the auxiliary-space bound is $O(n)$.

## Alternatives and edge cases

- **Trying every cycle value as a target:** This is correct because a median may be chosen from the input values, but evaluating every candidate costs quadratic time within a long cycle.
- **Quickselect medians:** Selection can reduce expected time to $O(n)$, though sorting gives deterministic behavior and simpler implementation.
- **`k = n`:** Every circular window contains the whole array, $gcd(n,k)=n$, and each singleton cycle costs zero.
- **`k = 1`:** There is one cycle, so all array values must become equal to a global median.
- **Even cycle length:** Either middle value minimizes the absolute deviations; selecting the upper median gives the same cost.
- **Large values:** The total operation count can exceed 32-bit range, so fixed-width implementations need 64-bit accumulation.
