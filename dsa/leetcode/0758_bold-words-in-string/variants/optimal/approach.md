## General

**Separate matching, merging, and formatting**

The minimum-tag result is easiest to produce in three stages:

1. Find every substring occurrence of every keyword.
2. Merge overlapping or directly adjacent matched ranges.
3. Insert one tag pair around each merged range.

The exact solution uses a trie for efficient prefix matching from every position in `s`.

**Build the keyword trie**

Each trie node has child slots indexed by character code and an `is_end` flag. Inserting a word follows or creates one child per character, then marks the final node.

Shared keyword prefixes share trie paths. For example, `"ab"` and `"abc"` reuse the nodes for `a` and `b`, with ending flags at two depths.

**Find all keyword occurrences**

For every possible start index `i` in `s`, traversal begins at the trie root and moves `j` to the right.

If the needed child does not exist, no longer substring starting at `i` can match a keyword, so the loop breaks. Whenever the reached node has `is_end = True`, range `[i, j]` is a complete keyword occurrence and is appended to `pairs`.

Continuing after an ending node is important because a longer keyword may share that prefix.

**Why overlapping occurrences must all be discovered**

Two keyword matches may overlap even when neither contains the other. For `"ab"` and `"bc"` inside `"abc"`, their ranges are `[0, 1]` and `[1, 2]`. Both must be known so their union becomes one bold region.

The scanning order produces ranges in increasing start order, and for the same start, increasing end order. That makes the later merge pass valid without another sort.

This ordering follows directly from the loops: `i` never decreases, and `j` moves right within one fixed start. Even if a shorter match is recorded before a longer match with the same start, the merge’s `max(ed, b)` expands the range correctly.

**Merge overlap and adjacency**

The current merged range is `[st, ed]`. For next match `[a, b]`:

- If `ed + 1 < a`, at least one unbolded character separates them. Finish the current range and start a new one.
- Otherwise they overlap or touch directly. Extend `ed` to `max(ed, b)`.

Adjacent matches are merged because `</b><b>` between them would add unnecessary tags while bolding the same consecutive characters.

The resulting list `t` contains maximal disjoint bold ranges separated by at least one ordinary character.

**Format the result**

The final scan maintains source index `i` and merged-range index `j`. Before a bold range, it appends any plain slice `s[i:st]`. It then appends the opening tag, the inclusive matched slice `s[st:ed + 1]`, and the closing tag.

After the last range, the untouched suffix is appended. Collecting pieces in a list and joining once avoids repeated whole-string concatenation.

If no match exists, the source string is returned immediately.

The source pointer jumps to `ed + 1` after every bold range, so no character is duplicated. Plain slices fill exactly the gaps between that pointer and the next range. The concatenated pieces therefore preserve the original text byte for byte apart from the inserted tags.

**Why the number of tags is minimum**

Every matched character must lie inside bold tags. Any two matched ranges that overlap or touch can be covered by one tag pair without bolding an unmatched gap, so using separate pairs would be nonminimal.

Two merged ranges separated by at least one unmatched character cannot share a tag pair, because doing so would incorrectly bold that gap. Therefore one pair per maximal merged range is both sufficient and necessary.


Trie traversal records exactly every keyword occurrence: every recorded path ends at a word, and every occurrence follows its word’s trie path from its start. Merging computes exactly the maximal union components of those ranges. Formatting preserves all characters and wraps precisely those components.

Thus every keyword appearance is bold, no unrelated gap is bolded, tags are properly nested and ordered, and their count is minimal.

## Complexity detail

Let `p` be the total keyword characters, `n` the source length, and `L` the maximum keyword length. Trie construction is `O(p)`. Each starting position follows at most `L` trie edges before failing or exhausting a longest word, so matching is `O(nL)`.

There can be `O(nL)` recorded matches in the worst case. Merging and formatting are linear in matches plus output length. Exact auxiliary space is therefore `O(p + nL)` in the broad worst case, although constraints keep `L <= 10` and it is often summarized as `O(p + n)`.

## Alternatives and edge cases

- **Boolean coverage array:** Mark every character covered by any direct keyword search, then emit tags at true-run boundaries. This is simple but may repeat substring searches.

- **Aho-Corasick automaton:** Finds all keyword occurrences in linear text-plus-match time, but its failure links are unnecessary for the small limits.

- **Do not merge adjacent ranges:** That produces extra tags and violates the minimum-tag requirement.

- **Nested matches:** The longer merged endpoint absorbs the shorter occurrence.

- **No keywords or no matches:** Return `s` unchanged.

- **Match at either boundary:** Empty plain slices are naturally omitted.

- **Multiple words sharing a prefix:** Ending flags allow all valid lengths to be recorded.

- **Inclusive endpoints:** Formatting uses `ed + 1` in the Python slice.
