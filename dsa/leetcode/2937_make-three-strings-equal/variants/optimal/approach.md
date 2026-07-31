## General

**Every reachable result is a prefix.** Deleting only rightmost characters can
turn each original string only into one of its nonempty prefixes. Therefore a
common final string must be a nonempty prefix shared by all three inputs.
Conversely, any such shared prefix is reachable by deleting every character
after it from each string.

**Keep the longest shared prefix.** Compare characters at matching positions
until one string ends or the first mismatch occurs. Let the shared-prefix
length be $p$. Retaining that prefix costs

$$
\lvert\texttt{s1}\rvert+\lvert\texttt{s2}\rvert+\lvert\texttt{s3}\rvert-3p
$$

deletions. Any shorter common prefix would delete three additional characters
for every lost position, so the longest one uniquely minimizes the operation
count. If $p=0$, no nonempty common prefix exists and the required result is
impossible. Otherwise, deleting each suffix realizes the stated minimum.

## Complexity detail

Let $L$ be the shortest input length. The comparison examines at most $L$
aligned character triples, taking $O(L)$ time. It stores only the prefix length
and current characters, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Try candidate prefixes from longest to shortest:** Recompare all characters for every candidate length; this is correct but takes $O(L^2)$ time in the worst case.
- **Simulate deletions:** Repeatedly trim the currently longest or mismatching strings until they agree; this reaches the same prefix but creates avoidable string copies.
- **Different first characters:** No nonempty common prefix exists, so return `-1` immediately.
- **One string is the common prefix:** Only the longer strings need deletions.
- **Already equal:** The full strings are the longest common prefix and the answer is zero.
- **Length-one strings:** They are either already the same, requiring zero operations, or impossible to equalize without emptying one.
