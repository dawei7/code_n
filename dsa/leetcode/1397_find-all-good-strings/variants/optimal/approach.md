## General

**Combine two independent constraints into one state**

Every counted string must satisfy both:

1. It lies lexicographically in the inclusive interval from `s1` through `s2`.
2. It never contains `evil` as a substring.

A position-by-position digit DP handles the lexical interval. A Knuth–Morris–Pratt, or KMP, automaton tracks how much of `evil` currently matches the suffix of the constructed prefix. The cached state combines these two pieces of information so the algorithm counts many strings without generating them individually.

Let $m=\texttt{len(evil)}$.

**Build the KMP prefix table**

`prefix[i]` is the length of the longest proper prefix of `evil[:i+1]` that is also its suffix. This tells the matcher where to resume after a mismatch.

For each index, `matched = prefix[index - 1]` starts from the best border of the previous prefix. While the next evil character does not match, `matched = prefix[matched - 1]` falls back to the next shorter viable border. If characters match, `matched` increases.

For a pattern with repeated structure, this avoids discarding all partial progress. If the constructed text has just matched a suffix that is also the beginning of `evil`, the automaton carries that useful overlap forward.

**Precompute every automaton transition**

The dynamic program will repeatedly ask: if the current matched-prefix length is `matched` and the next letter is `c`, what matched length results?

The `transitions` table answers that in constant time for every state from zero through $m-1$ and every lowercase letter. It applies the same KMP fallback loop, then increments if the next pattern character matches.

A result equal to $m$ means the appended letter completed `evil`. Such a transition is forbidden. The DP never recurses into a state $m$; it accepts only `next_matched < evil_length`.

State zero is safe: the fallback loop is skipped, and `evil[0]` is compared with the letter. Since `evil` is guaranteed nonempty, that index always exists.

**Meaning of the digit-DP state**

`count(position, matched, tight_low, tight_high)` returns the number of valid ways to fill positions from `position` through $n-1$, given:

- The already built prefix has length `position`.
- `matched` characters at the start of `evil` match the suffix of that prefix.
- `tight_low` says the prefix still equals `s1` so the next character cannot go below `s1[position]`.
- `tight_high` says the prefix still equals `s2` so the next character cannot exceed `s2[position]`.

These facts contain everything the future needs. The exact earlier characters no longer matter beyond their boundary tightness and KMP state.

**Choose the allowed character interval**

If the prefix is still tight to the lower bound, `low` is the code of `s1[position]`; otherwise it is `a`. Similarly, an upper-tight prefix uses `s2[position]`, while a prefix already below `s2` may use `z`.

The loop tries every character code from `low` through `high`, so both bounds are inclusive.

After choosing a letter:

- Lower tightness remains true only if it was true and the chosen code equals the current lower-bound character.
- Upper tightness remains true only if it was true and the chosen code equals the current upper-bound character.

The code compares with `low` and `high`. When a flag is already false, the leading Boolean `and` keeps it false; when true, those variables are exactly the corresponding bound characters. Thus the update is correct.

**Reject evil as soon as it appears**

The precomputed transition gives the new longest evil-prefix suffix. If it equals $m$, the newly appended character has completed an occurrence of `evil` ending at this position. The loop skips that branch permanently.

This immediate rejection is sufficient because any longer completion would still contain that forbidden substring. Conversely, if no transition ever reaches $m$, the completed string contains no occurrence.

**Base case, caching, and modulo**

When `position == n`, a full-length string has been built within the lexical bounds and no evil occurrence has been allowed. The state contributes one.

Many different prefixes lead to the same four-part state. `@cache` evaluates each state once and reuses its count, converting an exponential search tree into polynomial dynamic programming.

Each state's total is reduced modulo $10^9+7$. Modular addition is compatible with counting sums, so reducing intermediate totals yields the required final remainder without changing which branches exist.

**Why the algorithm is correct**

The tight flags admit exactly the strings in the closed lexical interval: they enforce the appropriate bound while equal and release it only after moving safely inside. The KMP state is exactly the longest suffix that could grow into `evil`, so filtering completion transitions excludes every and only string containing the forbidden pattern.

Every length-$n$ string in the interval corresponds to one unique sequence of loop choices. A good string reaches the base case once; a bad string is cut off at the first completed evil occurrence. Therefore the returned cached count is precisely the number of good strings modulo the required constant.

## Complexity detail

There are at most $n\cdot m\cdot2\cdot2=O(nm)$ cached DP states. Each tries at most 26 letters with constant-time table lookup, giving $O(26nm)$ DP time and $O(nm)$ cache space, matching the manifest.

The prefix table takes $O(m)$ time and space. Transition construction has $26m$ entries; the fallback loop can traverse several prefix links per entry, giving a straightforward worst-case bound of $O(26m^2)$ for this exact precomputation. Total time is therefore $O(26m^2+26nm)$; with $m\le n$ in many cases the DP term dominates, but the extra term is part of the exact code.

The transition table uses $O(26m)$ space. Recursive depth is $O(n)$, added to the $O(nm)$ cache. With $n\le500$, it normally remains below Python's default recursion limit.

## Alternatives and edge cases

- **Count up to a single bound twice:** Compute good strings at most `s2` minus those below `s1`. This uses one tight flag but needs a correct predecessor operation for `s1`.
- **Bottom-up DP:** Iterate positions and automaton states without recursion. It avoids call-stack limits but requires careful boundary-state layering.
- **Generate every string:** The interval can contain exponentially many strings and cannot be enumerated.
- **Naive suffix storage:** Keeping the entire built prefix makes states exponential; KMP compresses relevant history to at most $m$ values.
- **`evil` length one:** Any transition on that one letter reaches $m$ and is skipped; all other letters remain in state zero.
- **`s1 == s2`:** Tight flags force the one candidate string, which contributes either one or zero.
- **Every bounded string contains evil:** All branches are rejected and the result is zero.
- **Overlapping evil occurrences:** KMP fallback represents overlaps correctly, though the branch is rejected on the first complete occurrence.
- **Inclusive bounds:** Character loops include both `low` and `high`, so `s1` and `s2` themselves are eligible.
- **Completed pattern state:** It is never cached because transitions reaching $m$ are filtered before recursion.
- **Modulo timing:** Reducing each cached total is safe for addition and prevents unbounded count growth.
- **Generated-source note:** The local editorial is unavailable; the explanation follows the exact stored solution and its KMP/digit-DP invariants.
