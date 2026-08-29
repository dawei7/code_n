## General

**A valid match has the same length and one different position**

The allowed operation replaces one character. It does not insert or delete characters. Therefore, a successful dictionary word must:

- have the same length as `searchWord`;
- match at every position except exactly one.

The trie stores dictionary prefixes, while recursive search tracks whether the one allowed difference has already been used.

**Trie node representation**

Each `Trie` node contains:

- `children`: a dictionary from next character to child node;
- `is_end`: whether a complete dictionary word ends at this node.

`__slots__` restricts instances to those two attributes. This reduces per-node Python object overhead but does not change algorithm behavior.

Dictionary-based children store only edges that actually exist, which is useful when most trie nodes have few outgoing letters.

**Build the dictionary**

Insertion starts at the trie root. For each character of a dictionary word:

1. Create the child if it does not exist.
2. Move to that child.

After the final character, set `is_end = True`.

Shared prefixes reuse nodes. The dictionary words are distinct, but marking the same terminal twice would still be harmless.

**Search state**

The nested function `dfs(i, node, diff)` means:

- the first `i` characters of the query have been aligned with the path to `node`;
- `diff` is zero if no replacement has been used;
- `diff` is one if exactly one character has differed.

No state with more than one difference is explored.

**The terminal condition enforces both requirements**

When `i == len(w)`, every query character has been consumed. Search succeeds only when:

`diff == 1 and node.is_end`.

`node.is_end` ensures a dictionary word ends at exactly this length. `diff == 1` ensures exactly one replacement, not zero.

This is why searching for a word already present in the dictionary returns false when no other same-length word differs by one character. An exact match reaches a terminal node with `diff = 0` and is rejected.

**First try keeping the current character**

If `w[i]` exists among the current node's children, the search follows that edge without changing `diff`.

If this recursive call succeeds, return `True` immediately. This short-circuit avoids exploring replacement choices after a valid word has already been found.

Trying the exact edge first is an efficiency preference, not a correctness requirement.

**Try a replacement only if none has been used**

If exact continuation does not succeed, the return expression permits alternatives only when `diff == 0`.

It iterates over every child character different from `w[i]`. Following one such child represents replacing query character `w[i]` with that dictionary character. The recursive call advances to the next position with `diff = 1`.

Once `diff` is one, later calls can follow only exact matching edges. A second mismatch makes the exact edge unavailable and the replacement branch forbidden, so that path returns false.

**A successful example**

Suppose `"hello"` is in the trie and the query is `"hhllo"`.

- The first `h` follows the exact edge with `diff = 0`.
- At index one, query `h` does not match the needed trie edge `e`. The alternative branch follows `e` and sets `diff = 1`.
- The remaining `l, l, o` characters follow exact edges.
- Search reaches the terminal node after all query characters with one difference, so it returns true.

**Why shorter and longer words fail naturally**

If a dictionary word is shorter, its terminal node is reached before all query characters are consumed. Search must continue, and without a child path it fails.

If a dictionary word is longer, consuming the complete query reaches a nonterminal prefix node, so `node.is_end` is false.

No explicit length buckets are required.

**Why the traversal is correct**

Every recursive path spells one trie prefix of the same length as the processed query prefix. `diff` exactly records whether those prefixes differ at zero or one positions.

A successful terminal path therefore spells a dictionary word of equal length with exactly one differing character, so every true result is valid.

Conversely, suppose a dictionary word differs from the query at exactly position `p`. The recursion can follow exact edges before `p`, choose that word's different edge at `p`, and follow exact edges afterward. It reaches the word's terminal node with `diff = 1`, so the method finds every valid match.

**Why alternatives exclude the query character**

The exact-character path was already explored separately. Including the same character in the replacement generator would label a non-change as a used difference and could make an identical dictionary word incorrectly pass.

## Complexity detail

Let `S` be the total number of characters across dictionary words, `Q` the number of queries, `L` a query length, and `A = 26` the fixed alphabet size.

Building the trie processes each dictionary character once in expected `O(S)` time and stores at most one node per character, using `O(S)` persistent space.

For one query, the exact-prefix path can try replacement branches at each of `L` positions. A replacement branch then follows only exact edges for the remaining suffix. A conservative exact-source bound is `O(min(S, A * L^2))` time per query: no more trie nodes than exist can be visited, and with at most one mismatch there are at most a linear number of near-matching prefixes per depth. The manifest's `O(S + QL)` assumes replacement alternatives behave as a fixed amount of work per query position; that is a useful typical or tightly indexed target, but the literal recursive branching can do more than linear work on an adversarial trie.

Recursion depth is at most `L`. Generator and call-stack working space is `O(L)` per query, in addition to the persistent `O(S)` trie. With source bounds of at most 100 characters, recursion depth is safe.

## Alternatives and edge cases

- **Compare with every dictionary word:** Filter to equal lengths and count character differences, stopping above one. This is simple but costs `O(DL)` per query for `D` words.

- **Wildcard-pattern index:** For each dictionary word, replace each position with a marker and index the resulting patterns. Queries can check `L` patterns in near-linear time, but the structure must distinguish an identical word from a genuinely different word to enforce exactly one change.

- **Group words by length:** This quickly rejects impossible lengths and can reduce brute-force comparisons, but does not exploit shared prefixes.

- **Breadth-first trie state search:** Store `(index, node, differences)` states in a queue. It is equivalent but allocates an explicit frontier.

- **Exact dictionary word only:** It returns false unless another word differs by exactly one position.

- **One-character query:** Any different one-character dictionary word is a valid match; an identical one alone is not.

- **Different word length:** Replacement cannot change length, and the terminal condition rejects it.

- **Two differences:** After the first alternate edge sets `diff = 1`, no second alternate edge is permitted.

- **No differences:** Reaching a terminal with `diff = 0` fails because the operation must change exactly one character.

- **Several valid words:** `any` short-circuits after the first successful branch; only existence is requested.

- **Shared prefixes:** Trie nodes are reused, reducing persistent storage and allowing early rejection when an edge is absent.

- **Lowercase alphabet:** Child dictionaries support the guaranteed characters. A broader alphabet would still work but change branching constants.

- **Build called once:** The exact object accumulates inserted words. The source promises one build call before searches, so reset semantics are unnecessary.

- **Same-character alternative:** It is explicitly excluded to prevent treating zero actual changes as one.
