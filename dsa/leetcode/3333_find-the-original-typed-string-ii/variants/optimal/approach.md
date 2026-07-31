## General

Split `word` into maximal runs of equal characters. If a run has displayed length $L$, its intended length can be any integer from $1$ through $L$. Choices in different runs are independent, and their characters and order are fixed, so every tuple of chosen run lengths identifies exactly one possible original string. The total number of unrestricted tuples is therefore the product of all run lengths.

Let $r$ be the number of runs. Every possible original has length at least $r$. When $r \ge k$, the minimum-length condition is automatic and the product is already the answer. Otherwise, $r<k\le2000$, so it is affordable to count only the invalid tuples whose total length is below $k$ and subtract them from the product.

Let `counts[t]` be the number of ways the processed runs can have total intended length $t$, retaining only $0\le t<k$. It begins with `counts[0] = 1`. For a new run of length $L$,

$$
\texttt{next\_counts[t]}
=
\sum_{x=1}^{L}\texttt{counts[t-x]},
$$

where indices outside $0,\ldots,k-1$ contribute zero. Adjacent values of $t$ use almost the same interval of the previous array. Maintain its sum as a sliding window: add `counts[t - 1]` when advancing to $t$, and remove `counts[t - L - 1]` once that index enters the array. This makes every state transition constant time.

The run tuple bijection proves the product counts every possible original exactly once. The dynamic program considers every permitted length for each processed run, so after all runs, the sum of `counts` is exactly the number of originals shorter than $k$. Subtracting that invalid count from the unrestricted product leaves precisely the requested originals, with all arithmetic reduced modulo $10^9+7$.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. Extracting runs and multiplying their lengths takes $O(n)$ time. If the dynamic program runs, the number of runs $r$ is less than $k$, and it processes $k$ states for each run in $O(rk)\subseteq O(k^2)$ time. The total bound is $O(n+k^2)$. Run lengths are retained only while the run count is below $k$; once it reaches $k$, the algorithm needs only the product. The retained lengths and two dynamic-programming arrays therefore use $O(k)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every original string:** Taking the Cartesian product of run-length choices is exact but can require exponentially many tuples.
- **Triple-loop dynamic programming:** Summing every possible new run length separately takes $O(rk^2)$ time in the worst relevant case; the sliding window removes that extra factor.
- **Count valid lengths directly:** Tracking every length from $k$ through $n$ makes the state range depend on a word of length up to $5\cdot10^5$; counting the bounded invalid complement is smaller.
- **Enough runs already:** If $r\ge k$, even choosing one character per run is valid, so no dynamic programming is needed.
- **Threshold above displayed length:** No original can be longer than `word`, and subtracting all short tuples correctly returns zero.
- **Single run:** A run of length $L$ contributes exactly $\max(0,L-k+1)$ valid intended lengths.
- **Modulo subtraction:** Normalize the difference after subtracting the invalid count so it remains in the canonical modular range.
