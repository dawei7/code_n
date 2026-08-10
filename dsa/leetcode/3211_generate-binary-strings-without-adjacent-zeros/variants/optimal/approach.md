## General

**Simplify the validity rule.** A length-two binary substring fails to contain at least one `"1"` only when it is `"00"`. Therefore a valid length-$n$ string is exactly a binary string with no adjacent zeros.

This is a prefix-local restriction. Whether zero may be appended depends only on the immediately preceding character, while one is always safe. Backtracking can build strings from left to right and reject an invalid branch before completing it.

**Maintain one mutable prefix.** The list `t` contains the characters selected for positions $0$ through $i-1$ when `dfs(i)` begins. Lists support efficient append and pop operations, unlike repeatedly creating longer immutable strings at every internal node.

At position `i`, the loop tries `j=0` and then `j=1`:

- zero is allowed when `i == 0` or `t[i - 1] == "1"`;
- one is always allowed.

The condition in the source,

`(j == 0 and (i == 0 or t[i - 1] == "1")) or j == 1`,

encodes exactly those two rules. If the character is legal, it is appended, recursion fills the next position, and `t.pop()` restores the prefix for the next choice.

**Why backtracking restoration matters.** The same list object is shared by every recursive frame. After exploring strings beginning with one choice, that choice must be removed before exploring its sibling. Otherwise characters from the first branch would remain and corrupt indices or produce strings longer than $n$. Append-recursively-pop establishes the invariant that `len(t) == i` whenever `dfs(i)` begins.

**Emit only at complete length.** When `i >= n`, the prefix has exactly $n$ characters. `"".join(t)` creates an immutable string snapshot and appends it to `ans`. Saving the joined string rather than the mutable list prevents later pops from changing an already emitted result.

The function then returns immediately, so it never tries to append beyond the requested length.

**Why every emitted string is valid.** Initially the prefix is empty and valid. Appending one cannot create `"00"`. Appending zero is permitted only at the first position or after one, so it also cannot create `"00"`. Every recursive prefix is therefore valid by induction, and every completed emitted string is valid.

**Why every valid string is emitted.** Take any valid binary string of length $n$. At each position, the loop tries its actual bit. A one is always accepted. A zero in that string is either first or follows one, because the string has no adjacent zeros, so the zero branch is accepted too. The recursion follows all its positions and emits it. Different strings differ at a first position and therefore follow different branches, so no result is duplicated.

Together, these arguments show the output contains exactly all valid strings.

**Trace $n=3$.** At the root, zero leads to prefix `"0"`. Another zero is forbidden, so the next character must be one, after which both zero and one are allowed; this yields `"010"` and `"011"`. Starting with one allows both second characters. Prefix `"10"` must finish with one, giving `"101"`, while `"11"` can finish with zero or one, giving `"110"` and `"111"`.

The loop tries zero before one, so this implementation happens to produce lexicographic order. The problem accepts any order, and correctness does not rely on this incidental ordering.

**Output size determines the running time.** Let $V_n$ be the number of valid length-$n$ strings. These counts follow a Fibonacci recurrence: a valid string ending in one may extend any valid length-$(n-1)$ string, while one ending in zero must extend a string ending in one. The total is $V_n=F_{n+2}$ under the usual $F_1=F_2=1$ indexing.

No algorithm can return all $V_n$ strings without writing $nV_n$ characters. The backtracking prunes only invalid prefixes and performs work proportional to the valid output tree.

## Complexity detail

Joining `t` costs $O(n)$ for each of the $V_n$ emitted strings, so output construction takes $O(nV_n)$ time. Internal valid-prefix nodes add $O(V_n)$-scale work and do not change the bound. This matches the manifest.

The recursion depth and mutable path each use $O(n)$ auxiliary space. The returned list and its strings require $O(nV_n)$ output space. The manifest's $O(n)$ space is correct only under the convention that required output storage is excluded; total live memory including `ans` is output-sized.

With $n\le18$, recursion depth is safe and the maximum output remains manageable. The method receives only integer `n` and mutates no caller-owned collection.

## Alternatives and edge cases

- **Enumerate all $2^n$ bit strings:** Filter those lacking `"00"`. It is simple but explores invalid branches that prefix pruning rejects immediately.
- **Iterative generation:** Start with `[""]` and append legal next bits to every current prefix. It avoids recursion but stores an entire frontier in addition to final outputs.
- **Dynamic programming for only the count:** Fibonacci DP returns $V_n$ in $O(n)$ time, but it does not satisfy the requirement to list the strings.
- **Start with zero:** The next position, if any, is forced to one.
- **Start with one:** Either bit may follow.
- **$n=1$:** Both `"0"` and `"1"` are valid because no length-two substring exists.
- **All ones:** Always appears because the one branch is never restricted.
- **Alternating starting with zero:** Always valid and appears through alternating forced/optional decisions.
- **No adjacent-zero post-check:** None is needed because invalid prefixes are never created.
- **Any-order contract:** Zero-first branching yields lexicographic order, but callers must not require that beyond this source's current loop order.
- **Mutable path snapshot:** Joining at the leaf is essential; appending `t` itself would store multiple references to one list that backtracking later changes.
- **Positive-$n$ guarantee:** The source would emit the empty string for $n=0$, but that case is outside the contract.
