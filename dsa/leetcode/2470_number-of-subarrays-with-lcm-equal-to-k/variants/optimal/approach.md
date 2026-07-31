## General

**Group subarrays by their right endpoint.** After processing one array position, store how many subarrays ending there have each distinct least common multiple. When the next value arrives, every previous ending subarray can be extended by that value, and the one-element subarray containing only the new value must also be added.

For a previous LCM $x$ and new value $v$, the extended value is

$$
\operatorname{lcm}(x,v)=\frac{x}{\gcd(x,v)}v.
$$

Different subarrays may produce the same new LCM, so merge their counts in `next_states`. Once the new map is complete, its count stored under `k` is exactly the number of qualifying subarrays ending at the current position; add that count to the answer.

**Discard states that can never reach the target.** If a value does not divide `k`, every subarray containing it has an LCM that also does not divide `k`, so it separates the array into independent valid regions. Likewise, retain a combined state only when its LCM divides `k`. Every retained key is therefore a positive divisor of `k`, which bounds the map by $D$ distinct states.

The transition considers every non-empty subarray exactly once when its right endpoint is processed. The stored key is its actual LCM by the recurrence, and counts with identical keys are merged without losing multiplicity. Summing only the key `k` therefore yields precisely the requested number of subarrays.

## Complexity detail

Let $n$ be the array length and $D$ the number of positive divisors of `k`. Each of $n$ positions updates at most $D$ states. A greatest-common-divisor computation costs $O(\log k)$, so total time is $O(nD\log k)$.

The current and next maps each contain at most $D$ entries, giving $O(D)$ auxiliary space.

## Alternatives and edge cases

- **Extend from every starting index:** Maintaining one running LCM per start is simple and uses $O(1)$ extra space, but takes $O(n^2\log k)$ time when all values keep dividing the target.
- **Recompute each subarray from scratch:** Repeatedly folding the same prefixes can require cubic work and provides no benefit over incremental extension.
- **Non-divisor value:** A value for which `k % value != 0` clears every ending state because no containing subarray can later have LCM `k`.
- **Target one:** Only runs of ones can qualify; state compression still counts all of their subarrays.
- **Repeated equal states:** Counts must be added when multiple prior subarrays produce the same combined LCM.
- **Single-element subarray:** Start `{value: 1}` at every valid position so an element equal to `k` is counted.
