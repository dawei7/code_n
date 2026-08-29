## General

A merge uses an ordered pair of different phrase indices. The last word of the first phrase must equal the first word of the second phrase. When they match, the shared boundary word appears only once in the combined result. Both pair orders matter because changing which phrase comes first usually changes both compatibility and the merged text.

**Precompute only the words needed for matching**

The solution first processes every phrase with `p.split()`. The input guarantees lowercase words separated by single spaces, with no leading or trailing space, so splitting produces the words cleanly. It saves the pair `(ws[0], ws[-1])` in `ps`: the first word and last word of that phrase.

This preprocessing keeps the nested loop focused. It does not repeatedly split the same phrases for each possible partner. The complete original strings remain in `phrases` for constructing results, while `ps` contains the boundary words used for compatibility checks.

**Why the pair loops are ordered**

The outer index `i` represents the first phrase in a candidate merge, and `j` represents the second. Both loops range over every index from zero through `n - 1`. The condition first requires `i != j` because a phrase position may not be paired with itself. Two different indices are permitted even when their phrase strings are identical.

The second condition is

`ps[i][1] == ps[j][0]`.

The element at position one in `ps[i]` is phrase `i`’s last word. The element at position zero in `ps[j]` is phrase `j`’s first word. Their equality is exactly the definition of a valid Before and After boundary.

Because the loops examine both `(i, j)` and `(j, i)` when the indices differ, the code honors the requirement that pair order matters. It does not assume that compatibility in one direction implies compatibility in the other.

**Joining without repeating the shared word**

For a compatible pair, the code appends

`phrases[i] + phrases[j][len(ps[j][0]) :]`.

The first phrase is included in full, so its final copy of the shared word is already present. The slice of the second phrase begins immediately after its first word. If the second phrase contains more words, the character at that slice position is the separating space, so the suffix begins with a space and joins naturally.

For example, joining `"writing code"` with `"code rocks"` uses a first-word length of four. Slicing `"code rocks"` from index four yields `" rocks"`. Appending that suffix produces `"writing code rocks"`, with one copy of `"code"` and exactly one space between words.

If the second phrase consists of only the shared word, the slice begins at the string’s length and is empty. The result is simply the first phrase, which is correct because merging the shared one-word second phrase adds no new text. If both phrases are one-word occurrences at different indices, a result such as `"a"` can be generated.

**Why results are collected before deduplication**

Different ordered index pairs can generate the same final string. The input itself may contain duplicate phrase strings, and even different texts can sometimes lead to the same merge. The code initially stores every generated candidate in `ans`. At the end, `set(ans)` removes duplicate strings by value, and `sorted(...)` returns the unique values in lexicographic order.

This sequence exactly matches the output rules. Deduplication does not erase the distinction between indices while deciding whether a pair is legal: `i != j` is checked first during generation. It only removes repeated final texts after all legal pairs have had a chance to contribute.

**Why every returned string and only every valid string appears**

Whenever the algorithm appends a candidate, its indices differ and the first phrase’s last word equals the second phrase’s first word. The slicing operation removes only the duplicate first word from the second phrase, so the appended text is a correctly formed puzzle for that ordered pair.

Conversely, any legal puzzle comes from some ordered pair of distinct indices. The nested loops eventually visit that exact `i` and `j`. Their boundary words match, so the condition succeeds and the same merged text is appended. Converting to a set may combine it with an equal result from another pair, but the contract asks for distinct strings, so retaining one copy is sufficient. Sorting then establishes the required final order.

The preprocessing and construction preserve full phrase contents. Only the second phrase’s boundary word is omitted, as required; no later words are lost because the slice takes the remainder of the original string rather than rebuilding it from a partial word list.

## Complexity detail

Let $N$ be the number of phrases and let

$$
S=\sum_{p\in\texttt{phrases}}\lvert p\rvert
$$

be the total input character count. Let $G$ be the total number of characters across all generated candidates before duplicates are removed, and let $R$ be the number of distinct result strings.

Splitting all phrases takes $O(S)$ time. The nested loops always perform $N^2$ index-pair iterations, including instances where no pair matches. Boundary-word equality can inspect characters, so a fully length-sensitive bound also includes the total character work of those $N^2$ comparisons. Under the problem’s fixed maximum phrase length of 100, each comparison is bounded by a constant, and the pair-checking phase is $O(N^2)$.

Building all successful merged strings costs $O(G)$ character-copying time. Hashing candidates to build `set(ans)` is expected $O(G)$ character work. Sorting $R$ strings requires $O(R\log R)$ comparisons; lexicographic comparisons may inspect string characters. Because each result has bounded length under the stated constraints, this is conventionally $O(R\log R)$. A practical constraint-aware total is therefore $O(S+N^2+G+R\log R)$.

The exact code’s unconditional $N^2$ pair scan should not be omitted: if no boundary words match, then $G=0$, but the loops still examine every ordered pair.

The boundary tuple list uses $O(S)$ space in the worst case. The candidate list stores $O(G)$ characters before deduplication, and the set plus sorted output retain the distinct strings. Since distinct results are drawn from the generated candidates, the auxiliary and output storage is bounded by $O(S+G)$, with the returned list itself holding $R$ strings.

## Alternatives and edge cases

- **Index phrases by first word:** Build a map from each first word to compatible second-phrase indices, then visit only matching groups for each first phrase. This can avoid many of the $N^2$ failed comparisons, though all successful candidate strings still have to be constructed.
- **Insert directly into a set:** Deduplicating as candidates are generated can avoid storing repeated strings in an intermediate list. The exact code instead builds `ans` first and converts it at the end.
- **One phrase only:** Every potential pair has equal indices and is rejected. The returned list is empty.
- **Duplicate phrases at different indices:** They may legally pair because the restriction is on indices, not text equality. Duplicate merged outputs are removed only afterward.
- **A one-word second phrase:** Removing its first word leaves an empty suffix, so the merged result is exactly the first phrase.
- **A one-word first phrase:** It can participate whenever that word matches the second phrase’s first word. The same slicing rule still keeps one boundary copy.
- **Compatibility in only one direction:** A last-to-first match for `i` followed by `j` says nothing about `j` followed by `i`. Ordered nested loops test both independently.
- **Several pairs produce the same puzzle:** `set(ans)` retains one copy, satisfying the distinct-output rule.
- **Lexicographic order:** A set has no guaranteed order. Calling `sorted` after deduplication is necessary to meet the output contract.
- **Space at the merge boundary:** The suffix slice starts after the second phrase’s first word but preserves the following space. Manually adding another space would create two spaces, while slicing past that space would join words together.
