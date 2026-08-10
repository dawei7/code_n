## General

**Duplicates change the meaning of different index paths**

If all input values were distinct, choosing different indices at any position would necessarily create different permutations. With duplicates, two physical indices may contain the same value. For `[1a, 1b, 2]`, treating the two `1` copies as distinguishable would generate both `[1a, 1b, 2]` and `[1b, 1a, 2]`, even though both appear as `[1, 1, 2]` in the required output.

The solution still tracks physical indices so each input occurrence is used once, but it imposes one canonical order on equal occurrences. Sorting makes equal values adjacent. Along any recursion path, an earlier copy must be used before a later equal copy. This eliminates interchangeable index labelings while preserving every distinct value ordering.

**The duplicate-skip condition in plain language**

The loop rejects index `j` for either of two reasons:

- `vis[j]` is true, so that exact input occurrence is already in the partial permutation.
- `nums[j] == nums[j - 1]` and `vis[j - 1]` is false, so an equal earlier occurrence is still available and must represent this choice first.

The second rule is often misunderstood. It does **not** say “never choose adjacent equal values.” If the earlier copy is already used in the current path, `not vis[j - 1]` is false and the later copy is allowed. That is how a valid result can contain both `1`s.

At one recursion depth, after the branch using the earlier `1` has been fully explored and backtracked, that earlier flag becomes false. The later `1` is then skipped as a sibling first choice because it would generate exactly the same value suffixes. Thus the condition suppresses duplicate branches at each position while allowing multiplicity across positions.

**State and path invariant**

`dfs(i)` fills output position `i`. The preallocated list `t` has $n$ slots, and `vis` marks which sorted input indices have been used. At entry, `t[0:i]` contains the current prefix, exactly `i` flags are true, and equal selected occurrences respect their left-to-right canonical order.

For an allowed index `j`, the source writes `nums[j]` into `t[i]`, marks the index, and calls `dfs(i + 1)`. The child therefore has one more filled output position and one fewer available occurrence. After the child returns, clearing `vis[j]` restores the parent state.

The code does not clear `t[i]`. That is safe because the next allowed sibling overwrites the slot before recursion, and a result is copied only when all $n$ positions have been filled. The placeholder zeros and stale suffix entries are never interpreted as selections; `i` and `vis` define the active state.

**Why sorting is essential**

The comparison looks only at `j - 1`. It correctly represents “an equal earlier occurrence” only because sorting makes every copy of a value contiguous. Without sorting, equal values separated by other numbers would not be detected, and duplicate permutations could be generated.

Sorting also determines a deterministic traversal order, though the contract does not require the answers to be sorted. The selected source calls `nums.sort()`, so it mutates the caller's input order as part of preparation.

**Recording a complete permutation**

When `i == n`, every position has been written and every input occurrence has been used once. The source appends `t[:]`, an independent snapshot. Copying is mandatory because one shared `t` serves all branches; later overwrites must not alter previously recorded permutations.

The base case returns immediately. Backtracking in the parent then releases the final selected occurrence and explores the next canonical choice.

**Why no valid value permutation is lost**

Take any unique permutation of the input multiset. For each repeated value, assign its appearances in the desired output to that value's sorted input occurrences from earliest to latest. This produces a canonical sequence of physical indices. At every depth, when a later equal occurrence is needed, all earlier assigned copies have already been used, so the duplicate condition allows it. The search therefore contains a path for every distinct value permutation.

**Why no value permutation appears twice**

Suppose two search paths produced the same value sequence. At the first depth where their physical indices differ, they must choose different occurrences of the same value. One of those occurrences is later in the sorted equal-value group while an interchangeable earlier occurrence is unused on that branch. The skip condition forbids precisely that choice. Therefore, two canonical paths cannot yield the same sequence.

Every recorded path is also valid: usage flags prevent any physical occurrence from appearing twice, the path has length $n$, and all values come from the input. Completeness, uniqueness, and validity together prove correctness.

## Complexity detail

Let value frequencies be $f_1, f_2, \ldots$. The exact number of unique permutations is

$$
U = \frac{n!}{\prod_k f_k!}.
$$

Each result contains $n$ values, so copying outputs takes $\Theta(nU)$ time and result space. The search also scans up to $n$ candidate indices at internal states. In the worst case all values are distinct, $U=n!$, giving the manifest's $O(n \cdot n!)$ time bound. Sorting adds $O(n \log n)$ time and is dominated by enumeration.

The path, visited array, and recursion stack each use $O(n)$ space. Python's in-place sorting can use linear temporary memory in the worst case, which remains within $O(n)$. Required output storage is $\Theta(nU)$ and is excluded from the auxiliary-space figure.

## Alternatives and edge cases

- **Frequency-map backtracking:** Store each distinct value's remaining count and choose among keys. It removes occurrence labels entirely and naturally avoids duplicates, but needs a map and count restoration.
- **Depth-local set:** At each output position, remember which values have already begun a sibling branch. This works without the predecessor rule but allocates or clears additional sets throughout recursion.
- **In-place swapping with duplicate suppression:** Swap candidates into the current position and use a set to avoid equal swaps at that depth. It can remove `vis` but requires careful array restoration.
- **Post-generation set deduplication:** Generate all $n!$ labeled permutations and put tuples into a set. It is correct but wastes enormous work when multiplicities are high.
- **All values equal:** Only the earliest unused copy is allowed at each depth, producing exactly one permutation.
- **Earlier equal copy already used:** The later copy must be allowed; otherwise valid permutations containing multiple copies would disappear.
- **Single element:** One legal choice fills the path and records one result.
- **Negative values and zero:** Sorting and equality work identically; numeric sign has no special role.
- **Input mutation:** `nums.sort()` changes input order. A sorted copy would be needed if caller-visible preservation mattered.
- **Output order:** Canonical traversal happens to be lexicographic relative to sorted input, but only uniqueness and completeness are required.
