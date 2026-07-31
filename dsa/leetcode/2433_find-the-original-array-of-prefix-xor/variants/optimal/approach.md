## General

The first prefix contains only `arr[0]`, so `arr[0] = pref[0]`. For every later index,

$$
\texttt{pref[i-1]}=\texttt{arr[0]}\mathbin{\hat{}}\cdots\mathbin{\hat{}}\texttt{arr[i-1]}
$$

and `pref[i]` contains those same values plus `arr[i]`. XORing the two prefixes cancels every shared value because $x\mathbin{\hat{}}x=0$ and $0\mathbin{\hat{}}y=y$. Consequently, `arr[i] = pref[i - 1] ^ pref[i]`.

Append that adjacent-prefix XOR from left to right. Each output position follows directly from the defining equation, so the reconstructed array is both valid and unique.

## Complexity detail

The algorithm reads each of the $n$ prefix values a constant number of times, giving $O(n)$ time. The returned array uses $O(n)$ space; beyond that required output, only the current index is needed.

## Alternatives and edge cases

- **Recompute every original prefix:** XORing all previously recovered values again for each index is correct but takes $O(n^2)$ time.
- **Modify `pref` in place:** Processing from right to left can reduce auxiliary storage, but mutates the caller's input.
- **Single element:** The only original value equals the only prefix value.
- **Equal neighboring prefixes:** Their recovered value is zero.
- **Zero prefix:** Zero participates in XOR normally and does not reset the reconstruction.
- **Maximum values:** XOR depends on bits rather than arithmetic magnitude, so the same cancellation identity applies.
