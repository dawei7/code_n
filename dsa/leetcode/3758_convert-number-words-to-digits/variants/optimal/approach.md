## General

Keep an index at the next unprocessed character and a fixed mapping from the ten English number words to their digit characters. At each index, test whether one of those words starts there. A match is unambiguous because none of the ten words is a prefix of another: append its mapped digit and advance by the full word length.

If every candidate fails, advance the index by exactly one. This detail permits a valid word to begin inside or immediately after a malformed fragment; skipping an assumed fragment length could jump over such a start. Every emitted digit therefore corresponds to the earliest valid word reachable under the prescribed left-to-right rules, and the index always points to the next position the source parser would inspect.

## Complexity detail

Let $n$ be the length of `s`. There are only ten candidate words, and their maximum length is five, so the work performed at any visited position is bounded by a constant. The scan takes $O(n)$ time. The output buffer can contain $O(n)$ digit characters, giving $O(n)$ space including the returned result; auxiliary state apart from the result is $O(1)$.

## Alternatives and edge cases

- **Trie scan:** A trie also recognizes a word in at most five character transitions and has the same $O(n)$ bound, but the fixed ten-word vocabulary makes a table of candidates simpler.
- **Regular-expression search:** A fixed alternation can reproduce the nonoverlapping matches, although it obscures the required one-character fallback rule.
- **Try every substring ending:** Searching all possible end positions after every start is correct, but it performs $O(n^2)$ candidate checks and needless long-fragment work even though valid words have length at most five.
- **Consume by repeated slicing:** Replacing `s` with `s[1:]` after each miss is correct but repeatedly copies suffixes and can take $O(n^2)$ time.
- **Incomplete word at the end:** A prefix such as `"tw"` is never emitted because only complete words count.
- **Malformed near-match:** After a failure, move one character only; a valid word may start before the malformed fragment ends.
- **Adjacent valid words:** After a match, jump exactly its length so the following word is recognized immediately.
- **No matches:** The output buffer remains empty and joins to `""`.
