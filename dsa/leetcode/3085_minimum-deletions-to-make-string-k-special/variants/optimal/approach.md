## General

Only the frequency of each letter matters; deletion order and character positions do not affect the optimum. Count the positive frequencies of the at most 26 lowercase letters.

**Fix the smallest surviving frequency.** Consider an optimal nonempty result and let its minimum positive frequency be $x$. At least one surviving letter originally has frequency exactly $x$: if every surviving frequency were originally larger, lowering the chosen minimum would not force any additional deletion. It is therefore sufficient to try every original positive frequency as $x$.

For a fixed $x$, each letter is handled independently:

- If its frequency $f$ is below $x$, retaining it would make the chosen minimum smaller, so delete all $f$ occurrences.
- If $x \le f \le x+k$, retain all occurrences.
- If $f>x+k$, delete exactly $f-(x+k)$ occurrences so its final frequency reaches the largest allowed value.

These choices are forced or deletion-minimal for the selected range $[x,x+k]$. Summing them gives the best result having minimum frequency $x$; taking the minimum over every candidate $x$ covers the global optimum. A result containing a single character is included automatically because all other frequency groups may be deleted.

## Complexity detail

Let $n=\lvert \texttt{word} \rvert$ and let $A=26$ be the fixed alphabet size. Counting takes $O(n)$ time, while trying every frequency against every other frequency takes $O(A^2)=O(1)$ time. The total time is $O(n)$ and the frequency storage uses $O(A)=O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort frequencies and use prefix sums:** Sorting the at most 26 counts can reduce repeated arithmetic, but the alphabet is fixed and the asymptotic bounds remain unchanged.
- **Try every integer minimum:** Checking every value from $1$ through the maximum frequency and rescanning the string can take $O(n^2)$ time; only existing positive frequencies need consideration.
- **Delete one occurrence at a time:** Rebuilding counts after each greedy deletion is both slower and harder to justify globally.
- **One distinct letter:** Any one-frequency-set string is already k-special.
- **Zero `k`:** All surviving letters must have identical frequencies.
- **Large `k`:** If the original maximum and minimum positive frequencies differ by at most `k`, the answer is zero.
- **Remove a letter completely:** Zero-frequency letters are absent and do not participate in the pairwise condition.
- **Rare versus frequent groups:** Deleting a small group entirely may be cheaper than trimming every large group, which is why every candidate minimum must be tested.
