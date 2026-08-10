## General

**Simultaneous replacement means all decisions use the original string**

Each operation is valid only when its source occurs at its index in the original `s`. A replacement may have a different length from its source, so applying operations one by one would shift later positions and violate simultaneity.

The optimal source handles this in two phases:

1. validate every operation against unchanged `s` and mark the valid starting positions;
2. scan the original string from left to right, emitting either a target or one unchanged character.

No replacement is written during validation, so one operation can never affect another operation's match test.

**Use an index marker array**

Let `n = len(s)`. Array `d` has one entry per original index and begins filled with `-1`. Its meaning is:

- `d[i] == -1`: no valid replacement begins at original index `i`;
- `d[i] == k`: valid operation `k` begins at index `i`.

The loop enumerates `zip(indices, sources)`, so `k` is the shared operation index into all three parallel arrays, `i` is its proposed start, and `src` is its required source text.

**Validate with `startswith`**

`s.startswith(src, i)` tests whether `src` occurs beginning exactly at `i`. It does not merely search for `src` somewhere later. It also returns false if the source would extend beyond the end of `s`.

When the test succeeds, `d[i] = k` records which target and source length belong at that position. When it fails, `d[i]` remains `-1` and that operation will do nothing.

All checks read the same original `s`. This directly implements the simultaneous-match rule.

**Build the result with an append-only scan**

The output pointer `i` starts at zero. At each step, the code checks whether a valid replacement begins at that original index.

The exact condition is `if ~d[i]`. Python's bitwise complement behaves as follows:

- when `d[i] == -1`, `~(-1) == 0`, which is false;
- when `d[i] == k >= 0`, `~k == -(k+1)`, which is a nonzero integer and therefore true.

Thus, this compact expression is equivalent to `if d[i] != -1`.

**Emit a target and skip its source**

When a marker `k = d[i]` exists, the output appends `targets[k]`. The original source characters must not also appear, so the pointer advances by `len(sources[k])`.

The target's length does not affect `i`. The pointer always measures positions in the original string, preserving the coordinate system used by all replacement operations.

For a valid replacement of `"a"` at index 0 by `"eee"`, the output gets three characters, but `i` advances by only one because one original character was consumed.

**Copy an unchanged character otherwise**

When `d[i] == -1`, no valid operation begins at that index. The code appends `s[i]` and advances by one.

A source belonging to an earlier valid replacement is never copied this way because the pointer jumped past all of its original positions. The non-overlap guarantee ensures that this jump cannot skip the start of another valid replacement that should also occur.

**Why an output list is used**

Python strings are immutable. Repeatedly concatenating a growing result can repeatedly copy its entire prefix. Appending pieces to `ans` is efficient, and `"".join(ans)` creates the final string once.

Pieces may be full targets or individual unchanged characters. Joining them in append order preserves original left-to-right order.

**Trace the second example**

For `s = "abcd"`:

- operation 0 checks `"ab"` at index 0 and succeeds, so `d[0] = 0`;
- operation 1 checks `"ec"` at index 2 and fails, so `d[2]` stays `-1`.

The construction sees a marker at 0, appends `"eee"`, and advances by source length 2 to index 2. There is no marker there, so it copies `c`, then `d`. The result is `"eeecd"`.

**Why the result is correct**

After validation, `d` records exactly the operations whose sources match the original string. During construction, every original index is handled exactly once: either it begins a valid source and the entire source interval is replaced by its target, or its character is copied unchanged.

Valid replacement intervals do not overlap, so these choices never conflict. Failed operations leave no marker and consequently change nothing. Targets are emitted at the position of their original sources, in increasing original-index order. This is exactly the simultaneous replacement result.

## Complexity detail

Let `C` denote the total character volume examined and produced: the original string, all source strings tested at their indices, and the final output.

Initializing `d` takes `O(n)` time. Across operations, `startswith` may compare up to the corresponding source length, so validation costs `O(\sum |source_k|)`. The construction consumes each original character once, either individually or inside a skipped valid source, and creates output pieces whose joined length is the result length. Total time is `O(C)`.

The marker array uses `O(n)` space. The output list and joined result use space proportional to the output character count. These are both bounded by `O(C)`, matching the manifest.

The scan never inserts into the middle of a string and never shifts stored indices.

## Alternatives and edge cases

- **Apply replacements from right to left:** Sorting valid operations by decreasing index and slicing can preserve earlier indices, but repeated immutable-string rebuilding may copy large portions many times.

- **Sort operations and stream directly:** This can avoid a full length-`n` marker array, but requires explicit ordering. The exact source uses direct index lookup during the scan.

- **Apply operations left to right on a changing string:** This is incorrect because earlier target lengths shift later original indices.

- **Source does not match:** No marker is written, so every original character remains available to be copied.

- **Source reaches beyond the end:** `startswith` returns false safely.

- **Target longer than source:** Append the full target but advance by the original source length.

- **Target shorter than source:** The same rule skips the complete source and emits only the shorter target.

- **Replacement at index zero:** The first construction step handles it normally.

- **Replacement ending at the final character:** The pointer advances to `n` and the scan ends cleanly.

- **No valid replacements:** Every marker remains `-1`, so the scan reconstructs `s` unchanged.

- **All operations valid and nonoverlapping:** Each target is emitted once and every source interval is skipped.

- **The `~d[i]` idiom:** Its truth depends on `-1` being the unique sentinel. An explicit comparison would be easier to read but behaves identically.

- **Input arrays remain unchanged:** Validation and construction only read the original strings and arrays.
