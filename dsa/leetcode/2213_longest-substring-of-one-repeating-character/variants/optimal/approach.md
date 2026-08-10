## General

**What must be maintained after every character replacement**

After each query, the answer is the length of the longest contiguous run containing one repeated character. Recomputing that answer by scanning the entire string after every replacement would be easy to understand, but with a long string and many queries it repeats almost all of the same work. A point replacement changes only one position. The useful goal is therefore to store summaries of string intervals and repair only the summaries whose intervals contain the changed position.

The solution uses a segment tree. Every tree node represents an inclusive, one-based interval `[l, r]` of the string. It records three measurements:

- `lmx` is the length of the longest same-character run that starts exactly at `l`, so it is the interval's uniform prefix length.
- `rmx` is the length of the longest same-character run that ends exactly at `r`, so it is the interval's uniform suffix length.
- `mx` is the length of the longest same-character run anywhere inside the interval.

These three values are enough because a run in a parent interval has only three possible locations: entirely inside the left child, entirely inside the right child, or crossing the single boundary between the children. The children's `mx` values handle the first two cases. Their boundary-facing suffix and prefix handle the crossing case.

**Build leaves first, then combine upward**

The `SegmentTree` constructor converts the immutable input string into `self.s = list(s)` because individual characters must later be replaced. It allocates `self.tr` with `4 * n` slots, a conventional safe capacity for a binary segment tree over `n` elements, and calls `build(1, 1, n)`. Tree node index `1` is the root.

At a leaf, `l == r`, so the represented interval contains exactly one character. Its longest prefix, suffix, and internal run all have length one. The `Node` constructor initializes `lmx`, `rmx`, and `mx` to `1`, which means leaf construction needs no additional assignments. For a non-leaf interval, `build` recursively creates the two children and then calls `pushup` to derive the parent summary.

The implementation uses one-based interval positions but stores characters in a zero-based Python list. Thus, character at tree position `p` is `self.s[p - 1]`. The boundary comparison in `pushup` follows this conversion exactly: `self.s[left.r - 1]` is the last character of the left interval, and `self.s[right.l - 1]` is the first character of the right interval.

**How two child summaries become one parent summary**

Suppose the left child covers `[l, mid]` and the right child covers `[mid + 1, r]`. The merge first assumes no run crosses their boundary:

- the parent's prefix length begins as `left.lmx`;
- its suffix length begins as `right.rmx`; and
- its best internal run begins as `max(left.mx, right.mx)`.

If the last left character and first right character differ, that assumption is final. A same-character substring cannot cross a boundary whose two adjacent characters are different.

If the boundary characters match, a crossing run exists. It consists of the left interval's longest uniform suffix followed immediately by the right interval's longest uniform prefix, so its length is `left.rmx + right.lmx`. The parent updates `mx` with the larger of its current value and this crossing length.

The parent's prefix cannot always be extended into the right child merely because the boundary matches. It reaches the boundary only when the entire left interval is one uniform run. The code computes the left interval length as `a = left.r - left.l + 1` and checks `left.lmx == a`. Only then does it add `right.lmx` to the parent's prefix. Symmetrically, the parent suffix extends into the left child only if the entire right interval is uniform, tested by `right.rmx == b`.

These conditions prevent a subtle overcount. For example, if the left interval begins with `a` characters but ends with `b` characters, a matching `b` at the right boundary may create a crossing run, yet it cannot extend the parent's prefix because the different character inside the left interval breaks continuity.

The merge accounts for every possible longest run. Runs contained in one child are represented by the child maxima; every run using positions from both children must cross their common boundary and is exactly captured by the left suffix plus right prefix when the boundary characters agree. Therefore, once both children hold accurate summaries, `pushup` produces an accurate summary for the parent. Leaves are accurate by definition, so building upward makes the root's `mx` the answer for the whole initial string.

**Repair only the path containing an update**

Each query provides a zero-based string index `x` and replacement character `v`. The public method calls `tree.modify(1, x + 1, v)` because the segment tree uses one-based coordinates. At an internal node, `modify` compares the target with the midpoint and descends into exactly one child. At the target leaf, it changes `self.s[x - 1] = v`. As recursion returns, every ancestor calls `pushup` again.

Nodes outside this root-to-leaf path represent intervals that do not contain the changed position, so none of their characters or summaries can have changed. Recomputing only the ancestors is sufficient. Since a balanced segment tree has logarithmic height, one replacement repairs only `O(\log n)` nodes rather than rescanning `n` characters.

After modification, the solution appends `tree.query(1, 1, len(s))`. The requested interval is the entire string, exactly matching the root interval, so `query` immediately returns the root's `mx`. The implementation's `query` method is not a fully general range-query combiner: it descends correctly when a requested interval lies wholly in one child, but it has no merge logic for a requested interval that straddles the midpoint. That limitation does not affect this solution because every actual call requests the complete root range and returns before descending.

The paired iteration `zip(queryIndices, queryCharacters)` processes the replacement index and character at the same query position together. Under the problem contract both collections describe the same number of queries. Each appended value reflects the string after that query, so the returned list preserves query order.

Updating a position to the character already stored there is harmless. The method still walks to the leaf and recomputes ancestors, but all summaries regain their existing values and the reported maximum remains correct.

## Complexity detail

Let `n` be the string length and `q` be the number of replacement queries. Building the segment tree creates `O(n)` nodes. Although the backing array reserves `4n` references, the recursive build visits only a linear number of actual intervals, and each `pushup` performs constant work. Initial construction therefore takes `O(n)` time.

A point modification follows one child at every tree level and then recomputes the same number of ancestors. The height is `O(\log n)`, so one `modify` call costs `O(\log n)` time. The subsequent whole-string `query` matches the root and costs `O(1)`. Across all queries, the total is therefore `O(n + q \log n)` time. Constructing the returned answer list adds `O(q)` append work, already dominated by that bound.

The tree array has `4n` slots, each constructed node stores a constant number of integers, and `self.s` stores `n` characters. These structures use `O(n)` space. The answer list uses `O(q)` output space. The manifest's `O(n)` space describes the data structure's working storage; if required output is counted as well, the total resident space is `O(n + q)`. Recursive build and update calls use `O(\log n)` stack frames, which remain below the linear tree storage.

The custom top-level `max(a, b)` shadows Python's built-in `max`. It compares exactly two integers and is always called with two arguments in this implementation. This choice does not alter any asymptotic bound, but it is part of the exact solution behavior.

## Alternatives and edge cases

- **Rescan after every query:** Replace the character and scan the string while counting consecutive equal characters. This is simple and uses little auxiliary space, but it costs `O(nq)` time in the worst case because every query revisits the entire string.
- **Store only one maximum per segment-tree node:** Child maxima alone cannot describe a run that crosses the midpoint. The prefix and suffix lengths are necessary connection information; omitting either makes an exact constant-time merge impossible.
- **Balanced ordered set of run boundaries:** One can maintain maximal equal-character intervals in an ordered structure, splitting and merging near an update while separately tracking run lengths. This can also be efficient, but it requires more intricate bookkeeping than the three-field segment-tree summary.
- **A Fenwick tree:** Fenwick trees are excellent when an aggregate has an invertible prefix operation such as addition. Longest equal-character runs need boundary-aware merging and cannot be recovered from a single scalar prefix aggregate, so a standard Fenwick tree is not a natural match.
- **Single-character string:** The tree consists of one leaf. Every replacement writes that leaf, the root `mx` remains one, and every answer is `1`.
- **All characters initially equal:** The root prefix, suffix, and maximum all equal `n`. Replacing a middle position with a different character breaks the run, and the ancestor merges correctly choose the longer remaining side.
- **An update joins two runs:** When the new character matches both neighbors, the relevant merge eventually uses a left suffix plus a right prefix, allowing one update to combine the two neighboring runs and the updated position into a larger run.
- **An update breaks a run:** Replacing a character inside a uniform interval causes affected leaves and ancestors to stop extending prefixes or suffixes through mismatching boundaries. Unaffected subtrees retain their summaries.
- **Repeated replacement with the same value:** There is no early-return optimization. The work remains `O(\log n)`, but the reconstructed summaries and answer are unchanged.
- **Index conversion:** Query indices are zero-based while tree positions are one-based. The exact `x + 1` on entry and `x - 1` when accessing `self.s` are both required; dropping either conversion would update the wrong character.
- **Whole-range query only:** The provided `query` is sufficient for this method's exact call `query(1, 1, len(s))`. It should not be reused as a general arbitrary-range longest-run query without adding a richer return summary and explicit cross-boundary merge.
- **Output order:** One result is appended immediately after each update. Even when multiple queries target the same index, the list records the state after each operation in the original order.
