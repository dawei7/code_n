## General

**Precompute combinations, then iterate by index**

The exact class does all combinational work in its constructor. It generates strings of the required length in lexicographic order and stores them in `self.cs`. Method `next` then returns one stored string and advances an index, while `hasNext` compares that index with the list length.

This design favors extremely simple query operations at the cost of potentially large initialization time and persistent storage.

**Backtracking decides include or exclude**

Nested function `dfs(i)` considers character position `i`. List `t` contains the characters selected so far.

If `len(t) == combinationLength`, a complete combination has been formed. The code joins `t` into a string, appends it to `cs`, and returns immediately. Returning prevents longer selections.

If `i == n` before enough characters have been chosen, no positions remain and the branch returns without output.

Otherwise, the function first includes `characters[i]`: append it, recurse on `i + 1`, and then pop it to restore the previous prefix. It next excludes that character and recurses on `i + 1`. The append-recursion-pop sequence is standard backtracking and ensures sibling branches do not contaminate one another.

**Why generation order is lexicographic**

The input characters are sorted and distinct. At the earliest position where two generated combinations differ, the branch that included the earlier character is explored before the branch that skipped it for a later character. Therefore all combinations beginning with a smaller possible character are completed before combinations beginning with a larger one.

The same include-first ordering applies recursively at every subsequent position. This produces lexicographic order directly, so neither `cs.sort()` nor reversal is needed.

For `"abc"` and length two, the traversal completes `"ab"`, then `"ac"`, then `"bc"`.

**Why every valid combination appears exactly once**

Every length-$k$ combination corresponds to one unique set of $k$ input positions. Along the recursion, its positions choose include and all other positions choose exclude, so that branch reaches and appends it.

Two different decision paths differ on at least one position and therefore select different character sets. With distinct characters, they cannot create the same string. Thus generation is complete and duplicate-free.

**Iterator methods after precomputation**

The constructor assigns `self.idx = 0`. `next` reads `self.cs[self.idx]`, increments the index, and returns the saved string. The contract guarantees callers invoke `next` only when valid, so no bounds guard is needed.

`hasNext` returns whether `self.idx < len(self.cs)`. It does not modify state, so repeated checks are harmless.

The nested DFS closes over `characters`, `combinationLength`, `n`, `t`, and `cs` from the constructor. These names remain available throughout recursive generation without becoming object fields. Only the finished combination list and iterator index need to persist after construction.

**Exact precomputation explores more than completed outputs**

Let $n$ be character count, $k$ the requested length, and $B=\binom{n}{k}$. The output contains $B$ strings. However, this include/exclude DFS also explores partial and failing branches. It has no pruning rule such as “remaining positions are fewer than characters still needed.”

In the worst case it can visit $O(2^n)$ decision states. For example, when $k=n$, only one complete combination exists, but branches that exclude a character continue to the end before failing. This matters when comparing the exact code with a generator that visits only useful combination states.

## Complexity detail

Joining each of the $B$ completed combinations costs $O(k)$, for $O(Bk)$ output-construction work. The include/exclude recursion visits at most $O(2^n)$ states. Exact initialization time is therefore $O(2^n+Bk)$.

The persistent `self.cs` list stores $B$ strings of length $k$, requiring $O(Bk)$ space. The recursion stack and working list use $O(n)$ and $O(k)$ space, respectively. Total space is $O(Bk+n)$.

This differs from the manifest's `O(k)` space claim: that bound fits an on-demand iterator storing only the current combination, not this precomputing source. After construction, `next` and `hasNext` each take $O(1)$ time and constant extra space.

## Alternatives and edge cases

- **Algorithm L on demand:** Store $k$ selected indices and advance to the next lexicographic combination in $O(k)$ time, using $O(k)$ space and no full output cache.
- **Pruned backtracking:** Stop when remaining positions cannot fill the combination. It avoids many doomed branches while retaining precomputation.
- **Bitmask enumeration:** Test all $2^n$ masks and retain those with $k$ bits. It is simple but also explores the full subset space.
- **Combination length one:** Results are the individual input characters in order.
- **Combination length equals input length:** Only the full string is output, though the exact unpruned DFS still explores many exclusion branches.
- **Repeated `hasNext` calls:** They do not advance `idx`.
- **Valid `next` guarantee:** The exact method would raise an index error after exhaustion, but the contract prohibits such a call.
- **Sorted distinct input:** Both lexicographic proof and duplicate freedom rely on this guarantee.
- **Precomputation latency:** Construction may be expensive even if the caller consumes only the first few combinations.
- **Persistent memory:** Returned strings remain stored after being consumed because `idx` advances without removing them.
