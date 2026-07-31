## General

At each index, count the strictly increasing subarrays ending exactly there. If the current value is greater than its predecessor, every increasing suffix ending at the predecessor can be extended, and the one-element current subarray is added. Thus the suffix length increases by one.

If the comparison is equal or decreasing, no longer suffix survives, so only the current one-element subarray remains and the length resets to one. Add this suffix length to the answer at every position.

Every qualifying subarray has one unique ending index, and the recurrence counts precisely all valid starting positions for that end. Summing those disjoint groups therefore counts every strictly increasing subarray exactly once.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. One scan performs constant work per value, for $O(n)$ time. The running suffix length and total use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every start:** Extending each start until its first violation is correct but takes $O(n^2)$ time on a fully increasing array.
- **Sum maximal runs:** A maximal increasing run of length $\ell$ contributes $\ell(\ell+1)/2$ ranges; aggregating completed runs is another $O(n)$ formulation.
- **Equal neighbors:** Strictly increasing means equality resets the run.
- **Single element:** It contributes exactly one subarray.
- **Fully decreasing array:** Only the $n$ singleton ranges count.
- **Fully increasing array:** The answer is $n(n+1)/2$, which motivates 64-bit output types.
