## General

**Turn every frequency change into a constant-time score update**

For a value $x$ currently appearing $c$ times in the window, its contribution is $x^c$ when $c > 0$ and zero when $c = 0$. Adding another $x$ therefore replaces $x^c$ with $x^{c+1}$; removing one replaces $x^c$ with $x^{c-1}$, or removes the contribution entirely when the new count is zero. A frequency map supplies $c$, so the score can be updated without rebuilding the whole window.

Modular division would make removals awkward. Instead, count how often each value appears in the complete input and precompute its powers from exponent zero through that total frequency. Across all values, the numbers of positive exponents sum to $n$, so this preprocessing is linear rather than a product of the number of values and $n$.

**Slide one endpoint at a time**

Process `nums` from left to right. Add the current value's new power contribution. Once the processed prefix would exceed length `k`, remove the value that is exactly `k` positions behind, replacing its old contribution with the power for its decreased count. Reduce the updated score modulo $10^9 + 7$ after both changes.

At every index where a complete length-`k` window exists, this maintained score equals the definition because it contains exactly one power term for every value present and no term for an absent value. Comparing these reduced scores therefore yields precisely the requested maximum.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Building all power rows performs one multiplication per input occurrence, and the sliding window performs constant work per occurrence, for $O(n)$ time. The total power-table length is $O(n)$, while the frequency maps use at most $O(n)$ entries, so the space bound is $O(n)$.

## Alternatives and edge cases

- **Recompute every window:** Building a new frequency map and score for each length-`k` subarray is straightforward but costs $O((n-k+1)k)$ time, which becomes quadratic when both dimensions grow with $n$.
- **Binary exponentiation on every update:** Computing each changed power with modular exponentiation reduces auxiliary storage, but raises the running time to $O(n \log k)$.
- **Modular inverses:** Multiplying a contribution by $x^{-1}$ on removal can avoid power rows because every permitted value is below the prime modulus, but computing or storing inverses adds complexity without improving the linear asymptotic bound.
- **Modulo comparison:** The maximum must be selected after reduction; choosing the window with the largest unreduced sum can return the wrong answer.
- **Window length one:** Each window score is simply its element, so the result is the maximum element.
- **One repeated value:** A window containing only `1` always has score $1$, regardless of its length.
