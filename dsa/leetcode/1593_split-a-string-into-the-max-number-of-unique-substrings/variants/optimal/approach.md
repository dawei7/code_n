## General

**Why the problem needs backtracking**

A split is determined by choosing cut positions between characters. For a string of length $N$, there are $N-1$ possible cut locations, so there can be $2^{N-1}$ partitions before the uniqueness rule is applied.

The validity of a next substring depends on the exact substrings already chosen, not merely on the current index. Two different partitions of the same prefix can leave different sets of forbidden substrings. The solution therefore performs depth-first search with a set `st` representing the current partition’s chosen pieces.

The small constraint $N\le16$ makes this exponential exploration feasible, especially with pruning.

**The recursive state**

`dfs(i)` means that `s[:i]` has already been split into the distinct substrings currently stored in `st`, and the search must partition the remaining suffix `s[i:]`.

At a given start `i`, every legal next piece must be a non-empty prefix of that remaining suffix. The loop tries all endpoints:

`for j in range(i + 1, len(s) + 1)`.

The candidate is `s[i:j]`. Starting at `i + 1` guarantees at least one character, and allowing `j == len(s)` includes the complete remaining suffix.

If the candidate is already in `st`, choosing it would violate global uniqueness within the current split, so that branch is skipped.

**Choose, explore, and undo**

For a new candidate, the source performs the standard backtracking sequence:

1. add `s[i:j]` to `st`;
2. call `dfs(j)` to split the suffix after the candidate;
3. remove `s[i:j]` from `st`.

The removal is essential. The set describes only the choices along the current recursion path. When control returns to try a different endpoint, the previous candidate is no longer part of that alternative partition and must not remain forbidden.

Python slicing creates the substring each time the expression appears. The exact source evaluates `s[i:j]` for membership and again for addition and removal on an accepted branch. The values compare by content, so each removal deletes the same textual substring that was added.

**Completing a partition**

When `i >= len(s)`, every source character has been consumed. Because candidates are always non-empty and adjacent recursive calls begin at the prior endpoint, their concatenation is exactly `s` with neither gaps nor overlaps.

At this base case, `len(st)` is the number of pieces in the completed partition. The assignment:

`ans = max(ans, len(st))`

records the largest valid count seen over all completed branches. `ans` is declared in the outer method and updated with `nonlocal ans` inside `dfs`.

The set size equals the number of pieces because every chosen piece is unique. If duplicates were allowed, a set would lose multiplicity and could not serve as the count, but the uniqueness constraint makes it exact.

**The pruning upper bound**

Before the base case, the function checks:

`if len(st) + len(s) - i <= ans: return`.

There are `len(s) - i` characters remaining. Even in the most optimistic possible split, every remaining character becomes its own one-character substring, so at most that many additional pieces can be created. Some may conflict with `st`, but no branch can exceed this upper bound.

Therefore:

$$
\lvert\texttt{st}\rvert+(N-i)
$$

is the largest count the current branch could possibly achieve. If it is no greater than the best `ans` already found, exploring the branch cannot improve the answer. Returning early is safe.

The use of `<=` is correct because the task needs only the maximum count, not a list of every partition tied for the maximum. A branch that can only equal `ans` offers no improvement.

Trying short substrings first often finds a high-count partition early, which raises `ans` and makes this bound more effective for later branches.

**Why every valid split is considered unless safely pruned**

Take any valid partition. Its first piece is `s[0:j]` for some endpoint in the root loop. Since the partition is unique, the candidate is not in the empty set and that choice is available. At the next recursive state, the partition’s second piece is one of the loop candidates and differs from the first, so that choice is also available. Continuing this way follows a search path matching the entire partition.

If that path is pruned, its theoretical maximum count is already at most `ans`, so it cannot establish a better result. Otherwise, it reaches the base case and its count is compared with `ans`. Thus every partition that could improve the answer is evaluated.

Conversely, every base case comes from non-empty contiguous slices that cover the string and were admitted only when absent from `st`. Every recorded count belongs to a valid unique split. The final `ans` is therefore exactly the maximum.

**Example intuition**

For `"aba"`, the branch `"a" | "b"` cannot choose `"a"` again for the last character, so it does not complete with three pieces. Other branches include `"a" | "ba"` and `"ab" | "a"`, both valid with two pieces. The search records two as the maximum.

## Complexity detail

Let $N$ be the string length.

There are $2^{N-1}$ possible cut patterns. The DFS may examine exponentially many partition states and candidate endpoints. In an abstract model with constant-time substring references and hashing, the commonly stated bound is around $O(N2^N)$ candidate work.

The exact Python source creates and hashes slices `s[i:j]`, and a slice of length $K$ costs $O(K)$. A conservative exact bound is therefore $O(N^2 2^N)$ time in the worst case. The pruning can dramatically reduce explored work in practice, but it does not improve the formal worst-case exponential class.

The recursion depth is at most $N$. At most $N$ substrings are stored in `st`, and because they form disjoint pieces of the current partition, their total character payload is at most $N$. Including temporary slices and the call stack, auxiliary space is $O(N)$ along one depth-first path.

## Alternatives and edge cases

- **Backtracking without pruning:** It is correct and simpler, but explores branches even when every remaining character as a singleton cannot beat the known best.
- **Dynamic programming by index alone:** It is insufficient because validity depends on the entire set of previously used substring values. A richer state would need to encode that configuration and becomes impractical.
- **Enumerate cut masks:** Each bit mask defines a partition, after which a set can test uniqueness. This is conceptually direct but repeats substring construction and cannot prune partial partitions as early.
- **Greedy shortest unused substring:** Choosing the shortest available piece may create conflicts later and miss a better global partition. Backtracking must reconsider endpoints.
- **All characters distinct:** Splitting into single characters gives $N$ unique pieces, the maximum possible.
- **All characters equal:** Single-character pieces repeat, so longer groupings are required. The search tests all such combinations.
- **One-character string:** The only candidate is the whole string; it reaches the base case with set size one.
- **Candidate equal to an earlier piece:** Membership rejects it even if it occurs at a different source position, because uniqueness is by substring content.
- **Backtracking removal:** Omitting `st.remove(...)` would leak choices between sibling branches and incorrectly reject valid partitions.
- **Empty substrings:** The endpoint starts at `i + 1`, so they are never generated.
- **Pruning equality:** A branch whose upper bound equals `ans` may be skipped because tied solutions do not change the requested maximum value.
- **Small constraint:** The exponential method is appropriate because $N$ is at most 16; it would not scale to strings of length $10^5$.
