## General

**View every sentence as a path of dictionary prefixes**

At any recursive call, the parameter `s` is the remaining suffix that still needs to be split. The function tries every nonempty prefix of that suffix. If a prefix is a dictionary word, it recursively obtains every segmentation of the characters after that prefix and places the chosen word before each returned segmentation.

The dictionary is stored in a trie. Each trie node has 26 child positions, one for each lowercase English letter, plus `is_end`, which records whether the path from the root spells a complete dictionary word.

Building the trie once avoids scanning all dictionary words for each prefix. However, the exact source calls `trie.search` separately for each candidate prefix, restarting at the root each time.

**How insertion represents the dictionary**

For every word, `insert` starts at the trie root. Each character selects an array index from zero through 25 by subtracting `ord('a')`. A missing child is allocated; an existing child is reused.

After the final character, `is_end` becomes true. Shared prefixes share trie nodes. For example, `"pine"` and `"pineapple"` follow the same path through `"pine"`, but both corresponding endpoint nodes can be marked as complete words.

Dictionary entries are unique, so repeated insertion is not needed. Unlimited reuse in sentences requires no trie mutation; each recursive search starts from the root and may recognize the same word again at another position.

**What `dfs(remaining)` returns**

The recursive result is a list of word lists, not yet a list of sentences. Each inner list contains one complete segmentation of the exact `remaining` string.

The base case for an empty suffix returns `[[]]`, a list containing one empty segmentation. Returning `[]` would mean “there are no ways” and would prevent the final real word from producing an answer. The one empty continuation acts as a neutral completion.

For every prefix length `i`:

1. `s[:i]` is tested in the trie;
2. if it is a word, `dfs(s[i:])` returns all valid continuations;
3. `[s[:i]] + v` places the current word before one continuation `v`;
4. that complete word list is appended to `res`.

If a chosen prefix leads to a suffix with no segmentation, the recursive call returns an empty list, the inner loop performs no append, and that branch contributes no answer.

**Why every produced word list is valid**

The base result consumes an empty suffix with no pieces. In a nonempty call, a piece is prepended only after `trie.search` proves it is a full dictionary word. The recursive continuation covers exactly the remaining characters. Therefore, concatenating the returned pieces reconstructs the call’s suffix without gaps, overlaps, or reordering.

By induction from the empty suffix upward, every word list in `dfs(original_s)` is a complete dictionary segmentation.

**Why no valid sentence is missed**

Take any valid segmentation of the current suffix. Its first word has a unique length `i`. The loop tests that length, and the trie recognizes the word. The remaining words form a valid segmentation of `s[i:]`; by the same reasoning, recursion returns that continuation. The code then prepends the first word and records the complete segmentation.

Different sequences of cut positions follow different recursive choices, so distinct segmentations are represented independently. The dictionary words contain lowercase letters and no spaces, making `' '.join(v)` an unambiguous sentence construction.

The final list comprehension converts every word list into the required space-separated string. The contract allows any outer order, so the increasing-prefix depth-first order is acceptable.

**The trie does not provide memoization**

The recursive argument is a sliced suffix string. Different earlier segmentations can reach equal remaining suffix contents, but this source does not cache the result of `dfs` for that suffix. It recomputes the same subtree every time.

That is a material difference from memoized Word Break II. The trie accelerates dictionary-prefix recognition; it does not eliminate repeated segmentation subproblems.

For an input with many reusable prefixes such as repeated `a` characters, the recursion can branch at many gaps. Even branches that ultimately fail may be recalculated through multiple earlier cut patterns.

## Complexity detail

Let $n$ be the input-string length, let:

$$
S=\sum_{w\in\texttt{wordDict}}\lvert w\rvert,
$$

and let $R$ be the total size in characters and list entries of the returned sentences.

Trie construction takes $O(S)$ time and at most $O(S)$ nodes. At one recursive call with suffix length $k$, the loop performs searches for prefixes of lengths one through $k$. Python creates each `s[:i]` slice, and `search` scans its characters, producing $O(k^2)$ local work in the worst case. The source also creates `s[i:]` slices for recursive branches and copies word lists when prepending.

Without memoization, the recursion can have exponentially many calls across cut combinations. A safe source-faithful worst-case bound is $O(S+n^2 2^n+R)$ time. This bound is conservative; the precise work varies with dictionary prefixes and returned partitions, but it is not $O(S+n+R)$ as the manifest states. Output alone can be exponential, and repeated failing suffix work can occur beyond final-output construction.

Persistent trie space is $O(S)$. Recursion depth is at most $n$. The returned sentences and intermediate word lists require output-associated storage bounded on the same exponential scale as $R$. Thus total space including results is $O(S+n+R)$ at the high level, while working space excluding generated result structures includes $O(S+n)$ plus transient slices.

The trie uses an array of 26 child references per node, so its exact constant factor can be large even when many nodes have only one child.

## Alternatives and edge cases

- **Memoize by starting index:** Cache every list of segmentations for `s[i:]`. It prevents recomputing identical suffix subproblems, although cached sentence combinations still require output-sized memory.
- **Bottom-up sentence DP:** Build all sentences for suffixes from right to left. It avoids recursion but stores many intermediate strings.
- **Feasibility pruning:** First compute which suffixes can reach the end, then recurse only through edges with a feasible continuation. This prevents large dead subtrees.
- **Walk the trie once per suffix:** Advance a trie pointer as `i` grows instead of calling `search(s[:i])` from the root each time. It removes repeated prefix rescans and slices for recognition.
- **One dictionary word equal to `s`:** That prefix reaches the empty base and produces the one-word sentence without a trailing space.
- **No segmentation:** Every branch eventually returns no continuations, so `ans` is empty and the final comprehension returns `[]`.
- **Word reuse:** Trie contents remain unchanged, allowing the same word at multiple positions.
- **Overlapping dictionary prefixes:** Each endpoint marked `is_end` creates a branch; longer prefixes remain discoverable.
- **Empty suffix base:** `[[]]` is essential. Replacing it with `[]` would eliminate every completion.
- **Runtime dependency:** The selected source uses `List` annotations without importing it. Standalone Python needs `from typing import List`.
- **Manifest mismatch:** The exact un-memoized recursion and repeated trie searches cannot be described by the manifest’s $O(S+n+R)$ time.
