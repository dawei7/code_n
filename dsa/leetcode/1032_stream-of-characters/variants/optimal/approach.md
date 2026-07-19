## General
**Reverse every dictionary word:** Insert characters from each word's end toward its beginning into a trie. A terminal marker records when the path read so far is a complete word. This converts suffix testing on the stream into prefix traversal in the reversed trie.

**Retain only relevant stream history:** No dictionary word is longer than $W$, so letters older than the newest $W$ characters cannot participate in a matching suffix. Store the recent stream in a deque whose maximum length is $W$.

**Walk backward after each query:** Append the new letter, begin at the trie root, and inspect retained characters from newest to oldest. A missing trie edge proves that no longer suffix can match. Reaching a terminal marker proves that the characters examined form a configured word and allows an immediate `true` result.

Every reported match follows a reversed trie path ending at a terminal, so it is exactly a dictionary word and a suffix of the current stream. Conversely, any matching suffix has length at most $W$ and remains in the deque; reversing its characters follows its inserted trie path to a terminal, so it cannot be missed.

## Complexity detail
Building the reversed trie visits all $S$ dictionary characters. Each of the $Q$ queries examines at most $W$ retained characters, giving $O(S+QW)$ total time. The trie contains at most $S+1$ nodes, and the deque holds at most $W$ characters, for $O(S+W)$ space.

## Alternatives and edge cases
- **Check every word after every query:** Test whether the current stream ends with each dictionary word. This can take $O(QS)$ time and repeats shared suffix work.
- **Aho-Corasick automaton:** Failure links process each new character in amortized $O(1)$ time after preprocessing, but the construction is more involved.
- **Single-character word:** Its matching query can return `true` immediately without older stream characters.
- **Overlapping words:** A shorter terminal may occur before a longer terminal on the same reversed path; either is sufficient.
- **Stream shorter than a word:** Traversal simply ends without a terminal and returns `false`.
- **Bounded history:** Discarding characters beyond $W$ is safe because no possible answer can use them.
