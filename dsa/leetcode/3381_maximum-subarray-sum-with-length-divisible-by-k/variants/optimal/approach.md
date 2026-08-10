## General

**Express subarray sums as prefix differences.** After processing index `i`, running sum `s` equals the sum of `nums[0..i]`. If a candidate subarray begins at `j`, its sum is

$$
s-\operatorname{prefix}(j-1),
$$

where the conceptual prefix before the array, at index $-1$, has sum zero.

**Translate the length rule into matching remainders.** Subarray `[j,i]` has length `i-j+1`. This is divisible by `k` exactly when

$$
i-j+1\equiv0\pmod{k},
$$

or

$$
i\equiv j-1\pmod{k}.
$$

Thus, for an end index `i`, only earlier prefix endpoints whose indices have remainder `i % k` may be subtracted.

**Store the smallest eligible prefix per remainder.** Array `f[r]` is the minimum prefix sum seen at a conceptual or real prefix endpoint whose index modulo `k` is `r`. To maximize `s - previous_prefix` for the current end, subtract the smallest such previous value.

All entries start at infinity except `f[-1] = 0`. Python index `-1` means the last slot, remainder `k-1`. This represents conceptual index $-1$, because $-1\bmod k=k-1$. It enables subarrays beginning at zero whose length is divisible by `k`.

**Query before inserting the current prefix.** At index `i`, the source first computes

`ans = max(ans, s - f[i % k])`

and only afterward updates

`f[i % k] = min(f[i % k], s)`.

This order prevents the current prefix from subtracting itself and creating an empty length-zero subarray. Every stored prefix used by the query ends strictly before `i`.

**Why the minimum prefix is sufficient.** For fixed current `s` and required remainder, every eligible subarray differs only in the earlier prefix sum. The smallest earlier prefix gives the largest difference. Larger prefixes can never improve a future answer once a smaller prefix with the same remainder exists, so one value per class is enough.

**Handle all-negative input.** `ans` begins at negative infinity, not zero. The problem requires a nonempty subarray, and the maximum legal sum may be negative. Once index `k-1` is reached, the conceptual zero prefix supplies at least one finite candidate because `k <= n`.

**Trace `k=2`.** Conceptual index $-1$ initializes remainder one. At index one, the two-element prefix has end remainder one, so subtracting zero considers `nums[0..1]`. Prefixes ending at even indices populate remainder zero and can later begin valid even-length subarrays one position after those endpoints.

**Trace why an earlier negative prefix helps.** If two stored prefixes with the same remainder are five and negative three, a future running sum ten produces candidate sums five and thirteen. Retaining only negative three is always at least as good.

**Map a stored prefix back to a start index.** Suppose `f[r]` came from the running sum after index `p`, where `p % k == r`. When current index `i` has the same remainder, the represented subarray starts at `p+1` and has length

$$
i-(p+1)+1=i-p.
$$

Because $i$ and $p$ share a remainder, $i-p$ is a positive multiple of $k$. This makes the remainder table a compact encoding of all legal start positions.

The special zero prefix behaves the same way with `p=-1`. At current index `k-1`, length is `(k-1)-(-1)=k`, so the first full-length candidate is enabled at exactly the correct time.

**Why every legal subarray is represented.** Its end index and prefix-before-start share a remainder, so that earlier prefix was eligible for the corresponding `f` slot before the end was processed. The slot may contain an even smaller prefix, which yields an equal or better legal subarray. Conversely, every subtraction from a matching remainder has length divisible by `k` and uses an earlier endpoint, so it describes a nonempty legal subarray.

## Complexity detail

The loop processes each of $n$ elements once with constant arithmetic and array access, giving $O(n)$ time.

The remainder table has exactly `k` entries, giving $O(k)$ auxiliary space. Running sum and answer use $O(1)$ more. The input is not modified.

## Alternatives and edge cases

- **Full prefix array:** It makes formulas explicit but uses $O(n)$ space and still needs remainder minima.
- **Enumerate all subarrays:** It costs $O(n^2)$ even with prefix sums.
- **Fixed-length sliding windows:** Legal lengths include every multiple of `k`, not just one length.
- **`k=1`:** Every nonempty subarray is legal; the recurrence becomes the standard maximum-subarray prefix-minimum method.
- **`k=n`:** Only the full array has a positive legal length.
- **All-negative values:** Negative infinity initialization preserves the best required negative sum.
- **Conceptual prefix index:** `f[-1]=0` represents index $-1$ and remainder `k-1`.
- **Update order:** Inserting current `s` before querying would allow an illegal empty subarray.
- **Infinity slot:** Before a remainder has an eligible prefix, subtraction yields negative infinity and cannot change the answer.
- **Large sums:** Python integers avoid overflow.
- **Nonempty guarantee:** Since `k<=n`, at least one divisible-length subarray exists.
- **Remainder classes:** Only index remainders matter; prefix-sum numeric remainders are irrelevant.
- **Stored start recovery:** A prefix ending at `p` represents a subarray beginning at `p+1`.
- **First finite candidate:** The conceptual prefix guarantees one by index `k-1`.
- **Tied minima:** Keeping one numeric minimum is enough.
- **Input preservation:** Only a running sum and separate table are updated.
- **Import requirements:** `inf` and `List` must be available.
