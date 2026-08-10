## General

**A valid piece is any nonempty trie path from the root.** A string is valid when it is a prefix of at least one word. This definition differs from the more familiar “complete dictionary word” condition. If `"abcdef"` is in `words`, then `"a"`, `"ab"`, and `"abc"` are all valid even if none appears as a separate word.

The source builds a trie containing every word. Each `Trie` node owns an array of 26 child references, one for each lowercase English letter. Inserting a word walks from the root through its characters, creating a missing node whenever necessary. No terminal marker is stored. That omission is deliberate: during a target scan, reaching any trie node means the characters traversed so far form a prefix of an inserted word and therefore constitute a valid piece.

Shared prefixes occupy shared nodes. For `"abc"` and `"aaaaa"`, the root has one `a` child, after which their paths branch as needed. This shares structural work and lets the algorithm test many possible piece lengths with one forward walk.

**Define a suffix state with one clear meaning.** The memoized function `dfs(i)` returns the minimum number of valid strings needed to form `target[i:]`. If `i >= n`, the suffix is empty, so zero more pieces are required. The desired answer is `dfs(0)`.

At a nonempty suffix, the code starts at the trie root and advances `j` from `i` toward the end of the target. If the child for `target[j]` does not exist, the loop stops. Extending farther cannot recover, because every longer candidate begins with the already-invalid character sequence. If the child does exist, moving to it proves that `target[i:j+1]` is a prefix of some word and is therefore a legal first piece.

For every such legal endpoint `j`, the candidate cost is one for the chosen prefix plus `dfs(j + 1)` for the remaining suffix. The source keeps the minimum over all endpoints:

$$
D(i)=\min_{j\text{ forming a trie path from }i}\left(1+D(j+1)\right).
$$

The initial answer is positive infinity. If no prefix path exists, or every possible first piece leaves an impossible suffix, the state remains infinite. After evaluating `dfs(0)`, the method converts infinity to `-1` as required by the contract.

**Why trying every matching prefix is necessary.** The longest currently valid prefix need not lead to the fewest pieces, because its endpoint may leave an impossible suffix. The shortest prefix may work but use unnecessarily many pieces. The recurrence explores every valid boundary and lets memoized suffix costs decide. For instance, two different prefixes starting at the same index can lead to completely different next letters; knowing only their length does not prove which boundary is globally best.

**Memoization removes repeated suffix work.** Many prefix choices can end at the same target position. Without `@cache`, each route would recursively recompute the same remaining suffix and the search could become exponential. Since a suffix's answer depends only on its start index, caching gives at most $n+1$ evaluated `dfs` states.

The custom top-level `min(a, b)` simply returns the smaller integer and shadows Python's built-in `min` name within this module. The recurrence calls it with `ans` and one candidate. This has no algorithmic effect, but it is part of the exact source. Likewise, `inf` and `cache` are expected to be available through imports or the execution harness.

**Why the answer is correct.** For any reachable index $i$, every loop iteration considered by the recurrence follows trie edges, so its chosen first substring is a valid prefix. Appending an optimal decomposition returned for the remaining suffix produces a legal decomposition, meaning the recurrence never underestimates the required number.

In the reverse direction, take any valid decomposition of `target[i:]` and look at its first piece ending at $j$. Because that piece is a prefix of some word, its characters form a root-to-node trie path, so the loop considers exactly that endpoint. The remainder is a decomposition of `target[j+1:]`, whose size is at least `dfs(j+1)`. Therefore the recurrence considers a candidate no worse than the chosen decomposition. Induction from the empty suffix proves `dfs(i)` is the exact minimum, and the infinity result exactly characterizes impossibility.

**Recursion depth is an implementation limitation.** The target length may reach $5000$. A decomposition into one-character pieces can create a chain of roughly $n$ nested `dfs` calls, which exceeds ordinary CPython's default recursion limit. The recurrence and complexity classification are sound, but this exact implementation may require a raised recursion limit or an iterative DP to be robust for every legal maximum-size input.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$

be the total input-word length, and let $T=\lvert\texttt{target}\rvert$. Trie construction touches each word character once and takes $O(S)$ time. Across memoized suffix states, the inner loop can walk as far as the end of the target for every start position. The worst-case sum is $T+(T-1)+\cdots+1=O(T^2)$, so total time is $O(S+T^2)$.

The trie contains at most $S+1$ nodes. Each node allocates a fixed 26-entry child array, which is a large constant but still $O(S)$ space. The cache holds $O(T)$ suffix answers, and recursion can use $O(T)$ stack frames. Thus auxiliary space is $O(S+T)$. These bounds match the manifest's asymptotic claims; the practical recursion-limit risk remains even though stack space is already counted.

## Alternatives and edge cases

- **Bottom-up dynamic programming with the same trie:** Compute the minimum pieces for every target prefix or suffix iteratively. It keeps the same $O(S+T^2)$ worst-case time and $O(S+T)$ space but eliminates Python recursion-depth failures.
- **Hash set of every valid prefix:** Materializing all prefixes as strings can duplicate characters and consume much more memory. A trie shares common paths and checks all prefixes from one start incrementally.
- **Greedily take the longest valid prefix:** This can strand the remaining suffix even when a shorter first piece leads to a complete or smaller decomposition. The dynamic program is needed to compare future consequences.
- **Checking only complete words:** That solves a different problem. Every node on an inserted word's trie path is valid, which is why the trie has no terminal requirement.
- **No root child for `target[i]`:** Then no valid piece can begin at $i$, `dfs(i)` stays infinite, and any earlier choice leading there is correctly rejected.
- **A word is longer than the remaining target:** Its shorter prefixes can still be used. Trie traversal stops at the end of the target without requiring the stored word to end.
- **Repeated words and shared prefixes:** Reinserting an existing path creates no duplicate nodes. Counts are irrelevant because validity depends only on whether at least one word has the prefix.
- **One-character valid pieces:** They guarantee reachability only for target letters that occur as the first character of some word. They may also produce recursion depth proportional to $T$.
- **Impossible target:** Infinity propagates backward through all candidate splits, and the final conversion returns `-1` rather than exposing the sentinel.
- **Lowercase-letter assumption:** `ord(c) - 97` and the 26-slot arrays rely on every input character being between `a` and `z`. The stated constraints guarantee safe indices.
- **Custom `min` name:** The module-level function intentionally shadows the built-in. Extending this source with calls such as `min(iterable)` would fail unless the helper were renamed or the built-in explicitly used.
- **Maximum input size:** The quadratic target scan is acceptable for the smaller “I” constraints only to the extent intended by the problem; the companion harder version requires a faster matching/covering method.
