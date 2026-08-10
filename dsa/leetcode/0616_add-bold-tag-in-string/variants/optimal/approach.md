## General

**Separate matching from formatting.** The output rule sounds like a string-editing task, but inserting tags while searching is awkward. A newly found word may overlap a region already tagged, or it may touch that region exactly at the next character. The exact solution therefore performs three clean phases:

1. build a trie from all dictionary words;
2. discover every matched interval in `s`;
3. merge the intervals and construct the tagged string.

This separation ensures that overlap decisions are based on positions in the unchanged source string.

**Why a trie helps.** A trie stores words by shared prefixes. Each node has an array of 128 child references, indexed by `ord(c)`, and an `is_end` flag. Inserting a word walks its characters from the root, creating a child only when that prefix has not appeared before. If `words` contains `"ab"` and `"abc"`, both words share the nodes for `a` and `b`; the `b` node is terminal, and the following `c` node is terminal too.

The fixed child array makes each transition constant time. Its size is safe for this problem because English letters and digits have ASCII codes below 128. It would not be a general Unicode trie.

**Search from every possible starting position.** For each index `i` in `s`, the solution begins at the trie root and advances `j` from `i` toward the end:

- if there is no child for `s[j]`, no dictionary word can continue from this start, so the inner loop stops immediately;
- otherwise it moves to that child;
- whenever the reached node has `is_end = True`, the inclusive interval `[i, j]` is a complete dictionary occurrence and is appended to `pairs`.

It is important that the scan does not stop at the first terminal node. With dictionary words `"a"` and `"abc"`, the same start can produce both `[i, i]` and `[i, i + 2]`.

Starting a search at every `i` also finds overlapping occurrences. For `s = "aaa"` and word `"aa"`, the search from `0` records `[0, 1]`, while the search from `1` records `[1, 2]`. Advancing start positions by one rather than by the previous word length is what preserves the second match.

If no interval is found, the method returns `s` immediately. This handles an empty dictionary and a dictionary whose words never occur without doing any formatting work.

**Why the intervals are already ordered.** The outer search loop increases `i`, so start positions are nondecreasing. For one fixed start, the inner loop increases `j`, so end positions are also increasing. Therefore, `pairs` arrives in the exact order required by the merge phase; no separate sort is needed.

**Merge overlaps and adjacency with one condition.** Initialize the active region to the first interval, `[st, ed]`. For each later `[a, b]`:

- if `ed + 1 < a`, at least one unbolded character lies between the intervals. The active region is complete, so append it and begin a new one;
- otherwise the intervals overlap or are consecutive. They require one pair of tags, so extend `ed` to `max(ed, b)`.

The `+ 1` is what merges adjacency. If one match ends at index 4 and another starts at index 5, `ed + 1 < a` is false, and they become one bold region. Taking `max` is essential when a later interval is contained inside the current one; assigning `ed = b` could incorrectly shrink the region.

This scan maintains a useful fact: `[st, ed]` is the union of every interval processed since the last genuine gap. Because intervals are ordered by start, once a gap appears, no later interval can reach backward across it. Appending the active interval is therefore final and safe.

**Build the answer without changing source indices.** The list `t` contains disjoint, nonconsecutive merged intervals. Two pointers drive output: `i` is the next unprocessed source index, and `j` selects the next merged interval.

For interval `[st, ed]`, the method first appends an ordinary slice `s[i:st]` if a gap exists. It then appends `<b>`, the inclusive matched slice `s[st:ed + 1]`, and `</b>`. It advances `i` to `ed + 1` and moves to the next interval. When no intervals remain, it appends the untouched suffix `s[i:]` once and stops. A list is used because repeatedly concatenating immutable Python strings could copy an ever-growing prefix; one final `''.join(ans)` is linear in the output size.

Every source character is copied exactly once, in original order. A character is placed between tags exactly when it lies in the union of matched intervals. Since the merge phase turns each maximal connected union component into one interval, overlapping and consecutive occurrences receive one tag pair, while regions separated by a real gap receive separate pairs. That proves the returned formatting satisfies all rules.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$, let $D$ be the sum of dictionary-word lengths, let $L$ be the maximum dictionary-word length, and let $M$ be the number of matched word occurrences recorded in `pairs`.

Trie construction visits every dictionary character once, so it takes $O(D)$ time and creates at most $O(D)$ nodes. Because every node owns a 128-entry array and 128 is a fixed alphabet constant, its asymptotic storage is $O(D)$, though the practical constant is substantial.

The search from start `i` can follow at most `min(L, N - i)` trie edges before no word prefix can continue. Across all starts, this is $O(NL)$ worst-case time, plus $O(M)$ interval appends. The merge costs $O(M)$, and output construction costs $O(N)$ plus a constant amount per merged region. The honest total for the exact implementation is $O(D+NL+M+N)$ time.

The manifest lists $O(N+D)$ time and space. That linear time can describe more advanced multi-pattern matching, but a plain trie restarted at every source index does not guarantee it. For example, a long repeated source and many nested repeated prefixes can force long traversals from many starts. Exact auxiliary storage is $O(D+M+N)$ when the interval list and output are counted. Since $M$ can be much larger than $N$ when many dictionary words end at many starts, the stored-pair phase is another reason the literal implementation is not always linear.

## Alternatives and edge cases

- **Boolean coverage array:** Find each word occurrence and mark every covered source index. A final boundary scan inserts tags. This is conceptually simple, but repeated substring searches and repeated marking can be expensive.
- **Aho-Corasick automaton:** Add failure links to the trie so all patterns are matched in one left-to-right scan. This is the standard way to approach $O(N+D+M)$ matching without restarting from every index.
- **Track only the farthest covered end:** While scanning starts, retain the furthest endpoint reached by any match and emit maximal regions directly. This can avoid storing every `[start, end]` pair, but the ordering and emission logic must remain careful.
- **Empty `words`:** The trie has no outgoing path, `pairs` stays empty, and the original string is returned unchanged.
- **No matches:** The same early return avoids adding any tags.
- **Overlapping matches:** Intervals such as `[0, 1]` and `[1, 2]` merge because there is no gap.
- **Consecutive matches:** Intervals such as `[0, 1]` and `[2, 3]` also merge because `ed + 1 < a` is false.
- **Contained matches:** If `[0, 5]` is followed by `[1, 2]`, `max(ed, b)` preserves endpoint 5 rather than shrinking the bold region.
- **Match at the first or last character:** Python slices naturally handle empty prefix or suffix slices, so no special tag branch is needed.
- **Several words sharing a prefix:** Terminal flags at multiple trie depths ensure every complete word is recorded while traversal continues toward longer words.
- **Characters outside ASCII:** The 128-child array would be indexed out of range for sufficiently large code points. The input restriction to English letters and digits is therefore part of the implementation's safety argument.
- **Large numbers of matches:** `pairs` can consume significant memory even though the final bold union may contain only one interval. A streaming farthest-end design is preferable when constraints are much larger.
