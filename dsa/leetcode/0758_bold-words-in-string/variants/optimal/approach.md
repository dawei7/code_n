## General
**Share dictionary prefixes in a trie**

Insert every word into a trie and mark terminal nodes. Let `L` be the longest word length. From each source index, follow trie edges through at most `L` characters. Whenever a terminal node is reached, record that ending position as the farthest match currently known for the start. A missing edge ends that start's scan immediately.

**Accumulate the union with a difference array**

For a start with at least one match ending at `end`, add one at `difference[start]` and subtract one at `difference[end]`, where `end` is exclusive. A prefix sum over this array is positive exactly on characters covered by at least one match. Overlaps and adjacency need no separate interval-merging pass.

**Emit tags only at coverage transitions**

Before character `i`, open $<b>$ when coverage changes from zero to positive. Close $</b>$ when it changes from positive to zero. After the final character, close any still-open range. Because tags are emitted only at maximal-run boundaries, overlapping and adjacent matches receive one shared pair.

Each trie traversal represents a source substring with the same prefix, and terminal visits identify exactly the dictionary matches beginning there. The difference array therefore marks precisely their union. Coverage transitions partition that union into maximal consecutive ranges, so the reconstructed string has exactly the required tags.

## Complexity detail
Let `p` be the total number of dictionary characters, `n = len(s)`, and `L` the longest dictionary word. Trie construction costs $O(p)$, and at most `L` edges are followed from each source position, giving $O(p + nL)$ time. The trie and the $n + 1$ difference array use $O(p + n)$ space.

## Alternatives and edge cases
- **Try every word at every index:** Repeated `startswith` checks are simple but can cost $O(nwL)$ for `w` words.
- **Aho-Corasick automaton:** It finds all matches in $O(p + n + matches)$ time, but its failure-link machinery is heavier than needed for the bounded inputs.
- **Collect and sort match intervals:** Merging them is correct, though the difference array avoids storing every occurrence.
- **Overlapping matches:** Their coverage counts add, so no tag boundary appears inside the overlap.
- **Adjacent matches:** Coverage stays positive across their boundary, producing one bold segment.
- **No matches:** No coverage transition occurs and the original string is returned unchanged.
- **Match reaches the final character:** Close the open bold tag after the scan.
