## General

The score at index `i` depends only on how many even and odd values occur strictly after it; their exact values and positions do not matter. A right-to-left scan makes those two quantities available without building suffix arrays.

Maintain `even_to_right` and `odd_to_right`. Immediately before processing index `i`, they count the even and odd values at indices from `i + 1` through `n - 1`. Therefore:

- if `nums[i]` is odd, its opposite-parity partners are exactly the `even_to_right` values;
- if `nums[i]` is even, its partners are exactly the `odd_to_right` values.

Write that count into `answer[i]`, then add `nums[i]` to the matching parity counter. Updating after writing is essential: the definition requires $i<j$, so an index must never count itself.

The invariant is true before the first iteration because there is nothing to the right of the last index. Each update adds precisely the element that will lie to the right during the next iteration. By induction, the selected opposite counter contains every and only legal partner for each index, so every output score is correct.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan visits each element once, taking $O(n)$ time. Apart from the required length-$n$ output array, the two counters and loop index use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **All later-pairs scan:** Test every pair `i < j` and increment the score when their parities differ. This directly follows the definition but takes $O(n^2)$ time.
- **Two suffix-count arrays:** Precompute how many evens and odds occur after every position. This also takes $O(n)$ time, but consumes $O(n)$ avoidable auxiliary space.
- **Left-to-right totals:** Count all evens and odds first, then decrement the current parity before reading the opposite total. This is another $O(n)$ formulation, though the reverse-scan invariant mirrors “strictly to the right” more directly.
- **Singleton:** No later index exists, so the sole score is zero.
- **One parity only:** Every score is zero because no opposite-parity partner exists.
- **Duplicates:** Equality is irrelevant; only each value modulo two affects the score.
- **Update order:** Adding the current value before assigning its score would violate the strict condition `i < j` in formulations that read the same-parity counter.
