## General
**A trie shares dictionary prefixes and avoids substring construction**

Let $S$ be the total number of characters across `wordDict`. Insert every word into a trie and mark its terminal node. Record the maximum dictionary-word length $L$ while building the trie. Because the input alphabet contains only lowercase English letters, `None` is a collision-free terminal marker in the candidate's child maps.

**Reachable boundaries launch bounded trie walks**

Let `reachable[i]` mean that `s[:i]` can be segmented completely. Set `reachable[0] = True`. For each reachable boundary `start`, follow trie edges through `s` beginning there, stopping at the first absent edge or after $L$ characters. Whenever the traversal reaches a terminal node at position `end`, mark `reachable[end + 1]`.

A marked boundary is valid because it extends an already segmented prefix by one dictionary word. Conversely, take any valid segmentation and consider its words from left to right: boundary zero launches the trie walk for the first word, its terminal marks the next boundary, and induction marks every later word boundary through the end of the string. Thus the answer is exactly `reachable[-1]`. Reuse works naturally because a trie path remains available from every reachable boundary.

## Complexity detail
Let $n = \lvert\texttt{s}\rvert$, let $S$ be the total number of dictionary characters, and let $L$ be the maximum dictionary-word length. Trie construction takes $O(S)$ time and space. Each of the $n$ boundaries launches at most one walk of length $L$, giving $O(S + nL)$ time and $O(S + n)$ space including the trie and reachability array. The verified source constraint $L \le 20$ makes the legal-domain time bound $O(S + n)$ stated in the variant manifest.

## Alternatives and edge cases
- **Try every earlier boundary with slicing:** is conventional, but Python substring creation and hashing add candidate-length work and can make the apparent quadratic loop cubic.
- **Bound slicing by the longest word:** avoids irrelevant long substrings but still spends up to $O(nL^2)$ time materializing and hashing candidates.
- **Memoized depth-first search over trie paths:** has comparable state and traversal bounds but uses recursion.
- **Greedily take the longest matching word:** can block a later valid segmentation and is not correct.
- A dictionary word may be reused because no transition consumes or removes it.
- Partial reachable prefixes do not imply success; only boundary $n$ represents a complete segmentation.
