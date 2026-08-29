## General

**Why synonym pairs must be connected transitively**

A pair says that two words are equivalent, but equivalence is transitive. If `happy` is paired with `joy` and `joy` is paired with `cheerful`, then all three words may replace one another even if `happy` and `cheerful` never appear together in an input pair. The algorithm must therefore find connected components in the undirected graph of synonym words.

The exact source uses a disjoint-set union structure, also called union-find. It first flattens all pairs with `chain.from_iterable(synonyms)`, turns the result into a `set` to remove duplicates, and converts that set to the list `words`. The list's initial order is arbitrary, but each word receives a stable integer index through `d = {w: i for i, w in enumerate(words)}`. Union-find operates on these small integer indices rather than on strings.

The arrays `p` and `size` initially make every index the root of a one-element component. `find(x)` follows parent links to the component root. Its recursive assignment `self.p[x] = self.find(self.p[x])` performs path compression: after finding the root, it points `x` directly at that root, shortening future searches. `union(a, b)` finds both roots and joins them if they differ. It attaches the smaller component beneath the larger one according to `size`; when sizes are equal, the first root is attached beneath the second. Union by size prevents tall parent trees, while path compression makes a long sequence of operations nearly constant time per operation.

After processing every pair, two words have the same union-find root exactly when a chain of synonym pairs connects them. This captures direct and indirect synonym relationships without repeatedly exploring the graph for every word in the sentence.

**Building sorted replacement groups**

The dictionary `g` maps each component root to a list of word indices. The loop over every index calls `uf.find(i)`, which also finishes compressing paths, and appends `i` to the proper group. Each group is then sorted with `g[k].sort(key=lambda i: words[i])`.

Sorting the groups is crucial. The earlier `set` deliberately discarded any predictable global order, so neither the indices nor the insertion order can be trusted for output ordering. Sorting by the actual word strings makes each position's replacement choices lexicographically ascending.

Words that never occur in `synonyms` are absent from `d` and do not need a one-element union-find component. They can only remain unchanged. This distinction keeps the structure limited to the vocabulary for which replacement choices actually exist.

**Generating the Cartesian product in sentence order**

The sentence is split on spaces into `sentence`. The recursive function `dfs(i)` decides which word will occupy position `i`. The list `t` holds the currently chosen prefix, and `ans` collects completed sentences.

If `sentence[i] not in d`, that word has no synonym component. The code appends the original word, recurses to the next position, and then pops it. If the word is known, the code finds its component root and tries every index `j` in the already sorted list `g[root]`. Each candidate `words[j]` is appended, the suffix is generated recursively, and the append is undone with `t.pop()` before the next candidate. This append-recurse-pop pattern is backtracking: it reuses one prefix list while exploring every combination.

When `i` reaches `len(sentence)`, all positions have been chosen. The code joins `t` with single spaces and appends the resulting sentence to `ans`. It does not return after any partial choice, so every combination of valid replacements is produced. It also produces no duplicates: each component contains each distinct word once, and each output corresponds to one unique choice at every position.

**Why the returned list is already lexicographically sorted**

Depth-first generation processes positions from left to right. At a replaceable position, it explores candidate words in ascending order and completely generates all suffixes for one candidate before moving to the next. At a fixed position, all sentences produced under an earlier candidate precede all sentences produced under a later candidate because their first differing word is smaller. Within one candidate block, the same argument applies recursively to the remaining positions. Fixed words create only one branch and cannot disturb the ordering.

This gives an inductive argument. The empty suffix has one correctly ordered result. Assuming `dfs(i + 1)` generates each suffix in order, `dfs(i)` concatenates those ordered suffix blocks in the sorted order of the word at position `i`. The concatenation is ordered and complete. Therefore `dfs(0)` appends all full sentences to `ans` in the required lexicographic order, and no final sort of `ans` is needed.

For the first example, `happy` belongs to the sorted group `cheerful, happy, joy`, while `sad` belongs to `sad, sorrow`. The traversal first fixes `cheerful` and emits both endings, then does the same for `happy`, and finally for `joy`. That is exactly the displayed six-sentence order.

## Complexity detail

Let $P$ be the number of synonym pairs, $V$ the number of distinct words in those pairs, $W$ the number of words in `text`, and $K$ the number of returned sentences. Building `words` and `d` takes $O(P+V)$ time and $O(V)$ space. The $P$ union operations take $O(P\alpha(V))$ amortized time, where $\alpha$ is the inverse Ackermann function and grows so slowly that it is effectively constant for realistic inputs.

Grouping all indices performs $V$ finds, taking $O(V\alpha(V))$ amortized time. If component sizes are $s_1,s_2,\ldots$, sorting costs $\sum s_i\log s_i$, at most $O(V\log V)$. The grouping arrays and dictionaries occupy $O(V)$ space.

Generation must materialize every answer. Under the problem's bounded word length, joining one $W$-word sentence costs $O(W)$, so producing $K$ sentences costs $O(KW)$. The visited recursion tree also has $O(KW)$ relevant prefix work in the usual output-sensitive accounting. Total time is therefore $O(P\alpha(V)+V\log V+KW)$, with the linear setup terms absorbed.

The union-find data, maps, and groups use $O(V)$ space. The recursion depth and working list use $O(W)$. The returned strings collectively require $O(KW)$ space when bounded word lengths are treated as constants. Since at least one sentence is returned, this includes the working $O(W)$ term, giving $O(V+KW)$ total space including output. Excluding the required output, auxiliary space is $O(V+W)$.

## Alternatives and edge cases

- **Graph search per component:** An adjacency list plus DFS or breadth-first search can also discover connected synonym groups in $O(P+V)$ time. It is perfectly suitable here, but union-find expresses repeated equivalence merging compactly.
- **Generate then sort all sentences:** Unsorted choices followed by `ans.sort()` are simpler to reason about, but sorting $K$ complete strings adds roughly $O(K\log K)$ comparisons on top of unavoidable generation. Sorting each small component once avoids that final cost.
- **Pairwise-only replacement is incorrect:** Considering only words directly paired with the current word misses transitive synonyms such as `happy` and `cheerful` connected through `joy`.
- **No synonym pairs:** `words`, `d`, and `g` are empty. Every sentence position follows the fixed-word branch, and the original text is returned as the sole result.
- **Text word absent from all pairs:** That position remains unchanged in every result, even though other positions may branch.
- **Repeated text word:** Each occurrence is a separate position and independently chooses from the same component, so all combinations are generated.
- **Redundant connectivity:** Unique pairs may still create cycles, such as three pairs connecting the same three words. `union` detects identical roots and does not duplicate component members or outputs.
- **Arbitrary set order:** The initial indices are nondeterministic, but sorting every completed group by `words[i]` removes that nondeterminism from the returned order.
- **Backtracking cleanup:** Every append is matched by a pop after recursion. Omitting a pop would leave a previous branch's word in the prefix and corrupt later sentences.
- **Short recursion depth:** The sentence contains at most ten words, so the recursive generator cannot approach Python's normal recursion limit.
