## General

**Translate “built one character at a time” into a prefix condition**

A word is eligible only if every prefix obtained while spelling it is also present in the dictionary. For a candidate such as `apple`, the required words are `a`, `ap`, `app`, `appl`, and `apple`. Merely finding the character path in some data structure is not enough; each point along that path must correspond to a complete dictionary word.

The exact solution represents all dictionary words in a trie. A trie shares nodes among words with common prefixes. Each node owns 26 child positions, one for every lowercase English letter, and an `is_end` flag indicating that the path from the root through that node is a complete inserted word.

This distinction between “path exists” and “word ends here” is fundamental. After inserting `apple`, nodes for `a`, `ap`, `app`, and `appl` all exist, but none of those shorter strings should count as dictionary words unless it was independently inserted and its node was marked `is_end`.

**Building the trie**

For each input word, `insert` starts at the root and processes its characters from left to right. The letter’s numeric child index is `ord(c) - ord("a")`. If that child does not exist, a new trie node is created. The traversal then moves to that child.

After the final character, `node.is_end = True` records that the complete word belongs to the dictionary. Inserting all words before testing any candidate makes eligibility independent of input order. A longer word may appear before one of its required prefixes in `words`, but the later search still sees the fully built dictionary.

**How `search` checks every required prefix**

The search begins at the root and follows the candidate’s characters. At each character it performs two checks:

1. The required child must exist. If it does not, even the character path is absent, so the candidate fails.
2. Immediately after moving to the child, that node’s `is_end` flag must be true. If it is false, the prefix ending at this character was never supplied as a complete word, so the candidate fails.

Because the second check occurs after every character, it checks every nonempty prefix, including the candidate itself. A successful search therefore means exactly that the word can be assembled one character at a time using dictionary words.

The full-word check may seem redundant because every candidate came from `words` and was inserted. It is still consistent and keeps `search`’s contract self-contained: success means every visited prefix, including the last, is a complete word.

**Selecting the required winner**

The answer starts as the empty string. For each word whose prefix search succeeds, the solution replaces `ans` when either:

- The new word is longer than the current answer.
- The lengths are equal and `ans > w`, meaning the current answer is lexicographically larger and the new word is the smaller tie winner.

The second condition’s direction is easy to reverse accidentally. The problem asks for the lexicographically smallest word among equal maximum lengths. Therefore replacement happens when the new candidate `w` sorts before `ans`.

No sorting of `words` is required. The explicit comparison makes the final result independent of iteration order.

**A concrete example**

Suppose the dictionary contains `w`, `wo`, `wor`, `worl`, `world`, `banana`, and `ban`.

The trie path for `world` reaches an ending node after every character because all five required prefixes are words. Its search succeeds.

The path for `banana` may exist completely because `banana` was inserted, and `ban` is also an ending node. However, the node after `b` is not an ending unless `b` is separately present. Search fails at that first prefix. The existence of a longer partial prefix cannot repair a missing shorter one.

The answer therefore may become `world` even though another dictionary word is longer, because eligibility is checked before length comparison.

**Why the trie result is correct**

Insertion creates a path for every dictionary word and marks exactly the nodes corresponding to complete words. During a candidate search, reaching the node at depth `d` corresponds exactly to reading the candidate’s length-`d` prefix. Requiring `is_end` at that node is therefore equivalent to requiring that prefix to belong to the dictionary. Search succeeds if and only if all required prefixes exist as words.

The outer loop considers every dictionary word. It ignores precisely the ineligible ones, keeps a candidate whenever it improves maximum length, and resolves equal lengths toward the lexicographically smaller string. After all words are considered, no eligible word is longer than `ans`, and no equally long eligible word is lexicographically smaller. Thus `ans` satisfies both parts of the requested ordering.

**Why a trie is a natural fit**

Different words often share prefixes. A trie stores such a prefix path once and annotates whether each prefix is a complete word. The problem’s condition asks a question at every prefix boundary, which maps directly to walking the path and checking `is_end`. This avoids repeatedly constructing prefix strings or separately looking them up in a hash set.

## Complexity detail

Let `S` be the sum of the lengths of all input words.

Inserting a word visits each of its characters once, so inserting the whole dictionary costs `O(S)` time. Searching all candidate words again visits at most `S` characters in total. Some failed searches stop early, but `O(S)` remains the worst-case bound. Length comparisons are constant time because Python stores string lengths, while the occasional lexicographic comparison can inspect characters. Across candidate replacements this does not change the usual corpus-scale bound materially; a conservative accounting can include the characters examined by tie comparisons.

The main trie operations therefore run in `O(S)` time.

Each new trie node corresponds to a previously unseen dictionary prefix. There can be at most `S` non-root nodes. Every node contains a fixed array of 26 child references and one flag; 26 is constant because inputs use lowercase English letters. Trie storage is `O(S)`. The answer holds a reference to an existing string rather than copying the entire dictionary, and traversal uses `O(1)` additional state.

## Alternatives and edge cases

- **Hash set of words:** Put every word into a set, then test each candidate’s prefixes with set membership. This is simpler and also efficient, though constructing or slicing every prefix may add character-copying cost in Python. The trie represents prefix boundaries directly.

- **Sort by length and lexicographic order:** After sorting, maintain a set of buildable words and accept a word when its immediate prefix without the last character is buildable. If shorter words are processed first, that single-prefix fact is enough by induction. This approach is concise but pays sorting cost and depends on careful ordering.

- **Trie depth-first traversal:** One can traverse only through child nodes whose `is_end` flag is true and track the deepest reachable word. Visiting children in alphabetical order can handle the tie rule. The exact solution instead searches the original words, which keeps result construction simple.

- **Checking only whether the full trie path exists:** This is incorrect. Inserting a long word creates nodes for all its prefixes even when those prefixes are not dictionary words. The `is_end` check at every depth is mandatory.

- **Checking only the immediate shorter prefix without established induction:** A candidate’s length-minus-one prefix being present does not alone prove that all still-shorter prefixes are present. This shortcut is valid only if the shorter prefix has already been proven buildable, as in the sorted-set alternative.

- **Several eligible words with the same maximum length:** The condition `ans > w` replaces the current result with the lexicographically smaller candidate, regardless of their input order.

- **Only one-letter buildable words:** A one-letter word passes because its only visited prefix is itself and its node is marked as an ending. The longest and then lexicographically smallest such word is returned.

- **No eligible word:** If no candidate has all required prefixes, `ans` remains the empty string. The implementation naturally returns `""`.

- **Duplicate input words:** Reinserting a duplicate follows existing nodes and sets the same ending flag. Rechecking it cannot change correctness; it only repeats work already included in `S`.

- **Lowercase alphabet contract:** The fixed 26-entry child array relies on every character being between `a` and `z`. Supporting a broader alphabet would require a mapping-based child structure or a larger indexing scheme.
