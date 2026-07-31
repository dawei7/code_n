## General

After $t$ seconds, the first $tk$ original characters have been removed. If $tk < N$, the untouched suffix `word[tk:]` is forced to remain at the front of the current word; appended characters can affect only the positions after that suffix. Therefore, time $t$ is feasible exactly when `word[tk:]` equals the initial prefix of the same length, `word[:N - tk]`.

Check the positive reachable removal counts $k, 2k, 3k, \ldots$ in increasing order. The first suffix-prefix equality gives the minimum feasible time because every smaller positive time has already failed its forced-character comparison. If no equality occurs before all original characters disappear, then after $\lceil N/k \rceil$ seconds every position can be supplied by appended characters, so that time is always feasible.

## Complexity detail

There are at most $\lceil N/k \rceil$ candidate times. A Python slice comparison can inspect $O(N)$ characters, so the worst-case running time is $O(N^2)$. The temporary slices contain at most $N$ characters, giving $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Prefix-function or Z-function matching:** Preprocessing border lengths can find all suffix-prefix matches in $O(N)$ time and $O(N)$ space, which is required by the larger-input version of this problem but unnecessary for this version's $N \le 50$ contract.
- **Rolling hash:** Prefix hashes allow constant-time candidate comparisons after $O(N)$ preprocessing, but collision handling makes the deterministic direct comparison preferable at this input size.
- **Full removal:** When no proper suffix works, $\lceil N/k \rceil$ seconds remove every original character and the arbitrary appended characters can reconstruct the target.
- **Positive time:** Even if every character is identical, time zero is not a valid answer; the first completed operation may return the word in one second.
- **Arbitrary appended characters:** The method checks only the untouched suffix. It must not require the newly appended block to equal the block that was removed.
