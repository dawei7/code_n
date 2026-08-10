## General

**Build the square row by row from diagonal symmetry**

All words have the same length $L$, so a completed word square contains exactly $L$ rows. The defining condition is

`square[row][col] == square[col][row]`

for every coordinate. Once the first `d` rows have been chosen, this symmetry forces the first `d` characters of row `d`. Specifically, its character at column `i` must equal the character at column `d` of the already chosen row `i`.

The required prefix for the next row is therefore constructed as

`pref = [v[idx] for v in t]`,

where `t` is the current list of rows and `idx = len(t)`. Joining it gives

`t[0][idx] + t[1][idx] + ... + t[idx - 1][idx]`.

Any word that does not begin with this prefix can never extend the partial square, regardless of later choices. Backtracking only over matching words prunes those impossible branches immediately.

**Store prefix candidates in the trie**

Each trie node has 26 child slots, one for each lowercase letter, and a list `v` of input word indices. While inserting word index `i`, the code follows or creates the node for each successive character and appends `i` to that node's `v`.

Consequently, the node reached after prefix `p` stores exactly the indices of all words beginning with `p`. The list is attached at every prefix node rather than only at complete-word leaves, so a search need not traverse an entire subtree to collect candidates.

`search(w)` follows the characters of a requested prefix. If a child is absent, no input word has that prefix and it returns an empty list. Otherwise, after the final character it returns that node's candidate index list.

The trie shares nodes for common prefixes. For example, words beginning with `la` reuse the same `l` and `a` nodes, while their indices coexist in the relevant `v` lists.

**Explore all legal continuations**

The outer loop tries every input word as the first row by calling `dfs([w])`. This is necessary because the first row has no forced nonempty prefix, and any word may begin a square.

At recursive depth `idx`, the required prefix is derived from all current rows and looked up in the trie. For every returned index `i`, the corresponding `words[i]` is appended, recursion continues, and then `t.pop()` removes the trial row before the next candidate is tried. This append/recurse/pop pattern restores the exact prior partial square and is the essence of backtracking.

The same input word may be used multiple times. The code intentionally has no `used` set, and trie candidates remain available at every depth. This matches the contract.

When `len(t) == L`, all rows have been chosen. `t[:]` copies the current list into `ans`; copying is essential because later backtracking mutates `t`. Storing `t` itself would make previously recorded results change as rows are popped and appended.

**Why the prefix condition is sufficient**

Assume the current `d` rows already satisfy symmetry among all coordinates whose row and column are below `d`. A candidate for row `d` is selected only if its first `d` characters match `t[i][d]` for every earlier row `i`. Therefore every new pair `(d,i)` and `(i,d)` becomes symmetric.

Coordinates involving future rows are not yet known and impose no additional check now. By induction, after choosing all $L$ rows, every coordinate pair in the $L\times L$ matrix matches. The sequence is a valid word square.

Conversely, consider any valid square constructible from `words`. Its first row is tried by the outer loop. At depth `d`, validity forces its next row to have exactly the prefix computed by the algorithm, so that row's index appears in the trie result and its branch is explored. Induction shows the algorithm reaches and records every valid square. Thus the search is both sound and complete.

**Example of pruning**

Starting with `"ball"`, the next row must begin with `"a"` because `ball[1]` is `a`. If `"area"` is selected, the third-row prefix is `"le"`, formed from `ball[2]` and `area[2]`. The trie returns `"lead"`. The fourth-row prefix becomes `"lad"`, selecting `"lady"`. A choice such as a second row that makes prefix `"ll"` fails immediately when the trie has no such branch, so no deeper combinations are wasted on it.

**Why uniqueness and reuse do not conflict**

Input words are unique, so a sequence of word indices identifies one row sequence without duplicate dictionary entries creating duplicate paths. Reusing the same unique word at multiple row positions remains allowed because positions are separate choices. The algorithm follows exactly that interpretation.

## Complexity detail

Let $N$ be the number of words, $L$ their common length, and $P$ the number of partial-square states actually explored by DFS, including completed states. Trie insertion visits $L$ characters for each word and appends one index at each depth, taking $O(NL)$ time.

At a state of depth at most $L$, forming the forced prefix, joining it, and searching the trie each cost $O(L)$ in the worst case. Candidate-loop edges correspond to newly explored states. Including the $O(L)$ copy for each completed square, the output-sensitive search cost is $O(PL)$, so a sharp overall bound is $O(NL + PL)$.

The manifest's $O(NL^2 + PL)$ time is a conservative upper bound; because $L\ge1$, it safely includes trie preparation but is looser than the direct $O(NL)$ insertion analysis.

Across the trie, there are at most $O(NL)$ created nodes and exactly $NL$ index-list append operations. The current square, recursion stack, and temporary prefix use $O(L)$ additional working space. A sharp auxiliary bound excluding returned squares is therefore $O(NL + L)$. The manifest's $O(NL^2 + L^2)$ space is likewise conservative. The output itself requires $O(AL)$ references for $A$ returned squares, plus the existing word strings they reference.

The exponential nature is unavoidable in the output-sensitive sense: the number of valid squares and viable partial squares can itself be large. Here $L\le4$, making exhaustive prefix-pruned search practical.

## Alternatives and edge cases

- **Try every sequence of `L` words:** This explores $N^L$ combinations and checks symmetry only afterward. Prefix pruning rejects impossible sequences as soon as their next forced prefix has no candidate.
- **Scan all words for each prefix:** Backtracking remains correct but each state pays $O(NL)$ to find candidates. The trie changes lookup to $O(L)$ plus iteration over actual matches.
- **Prefix hash table:** Map every prefix directly to word indices. It offers fast lookup and similar storage; the trie shares common prefix structure and matches the exact solution.
- **Forbid reusing a word:** A `used` set would violate the contract and lose valid squares such as those containing the same word in multiple rows.
- **Store a completed `t` without copying:** Later `pop` operations would corrupt the recorded answer. `t[:]` freezes the row list for that result.
- **Word length one:** Each input word alone is a valid one-row square. DFS receives a length-one list and records it immediately.
- **No word for a forced prefix:** Trie search returns `[]`, naturally terminating that branch.
- **Several words share a prefix:** Every stored index is explored, ensuring that all valid continuations and outputs are found.
- **Any output order:** Trie insertion and input iteration determine a stable order, but the contract does not require sorting results.
- **Unique input words:** This prevents duplicate dictionary entries from generating identical search branches, though different valid row sequences are all retained.
