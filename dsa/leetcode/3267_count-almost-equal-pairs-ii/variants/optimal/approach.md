## General

Let $n$ be the array length and $d$ the maximum digit count.

**Orient every asymmetric match by sorting**

Sort the values numerically and keep frequencies of exact values already processed. A swap sequence that preserves digit width is reversible by applying its swaps in reverse order. The only asymmetric outcome discards leading zeros and is numerically smaller, so the later, larger value can generate the earlier one. It is therefore sufficient to enumerate transformations only from the current sorted value.

**Enumerate zero, one, and two swaps**

Start a set with the unchanged value. For every first pair of digit positions, swap them and record the resulting integer. While that first swap is active, try every pair of positions for a second swap and record those results too. Restore each swap immediately after its branch so all branches begin from the correct digit arrangement.

The set deduplicates repeated outcomes caused by equal digits, reversing the first swap, or different swap sequences reaching the same arrangement. Sum the stored frequencies of every distinct reachable integer, then increment the frequency of the current original value.

Every contribution corresponds to a legal zero-, one-, or two-swap transformation of the current value. Conversely, reversibility plus the sorted leading-zero argument ensures the later member of every almost-equal pair generates the earlier member. Since an index enters the frequency map only after it has been queried, every pair is counted once and only once.

## Complexity detail

Sorting takes $O(n \log n)$. There are $O(d^2)$ choices for each of two swaps, and joining and converting a final digit list costs $O(d)$, giving $O(n \log n + n d^5)$ time in an explicit digit-cost model. The contract fixes $d \le 7$, so the digit factor is bounded and the scaling in $n$ is $O(n \log n)$. The frequency map uses $O(n)$ entries and at most $O(d^4)$ generated results are retained for one value.

## Alternatives and edge cases

- **Check every index pair:** Precomputing transformations and testing all $O(n^2)$ pairs avoids repeated generation but remains quadratic in the array length.
- **Compare digit-frequency signatures:** Equal multisets do not prove that two swaps suffice; three disjoint transpositions require three operations.
- **Handle one swap on each side separately:** Composing one side's swap with the inverse of the other side's swap gives an equivalent sequence of at most two swaps on one fixed-width representation, which the enumeration already covers.
- **Discard leading-zero results:** This misses valid cross-length pairs such as `1` and `100`.
- Equal values qualify without any swap and contribute all index combinations.
- A three-cycle of digit positions is reachable in two swaps.
- Repeating or reversing a swap may return the original value; the result set prevents duplicate counting.
- Equal digits can make many swap sequences indistinguishable.
- Seven-digit inputs remain within the bounded enumeration promised by the source constraints.
