## General

An abbreviation keeps a prefix, replaces a middle block with its character count, and keeps the final character. Two words can collide only when the visible and numeric parts agree. The solution uses tries to discover the shortest prefix that distinguishes each word from every possible collision partner.

Let $S$ denote the total number of characters across all input words.

**Group words that could interact.** Dictionary `tries` is keyed by `(len(w), w[-1])`. Words with different lengths produce different omitted-count behavior, and words with different final characters end differently, so they cannot require conflict resolution with one another.

The key does not explicitly include the first character. This is still correct because each group's trie begins at the first character. Words with different first letters enter different root children, whose counts become one, and their unique-prefix search stops after that first character. Using a coarser group key does not merge their trie paths beyond the root.

For each word, the code creates the appropriate trie if necessary and calls `insert(w)`.

**What each trie count means.** A trie node represents a prefix. During insertion, the code follows or creates one child for each lowercase letter, then increments that child node's `cnt`. Therefore `node.cnt` equals the number of words in this group sharing the prefix represented by that node.

The root's count is unused. Counts begin on the first-character nodes, exactly where prefixes begin.

Because all input strings are distinct, following a word's complete path eventually reaches a node whose count is one. There may be shared early prefixes, but no different word shares the entire string.

**Find the minimal distinguishing prefix.** Method `search(w)` walks the same trie path and increments local `cnt` for each consumed character. As soon as `node.cnt == 1`, the prefix seen so far belongs only to `w` within its collision group, so its length is returned.

Suppose two words share their first three characters and differ at the fourth. Nodes for prefix lengths one through three have count greater than one; each fourth-character child has count one. Search returns four, which is exactly the first prefix length that distinguishes them.

Stopping at the first count-one node makes the prefix minimal. Every shorter prefix had a node count greater than one and was shared by another relevant word, so using it could not guarantee uniqueness. The returned prefix is unique, so using more characters is unnecessary.

If search reaches the full word without an earlier unique node, it returns `len(w)`. With distinct words this mainly reflects uniqueness arriving at the end; the later abbreviation-length check keeps the original word.

**Build the abbreviation only when it is shorter.** For a returned prefix length `cnt`, the abbreviation would be:

`w[:cnt] + str(len(w) - cnt - 1) + w[-1]`.

The number `len(w) - cnt - 1` counts characters after the retained prefix and before the retained last character. Those are exactly the omitted middle characters.

The condition `cnt + 2 >= len(w)` means at most one character lies between the prefix and last character. Replacing zero or one character with its count would not make the representation shorter, so the original `w` is appended instead. Otherwise the constructed abbreviation removes at least two middle characters and is shorter.

For words `"abcdef"` and `"abndef"`, the initial one-character prefix is shared. Prefix `"ab"` is also shared. At the third character, trie paths split into `c` and `n`, so each search returns three. Their abbreviations become `"abc2f"` and `"abn2f"`, now unique.

For a word such as `"god"`, even a unique one-character prefix leaves only one middle character. The shortening condition fails and the original word is returned.

**Why the generated outputs are unique.** Within one trie group, each abbreviated word uses a prefix whose trie count is one, so no other group member has that same retained prefix. Since group members also share length and final character constraints, this unique prefix prevents equal abbreviations. Words in different groups already differ in source length or last character; when a word is kept in full, source distinctness and the same minimality rules prevent it from colliding with another produced representation.

**Why prefixes are minimal.** Search stops at the first unique prefix node. All earlier nodes have count at least two, meaning a conflicting word shares that prefix within the relevant length/final-letter group. Increasing the prefix to the returned length is therefore necessary. The final check separately enforces the rule that a non-shortening abbreviation must be replaced by the original.

The answer loop processes words in their original order and appends one result per word, so output order matches input order even though trie groups are stored in a dictionary.

The fixed 26-child arrays use lowercase-English indexing through `ord(c) - ord("a")`. This gives direct child access and relies on the source's character guarantee.

## Complexity detail

Each word is traversed once during insertion and once during search. Both operations do constant work per character, so total time is $O(S)$, matching the manifest. Constructing all returned strings also writes at most $O(S)$ output characters.

Across all tries, at most one new node is created per inserted character, so there are $O(S)$ nodes. Each node owns a fixed array of 26 child references and one count; 26 is constant, giving $O(S)$ auxiliary space. The output list and strings also occupy $O(S)$ result space.

Dictionary lookup by the length/final-character tuple is expected $O(1)$. Fixed-array trie navigation is worst-case constant per lowercase character.

## Alternatives and edge cases

- **Repeatedly lengthen duplicate abbreviations:** It follows the rules directly but may rescan and rebuild abbreviations many times, leading to substantially more than linear work.
- **Sort each collision group:** Adjacent lexicographic neighbors determine the longest common prefix. This uses less per-node overhead but costs sorting time.
- **Pairwise longest common prefixes:** Comparing every relevant word pair can require quadratic work in the number of words.
- **Different first characters in one trie key:** They split at the first trie edge and immediately obtain unique one-character prefixes.
- **Different final characters or lengths:** Separate trie groups ensure they never influence one another's prefix length.
- **Very short words:** When abbreviation does not shorten them, the exact original word is returned.
- **Prefix unique at the first character:** `search` returns one and creates the initial-style abbreviation when it is shorter.
- **Long shared prefix:** Search continues until the first count-one node, then the remaining middle length is calculated exactly.
- **Distinct-word guarantee:** It ensures complete trie paths do not represent multiple identical inputs.
- **Input order:** Results are generated in a second pass over `words`, preserving the required order.
- **Lowercase guarantee:** Every child index lies between zero and 25.
- **Multi-digit counts:** `str(...)` writes the full omitted-character count; the algorithm does not assume it is one digit.
