## General

**Why searching each word independently repeats too much work**

A direct strategy would run a separate board backtracking search for every word.
That is correct, but many dictionary words can share beginnings. Searching
`oath`, `oat`, and `oak` independently rediscovers the same paths for `o` and
`oa` three times. With up to $3 \cdot 10^4$ candidate words, that repeated work
is the central obstacle.

The exact solution combines every candidate in one trie. A trie node represents
a dictionary prefix, and each child edge adds one lowercase letter. During a
board walk, the algorithm advances through the board and trie together. The
moment the current board letters are not a prefix of any candidate, the trie
has no matching child and the search stops. This prefix pruning prevents the
backtracking from exploring paths that cannot produce an answer.

**Build one trie containing all candidate words**

Each `Trie` node has a 26-position `children` array and an integer `ref`.
Positions 0 through 25 correspond to `a` through `z`. A missing child is
`None`. The root represents the empty prefix.

To insert a word, `tree.insert(w, i)` starts at the root, converts each
character with `ord(c) - ord('a')`, creates a missing child when necessary,
and moves down that edge. At the final node, it stores `i` in `ref`. That
integer is the word's index in the original `words` list. The sentinel `-1`
means that no still-unreported candidate ends at this node.

Storing the index has two advantages. The DFS does not need to build a path
string during recursion, and when it reaches an ending it can recover the exact
candidate with `words[node.ref]`. Different words with shared prefixes reuse
the same initial nodes. If one word is a prefix of another, its endpoint can
have a nonnegative `ref` and also have children, so both words remain
representable.

**Start a trie-guided search from every board cell**

Any cell can be the first letter of a valid word, so `findWords` calls
`dfs(tree, i, j)` for every board coordinate. It does not precheck whether the
root has that letter; the first lines of `dfs` perform the same test. If the
corresponding trie child is absent, the call returns immediately after constant
work.

Inside `dfs(node, i, j)`, `node` represents the trie prefix matched before
using board cell `(i, j)`. The method converts `board[i][j]` to a child index.
If `node.children[idx]` is absent, appending this board letter would no longer
match any candidate prefix, so the entire branch is impossible. Otherwise it
moves `node` to that child. After the move, the trie depth agrees with the
number of board cells used in the current path.

**Report a word at its endpoint, but only once**

After advancing the trie, a nonnegative `node.ref` means the board path spells
one complete candidate. The solution appends `words[node.ref]` to `ans`, then
sets `node.ref = -1`.

Clearing the reference is safe because the output needs each candidate word,
not every board path that spells it. A word may appear along many routes or
from many starting cells, but after the first discovery all later visits to its
endpoint see `-1` and do not append a duplicate. The trie nodes and children
are not removed, so clearing an endpoint does not block a longer word that has
this word as a prefix. For example, after reporting `oat`, DFS can still follow
the endpoint's `h` child and report `oath`.

The implementation reads `words[node.ref]` before replacing the reference.
Reversing those two statements would attempt to read `words[-1]` and append
the wrong candidate.

**Mark the current cell to enforce single use**

A board cell may not occur twice in one word path. The DFS saves its character
in `c`, replaces `board[i][j]` with `'#'`, explores neighbors, and restores
the saved character afterward. Because valid board characters are lowercase
letters, `'#'` cannot be confused with real input.

Before recursing to a neighbor, the code checks `board[x][y] != '#'`. Every
cell on the active recursion path is marked, so this excludes the current cell
and every earlier cell in that same path. Cells used by a completed sibling
branch have already been restored, which is exactly what backtracking needs:
a cell cannot be reused within one candidate path but may participate in a
different path.

Restoration is mandatory. Without `board[i][j] = c` after exploring all
neighbors, a cell visited by one starting point would remain blocked for later
independent searches, causing valid words to be missed. The mutation is only
temporary; the caller receives the board in its original state when the method
finishes.

**Generate exactly the four legal neighbors**

The expression `pairwise((-1, 0, 1, 0, -1))` produces the offset pairs
`(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`: up, right, down, and left. The
repeated final `-1` closes the four-pair sequence. Diagonal offsets never
appear, matching the adjacency rule.

For each offset, the method computes `(x, y)` and checks both row and column
bounds before reading the destination. It also excludes currently marked
cells. Every remaining neighbor is passed to `dfs` with the already-advanced
trie node. The callee performs the prefix-child check, so the loop itself does
not need to convert the neighbor character or inspect the trie.

**Follow one representative discovery**

In the first example, begin at the top-left `o`. The root has an `o` child, so
the DFS advances and marks that board cell. One legal neighbor is the `a` to
its right. If the trie contains `oath`, the current trie node has an `a` child,
so recursion continues. From `a`, moving down to `t` and then left to `h`
follows the successive trie edges for `oath`. At `h`, the endpoint carries the
index of `oath`, so the word is appended and its reference is cleared.

Other moves are cut off as soon as a trie edge is missing. A tempting board
path beginning `oe`, for example, is not explored beyond `e` unless some
candidate begins with `oe`. After the `h` call returns, it restores `h`; each
earlier call restores its own cell in turn. The outer loops can then safely
start another search, eventually discovering `eat` without being affected by
the first traversal.

**Why every reported word is valid**

The DFS moves to a trie child only when the current board character labels that
edge, so its trie path spells exactly the sequence of chosen board letters.
Recursive moves are only horizontal or vertical, and marking prevents a cell
from appearing twice in the active path. A word is appended only at a trie node
whose `ref` was set at the end of an original candidate. Therefore every item
placed in `ans` is in `words` and has a legal board path.

**Why every valid candidate can be found**

Take any candidate that has a legal board path. The outer loops invoke DFS at
its first cell. Since the candidate was inserted, the root has the required
first-letter child. At every later cell, its next letter has the corresponding
trie child, the coordinate is an in-bounds orthogonal neighbor, and the legal
path never reuses a marked cell. Thus the recursion includes the entire valid
path and reaches the candidate's endpoint. It appends the word unless that same
word was already found through another path, in which case omitting a duplicate
is required. Hence the result contains exactly the candidates present on the
board, in an arbitrary permissible order.

Unlike the editorial's more aggressive version, the exact source clears only
terminal `ref` values; it does not delete trie branches after their words are
found. The duplicate suppression is present, while structural trie pruning is
not. The source also expects `List` and `pairwise` to be available in the
execution environment rather than importing them locally.

## Complexity detail

Let $m$ and $n$ be the board dimensions, $L$ the maximum candidate length,
$S$ the sum of all candidate lengths, and $T$ the number of created trie nodes.
Building the trie takes $O(S)$ time and $O(T)$ space, with $T \le S+1$.

There are $mn$ starting calls. From one start, the first cell can lead to at
most four neighbors. At later depths, the previously used cell is unavailable,
so a common tighter backtracking bound is $O(4 \cdot 3^{L-1})$ explored path
states. Trie prefix failures often prune much earlier, but the conservative
manifest-style bound is $O(mn4^L)$ for board search. Including construction,
total time is $O(S + mn4^L)$. Clearing found references improves repeated work
in practice but does not remove trie branches and does not change this worst
case.

The trie occupies $O(T)$ space. The recursive call stack and active board path
have depth at most $L$, because no trie path extends beyond the longest word,
so temporary search space is $O(L)$. Board marking uses the input matrix rather
than a separate visited set. Excluding the returned strings themselves, total
auxiliary space is therefore $O(T+L)$.

## Alternatives and edge cases

- **Run board DFS once per word:** This avoids a trie but repeats shared-prefix exploration for many candidates. Its cost grows with both the number of words and the board search space, which is especially poor when the dictionary is large.
- **Hash set plus prefix set:** Store complete words and every valid prefix, build the current path string during DFS, and stop when it is not in the prefix set. It recreates trie-like information with duplicated strings and extra path construction.
- **Delete exhausted trie branches:** After reporting a terminal word, recursively remove nodes that have no terminal reference and no children. The editorial uses this optimization to reduce later searches; it can be faster but requires careful parent bookkeeping and is absent from the exact source.
- **Separate visited matrix:** It preserves the board without temporary mutation but needs $O(mn)$ extra space or repeated allocation. In-place marking is safe because `'#'` is outside the lowercase board alphabet and every call restores its cell.
- **A word found along several paths:** Clearing `ref` after the first discovery ensures it appears only once in `ans`, even though later DFS calls can still traverse the same trie endpoint.
- **One word prefixes another:** Reporting the shorter word clears only its own reference. Its child edges remain available, allowing the longer word to be found in the same or a later traversal.
- **A board with one cell:** Each DFS either matches a one-letter trie endpoint or stops. There are no in-bounds neighbors, so longer candidates cannot be reported.
- **A one-letter candidate:** It is reported immediately after the DFS advances from the root to that letter's node; neighbor exploration may still continue for longer candidates sharing that prefix.
- **Repeated board letters:** Position, not character value, determines reuse. Different cells containing the same letter may both appear in one path, while the same coordinate cannot be revisited before restoration.
- **Duplicate candidate words:** The contract says `words` is unique. If duplicates were supplied, later insertion would overwrite the endpoint reference with the last index, and the result would still contain only one equal string because the reference is cleared after discovery.
- **No candidate begins with a cell's letter:** The outer loop still calls DFS, but its first child test returns immediately. No marking or neighbor exploration occurs.
- **No matches anywhere:** No endpoint reference is reached, `ans` stays empty, and all temporary board marks are restored normally.
- **Output order:** The nested board scan, neighbor offset order, and trie paths determine discovery order. The contract allows any order, so no sorting step is necessary.
