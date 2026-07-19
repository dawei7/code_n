## General
**DP states live between characters, not on characters**

Let `reachable[i]` mean prefix `s[:i]` can be segmented completely into dictionary words. Indices are boundaries: state zero is before the first character, and `reachable[0] = True` represents the valid empty segmentation that anchors the first word.

**Every true boundary is justified by one final dictionary word**

For each ending boundary `end`, try starts before it. If `reachable[start]` and `s[start:end]` belongs to the dictionary, that word extends a complete segmentation to `end`; mark it true and stop scanning additional starts.

Checking reachability before constructing or looking up the substring can avoid work from starts that no valid segmentation can reach. Restricting candidate lengths to dictionary word lengths or using a trie further reduces practical substring work.

**Prefix order makes every predecessor state final**

After computing boundary `end`, `reachable[end]` is true exactly when some complete dictionary segmentation ends there, and all smaller boundary states are final.

**Trace two reachable boundaries in `leetcode`**

Boundary four becomes reachable through `leet`; boundary eight then becomes reachable through `code` starting at four, proving the whole string.

**Reachable boundaries characterize segmentable prefixes**

A boundary is marked reachable only by extending an already segmentable prefix with one dictionary word, so every true state witnesses a valid segmentation.

Conversely, any segmentation of a prefix has a final word starting at an earlier boundary. Removing that word leaves a segmentable prefix, and the transition examines that boundary-word pair. Every valid segmentation therefore marks its ending boundary, including the full string exactly when it can be segmented.

## Complexity detail
There are $O(n^2)$ boundary pairs and $O(n)$ Boolean states. This is the conventional DP-transition bound with expected hash-set lookup; runtimes that materialize and hash every substring charge additional work proportional to candidate length. Limiting checks by dictionary lengths or trie traversal avoids treating substring creation as free.

## Alternatives and edge cases
- **Plain backtracking:** can revisit the same suffix exponentially many times.
- **Memoized DFS:** has equivalent state complexity and is also valid.
- **Greedily choose the longest word:** can block a later valid segmentation.
- Reusing a dictionary word is naturally allowed because transitions never remove words from the set.
- If the full boundary never becomes reachable, partial valid prefixes do not change the false result.
