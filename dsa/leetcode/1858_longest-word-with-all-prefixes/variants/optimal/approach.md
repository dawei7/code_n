## General

**Store every complete word in a trie.** A trie shares nodes among common prefixes. Following characters from the root traces a prefix, while `is_end` distinguishes a prefix that is itself present as a complete word from one that exists only because a longer word uses it.

Each `Trie` node contains a 26-slot child array and one Boolean. `__slots__` prevents a per-instance attribute dictionary, reducing overhead across potentially many nodes.

**Insert all words before checking candidates.** `insert` begins at the root and maps each lowercase character to index `ord(c) - ord("a")`. A missing child is created; an existing child is reused. After the final character, `node.is_end = True` records that the full word occurs in `words`.

All words are inserted first, so validation does not depend on input order. A prefix may appear later in the original list and is still marked before searches begin.

**Check every prefix during one trie walk.** `search(w)` follows the path for `w` one character at a time. Immediately after moving to the node for each character, it tests `node.is_end`. At depth one this checks the one-letter prefix, at depth two the two-letter prefix, and so on through the full word.

If any prefix node is not an end-of-word marker, the method returns false. If all are marked, every nonempty prefix belongs to the input and it returns true.

The code does not check whether `node` is `None` before reading `is_end`. This is safe in its exact calling context because `search` is invoked only on words from `words`, and every one of those words was inserted, so its complete trie path necessarily exists.

**Evaluate only candidates that could improve the answer.** `ans` begins as the empty string. For each word `w`, the outer condition first asks whether it is longer than `ans`, or equal in length and lexicographically smaller. Only if it could win does Python evaluate `trie.search(w)` because `and` short-circuits.

If the word is valid, it replaces `ans`. A shorter word cannot improve the requested result, and a lexicographically larger equal-length word cannot win the tie, so skipping their searches is safe.

**Trace the tie in the second example.** Both `"apple"` and `"apply"` have the prefixes `"a"`, `"ap"`, `"app"`, and `"appl"` in the trie. When `"apple"` becomes the answer, `"apply"` has equal length but is lexicographically larger, so it cannot replace it. If their input order were reversed, `"apply"` could be temporary, then valid `"apple"` would satisfy the smaller tie condition and replace it.

**Why checking each prefix marker is sufficient.** In a trie, the node reached after the first `t` characters represents exactly the length-`t` prefix. Its `is_end` flag is true exactly when that prefix was inserted as a whole word. Therefore all markers along the path being true is logically equivalent to every prefix existing in `words`.
The trie search classifies every potentially winning word correctly. The update rule orders valid candidates first by greater length and then by smaller lexicographic value. Starting from empty and applying that rule leaves exactly the best valid word seen so far. After all words, it is the required global best. If no word passes, `ans` remains empty.

**Why the full word check is harmless.** Every searched `w` was inserted, so its final node is always marked. Testing it alongside shorter prefixes makes the loop uniform and reinforces that the path represents a complete word.

## Complexity detail

Let `S` be the sum of all word lengths. Insertion visits each input character once, taking `O(S)` time. Each word can be searched at most once, and total searched character length is at most `S`, so validation is `O(S)`. Lexicographic tie comparisons can inspect word characters, but under the total-length input bound the intended overall accounting remains linear in corpus size for trie work.

The trie has at most `S + 1` nodes. Each stores 26 child references and a Boolean, so space is `O(26S) = O(S)` for the fixed alphabet.

## Alternatives and edge cases

- **Sort plus valid-word set:** Process words in lexicographic order and accept a word when its immediate prefix is already valid. It is simpler but includes sorting cost.
- **Check every prefix in a hash set:** Straightforward slicing can repeat character copying and lead to quadratic work per long word.
- **One-letter word:** Its only nonempty prefix is itself, which is marked after insertion, so it is valid.
- **Missing immediate prefix:** Search fails at that prefix node even if longer structural trie nodes exist.
- **Missing shorter prefix:** Every depth is checked, so an earlier gap cannot be hidden by later complete words.
- **Several longest valid words:** The lexicographically smallest replaces or blocks larger ties regardless of input order.
- **No valid word:** This can happen when no one-letter starting prefix exists; the empty answer is returned.
- **Duplicate input words:** Insertion simply marks the same node again and does not affect correctness.
- **Existing-path assumption:** `search` omits a null-child guard only because every searched word was inserted first.
- **Short-circuit optimization:** Noncompetitive lengths or ties are not searched because they cannot change `ans`.
- **Fixed lowercase alphabet:** Direct 26-slot arrays trade memory for constant child access.
- **Input order:** Insert-all-first design makes prefix validation independent of order.
