## General

Simulating up to $10^9$ heap operations is impossible. The solution simulates only an initial balancing phase. Once all current values lie within one multiplicative band, future minimum selections repeat in sorted rounds and can be distributed arithmetically.

If `multiplier == 1`, no operation changes any value. The original values are already below the modulus because they are at most $10^9$, so returning `nums` immediately is correct.

Otherwise, a heap of `(value,index)` pairs enforces minimum value and earliest-index tie-breaking. Let `m = max(nums)` be the original maximum. While operations remain and the current heap minimum is below `m`, the code pops it, multiplies its exact value, reinserts it, and decrements `k`.

This phase ends when every current value is at least `m`. Any value multiplied during the phase was below `m` immediately beforehand, so afterward it is below `m * multiplier`. Original values never exceeded `m`. Thus all values now lie in

$$
m\le x<m\cdot\texttt{multiplier}.
$$

If the current minimum is multiplied once more, it becomes at least `m * multiplier` and cannot be minimum again until every other current value has been selected once. Therefore subsequent operations proceed through the current values in ascending `(value,index)` order, one complete round at a time. After a complete round, all values have gained one common multiplier factor, so their relative order returns to the same order.

The heap list is sorted to obtain that next-selection order. If the remaining operation count is `k = qn + r`, every element is selected in `q = k // n` complete rounds, and the first `r = k % n` sorted elements are selected once more.

For sorted position `i`, its exponent is

`k // n + int(i < k % n)`.

The result for its original array index `j` is `x * multiplier**exponent`, reduced modulo `10 ** 9 + 7`. Modular exponentiation `pow(multiplier, exponent, mod)` handles huge exponents in logarithmic time.

Modulo is applied only to final outputs. Applying it during selection would change numerical ordering and produce the wrong simulated process. Preliminary heap values remain exact Python integers; only the bulk-computed final values are reduced.

Tuple sorting preserves the first-index rule for equal current values. Those equal entries are selected in increasing original index within each remaining round.

The algorithm is correct because the preliminary loop exactly reproduces every operation until the band invariant holds. The band proves the rest decomposes into repeated sorted rounds. Quotient and remainder assign exactly the number of selections each element would receive, and writing results back by original index reconstructs the requested array.

## Complexity detail

Let $n$ be the array length and $M$ the original maximum. For multiplier greater than one, each element can be selected only $O(\log_{\texttt{multiplier}} M)$ times before reaching `m`. Each preliminary pop/push costs $O(\log n)$, for $O(n\log M\log n)$ in a coarse bound.

Sorting the heap costs $O(n\log n)$. Computing $n$ modular powers costs $O(n\log k)$. Total matches the declared $O(n\log M\log n+n\log k)$ scale.

The heap and sorted list representation use $O(n)$ space. The input is mutated in place.

## Alternatives and edge cases

- **Simulate all operations:** Heap simulation costs $O(k\log n)$ and is impossible for $k=10^9$.
- **Apply modulo during heap updates:** This is incorrect because modulo residues do not preserve the order of exact values.
- **Binary-search a global level:** One can derive selection counts by logarithmic leveling, but the multiplicative-band round argument is simpler.
- **`multiplier = 1`:** Every operation is a no-op, and the early return avoids a nonterminating “below maximum” balancing concept.
- **All values equal:** The initial phase is skipped. Remaining operations are distributed by value-index order, starting from the earliest index.
- **Operations exhausted during balancing:** `k` becomes zero; every exponent is zero and the sorted exact values are written back modulo the modulus.
- **Ties after balancing:** Sorting pairs uses the index as the required secondary key.
- **One element:** Every remaining operation belongs to that element, so its exponent is exactly `k`.
- **Large exact products:** Python integers safely hold preliminary values before final modular reduction.
- **Input mutation:** Results are assigned into original positions in `nums`; the caller's list is changed.
- **Why the original maximum stays fixed:** `m` is a threshold, not a current maximum tracker. Raising it after each multiplication would postpone the round phase indefinitely. The proof needs the maximum from the initial array as one common level every element can reach.
- **Values overshooting `m`:** A selected value may jump far above `m`, but it remains below `m * multiplier` because it was strictly below `m` before multiplication. This strict band is what guarantees one selection per element in a round.
- **Remainder-round ordering:** Only the first `k % n` pairs in sorted value-index order receive the extra exponent. Assigning extras by original array order would be wrong when current values differ.
- **Final array order:** Sorting `pq` is used only to allocate future operations. Writing each result to stored index `j` restores the original positional layout instead of returning the heap's sorted order.
