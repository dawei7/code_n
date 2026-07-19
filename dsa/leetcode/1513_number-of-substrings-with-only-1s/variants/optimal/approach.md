## General
**Count qualifying substrings by their right endpoint**

Maintain `run`, the number of consecutive `1` characters ending at the current position. Reading a `1` extends that run by one; reading a `0` resets it to zero.

If the current run length is $r$, exactly $r$ qualifying substrings end here: the final `1` alone, the final two `1`s, and so on through the entire run. Add $r$ to the answer at every position. This counts a range precisely when its right endpoint is processed, so no substring can be missed or counted twice.

**Connection to triangular run totals**

A maximal run of $k$ ones contributes

$$
1+2+\cdots+k=\frac{k(k+1)}{2}
$$

substrings. The streaming additions reproduce that sum without waiting for the run to end or storing its boundaries. Zeros reset the state, so no counted range crosses between runs. Taking the modulus after each addition keeps intermediate values bounded and is equivalent to reducing only the final sum.

## Complexity detail
Each of the $n$ characters is examined once and triggers constant work, giving $O(n)$ time. The running length, total, modulus, and current character are the only stored state, so auxiliary space is $O(1)$.

The output modulus does not affect which substrings qualify; it is applied only to the accumulated count.

## Alternatives and edge cases
- **Split into runs:** split on `0` and sum $k(k+1)/2$ for each resulting run. This is linear time but may allocate substrings proportional to the input length.
- **Scan maximal runs manually:** detect each run's boundaries and add its triangular number at the end. This has the same bounds but slightly more boundary bookkeeping.
- **Enumerate all substrings:** verify each range or use prefix counts. It is correct but requires at least $O(n^2)$ candidate ranges.
- **All zeros:** every run length stays zero and the answer is zero.
- **All ones:** the answer is $n(n+1)/2$ before reduction.
- **Isolated ones:** each contributes exactly one single-character substring.
- **Several runs:** their contributions add independently; a zero blocks every cross-run range.
- **Single character:** `"1"` returns one and `"0"` returns zero.
- **Modulo overflow:** apply modulo arithmetic during accumulation so fixed-width implementations remain safe on long runs.
