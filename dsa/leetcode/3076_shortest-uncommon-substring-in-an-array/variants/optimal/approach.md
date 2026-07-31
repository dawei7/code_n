## General

Let $n$ be the number of strings and $L$ the maximum string length.

**Count owning words, not occurrences.** A substring is eligible for `arr[i]` precisely when no other array element contains it. Multiple appearances inside `arr[i]` do not make it common. For each word, generate its substrings into a temporary set, then increment a global owner count once for every distinct substring in that set. After all words are processed, a substring enumerated from the current word is uncommon exactly when its owner count is one.

**Compare candidates by the requested priority.** Enumerate every substring of a word again. Ignore candidates whose owner count is not one. Among the remaining candidates, prefer a shorter string; when lengths match, prefer the lexicographically smaller string. This is equivalent to minimizing the pair `(length, substring)`, so the retained candidate is exactly the required answer. If no candidate survives, the initial empty string remains in the result.

**Why the ownership test is sufficient.** Every generated candidate occurs in the word currently being answered. An owner count of one therefore means that current word is its sole owner, so the candidate appears in no other array element. Conversely, any valid answer belongs only to its current word and must receive owner count one. The enumeration considers every such substring, and the length-then-lexicographic comparison selects the unique result required by the contract.

## Complexity detail

Each word has $O(L^2)$ substring positions. In Python, constructing and hashing a sliced substring can take $O(L)$ time, so building the owner counts and scanning candidates each take $O(nL^3)$ time. The total time is $O(nL^3)$.

The global map can retain $O(nL^2)$ distinct strings containing $O(nL^3)$ characters in total, which gives $O(nL^3)$ auxiliary space under the same explicit-string representation. The temporary per-word set does not exceed that bound.

## Alternatives and edge cases

- **Direct cross-word search:** For every candidate substring, testing membership in every other word avoids the ownership map but adds another factor of $n$, giving up to $O(n^2L^3)$ time with ordinary string search costs.
- **Trie or suffix structures:** Generalized suffix structures can share character storage and support richer substring queries, but the limits $n \le 100$ and $L \le 20$ make their implementation complexity unnecessary here.
- **Repeated occurrences in one word:** Deduplicate each word's substrings before updating owner counts; occurrence frequency is not the same as the number of owning strings.
- **Duplicate input strings:** Every substring of either duplicate appears in another array element, so both corresponding answers must be empty.
- **Tie-breaking order:** Minimize length before lexicographic value; a lexicographically smaller but longer substring must not replace a shorter candidate.
- **No eligible substring:** Preserve `""` when every substring is owned by at least two input strings.
- **Whole-word answer:** A word itself can be the shortest uncommon substring when all of its proper substrings occur elsewhere.
