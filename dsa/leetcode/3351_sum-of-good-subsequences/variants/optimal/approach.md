## General

Process the array from left to right so every stored subsequence uses only indices before the current element. For each ending value $v$, maintain:

- $C_v$: the number of good subsequences seen so far whose last value is $v$;
- $S_v$: the sum of the element sums of all those subsequences.

**Append the current value.** Let the next array value be $x$. A good subsequence ending at this position is either the singleton `[x]`, or is formed by appending $x$ to an earlier good subsequence ending at $x-1$ or $x+1$. Therefore the number of newly formed subsequences is

$$
\Delta C = 1 + C_{x-1} + C_{x+1}.
$$

Appending $x$ preserves every prior element sum and adds $x$ once to each new subsequence, including the singleton. Hence their combined element sum is

$$
\Delta S = S_{x-1} + S_{x+1} + x\Delta C.
$$

Add these new states to the existing aggregates for ending value $x$: `C[x] += ΔC` and `S[x] += ΔS`. The additions are essential because earlier occurrences of $x$ end different index-selected subsequences that remain available. Also add $\Delta S$ to the global answer, since it represents exactly the good subsequences whose final selected index is the current position.

Every non-empty good subsequence has one unique final index. Removing that final value leaves either the empty sequence or a previously processed good subsequence ending one away from it, so the transition creates every valid subsequence exactly once. Conversely, every transition appends only to an eligible neighboring value, so it cannot create an invalid sequence.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $u$ be the number of distinct values encountered. Each element performs a constant number of expected-time hash-table reads and writes, so the expected time complexity is $O(n)$. The two tables store $O(u)$ keys, giving $O(u)$ auxiliary space.

All counts, totals, products, and the answer are reduced modulo $10^9+7$ after each transition. The benchmark size is $n$. Alternating zero and one creates many extendable index-based states; the aggregated method still performs constant work per element, while the calibrated slower DP scans all earlier indices for each new position and requires $O(n^2)$ time.

## Alternatives and edge cases

- **DP by ending index:** Keeping a state for every position and checking all earlier positions is direct and correct, but takes $O(n^2)$ time.
- **Enumerate subsequences:** There are $2^n-1$ non-empty index selections, so explicit generation is infeasible.
- **Fixed-size arrays by value:** The value bound permits array states, but initialization and storage depend on the full value domain; hash maps keep space proportional to encountered values.
- **Repeated equal values:** Equal values cannot be consecutive inside a good subsequence, yet each occurrence creates a distinct singleton and may extend the same neighboring states.
- **Zero values:** A zero singleton contributes no sum but must still increase its count because later ones can extend it.
- **Values absent from the prefix:** Missing states contribute zero through the default-valued maps.
- **Index order:** States are updated only after reading both neighboring values, ensuring extensions always respect original index order.
- **Modulo arithmetic:** Counts must also be reduced, because they are multiplied by the appended value in later transitions.
