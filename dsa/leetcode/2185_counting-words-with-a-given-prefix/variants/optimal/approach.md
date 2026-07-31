## General

**Test only the position a prefix can occupy**

For each word, compare `pref` with the word's leading characters. A prefix is
required to begin at index zero, so there is no reason to search any later
position. If the word is shorter, or any compared character differs, that
word contributes nothing; otherwise increment the count.

This decision is exactly the definition of a prefix. Every matching word is
visited once and contributes one, while every rejected word either lacks
enough characters or differs within the required leading segment. Summing
those independent Boolean decisions therefore gives the requested number,
including separate contributions from duplicate entries.

## Complexity detail

For a word $w$, at most
$\min(\lvert w\rvert,\lvert\texttt{pref}\rvert)$ characters are inspected.
With $C$ defined in the contract as the sum of those bounds, total time is
$O(C)$. The scan keeps only the running count and comparison state, so it uses
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Build every possible prefix:** Generate all leading substrings for each
  word and test membership. This is correct but can take quadratic time in
  each word's length and materialize unnecessary strings.
- **Trie:** Insert every word into a prefix tree and store subtree counts. This
  is useful for many prefix queries, but for one query it uses $O(S)$
  additional space for total input length $S$ without improving this scan.
- A word equal to `pref` is a match because a whole string is its own prefix.
- A word shorter than `pref` cannot match.
- Finding `pref` only after index zero does not qualify.
- Duplicate matching words are counted separately.
- Comparisons are case-sensitive, although the contract supplies only
  lowercase English letters.
