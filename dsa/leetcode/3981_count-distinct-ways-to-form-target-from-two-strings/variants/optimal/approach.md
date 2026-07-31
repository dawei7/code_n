## General

After forming a prefix of `target`, the future depends only on the latest selected index in each source word. Use one-based state coordinates: `dp[i][j]` counts constructions of the processed target prefix whose most recent selection from `word1` is index `i - 1` when $i>0$, and whose most recent selection from `word2` is index `j - 1` when $j>0$. A zero coordinate means that source has not been used. Initially only `dp[0][0] = 1`.

Suppose the next required character is `needed`. If it is taken from one-based position `p` in `word1`, the previous first coordinate may be any value smaller than `p`, while the second coordinate remains fixed. Therefore, when `word1[p - 1] == needed`,

$$
\textit{next}[p][j] = \sum_{i=0}^{p-1} \textit{dp}[i][j].
$$

For every fixed `j`, scan `p` from left to right and maintain this sum as a running prefix. The symmetric transition for choosing one-based position `q` in `word2` is

$$
\textit{next}[i][q] \mathrel{+}= \sum_{j=0}^{q-1} \textit{dp}[i][j],
$$

which is computed by a running prefix along the second coordinate. Adding both transition families is essential: when they reach the same pair of latest indices, their final target character came from different words, so they represent distinct constructions rather than duplicates.

Inductively, every state before a layer counts exactly the valid index selections for that target prefix. Each extension chooses one later matching index from exactly one word, and the prefix sum includes every permitted previous index exactly once. Conversely, every valid longer construction has a unique final source word and index, so removing that final choice reaches exactly one state included by the corresponding sum. Thus the next layer counts every construction once. After all $t$ characters, summing only `dp[i][j]` with $i>0$ and $j>0$ enforces that both words were used. All additions are reduced modulo $10^9+7$.

## Complexity detail

Let $n = \lvert\texttt{word1}\rvert$, $m = \lvert\texttt{word2}\rvert$, and $t = \lvert\texttt{target}\rvert$. Each target layer scans $n(m+1) + m(n+1)$ state positions, so the time complexity is $O(tnm)$. The current and next tables each contain $(n+1)(m+1)$ entries, giving $O(nm)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every later matching index:** Extending every state by a loop over the remaining suffixes is correct but costs $O(tnm(n+m))$ time in the all-matching case.
- **Memoized four-dimensional search:** Tracking target position, both next indices, and a two-bit used-source mask follows the statement directly, but naively enumerating choices has the same extra transition factor and heavier recursion overhead.
- **Omit the zero row and column:** This loses prefixes that have used only one source so far; those states are necessary before the first switch to the other word.
- **Count single-source constructions:** Returning all states would violate the both-words requirement. The final sum deliberately excludes row zero and column zero.
- **One-character target:** No construction can use both words for a single target position, so the answer is zero.
- **Repeated equal characters:** Different indices remain distinct choices even when their characters are identical; the state coordinates preserve that distinction.
- **Independent source orders:** Switching from `word2` back to `word1` is legal whenever the new `word1` index exceeds the last index previously used in `word1`.
- **Modulo arithmetic:** Reduce every running sum and merged transition, not just the final answer, because the number of constructions grows rapidly.
