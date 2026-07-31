## General

For each start position in `target`, first determine the greatest length of a valid string beginning there. Process one word at a time by forming `word + "{" + target`, where `{` cannot occur in the lowercase input. Its Z-function reports, at every target position, the longest common prefix between that target suffix and the word. Taking the maximum over all words yields `longest[i]`, the greatest valid step from position $i$.

Every length from 1 through `longest[i]` is also valid because validity is prefix-closed. The remaining task is therefore the minimum-jump problem on positions from 0 through $T$: from $i$, any next position up to `i + longest[i]` is reachable in one piece.

Scan positions in layers. `current_end` is the farthest position reachable with the current number of pieces, while `farthest` is the greatest endpoint obtainable by taking one more piece from any position in that layer. When the scan reaches `current_end`, commit one piece and advance the layer boundary to `farthest`. No alternative using the same number of pieces can pass that maximum, so choosing the farthest boundary never loses an optimal construction. If a layer cannot advance, the target is impossible.

## Complexity detail

Let $W$ be the number of words, $S$ their total length, $T$ the target length, and $L$ the maximum word length. A Z-function for one word and the target costs $O(lvert word\rvert + T)$, totaling $O(S + WT)$ time over all words. The greedy scan is $O(T)$. Only one combined string and Z-array are retained at a time alongside the `longest` array, giving $O(T + L)$ auxiliary space. The official constraint fixes $W \le 100$.

## Alternatives and edge cases

- **Rolling hash with binary search:** Prefix-hash sets can find each longest match in $O(\log L)$ queries, but deterministic correctness requires collision resolution or multiple hashes.
- **Quadratic trie dynamic programming:** Walking a trie from every reachable target position works for problem 3291 but can take $O(T^2)$ time here.
- **Proper prefixes:** Z-values are useful even when shorter than their word because every nonempty word prefix is valid.
- **Overlapping reach intervals:** Greedy layer expansion considers all starts reachable with the same piece count before committing the next boundary.
- **Gap in coverage:** If `farthest` equals the current position when a new layer is required, no valid piece crosses that point and the answer is `-1`.
