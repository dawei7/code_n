## General

Applying each operation character by character repeats work whenever ranges overlap. A difference array records each range's net effect using only its two boundaries.

**Encode an inclusive range.** Treat a forward shift as `+1` and a backward shift as `-1`. For `[start, end]`, add that amount at `difference[start]` and subtract it at `difference[end + 1]`. Allocating `n + 1` entries makes the closing boundary valid even when `end` is the final index.

**Recover each position's total.** Scan the string from left to right while accumulating the difference-array prefix sum. At index `i`, the running value equals the algebraic sum of every operation whose range contains `i`.

Convert the current letter to an offset from `'a'`, add the running shift, take the result modulo 26, and convert back to a character. Python's modulo also normalizes negative totals, so backward wraparound follows naturally.

Each range contributes its amount beginning exactly at `start` and stops contributing immediately after `end`. Therefore the prefix sum gives every character precisely the combined shift specified by all and only its covering operations.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$ and let $m$ be the number of operations. Recording the $m$ ranges and scanning the $n$ characters take $O(n+m)$ time. The difference array and output use $O(n)$ space.

## Alternatives and edge cases

- **Apply every operation directly:** Updating each covered character is straightforward but can take $O(nm)$ time when all ranges span the string.
- **Fenwick tree:** Range updates and point queries also work in $O((n+m)\log n)$ time, but an offline difference array is simpler and faster.
- **Inclusive endpoint:** The closing difference belongs at `end + 1`, not at `end`.
- **Final-index range:** An array of length `n + 1` handles a range ending at `n - 1` without a branch.
- **Negative net shift:** Modulo 26 must normalize backward totals and `'a'` to `'z'` wrapping.
- **Cancellation:** Equal forward and backward coverage cancels before character conversion.
