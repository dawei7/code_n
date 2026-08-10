## General

**The replacement relation is a prefix relation**

A dictionary root can replace a sentence word only when the root appears at the very beginning of that word. For example, `"cat"` can replace `"cattle"`, but it cannot replace a word merely because `"cat"` occurs in the middle.

When several roots match, the shortest one must win. This means a search should examine a word from left to right and stop at the first dictionary root it completes.

A trie is designed for exactly this operation. It stores common prefixes once and lets the search consume one character at a time without repeatedly constructing and hashing every possible prefix.

**What one trie node means**

The root trie node represents the empty prefix. Following an edge labeled with a letter extends that prefix by one character. A path from the root therefore spells a dictionary prefix.

Each node contains:

- `children`, an array of 26 child references for lowercase English letters;
- `is_end`, which says whether the path ending at this node is a complete dictionary root.

The array index for character `c` is `ord(c) - ord("a")`. Thus `a` maps to zero, `b` to one, and `z` to twenty-five. The source guarantees lowercase letters, so every dictionary and sentence-word character maps to a valid slot.

It is important to distinguish “this prefix exists” from “this prefix is a root.” A node may exist only because it is on the path to a longer dictionary word. `is_end` records when stopping at that node is legally allowed.

**Insert every dictionary root**

Insertion starts at the trie root and processes the letters of a dictionary word in order. For each letter:

1. Compute its child index.
2. Create a child node if that edge does not exist.
3. Move to the child.

After the last letter, mark `is_end = True`.

If several roots share a prefix, they reuse the same initial nodes. For dictionary roots `"cat"` and `"car"`, the `c` and `a` nodes are shared, then the paths branch. If one root is a prefix of another, such as `"a"` and `"apple"`, the node for `a` is terminal and still has descendants.

Inserting the same root more than once simply sets the same Boolean to true again. Duplicate dictionary entries, if present, do not alter replacement behavior.

**Search one sentence word**

`Trie.search(w)` walks the characters of `w` from left to right. The enumeration starts its position count at one, so after consuming character number `i`, the matching prefix is `w[:i]`.

At each character:

- If the required child is absent, no dictionary path matches the word through this position. Since every longer prefix includes the same missing edge, no longer dictionary root can match either. Return the original word immediately.
- Otherwise, move to the child.
- If that node has `is_end = True`, return `w[:i]` immediately.

The first terminal reached is necessarily the shortest matching root because the traversal examines prefix lengths one, two, three, and so on. There is no need to continue searching for longer terminal descendants after finding it; the problem explicitly prefers the shortest root.

If every character is consumed without reaching a terminal node, the word itself may be a trie prefix but is not a complete dictionary root. In that case, return the original word.

**Why an absent edge permits an immediate answer**

Suppose the search has matched `"ca"` but the word's next letter is `t` and the trie has no `t` child there. Every longer prefix of the word begins with `"cat"`, so all of them require that same missing edge. None can be a stored root. Returning early is therefore logically complete, not merely a performance shortcut.

**Rebuild the sentence without changing word boundaries**

The solution uses `sentence.split()` to obtain the words. The contract guarantees exactly one space between consecutive words and no leading or trailing spaces, so splitting loses no meaningful formatting.

It applies `trie.search(w)` to each word through a generator and joins the returned replacements with one space. Therefore:

- word order remains unchanged;
- each derivative is independently replaced by its shortest root;
- words with no matching root remain unchanged;
- the output preserves the required single-space sentence format.

For `"the cattle was rattled by the battery"` with roots `"cat"`, `"bat"`, and `"rat"`, the searches stop at `cat` within `cattle`, `rat` within `rattled`, and `bat` within `battery`. Other words hit missing edges and remain unchanged.

**Why the whole method is correct**

Insertion creates a path for every dictionary root and marks precisely the node at which that root ends. During search, reaching a node after consuming `i` characters means the first `i` characters of the word equal the path prefix. Therefore, a terminal node reached during the walk corresponds exactly to a dictionary root that prefixes the word.

The first such node has the smallest consumed length, so returning there satisfies the shortest-root rule. If no terminal is reached, either a missing edge proves no longer prefix can occur or the word ends before any complete root; returning the original word is then required.

Applying this correct search independently to every sentence word and joining results in their original order proves that the final sentence is correct.

## Complexity detail

Let `D` be the total number of characters across all dictionary roots and `S` be the number of characters in the input sentence.

Trie construction follows or creates one edge per dictionary character, so it takes `O(D)` time. Searching a word reads characters only until the first matching root, a missing edge, or the word's end. Across all sentence words, at most `O(S)` characters are examined. Splitting and joining also take `O(S)` time. Total running time is `O(D + S)`.

The trie creates at most one new node per dictionary character, so it has `O(D)` nodes. Every node stores 26 child slots, but 26 is a fixed alphabet constant, leaving `O(D)` asymptotic trie space.

The manifest's `O(D)` space describes the persistent indexing structure. The exact Python operation also materializes the word list returned by `sentence.split()`, returned prefix slices, and the final output string. These require `O(S)` transient or output-related storage in the worst case. Thus literal peak additional storage including sentence processing is `O(D + S)`; excluding the returned output and treating split words as input processing gives the advertised trie-focused `O(D)` bound.

## Alternatives and edge cases

- **Hash set of roots:** Put all roots in a set and test every prefix of each word from shortest to longest. The logic is simple, but Python slicing constructs progressively longer strings, which can make processing one long word quadratic in its length.

- **Sort roots by length and test each against each word:** This guarantees that the first match is shortest but may compare many unrelated roots for every word, performing much more work than following one trie path.

- **Dictionary child maps:** A hash map per trie node stores only existing edges and may use less space for sparse nodes. The 26-slot array offers direct indexing and predictable behavior for the fixed alphabet.

- **Store a full root string at terminal nodes:** This can avoid slicing `w[:i]` when a match is found, at the cost of another stored reference. The exact implementation reconstructs the prefix once.

- **One root prefixes another:** If `"a"` and `"apple"` both exist, a word beginning with `a` is replaced by `"a"` because search stops at the first terminal.

- **The word exactly equals a root:** The terminal is reached on the final character and the returned prefix has the same text as the word, which is correct.

- **The word is only a nonterminal trie prefix:** If dictionary contains `"apple"` and the word is `"app"`, no terminal is reached before the word ends, so `"app"` remains unchanged.

- **Missing first edge:** Search returns immediately after the first character, avoiding examination of the rest of a word that cannot possibly match.

- **No dictionary root matches any sentence word:** Every search returns its original word, and joining reconstructs the original sentence.

- **Every word has a one-letter root:** Each search stops after one edge, giving especially small practical query work.

- **Repeated sentence words:** They are searched independently. Caching replacements could speed repeated words but is not necessary for the stated bounds.

- **Spacing guarantees:** Plain `split()` normalizes arbitrary whitespace. That is harmless here only because the source promises one space between words and no leading or trailing spaces.

- **Uppercase letters or punctuation:** The child-index calculation assumes lowercase English letters. Supporting a wider alphabet would require validation or a mapping-based child representation.

- **Very long sentence:** The trie prevents dictionary scanning for every word, but Python still must allocate the split representation and final output string, which explains the sentence-dependent memory noted above.
