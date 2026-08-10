## General

**A word can share an encoding only as a suffix**

In a reference string, a word is read from its starting index up to the next `#`. Suppose `"time#"` occurs in the encoding. Starting at its first character reads `"time"`, while starting two characters later reads `"me"`. Therefore, one stored word automatically encodes all input words that are its suffixes.

This is the only useful sharing relationship. A prefix such as `"tim"` cannot be read from inside `"time#"` through the same terminating `#`, because reading continues through the final `e`. Likewise, a substring in the middle that is not a suffix cannot end at the same delimiter.

The shortest encoding therefore needs one explicit `word#` segment for every distinct input word that is not a suffix of another input word. The answer is the sum of `len(word) + 1` over those maximal words, with one extra character for each `#`.

**Reverse words to turn suffixes into prefixes**

Suffix comparisons are awkward in an ordinary prefix trie. Reversing every word transforms them into prefix relationships:

- `"time"` becomes `"emit"`;
- `"me"` becomes `"em"`.

Now reversed `"me"` is a prefix of reversed `"time"`. If all reversed words are inserted into one trie, an original word is a suffix of another exactly when its trie path ends at an internal node that continues to at least one child.

An original word that is not a suffix of a longer input ends at a leaf. Thus, only leaf paths contribute explicit segments to the shortest encoding.

**The trie node representation**

Each `Trie` object contains `children = [None] * 26`. Index 0 represents `a`, index 1 represents `b`, and so on through index 25 for `z`.

For character `c`, the code computes

`idx = ord(c) - ord("a")`.

Because input words contain only lowercase English letters, `idx` is always a valid array position from 0 to 25.

An array of 26 child slots gives constant-time navigation for each letter. A dictionary could store only existing children and use less space for sparse nodes, but the fixed array is simple and predictable.

**Insert every word backward**

Insertion starts at `root`. The slice `w[::-1]` iterates over the word's characters in reverse. For each character, the algorithm follows the corresponding child. If that child is `None`, it allocates a new `Trie` node first.

Words with a common suffix share an initial reversed path. Inserting `"time"` builds the path `e -> m -> i -> t`. Inserting `"me"` follows the already existing `e -> m` path and stops there. No duplicate branch is created.

Duplicate input words also follow the same complete path. Because nodes represent character paths rather than occurrences, duplicates automatically occupy one trie endpoint and never add repeated encoding length.

The trie does not store an explicit “word ends here” flag. That omission is intentional for this problem:

- if a word ends at an internal node, it is a suffix of a longer inserted word and should contribute nothing separately;
- if it ends at a leaf, it is maximal and its path should contribute once.

Every leaf necessarily corresponds to at least one inserted word because nodes are created only while inserting words.

**Depth includes the terminating delimiter**

After insertion, `dfs(root, 1)` traverses the trie. Parameter `l` is one more than the current character depth. At the root, character depth is zero and `l = 1`. Each child call passes `l + 1`.

Therefore, at a leaf representing a word of length `d`, `l = d + 1`. That value is exactly the number of characters needed for `word#`: `d` letters plus one delimiter.

This initialization avoids separately adding 1 for every leaf.

**How the depth-first traversal sums only leaves**

At each trie node, `isLeaf` begins as `True` and `ans` begins at zero. The loop checks all 26 child slots.

For every non-`None` child:

- `isLeaf` becomes `False`;
- the recursive result for that child at depth `l + 1` is added to `ans`.

After all children are processed, `isLeaf` remains true only when the node has no child. In that case, the code adds `l`. An internal node adds no own length; it returns only the sum contributed by leaves below it.

At the root, there is always at least one child because `words` is nonempty and words have positive length, so the artificial root itself is never incorrectly counted as an encoded word.

**Example with `["time", "me", "bell"]`**

Reversed `"time"` and `"me"` share the path `e -> m`. The `"me"` endpoint is internal because the path continues through `i -> t`. Therefore, `"me"` adds no separate length.

Reversed `"bell"` follows `l -> l -> e -> b`, ending at another leaf. The two leaf depths contribute:

$$
|\texttt{"time"}|+1=5
$$

and

$$
|\texttt{"bell"}|+1=5.
$$

Their sum is 10, corresponding to a reference string such as `"time#bell#"`. The word `"me"` is recovered by starting at index 2 of that string.

**Why the leaf sum is minimal**

Every non-leaf word is a suffix of a longer inserted word. Encoding that longer leaf word already contains the shorter word immediately before the same `#`, so giving the shorter word its own segment is unnecessary.

Every leaf word is not a suffix of any other input word. If its letters were not explicitly present immediately before some delimiter, there would be no starting index that reads exactly that word. Therefore, every leaf requires `len(word) + 1` characters in any valid encoding.

The construction can concatenate all leaf words followed by `#`. It meets that unavoidable lower bound and encodes every internal-node suffix through an index inside one leaf segment. Hence, the leaf-depth sum is exactly the shortest possible length.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}|w|,
$$

the total number of input characters, counting duplicates.

Reversing and inserting a word takes `O(|w|)` time. Across all words, insertion takes `O(S)` time. The trie contains at most `S+1` nodes because every input character can create at most one new node.

DFS visits each created node once. It scans 26 child slots per node, and 26 is a constant, so traversal is `O(S)`. Total time is `O(S)`.

The trie stores up to `O(S)` nodes. Each node has 26 fixed child references, which is a constant-size record, so total trie space is `O(S)`. DFS recursion depth is at most the maximum word length, at most 7 here, and in general `O(L)` for maximum length `L`. This is bounded by `O(S)`, leaving total auxiliary space `O(S)`.

The temporary reversed slice `w[::-1]` uses `O(|w|)` space for one word at a time. Its peak is no larger than the trie bound.

## Alternatives and edge cases

- **Set and proper-suffix removal:** Put distinct words in a set, discard every proper suffix of every word, and sum the survivors' lengths plus one. It is simpler, but generating sliced suffix strings can take `O(\sum |w|^2)` time; word length is small here, while the reversed trie is linear in total characters.

- **Sort reversed words:** After reversing and sorting, prefix relationships become adjacent and can be detected without a trie. This adds sorting comparisons but can be concise.

- **Forward trie:** It groups common prefixes, which do not provide encoding sharing. Reversal is what aligns the trie structure with suffixes.

- **Duplicate words:** They traverse the same path and contribute once, which is optimal because multiple indices may point to the same encoded occurrence.

- **One word is a suffix of another:** Its endpoint is internal and contributes nothing separately.

- **One word is a prefix but not a suffix:** A forward prefix relationship gives no sharing. In the reversed trie, the paths do not have the internal-endpoint relationship unless the original word is truly a suffix.

- **Single-character word:** It contributes 2 when its root child is a leaf: one letter and one `#`. If it is the final character of a longer word, it is encoded within that longer segment.

- **All words unrelated by suffix:** Every endpoint is a leaf, so the answer is the sum of every distinct word length plus one.

- **Chain of suffixes:** For words such as `"time"`, `"ime"`, `"me"`, and `"e"`, only the longest path ends at a leaf, so one segment encodes the entire chain.

- **Branching after a shared suffix:** If several longer words share a shorter suffix, the short word ends at their branching ancestor and is covered by any one of the leaf segments. Each distinct leaf word still needs its own segment.

- **No terminal flag:** This is correct specifically because only maximal suffix words contribute. A general word-search trie would need terminal markers, but this length calculation does not.

- **Root depth starts at one:** The extra unit represents the delimiter. Starting at zero would undercount every explicit word by one.

- **No input mutation:** Reversed slices and trie nodes are new objects; the original `words` array and strings are unchanged.
