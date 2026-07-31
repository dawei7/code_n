## General

**Reduce products to parity.** A product of integers is even if and only if at least one factor is even. There is no need to multiply values, so neither product growth nor overflow affects the algorithm.

Process `nums` from left to right and remember `last_even`, the index of the most recent even value, or `-1` if none has appeared. Consider a subarray ending at the current index `i`. It has an even product exactly when its start is at or before `last_even`; such a subarray contains that even value. Therefore the valid starts are the indices from `0` through `last_even`, giving `last_even + 1` qualifying subarrays ending at `i`.

When `nums[i]` is even, update `last_even = i` before adding this contribution. When it is odd, the saved index remains unchanged, and the same earlier even value continues to certify every start at or before it. Summing the contribution for every right endpoint counts each non-empty subarray exactly once, according to its unique ending index.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. The scan performs constant work per element, so it takes $O(n)$ time. The answer, current index, and most recent even index use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Subtract all-odd runs:** Start from the total $n(n+1)/2$ subarrays and subtract $k(k+1)/2$ for every maximal run of $k$ odd values. This is also $O(n)$ time and $O(1)$ space.
- **Quadratic enumeration:** Checking every start and end directly is straightforward but takes $O(n^2)$ time and is unnecessary because parity depends only on whether an even value occurs.
- **All values odd:** `last_even` stays `-1`, every contribution is zero, and the answer is zero.
- **All values even:** At endpoint `i`, all `i + 1` starts qualify, yielding every possible non-empty subarray.
- **Single element:** An even value contributes one; an odd value contributes zero.
- **Large values:** Only `value % 2` is evaluated, so the algorithm never forms potentially enormous products.
