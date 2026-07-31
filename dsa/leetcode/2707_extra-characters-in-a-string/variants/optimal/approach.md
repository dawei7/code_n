## General

Define `minimum_extra[end]` as the smallest number of uncovered characters in the prefix `s[:end]`. The empty prefix has value zero. For every later endpoint, one always-valid choice is to leave `s[end - 1]` uncovered, giving `minimum_extra[end - 1] + 1`.

**Find matching suffixes without rebuilding substrings**

Insert each dictionary word into a trie in reverse character order and mark its terminal node. To process a prefix ending at `end`, walk `s` backward from `end - 1` through that trie. If a trie edge is absent, no longer suffix ending there can be a word, so the scan stops. Whenever a terminal node is reached at `start`, `s[start:end]` is a dictionary word and contributes no new extras; update the state with `minimum_extra[start]`.

The recurrence considers the final decision of every optimal prefix solution. Its last character is either extra, represented by the one-character transition, or belongs to a selected dictionary word ending at `end`, represented by the corresponding terminal trie path. The preceding portion uses the already optimal state at its boundary. Taking the minimum over these exhaustive, non-overlapping choices proves each state and ultimately `minimum_extra[n]` optimal.

## Complexity detail

Building the reversed trie takes $O(W)$ time and space. For each of the $n$ endpoints, the backward scan examines at most $n$ characters, so dynamic programming takes $O(n^2)$ time. The total bounds are $O(n^2+W)$ time and $O(n+W)$ space for the DP array and trie. The benchmark scales $W=\Theta(n^2)$ and contrasts the trie with an explicit character-by-character scan of every dictionary word at every position.

## Alternatives and edge cases

- **Hash every substring:** Testing all `s[start:end]` values in a set is concise, but materializing and hashing slices can add another factor in languages where slicing copies characters.
- **Scan every dictionary word at every position:** This avoids a trie but can repeatedly compare long shared prefixes and take $O(nW)$ time.
- **Unmemoized recursion:** Branching between extra characters and every matching word repeats the same suffix states exponentially.
- A dictionary word may occur multiple times even though dictionary entries themselves are distinct.
- Selected word occurrences cannot overlap; DP boundaries enforce this automatically.
- If no word occurs, every character is extra and the answer is $n$.
- A complete cover yields zero even when several different segmentations exist.
- Words longer than `s` simply fail to produce a terminal path within any endpoint scan.
