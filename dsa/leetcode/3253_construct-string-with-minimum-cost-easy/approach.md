## General

Every operation appends one whole dictionary word. Therefore any successful construction partitions `target` into consecutive pieces, each equal to a word. The cost of a construction is the sum of the selected word costs. The problem is a shortest-path or minimum-cost prefix-partition problem.

The solution combines a trie with memoized suffix recursion. The trie lets it examine all dictionary words that match a target prefix without comparing every word separately at every position.

**Build the trie and keep only the cheapest duplicate.** Each `Trie` node has twenty-six child slots, one per lowercase letter, and a `cost` initialized to infinity. Inserting a word follows or creates the path for its letters. Only the terminal node receives a finite cost. If the same word appears more than once, `node.cost = min(node.cost, cost)` retains the cheapest occurrence. A more expensive duplicate can never help because it appends exactly the same text.

Internal prefix nodes remain at infinite cost unless that prefix is itself a complete inserted word. For example, inserting `"abc"` creates nodes for `"a"`, `"ab"`, and `"abc"`, but only the final node represents an available append operation unless shorter words were separately inserted.

Define `dfs(i)` as the minimum additional cost needed to construct suffix `target[i:]`, assuming the prefix before `i` has already been built. If `i >= len(target)`, no characters remain, so the cost is zero.

For a nonterminal position, traversal starts at the trie root and follows `target[i]`, `target[i+1]`, and so on. After reaching the node for `target[i:j+1]`, the candidate

`node.cost + dfs(j + 1)`

means append that matching word and optimally construct the remaining suffix. Taking the minimum over all matched trie prefixes gives the best first operation at position `i`.

If the required next trie child is absent, the helper immediately returns its current `ans`. No longer word can match from `i` after a shorter prefix has already failed, so stopping the scan is safe.

The `@cache` decorator stores one result per suffix index. Many segmentations can reach the same boundary `i`, but the optimal remaining cost depends only on that index, not on how the prefix was formed. Memoization prevents recomputing the same suffix problem exponentially many times.

For `target = "abcdef"`, traversal from zero finds `"abc"` as a finite terminal with cost one and can recurse at index three. From three, `"d"` costs one and recurses at four. From four, `"ef"` costs five and reaches the base case. Their total is seven. The trie may also expose other candidates, but the minimum recurrence selects this partition.

When no segmentation exists, every route eventually yields infinity. The top result `ans = dfs(0)` remains infinite, and the method converts it to minus one. If it is finite, it is returned unchanged.

**A subtle behavior of the exact expression.** Python evaluates `dfs(j + 1)` even when `node.cost` is infinity. Thus the source may recursively explore suffixes reached through trie prefixes that are not complete words. Those candidates can never improve `ans` because infinity plus anything is infinity. Guarding with `if node.cost < inf` before recursing would avoid such unreachable work and reduce call-chain risk. Memoization still bounds the number of distinct suffix states to $O(n)$, but the exact data flow is broader than only reachable construction boundaries.

**Why the recurrence is optimal.** Any valid construction of suffix `target[i:]` has a first appended word. That word must match some prefix ending at `j`, and the rest is a valid construction from `j+1`. The recurrence considers that terminal and combines its cost with the optimal cached remainder, so it is no worse than any valid construction. Conversely, every finite candidate consists of an available matching word followed by a valid recursive construction, so it describes a legal construction. Taking the minimum is exactly the optimum.

## Complexity detail

Let $n$ be the target length, let $S$ be the sum of all input-word lengths, and let $W$ be the maximum word length. Building the trie takes $O(S)$ time and creates $O(S)$ nodes in the worst case.

There are at most $n+1$ cached suffix states. From each `i`, trie traversal reads at most $\min(W,n-i)$ target characters before reaching maximum trie depth or a missing child. The time bound is $O(S+nW)$, which becomes $O(S+n^2)$ because $W\le n$. The manifest's $O(nS)$ is a looser bound if `S` denotes total dictionary characters; it is not the tightest description of the exact trie scan.

The trie uses $O(S)$ nodes, and the cache uses $O(n)$ entries. Recursive depth can reach $O(n)$, so total auxiliary space is $O(S+n)$. Each trie node also allocates a fixed twenty-six-slot child list, making the constant memory per node significant.

With target length up to two thousand, the exact recursive implementation may exceed Python's default recursion limit on a deep chain of suffix calls, especially because it calls `dfs` even at nonterminal trie prefixes. This is a genuine robustness concern. A bottom-up DP avoids it.

## Alternatives and edge cases

- **Bottom-up prefix DP:** Let `dp[i]` be the minimum cost to build the first `i` characters and traverse the trie forward from each reachable `i`. It has similar $O(S+nW)$ time, avoids recursion depth, and naturally skips unreachable boundaries.
- **Compare every word at every position:** Checking `target.startswith(word, i)` for all words gives a simpler DP but can cost $O(nS)$ character work. The trie shares common word prefixes.
- **Aho-Corasick plus shortest path:** A multi-pattern automaton can find all word occurrences efficiently and then relax prefix boundaries. It is more sophisticated and more useful in the harder version with larger data.
- **Keep all duplicate costs:** Duplicate words lead to identical transitions. Retaining only the minimum terminal cost is always safe and reduces useless candidates.
- **Target equals one word:** Its terminal candidate reaches the base case and returns that word's cheapest cost.
- **Repeated use of a word:** The recurrence may choose the same trie terminal at different target positions; operations are allowed any number of times.
- **Impossible first character:** The first trie lookup fails, `dfs(0)` returns infinity, and the method returns minus one.
- **A prefix exists but is not a word:** Its node cost is infinity. It can still be traversed to reach a longer terminal, but it should not by itself form an operation.
- **Several segmentations:** Memoization computes the cheapest suffix once, while the outer minimum compares all legal first words.
- **Positive costs:** There are no negative cycles or incentives to append extra text. Every valid construction ends exactly at target length.
- **Recursive depth:** A target made of many one-character pieces can create $O(n)$ nested calls and exceed the default Python limit; iterative DP is operationally safer.
- **Missing imports:** The source assumes `inf`, `cache`, and typing names are supplied by imports or the harness. A standalone file needs them explicitly.
