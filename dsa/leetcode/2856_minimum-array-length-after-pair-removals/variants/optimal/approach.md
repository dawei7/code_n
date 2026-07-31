## General

**Identify what can prevent another pair**

Every operation removes two unequal values; the index order is immaterial because the smaller selected value can be named `i` and the larger one `j`. Let $f$ be the largest frequency of any value and let $n$ be the array length. The $f$ copies of that dominant value can only be removed by pairing them with the other $n-f$ elements. Therefore at least

$$
f - (n-f) = 2f-n
$$

copies remain when $f > n-f$. Separately, every operation removes exactly two elements, so a remainder must have the same parity as $n$; at least $n \bmod 2$ elements remain.

These bounds are attainable. If $f > n/2$, pair every non-dominant element with one dominant copy. That removes $2(n-f)$ elements and leaves exactly $2f-n$. If $f \le n/2$, no value outnumbers all possible partners. The values can be matched into unequal pairs until nothing remains for even $n$, or one element remains for odd $n$. Thus the answer is

$$
\max(n \bmod 2,\; 2f-n).
$$

**Exploit the non-decreasing input**

Equal values occupy contiguous runs. Scan `nums` once, maintaining the current run length and the largest run length seen. This obtains $f$ without a hash table. Substitute it into the formula after the scan.

## Complexity detail

The scan visits all $n$ elements once, taking $O(n)$ time. It keeps only the current and maximum run lengths, so it uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size` and supplies legal, strictly increasing arrays. The optimal method still scans the complete input. A correct binary-search method checks $O(n)$ aligned pairs at each of $O(\log n)$ candidate counts; it completes all three tiers but its $O(n \log n)$ growth fails the scaling verdict.

## Alternatives and edge cases

- **Two pointers across the halves:** Pair the lower half against the upper half, advancing the upper pointer until it holds a strictly larger value. This also finds the maximum pair count in $O(n)$ time and $O(1)$ space.
- **Frequency map:** Count every value and apply the same formula. It remains $O(n)$ time but uses $O(n)$ space and ignores the useful sorted-order guarantee.
- **Binary search on the pair count:** Test whether the smallest $k$ elements can pair with the largest $k$ elements, then binary-search the largest valid $k$. This is correct in $O(n \log n)$ time, but the linear characterization is simpler.
- **All values equal:** No valid pair exists, so the entire array remains.
- **Odd balanced array:** Even with sufficient partners, one element remains because removals occur in pairs.
- **Dominant value at any position:** The largest run may be first, last, or in the middle; the scan must retain the maximum across all completed runs.
- **Strict comparison:** Equal values cannot be paired because the operation requires `<`, not `<=`.
