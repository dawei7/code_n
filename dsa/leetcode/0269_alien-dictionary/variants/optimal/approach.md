## General

**Treat letter order as a directed dependency graph**

The input does not directly reveal one alphabet string. It reveals comparisons between words that are claimed to be sorted under an unknown alphabet. Each trustworthy comparison can impose a rule of the form “letter `x` must come before letter `y`.” These rules are naturally represented as a directed graph: every distinct letter appearing in the dictionary is a vertex, and an edge `x -> y` means that `x` must precede `y` in any valid alien alphabet.

Once the graph has been built, the requested alphabet is a topological ordering of its vertices—an ordering in which every edge points from an earlier letter to a later letter. If the graph has a directed cycle, no such ordering exists, because following the cycle would require a letter to come before itself. The solution then returns the empty string.

**A word's internal letters do not create rules**

Seeing a word such as `"wrt"` does not imply `w < r < t`. Lexicographic sorting compares different words, not consecutive characters inside one word. The only reliable rules come from comparing words that occupy ordered positions in the given list.

It is enough to compare adjacent words. If the entire list is sorted, every adjacent pair must be in the correct order. Conversely, if every adjacent comparison is compatible with one letter order, transitivity makes all nonadjacent pairs compatible as well. Comparing every pair would add work without providing a fundamentally different source of constraints.

**Only the first differing position matters**

Consider adjacent words `first` and `second`. Scan their characters from left to right. Equal characters provide no new information: both words share that prefix, so the comparison has not yet been decided. At the first index where the characters differ, suppose `first` contains `x` and `second` contains `y`. Since `first` appears earlier in the sorted dictionary, the alien alphabet must place `x` before `y`, so the graph needs edge `x -> y`.

After that first difference, later characters must be ignored. Lexicographic order has already been decided at the earliest unequal position. Adding edges from later differences would invent constraints that the dictionary does not imply and could falsely make a valid input appear inconsistent.

For example, comparing `"wrt"` with `"wrf"` gives no rule from the shared `w` and `r`; the first difference is `t` versus `f`, so it gives only `t -> f`.

**Detect the invalid-prefix case separately**

There is one comparison that has no differing character but can still be invalid. If the second word is a strict prefix of the first, such as `"abc"` followed by `"ab"`, no alphabet order can justify that placement. Under lexicographic rules, a shorter word must come before a longer word when every character of the shorter word matches the longer word's prefix.

The exact solution loops across every position of the first word. If it reaches an index that does not exist in the second word before finding a difference, it returns `""`. This precisely detects a longer word followed by its own prefix. If the first word is shorter, its loop simply finishes after all shared characters match, which is valid and creates no edge. Equal adjacent words are also valid and create no edge.

**Record every appearing letter, including isolated ones**

The Boolean array `s` marks which of the 26 lowercase English letters appears anywhere in any word, and `cnt` stores how many distinct letters have been found. Most words are scanned while their adjacent comparison is processed; the final word is scanned separately because it never serves as the first member of a pair.

This node-discovery phase is necessary even for letters that participate in no edge. A letter appearing in a single word may have no known relationship to any other letter, but the returned alphabet must still contain it. Such a vertex is free to appear in any position consistent with the known edges; omitting it would produce an incomplete answer.

The `cnt == 26` checks only skip unnecessary discovery work after every lowercase letter has already been seen. They do not skip adjacent-word comparisons, so reaching all 26 letters cannot hide an ordering constraint or a bad prefix.

**Store constraints in a fixed adjacency matrix**

The solution maps `a` through `z` to indices `0` through `25` and uses a `26 x 26` Boolean matrix `g`. `g[u][v]` is true exactly when an extracted rule requires letter `u` before letter `v`. A Boolean matrix automatically deduplicates repeated evidence: assigning the same cell `True` several times still represents one graph edge.

Before adding `u -> v`, the code checks whether `g[v][u]` is already true. If so, there is an immediate two-letter contradiction, and it returns `""` early. This check is a useful shortcut, but it is not the complete cycle detector. A longer cycle such as `a -> b -> c -> a` may exist without any reverse edge pair. The later topological sort detects every cycle length.

**Compute indegrees without double-counting edges**

The indegree of a vertex is the number of distinct incoming edges it has. After all rules have been extracted, the solution scans the matrix. For every true `g[i][j]` connecting two letters that actually appear, it increments `indegree[j]` once.

Computing indegrees from the final Boolean matrix is important because the same rule can be inferred by several adjacent pairs. If indegree were incremented every time such evidence appeared, a duplicated rule could be counted twice even though only one edge would later be removed. The matrix collapses duplicates before the indegree count, keeping edge additions and removals balanced.

**Use Kahn's algorithm to assemble a valid alphabet**

Any vertex with indegree zero has no remaining prerequisite, so it may safely be the next letter in the alphabet. The solution initially enqueues every appearing letter whose indegree is zero.

It repeatedly removes one letter `t` from the front of the queue and appends it to `ans`. Placing `t` satisfies every outgoing rule `t -> i`, so the algorithm scans row `g[t]` and decrements each neighbor's indegree. If a neighbor's indegree becomes zero, all of its prerequisites have now been placed, and it joins the queue.

The key safety fact is that a letter is appended only when every incoming dependency has been removed by an earlier appended letter. Thus every produced edge has its source before its destination. The algorithm may have several zero-indegree choices simultaneously; selecting any of them is safe because there is no known rule requiring one of those currently available vertices to follow another.

**Use the processed-node count to recognize cycles**

If the graph is acyclic, it always has at least one zero-indegree vertex, and repeatedly removing such vertices eventually processes all `cnt` appearing letters. If a directed cycle exists, every vertex on that remaining cycle has an incoming edge from another remaining cycle vertex. None can reach indegree zero, the queue eventually empties, and fewer than `cnt` letters have been appended.

The final comparison `len(ans) < cnt` therefore distinguishes an impossible cyclic graph from a complete topological ordering. Returning `""` is correct in the cyclic case; otherwise, joining `ans` returns every appearing letter exactly once in a valid order.

**Trace the main example**

For `words = ["wrt", "wrf", "er", "ett", "rftt"]`, adjacent comparisons produce:

| Adjacent words | First difference | Edge |
|---|---|---|
| `wrt`, `wrf` | `t` versus `f` | `t -> f` |
| `wrf`, `er` | `w` versus `e` | `w -> e` |
| `er`, `ett` | `r` versus `t` | `r -> t` |
| `ett`, `rftt` | `e` versus `r` | `e -> r` |

The dependencies form the chain `w -> e -> r -> t -> f`. Initially only `w` has indegree zero. Processing it releases `e`, then `e` releases `r`, and so on, producing `"wertf"`.

For `["z", "x"]`, the only edge is `z -> x`, so the result is `"zx"`. For `["z", "x", "z"]`, the first pair gives `z -> x` and the second requests `x -> z`. The direct reverse-edge check detects the contradiction and returns `""`; the same graph would also fail topological sorting.

## Complexity detail

Let $c$ be the total number of characters across all words, let $a$ be the number of distinct appearing letters, and let $e$ be the number of distinct precedence edges.

Discovering letters scans each word once overall and costs $O(c)$. Adjacent comparisons can inspect long common prefixes, but each word except the last is the first word in only one comparison, so the total number of inspected first-word characters is also $O(c)$. Edge extraction therefore costs $O(c)$ time.

At the abstract graph level, Kahn's algorithm with adjacency lists costs $O(a+e)$ time and $O(a+e)$ space. Combined with extraction, that gives the manifest's $O(c+e)$ time—the $a$ term is bounded by $c$—and $O(a+e)$ auxiliary-space description.

The exact protected source uses a dense matrix over the fixed 26-letter alphabet instead. Building indegrees scans all $26^2$ cells, and processing a vertex scans a row of 26 cells. Thus its exact time is $O(c + 26^2 + 26a)$, which simplifies to $O(c)$ because 26 is a fixed constant. The arrays, matrix, queue, and answer hold at most 26-letter state, so auxiliary space is $O(26^2)=O(1)$ with respect to the input size.

If this exact matrix design were generalized to an alphabet of size $A$, its bounds would be $O(c+A^2)$ time and $O(A^2)$ space, not the sparse graph's $O(c+e)$ time and $O(A+e)$ space. The fixed lowercase-English contract makes the matrix both simple and efficient here, while the manifest expresses the more general sparse-graph complexity.

The returned string contains $a$ characters and takes $O(a)$ output space. Whether output storage is included or excluded does not change the fixed-alphabet asymptotic result for this problem.

## Alternatives and edge cases

- **Sparse adjacency sets:** Store only actual outgoing neighbors and increment indegree when a set gains a new edge. This gives the manifest's $O(c+e)$ time and $O(a+e)$ space for arbitrary alphabets, but the 26-by-26 matrix is straightforward and safely deduplicates edges under the fixed contract.
- **DFS topological sort:** Three-state graph coloring can detect a back edge and append vertices after exploring their dependencies. It has the same sparse asymptotic bounds, but its cycle reasoning and reversed finishing order differ from the exact queue-based source.
- **Compare every pair of words:** Nonadjacent comparisons are unnecessary because adjacent sortedness is sufficient and graph transitivity captures implied relations. Comparing every pair increases work and complicates extraction.
- **Infer rules from characters within one word:** This is invalid. A word's spelling does not say that each character precedes the next in the alphabet; only the first mismatch between ordered words carries comparison information.
- **Longer word before its prefix:** Inputs such as `["abc", "ab"]` are impossible regardless of the letter order. They must be rejected even though no mismatching character exists.
- **Shorter prefix first:** Inputs such as `["ab", "abc"]` are valid and add no edge. Prefix order alone already explains why the shorter word comes first.
- **Repeated identical words:** They add no edge and cause no prefix failure. Their letters still become graph vertices and must appear in the result.
- **Duplicate inferred edges:** Several pairs may imply the same rule. The Boolean matrix stores it once, so indegree is incremented once and later decremented once.
- **Direct contradiction:** If both `x -> y` and `y -> x` are inferred, the source rejects immediately. This optimization is sound because no linear alphabet can satisfy both inequalities.
- **Longer directed cycle:** A cycle involving three or more letters may evade the reverse-edge shortcut. Kahn's processed-count check is the definitive cycle test and rejects it.
- **Isolated letters:** A letter with no incident edge starts with indegree zero and is still appended. Its exact location may vary, which is allowed because the evidence does not constrain it.
- **Multiple valid orders:** When several letters have indegree zero, queue order selects one valid answer. The problem does not require the lexicographically smallest ordinary-English representation.
- **Single word:** There are no adjacent comparisons, so every distinct letter in that word is isolated. The source returns them in its zero-indegree initialization order, with each distinct letter appearing once.
- **Single distinct letter:** Repeated occurrences create only one graph vertex, no self-edge, and the result is that one letter.
