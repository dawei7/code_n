## General

**Track the current cyclic run**

Scan `p` from left to right. At position `i`, compare the current character with `p[i - 1]`. Their character-code difference modulo 26 equals one exactly when the current character is the cyclic successor of the previous one, including the `z`-to-`a` transition. Extend `run` in that case; otherwise reset it to one because the current character alone is still valid.

**Summarize valid substrings by their final letter**

For each lowercase letter, `longest` stores the greatest valid run length seen with that ending letter. If a valid run of length $L$ ends in a letter, its suffixes contribute one qualifying substring of every length from $1$ through $L$ with that same final letter.

An ending letter and length uniquely determine the substring in `base`, because every preceding character is forced by cyclic alphabet order. Consequently, a shorter run ending at the same letter adds no text that the longest run did not already include. Updating only the maximum removes duplicates, and summing the 26 maxima counts every distinct qualifying substring exactly once.

## Complexity detail

Let $n = \lvert\texttt{p}\rvert$. The candidate performs constant work for each character, so it runs in $O(n)$ time. `longest` always has 26 entries and every other value is scalar, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Materialize valid substrings in a set:** is direct, but enumerates quadratically many occurrences and repeatedly constructs substring objects on a long cyclic run.
- **Dictionary keyed by ending letter:** implements the same recurrence with at most 26 keys, but an array expresses the fixed alphabet more directly.
- **Suffix trie:** deduplicates substring texts but stores far more structure than cyclic determinism requires.
- **Single character:** starts a run of one and contributes exactly that character.
- **Repeated occurrence:** changes the answer only when it creates a longer run for its ending letter.
- **`z` followed by `a`:** extends the run because adjacency is computed modulo 26.
- **Broken adjacency:** resets the run to one rather than zero because the current character remains a valid substring.
