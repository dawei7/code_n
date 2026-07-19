## General
**Share word prefixes in a trie:** Insert every word character by character. Mark the node reached at the end of each word as terminal. Common prefixes occupy the same path, so they are processed together rather than compared independently against the text.

**Walk from every possible start:** For each start index in increasing order, follow trie edges while moving the text end index rightward. Stop immediately if the next character has no trie edge, because no longer word can match that start. Whenever the reached node is terminal, append `[start, end]`.

**Produce sorted output directly:** Starts are visited from smallest to largest, and for a fixed start the end index only increases. The appended pairs are therefore already ordered by start and then end, so no separate sorting pass is needed.

Every reported terminal path spells a complete supplied word and exactly matches the corresponding contiguous text range. Conversely, any supplied word occurring at a start follows its trie path without encountering a missing edge and reaches a terminal node at its final character, so its pair is reported.

## Complexity detail
Building the trie takes $O(S)$ time and space. From each of the $N$ starts, traversal examines at most $L$ characters, giving $O(NL)$ search time. The total time is $O(S+NL)$ and the trie uses $O(S)$ auxiliary space, excluding the required output.

## Alternatives and edge cases
- **Check every word at every start:** Direct matching is simple but can take $O(NWL)$ time because common prefixes are compared repeatedly.
- **Search each word independently:** Repeated substring searches still need a final sort and may revisit the text for every word.
- **Aho-Corasick automaton:** It can scan the text in $O(S+N+R)$ time for $R$ matches, but failure links add complexity unnecessary for these bounds.
- **Overlapping matches:** Advancing to the next start rather than past a match ensures none are skipped.
- **Nested words:** Terminal markers at multiple depths report both a short word and a longer word beginning at the same index.
- **No match:** No terminal node is reached, so return an empty list.
- **Word longer than remaining text:** Traversal simply reaches the end of `text` before reaching that terminal.
