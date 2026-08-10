## General

A candidate is concatenated when its entire character range can be segmented into at least two dictionary words. The exact solution processes candidates from shortest to longest and stores usable shorter words in a trie. For each candidate, a depth-first search tries every trie word that matches its current prefix, then recursively checks the remaining suffix.

Processing by length solves the “at least two shorter words” requirement without temporarily removing the candidate from a global dictionary: the current word has not been inserted yet, so it cannot match itself as one component.

**Trie structure**

Each `Trie` node owns an array of 26 child references, one for every lowercase English letter, and an `is_end` flag. Insertion walks through a word character by character, creating missing nodes. The final node is marked as a complete dictionary word.

The trie supports prefix discovery in one pass. Starting at its root and following candidate characters, every encountered `is_end` node identifies a component word ending at that position. A hash set could test all sliced prefixes separately; the trie shares common prefix traversal.

**Why words are sorted by length**

`words.sort(key=lambda x: len(x))` ensures the trie contains only words no longer than candidates already processed. A same-length word cannot be a proper component of the current nonempty candidate unless it consumes the entire candidate; distinct input words of equal length cannot equal it, and the current candidate itself is absent. Thus only genuinely shorter components can match.

If a candidate is not concatenated, it is inserted as a new base word. If it is concatenated, it is appended to the answer but not inserted.

Excluding concatenated words from the trie does not lose solutions. Any concatenated component can itself be expanded into its shorter component words. Replacing it by that expansion yields the same text, so irreducible non-concatenated words are sufficient building blocks for every later candidate.

**Meaning of `dfs(w)`**

`dfs(w)` returns true when the entire suffix string `w` can be segmented into words currently in the trie.

The empty string is the successful base case. Reaching it means earlier recursive choices consumed the candidate exactly, with no leftover characters.

For a nonempty suffix, start at the trie root and scan its characters. If the needed child is missing, no longer prefix can match because every longer prefix begins with the same failed path, so return false immediately.

Whenever a traversed node has `is_end = True`, the prefix `w[:i+1]` is a stored word. Recursively test `w[i+1:]`. If that remainder can also be segmented, the current suffix can, so return true. If not, continue the trie scan to try a longer component prefix.

Only after every possible stored prefix fails does the function return false.

**Why a successful top-level call uses at least two words**

The current candidate is not yet in the trie. Every stored word is strictly shorter or, for equal lengths, different and therefore unable to match the entire candidate. The first DFS component cannot consume all candidate characters as one dictionary word. Reaching the empty suffix consequently requires at least two nonempty components.

The empty base case does not allow zero-length components: recursion is called only after consuming `i + 1` characters, so every selected prefix has positive length.


If `dfs` returns true, every recursion level ended at an `is_end` trie node, so every consumed piece is a valid earlier dictionary word. Suffix slicing covers consecutive, nonoverlapping portions, and the empty base case proves they cover the whole candidate. The candidate is therefore a valid concatenation.

Conversely, suppose a candidate has a valid segmentation into stored base words. The initial trie walk reaches the end node of its first component and recursively considers the remaining suffix. Applying the same argument to each component eventually reaches empty text, so one search branch returns true. Trying all end-node prefixes ensures the valid first boundary cannot be missed.

**Trace `"catdog"`**

After shorter words `"cat"` and `"dog"` have failed their own DFS checks, both are inserted. While checking `"catdog"`, the trie walk reaches an end node after `"cat"`. The recursive call on `"dog"` reaches another end node at its final character and calls `dfs("")`, which returns true. `"catdog"` is added to the result and is not inserted.

The method mutates `words` by sorting it. The answer consequently follows nondecreasing candidate length, but result order is not semantically significant.

## Complexity detail

Let $S$ be the sum of input word lengths, $N$ the number of words, and $L$ the maximum word length.

Sorting costs $O(N\log N)$ comparisons, with short integer length keys. Trie insertion across non-concatenated words creates at most $O(S)$ nodes and takes $O(S)$ total character steps.

The exact DFS has no memoization by suffix position. A word with many matching prefixes can revisit the same suffix through many segmentation paths. In the worst case, the number of segmentations is exponential, giving a conservative per-word bound such as $O(L2^L)$ character work when slice creation is included. The total worst-case search cost is therefore exponential in maximum word length, despite the current manifest's $O(\sum |word|^2)$ claim.

Trie nodes use $O(S)$ space, with a constant-size 26-child array per node. Recursion depth is at most $L$. Active suffix slices can retain $O(L^2)$ total characters across one deepest call chain. The answer contains references to input strings. A memoized index-based DFS would reduce repeated search and avoid most slicing.

## Alternatives and edge cases

- **Memoize DFS by start index:** Cache whether each suffix position is segmentable. This reduces a candidate to polynomial work and is the direct repair for the exact source's exponential repetition.
- **Word-break dynamic programming:** A Boolean array over prefix lengths tests all splits in $O(L^2)$ dictionary queries per candidate and naturally prevents whole-word self-use.
- **Global set with temporary removal:** Remove the current word, run word break, then restore it. This avoids length sorting but performs mutation around every query.
- **Insert concatenated words too:** Correctness would remain if self-matching were prevented, but excluding them keeps the trie smaller because their primitive components are sufficient.
- **Equal-length words:** They cannot be proper whole components of one another under distinct input strings, so processing tie order is harmless.
- **Repeated components:** DFS may use the same trie word multiple times because insertion does not consume it.
- **No valid prefix:** A missing trie edge rejects the suffix immediately.
- **One-word candidate:** It is absent from the trie during its own test and cannot be falsely accepted as one component.
- **Input mutation:** Sorting changes the order of `words`; callers needing the original order must pass a copy.
- **Manifest mismatch:** The exact recursive search is not memoized, so the quadratic-sum time bound is not guaranteed.
