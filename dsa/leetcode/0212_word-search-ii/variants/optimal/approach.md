## General
Searching each dictionary word independently repeats the same board exploration for shared prefixes such as `eat`, `eater`, and `eating`. Build one trie from all candidates so a board path is explored only while it remains a prefix of at least one word.

Store the complete word at terminal trie nodes rather than reconstructing it from the recursion path. Begin a backtracking search at every board cell, carrying the current trie node. If the cell's character has no child edge, stop immediately; no dictionary word can extend this board path.

After following a matching edge:

1. If the new trie node is terminal, record its stored word.
2. Temporarily mark the board cell as unavailable.
3. Recurse to its in-bounds up, down, left, and right neighbors.
4. Restore the original character before returning.

The temporary mark is path-local. It prevents reusing a cell within one word but restoration permits the same cell to participate in independent searches and different candidate words.

**Deduplication and pruning**

A word may be formable by several board paths but must appear once. Results can be stored in a set, or the terminal word can be cleared after first discovery. Clearing is often cheaper because later paths do not repeatedly report the same word while longer words below that terminal remain searchable.

After exploring a child, an implementation may delete its trie edge if the child has no remaining children and no terminal word. This pruning is optional for correctness but can greatly reduce later search work once all words under a prefix have already been found.

For the standard board, starting at `o` follows trie edges `o -> a -> t -> h` through adjacent distinct cells and records `oath`. A path beginning with a character absent from the root stops after one lookup. A diagonal `o -> t` is never considered, and a path cannot step back onto its temporarily marked cell.

Every recursive state corresponds to a path of distinct, four-directionally adjacent board cells, and its characters spell exactly the prefix represented by the current trie node. Therefore any terminal word recorded by the search has a valid board path and belongs to the dictionary. Conversely, consider any valid dictionary word and one board path spelling it. Its characters form a trie path, and the outer scan starts at its first cell. At every step the recursion includes the next adjacent cell, which is not yet marked on this valid path, so it reaches the terminal node and records the word. Deduplication changes only multiplicity, not membership.

## Complexity detail
Let the board be `m x n` and `L` the maximum candidate length. From each start, the coarse worst-case branching bound is $O(4^L)$, giving $O(mn4^L)$ time; after the first step, immediate backtracking is forbidden, so tighter practical branching is smaller, and trie prefix failures prune heavily. Building and storing the trie uses $O(T)$ for `T` total dictionary characters. Recursion and path marking use $O(L)$ stack depth beyond the trie and output.

## Alternatives and edge cases
- Searching each word separately repeats shared-prefix exploration and can be much slower for a large related dictionary.
- A permanent global visited set is incorrect because cells may be reused across separate paths; visitation belongs to one recursion path.
- A separate path-local visited set is correct but uses extra space compared with temporary board marking.
- One-letter words can match immediately. A word that is a prefix of a longer word and the longer word may both be found.
- Diagonal movement and cell reuse are forbidden, and each returned word appears once.
