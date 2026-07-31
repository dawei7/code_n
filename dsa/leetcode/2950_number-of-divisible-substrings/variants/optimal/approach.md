## General

**A divisible substring has an integer average.** Map the letters with the
nine groups from the contract. For a substring of length $L$ and mapped-value
sum $S$, divisibility is exactly $L\mid S$, or equivalently that $S/L$ is an
integer. Every mapped value lies from $1$ through $9$, so any such average is
one of those same nine integers.

**Reduce each possible average to a zero-sum condition.** Fix a candidate
average $a\in\{1,\ldots,9\}$ and replace every mapped value $x$ by $x-a$.
For a substring,

$$
\sum (x-a)=S-aL.
$$

The transformed sum is zero exactly when the original substring has average
$a$. Therefore, for this fixed average, two equal transformed prefix sums
identify one divisible substring.

**Count equal transformed prefixes.** Scan the word once for each of the nine
candidate averages. Maintain the transformed prefix sum and a frequency table
of earlier sums, initially containing the empty prefix sum zero. At every
position, add the frequency of the current sum before recording it. A
substring has only one average, so it can be counted in at most one of the nine
passes; every divisible substring has an integer average in the range and is
counted in its corresponding pass. This proves the total counts each valid
substring exactly once.

## Complexity detail

Let $N=\lvert\texttt{word}\rvert$. There are exactly nine passes, each taking
$O(N)$ expected time with hash-table operations, so total expected time is
$O(N)$. One pass stores at most $N+1$ prefix sums, requiring $O(N)$ auxiliary
space; its table is discarded before the next average.

## Alternatives and edge cases

- **Enumerate every substring:** Extending each starting position and maintaining its mapped sum is correct but takes $O(N^2)$ time.
- **Store sum modulo length:** The modulus changes with every substring length, so one ordinary prefix-remainder table cannot compare all endpoints.
- **Check only one global average:** Different divisible substrings may have different integer averages; all values from 1 through 9 must be considered.
- **Single character:** Its mapped sum equals its mapped digit, so every length-one substring is divisible.
- **Letters in one mapping group:** Every substring has that group's integer average and therefore qualifies.
- **Nonintegral average:** A substring such as values 1 and 2 has average $3/2$ and is not counted by any pass.
- **Overlapping substrings:** Separate pairs of prefix positions are separate substrings and are counted independently.
