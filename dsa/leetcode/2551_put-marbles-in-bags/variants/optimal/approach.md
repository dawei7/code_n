## General

Dividing $n$ marbles into `k` non-empty contiguous bags is equivalent to choosing `k - 1` cuts among the $n - 1$ gaps. The first marble and last marble always contribute once to every score. A cut between positions `i` and `i + 1` additionally makes `weights[i]` the end of one bag and `weights[i + 1]` the start of the next, contributing `weights[i] + weights[i + 1]`.

**The fixed endpoints cancel**

Every distribution has the same outer contribution `weights[0] + weights[-1]`. Only the chosen adjacent-pair contributions vary. To minimize the score, choose the `k - 1` smallest boundary costs; to maximize it, choose the `k - 1` largest. The requested difference is the difference of those two sums because the fixed outer contribution cancels.

Sorting all adjacent sums makes both extreme selections contiguous slices of one ordered list. When `k = 1`, there are no cuts and only one distribution, so the difference is zero.

## Complexity detail

Let $n$ be the number of marbles. Building the $n-1$ boundary costs takes $O(n)$ time, sorting them takes $O(n \log n)$ time, and summing the selected extremes takes $O(n)$ time in the worst case. The boundary list and sorting workspace use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all partitions:** Choosing every set of `k - 1` gaps is combinatorial and infeasible.
- **Repeated minimum and maximum selection:** Selecting each boundary with a fresh scan is correct but can take $O(n^2)$ time.
- **Two heaps:** Keeping only the smallest and largest `k - 1` values can use $O(k)$ space with $O(n \log k)$ time, but full sorting is simpler and meets the required bound.
- **Include outer endpoints in each comparison:** They are identical for every distribution and cancel from the final difference.
- **One bag:** With `k = 1`, no cut is chosen and the answer is 0.
- **One marble per bag:** With `k = n`, every gap must be cut, so there is only one distribution and the answer is also 0.
- **Repeated boundary costs:** Equal adjacent sums may be selected in any order without changing either extreme score.
- **Large weights:** The total score may exceed 32-bit integer range in other languages.
