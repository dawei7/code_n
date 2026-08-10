## General

There are two separate jobs:

1. discover every four-directionally connected island;
2. decide which discovered islands have the same shape under translation only.

The solution performs a deterministic depth-first traversal of each island and encodes the traversal—including backtracking—as a string. Equal translated shapes receive equal strings; rotations and reflections retain different strings.

**Discovering islands and marking cells**

The outer loops scan the grid row by row and left to right. When they encounter a `1`, that cell has not belonged to any earlier traversal, so it begins a new island.

Inside `dfs`, the statement `grid[i][j] = 0` marks the current land cell visited by turning it into water. This prevents the four-directional traversal from returning to the same cell and prevents the outer scan from starting the island again.

The method intentionally mutates `grid` instead of allocating a separate visited matrix.

The sequence `dirs = (-1, 0, 1, 0, -1)` encodes four neighbor offsets in a cycle. For `h` from `1` through `4`, the pair

`(dirs[h - 1], dirs[h])`

is respectively:

- `(-1, 0)`: up;
- `(0, 1)`: right;
- `(1, 0)`: down;
- `(0, -1)`: left.

This fixed order is essential: congruent translated islands must be explored in the same relative order.

**Encoding how DFS enters a cell**

The parameter `k` records the direction used to enter the current cell. A root call uses `0`. Recursive calls use `h` from `1` to `4`.

As soon as a cell is visited, `path.append(str(k))` records its entry direction. If two islands are translations of one another, their row-major first cells occupy the same relative position in the shape, and the deterministic neighbor order makes DFS take the same entry-direction sequence.

Entry directions alone are not sufficient, however. Different branching shapes can produce the same preorder directions if the signature does not say when one branch ends.

**Why exit markers are necessary**

After all reachable neighbors of a cell have been explored, the code appends `str(-k)`. This records that DFS is leaving the cell and backtracking over the same conceptual traversal edge.

For example, entering in direction `2` contributes `"2"`, and leaving that call contributes `"-2"`. The root contributes `"0"` on both entry and exit because negative zero is still zero when converted to a string.

These exit tokens preserve the nesting structure of the DFS tree. A direction explored as a child of the current cell can be distinguished from the same direction explored after returning to an ancestor.

Without exit markers, two different island shapes can share an entry preorder. With paired entry and exit events, the signature describes the entire ordered traversal structure.

**Why concatenating decimal tokens is unambiguous here**

Each direction code is one of `0`, `1`, `2`, `3`, `4` or its negative form. Positive and zero entry tokens are one character; negative exit tokens include a minus sign.

Because the code set is tiny and contains no multi-digit magnitudes, joining without separators does not create ambiguity such as confusing `1, 23` with `12, 3`. Every minus sign clearly begins one exit token.

**Translation invariance**

The signature contains directions and traversal structure, not absolute row or column coordinates. Moving an island the same number of rows and columns changes none of its relative neighbor relations.

The outer row-major scan starts each island at the first land cell in its topmost occupied row and, within that row, its leftmost cell. A translated copy has the same relative starting cell. Fixed up-right-down-left exploration then produces the same signature.

Thus translation-equivalent islands are inserted as the same string in `paths`.

**Why rotations and reflections remain distinct**

Direction numbers are tied to absolute grid directions. Rotating a shape changes up edges into right edges, for example, and reflecting it swaps left and right relationships. The resulting entry and exit codes generally change.

That is desired: the problem permits translation but explicitly does not treat rotations or reflections as equal.

**Managing the shared `path` list**

`path` is allocated once outside `dfs`. During one island traversal, recursive calls append all entry and exit tokens to it. When DFS returns to the outer loop, `"".join(path)` creates the complete immutable signature and inserts it into `paths`.

Then `path.clear()` removes the tokens in place before the next island. Clearing only after a whole traversal is important; clearing inside recursion would destroy the signature assembled by sibling calls.

A set keeps only one copy of each distinct string, so the final answer is `len(paths)`.

**Why the encoding characterizes shape**

If two islands are translations, the starting-cell and deterministic-neighbor arguments show that corresponding DFS calls have identical entry directions and identical child structure. Their entry/exit strings are equal.

Conversely, equal signatures describe identical ordered DFS trees with the same direction on every traversal edge. Starting both roots at relative coordinate `(0, 0)` and replaying those direction edges places corresponding cells at identical relative coordinates. Because DFS visits every island cell exactly once, the two relative cell sets match. Therefore, equal signatures imply translation-equivalent shapes.

This establishes both directions required for a valid shape key.

## Complexity detail

Let `R` be the number of rows and `C` the number of columns.

The outer scan inspects every cell. Each land cell is entered by DFS once because it is immediately changed to zero. For each visited land cell, four neighbor directions are checked. Total traversal time is

$$
O(RC).
$$

Joining and hashing signatures also takes time proportional to their lengths. Each land cell contributes one entry and one exit token to exactly one island signature, so the total signature length over all islands is `O(RC)`. This does not change the overall time bound.

The set can retain signatures whose total length is `O(RC)`. The active path list and recursion stack can each reach `O(RC)` for one large island. Auxiliary space is therefore

$$
O(RC).
$$

The grid itself supplies visited storage through mutation, but the stored signatures and recursion still require linear worst-case space.

## Alternatives and edge cases

- **Relative-coordinate sets:** Record `(row - origin_row, col - origin_col)` for each island and insert a `frozenset` of those offsets into the shape set. This is often easier to prove and has the same asymptotic bounds.

- **Sorted coordinate tuples:** Collect relative coordinates, sort them, and use the tuple as a hashable key. Sorting can add logarithmic work within islands.

- **Entry directions without exits:** This is insufficient because different branching structures can share the same preorder direction sequence. Backtracking markers are material, not decorative.

- **Single-cell islands:** Each receives the root entry and root exit signature `"00"`, so all isolated single cells form one shape class.

- **Touching diagonally:** Diagonal cells are never among the four generated offsets and therefore belong to different islands.

- **Translated copies:** Absolute locations never enter the signature, so they collapse to one set entry.

- **Rotated or reflected copies:** Absolute direction codes change, so they remain separate unless the shape itself is symmetric.

- **Grid mutation:** After the call, original land cells have become zero. A caller needing the grid later must pass a copy or use a visited set.

- **Recursion depth:** A long winding island can create `O(RC)` nested calls. An iterative traversal with explicit entry/exit frames avoids Python recursion-limit risk.

- **Direction order:** Every island must use the same neighbor order. Changing order between traversals would make equal shapes appear different.

- **Clearing at island boundaries:** `path.clear()` must occur after the signature is joined and inserted, never before or during DFS.

- **All-water grid:** No DFS begins, `paths` stays empty, and the method returns zero.

- **One enormous island:** Only one signature is inserted, regardless of its size, and the result is one.
