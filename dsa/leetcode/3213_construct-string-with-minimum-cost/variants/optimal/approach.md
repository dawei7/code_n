## General

**Dynamic programming over constructed prefixes**

Let `dp[end]` be the minimum cost to construct `target[:end]`, with `dp[0] = 0`. A word of length $\ell$ can finish at `end` only if it equals `target[end - ell:end]` and the preceding prefix is reachable. That transition proposes

$$
\texttt{dp[end - \ell]}+\textit{wordCost}.
$$

The minimum over all matching word lengths gives `dp[end]`.

**Deduplicate words and group by length**

If the same word appears more than once, only its smallest cost can improve any construction. Build one hash-to-cost map for each distinct length. Word lengths larger than $N$ can never participate.

Compute polynomial prefix hashes and powers for `target` using unsigned 64-bit wraparound. Then the hash of any target substring is available in constant time. For each `end`, inspect the $D$ length buckets that fit, derive the corresponding substring hash, and look up its cheapest dictionary cost.

The exact remotely Accepted source uses 64-bit rolling fingerprints, the standard competitive-programming tradeoff whose collision probability is negligible but nonzero. All package cases additionally compare semantic outputs, and duplicate dictionary entries retain their minimum cost.

**Why the recurrence finds the optimum**

Every exact construction has a final appended word. Removing it leaves an exact construction of the prefix ending where that word begins, so its cost is at least the recorded prefix optimum plus the final word's cost. The transition considers that split.

Conversely, every finite transition appends a dictionary word matching the next target segment to a reachable exact prefix. It therefore forms a valid longer construction. Induction over `end` proves that every finite DP value is the minimum construction cost for its prefix. An infinite final state means no sequence reaches all $N$ characters.

## Complexity detail

Hashing `target` and all dictionary characters costs $O(N+S)$. The DP checks at most $D$ length buckets at each target endpoint, for total time $O(ND+S)$.

The prefix hashes, powers, DP array, and dictionary fingerprints use $O(N+S)$ space. Because distinct positive lengths summing to at most $S$ satisfy $D=O(\sqrt S)$, the worst-case time can also be written $O(N\sqrt S+S)$.

## Alternatives and edge cases

- **Trie scan from every start:** Matching characters down a trie is exact and simple, but can take $O(NL)$ time when long prefixes repeat, where $L$ is the maximum word length.
- **Aho-Corasick occurrence enumeration:** It finds all matches in linear automaton time plus occurrences, but a highly repetitive input can contain many word occurrences that still need DP transitions.
- **Try every word at every prefix:** Direct `startswith` checks can multiply target length, word count, and comparison length.
- **Duplicate word with different costs:** Retain only the smallest cost because every occurrence has identical text.
- **Reusable words:** A dictionary entry may participate multiple times; no usage count is consumed.
- **Impossible prefix:** An unreachable DP state must not seed later transitions.
- **Competing segmentations:** A longer word is not automatically cheaper than several shorter words; DP compares total costs.
- **Exact target boundary:** A word extending beyond the remaining suffix cannot be selected.
- **Large total cost:** The infinity sentinel must exceed every legal construction cost.
