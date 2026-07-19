## General
**Recognize when separation is possible**

Let the most frequent character occur `maximum` times in a length-`n` string. Its copies require at least `maximum - 1` other characters as separators, so a solution exists exactly when `maximum <= (n + 1) // 2`. Return the empty string if this bound fails.

**Fill even positions before odd positions**

Sort the distinct lowercase characters by descending frequency. Write all copies of each character into positions `0, 2, 4, ...`, continuing at positions `1, 3, 5, ...` after the even positions are full. The feasibility bound ensures the most frequent character fits entirely into alternating slots. Less frequent characters then fill the remaining alternating slots.

Copies of one character are placed two positions apart unless placement crosses from the final even slot to the first odd slot. At that crossing, the previous character came from a frequency at least as large and has already exhausted its copies; descending-frequency placement together with the feasibility bound prevents the same character from occupying both sides of the boundary. Thus adjacent output positions differ. Every counted occurrence is written exactly once, so the result is also a permutation of the input.

## Complexity detail
Counting and filling take $O(n)$ time. Sorting at most 26 lowercase character entries is constant work relative to `n`. The output buffer uses $O(n)$ space, while the frequency table is $O(1)$ for the fixed alphabet.

## Alternatives and edge cases
- **Maximum heap with one held-back character:** Repeatedly choose the most frequent available character and delay its reuse; this is $O(n \log k)$ for `k` distinct characters and effectively linear for lowercase input.
- **Repeatedly recompute remaining frequencies:** It can make the same greedy choice correctly but costs $O(n^2)$ time.
- **Backtracking over permutations:** This becomes exponential and is unnecessary once the frequency bound is known.
- **One-character string:** It is already valid.
- **Dominant count above the bound:** Return the empty string immediately.
- **Dominant count exactly at the bound:** Its copies occupy every even position and remain separated.
- **Multiple valid outputs:** Any output with the same character multiset and no equal neighbors is correct.
