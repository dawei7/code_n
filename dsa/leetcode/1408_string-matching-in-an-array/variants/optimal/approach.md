## General
For each candidate word, examine every other array entry. Skip the candidate's own index, and use substring search to test whether the candidate occurs contiguously in the other word. Append it as soon as one containing word is found, then stop checking that candidate so it is emitted once.

If a word is appended, the successful comparison supplies a distinct containing entry, so it satisfies the contract. Conversely, every qualifying word has at least one such other entry, and the complete pair scan eventually tests that pair. The early stop affects only duplicate discovery, not membership in the result.

## Complexity detail
There are $O(n^2)$ ordered word pairs. Under a straightforward substring-search model, checking strings of length at most $L$ costs $O(L^2)$, giving $O(n^2L^2)$ time. The result and loop state use $O(n)$ space; language substring routines may use implementation-specific temporary storage.

## Alternatives and edge cases
- **Aho-Corasick automaton:** Match all words against all texts together for stronger large-input behavior, but it is substantially more machinery for the small source bounds.
- **Repeat every pairwise decision:** Recomputing the entire answer once per word remains correct but adds a factor of $n$.
- **Self-match:** Skip equal indices; every string trivially contains itself.
- **Several containers:** Emit the candidate only once after its first match.
- **Equal lengths:** Since words are distinct, neither equal-length word can be a substring of the other.
- **No matches:** Return an empty list.
- **Output order:** Any order is valid, so judging must compare membership rather than one serialization.
