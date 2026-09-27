# Guided Example: Words Within Two Edits of Dictionary

## 1. The Instance We Will Trace

We trace the reference instance in full:

- **Input:** `queries = ["word", "note", "ants", "wood"]`, `dictionary = ["wood", "joke", "moat"]`
- **Required output:** `["word", "note", "wood"]`

All six words have the same length. One *edit* replaces a single letter of a query word with any other letter, and a query qualifies when at most two such replacements turn it into some dictionary word. The output lists the qualifying queries in their original order. This instance is chosen because it contains a query that qualifies through one edit, a query that qualifies through exactly two edits, a query that needs three edits and must be rejected, and a query that already equals a dictionary word with zero edits — the full span of admissible edit counts inside one input.

## 2. Why the Answer Is a Hamming-Distance Test

Because every query and every dictionary word has the same length $n$, and because the only permitted operation is replacing one letter by another, the cheapest way to turn a query $s$ into a dictionary word $t$ is to repair the positions where they already disagree and leave the rest alone. Positions where the two letters agree cost nothing, and each disagreeing position costs exactly one edit. Therefore

$$
\text{edits}(s, t) \;=\; H(s, t) \;=\; \bigl\lvert \{\, j : s[j] \neq t[j] \,\} \bigr\rvert ,
$$

the Hamming distance between the two equal-length words. Insertions, deletions, and reorderings are not available operations, so no cheaper alignment can ever beat this count, and no more expensive alignment is ever needed.

A query qualifies exactly when some dictionary word satisfies $H(s,t) \le 2$, i.e. when the number of disagreeing positions is *strictly less than three*. Two edits are admissible; three are not. That single inequality is the entire acceptance rule, and it also means each comparison is decided by a small integer we can tabulate.

## 3. The Full Comparison Trace

For each query we compare against every dictionary word and record the number of disagreeing positions. The query is accepted as soon as one comparison yields a value below three, and the witness word that produced it is recorded for explanation.

| query $s$ | $H(s,\texttt{"wood"})$ | $H(s,\texttt{"joke"})$ | $H(s,\texttt{"moat"})$ | smallest | verdict | witness |
|---|---|---|---|---|---|---|
| `"word"` | $1$ | $3$ | $3$ | $1$ | accepted | `"wood"` |
| `"note"` | $3$ | $2$ | $3$ | $2$ | accepted | `"joke"` |
| `"ants"` | $4$ | $4$ | $4$ | $4$ | rejected | — |
| `"wood"` | $0$ | $3$ | $3$ | $0$ | accepted | `"wood"` |

Reading the accepted rows in the original query order gives `["word", "note", "wood"]`, which agrees with the authored expected output for this input. The rejected row shows the boundary being enforced rather than approximated: `"ants"` is four mismatches away from every dictionary word, and no amount of searching can change that.

Two further facts are visible in the table and matter for the design. First, one witness inside the dictionary is enough on its own; the query is emitted once, no matter how many dictionary words happen to be within budget. Second, a mismatch count of $0$ is perfectly legal, because "a maximum of two edits" includes doing nothing at all.

## 4. A Position-by-Position Look at the Decisive Comparisons

The counts in the previous table are produced by walking the two words in lockstep. Two comparisons carry the lesson.

The pair `"note"` versus `"joke"` qualifies, and the two repaired positions are exactly the two that disagree:

| position $j$ | `"note"`$[j]$ | `"joke"`$[j]$ | equal? | edits counted so far |
|---|---|---|---|---|
| 0 | `n` | `j` | no | $1$ |
| 1 | `o` | `o` | yes | $1$ |
| 2 | `t` | `k` | no | $2$ |
| 3 | `e` | `e` | yes | $2$ |

The pair `"ants"` versus `"moat"` fails, and the failure is not marginal:

| position $j$ | `"ants"`$[j]$ | `"moat"`$[j]$ | equal? | mismatches so far |
|---|---|---|---|---|
| 0 | `a` | `m` | no | $1$ |
| 1 | `n` | `o` | no | $2$ |
| 2 | `t` | `a` | no | $3$ (budget already exceeded) |
| 3 | `s` | `t` | no | $4$ |

This is the mechanism behind early rejection: once the running mismatch count reaches three, the pair is hopeless, and the remaining positions cannot reduce the count, because a disagreement can never become an agreement by reading further characters. Only additions are possible.

## 5. The Invariant and Why the Method Is Correct

**Counting invariant.** While a query $s$ is compared with a dictionary word $t$, after $j$ positions have been read the running counter equals the number of indices in $\{0, \dots, j-1\}$ at which $s$ and $t$ differ. Each position contributes exactly one to the counter if and only if the two letters differ, and the positions are visited once each in increasing order, so when all $n$ positions have been read the counter equals $H(s,t)$ exactly.

**Acceptance rule.** The invariant lets us decide membership from the counter alone. If the final counter is below three, the disagreeing positions themselves form a repair set of size at most two, so replacing those letters turns $s$ into $t$ within the allowed budget and $s$ genuinely qualifies. Conversely, if $s$ qualifies then some admissible set of at most two replacements must repair every disagreement, because replacements cannot create or remove disagreements at positions left untouched; hence the counter would have been at most two. The test is therefore both necessary and sufficient, with no gap in either direction.

**Completeness over the dictionary.** A query is accepted only after the whole dictionary has been examined, or after one witness has been found. If the witness is found first, the decision is final and the remaining comparisons cannot revoke it, so stopping is safe. If no witness is found before the dictionary is exhausted, then no dictionary word passed the test, and the invariant guarantees that no word within budget was overlooked. Rejection is therefore justified by exhaustive evidence, not by a heuristic pruning rule.

**Output identity.** Each query is appended at most once, at the moment the first witness appears. Consequently the answer is a subsequence of `queries` in the original order, duplicates included: two occurrences of the same query word yield two occurrences in the answer, because they are two distinct positions of the input array, not one repeated value.

## 6. Boundaries and Traps This Instance Exposes

| situation | concrete instance | outcome and the trap it exposes |
|---|---|---|
| Exactly two edits needed | `queries = ["abcdefghij"]`, `dictionary = ["abcdefghxy"]` | The two trailing disagreements are admissible, so `"abcdefghij"` qualifies. The bound is inclusive; demanding strictly fewer than two edits would wrongly reject it. |
| Zero edits | `"wood"` against `"wood"` | Identity is a valid match with $H = 0$. A rule that demands at least one edit would break this row. |
| Three or more edits required | `"ants"` against every dictionary word | Rejected. The decisive event is the mismatch count reaching $3$, not any particular larger value. |
| Very short words, $n \le 2$ | `queries = ["a", "z", "m"]`, `dictionary = ["q"]` | Every same-length pair differs in at most $n \le 2$ positions, so *every* query qualifies whenever the dictionary is non-empty. With $n \le 2$ the answer is the whole query array, a fact worth stating rather than discovering by accident. |
| Witness appears late | `queries = ["aaaa"]`, `dictionary = ["zzzz", "yyyy", "aaaz"]` | `"aaaa"` is $4$, then $4$, then $1$ away. The qualifying comparison is last, so the scan cannot be limited to the beginning of the dictionary. |
| Duplicate witnesses | e.g. `"code"` against `["cope", "coda"]` | Two dictionary words are each one edit away. The query is emitted once, not twice; the first witness found is enough. |
| Duplicate queries | `queries = ["code", "xxxx", "code"]` | Both occurrences of `"code"` are emitted, preserving order and multiplicity. Treating the output as a set loses an element. |
| Repeated dictionary entries | any duplicated dictionary word | Repetition only wastes comparisons; it never changes the verdict, and once a witness fires the remaining copies are skipped. |
| Single-character words, $n = 1$ | `queries = ["yes"]` versus `dictionary = ["not"]` | With $n = 3$ here, all three positions disagree and the query is rejected; contrast with $n = 1$, where one disagreement is the maximum possible and the whole dictionary is interchangeable as a witness. |
| Order guarantee | any input | The answer must follow `queries` order; a set- or map-ordered construction that also de-duplicates violates both the order and the multiplicity requirement. |

## 7. Alternative Methods and Their Trade-offs

| method | time | auxiliary space | trade-off |
|---|---|---|---|
| Pairwise lockstep mismatch counting with early stop (derived above) | $O(q\,d\,n)$ worst case | $O(1)$ working storage | No preprocessing, exact answer, and typically far below worst case because a witness often appears early; every query re-scans the dictionary. |
| Precompute a wildcard index of the dictionary | $O(d\,n^2 \cdot 26^2)$ build, then membership probes per query | $O(d\,n^2 \cdot 26^2)$ | Each dictionary word generates every word reachable from it within two letter changes, after which each query is answered by a lookup. Excellent when the query count dwarfs the dictionary size, ruinous when $n$ is large. |
| Trie over dictionary words with a walking mismatch budget | $O(q\,n^2)$ states explored per query in the worst case | $O(d\,n)$ for the trie | Shares prefixes across dictionary words and prunes whole subtrees once the budget is exhausted; the pruning is an optimization of the same counting invariant, not a different acceptance criterion. |
| Group dictionary words by a prefix hash of the first few letters | not sound in general | $O(d)$ | Two words within two edits can still differ at the first two letters, so no prefix partition is guaranteed to keep witnesses and queries in the same bucket. |
| General edit-distance computation | $O(q\,d\,n^2)$ | $O(n)$ | Allows insertions and deletions, which this problem forbids. It measures a different relation and would accept queries that are not valid here. |
| Sorting the dictionary and binary searching | $O(d\,n \log d)$ build, $O(\log d)$ probes | $O(d\,n)$ | Ordering gives no help: the set of words within two mismatches of a query is not an interval in lexicographic order. |

## 8. Complexity Derivation

Let $q$ be `queries.length`, $d$ be `dictionary.length`, and $n$ the common word length.

- **One comparison.** Walking two words in lockstep reads all $n$ positions and performs one comparison and one conditional increment per position, so a single pair costs $O(n)$ time and stores only a counter.
- **One query.** In the worst case the query is compared with all $d$ dictionary words at $O(n)$ each, giving $O(d\,n)$. The early stop can only lower this: a query whose witness is the first dictionary entry costs $O(n)$, while a rejected query always pays the full $O(d\,n)$.
- **All queries.** Summing over the $q$ queries gives a worst case of $\Theta(q\,d\,n)$, attained when every query is far from every dictionary word so that no query can stop early. No sorting or hashing is involved, so the bound contains no logarithmic factor.

For space, the working state of one comparison is a single mismatch counter and a position cursor, so the method needs $O(1)$ auxiliary storage independent of $q$, $d$, and $n$. The returned list holds at most $q$ references to query words that already exist in the input, so the output contributes $O(q)$ and nothing is allocated per comparison. The wildcard-index alternative trades exactly this constant auxiliary space for a large precomputed table, which is the clearest way to see that the pairwise scan is the space-minimal choice for the given limits.