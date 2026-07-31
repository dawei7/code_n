## General

**Treat placeholders as dependencies.** Store every raw replacement value by key. When `%X%` appears inside another value, that value depends on the fully expanded form of `X`. The contract guarantees that these dependencies contain no cycle, so a depth-first expansion always reaches literal-only values.

Define an expansion operation for a key. Scan its raw value from left to right, copying maximal literal runs and recursively expanding the key between each matching pair of percent signs. Join those pieces and memoize the result. A later occurrence of the same key returns the memoized string instead of traversing its dependency subtree again.

Finally, apply the identical scanner to `text`. Its placeholders obtain the already defined key expansions, while underscores are copied as literals. Every placeholder is valid, so a closing delimiter and mapped key always exist.

When a key is memoized, all of its dependencies have already been completely expanded. Induction over the acyclic dependency graph therefore shows that every memo entry is placeholder-free and equals its recursive substitution. The final scan replaces each text placeholder with exactly that value, which produces the required fully substituted string.

## Complexity detail

Let $k$ be the number of keys, $L$ the total number of characters in the raw replacement values and `text`, and $E$ the final output length. Because `text` contains every key placeholder exactly once, the sum of all memoized expanded-value lengths is at most $E$. Each raw value is scanned once and each produced character is copied a constant number of times, giving $O(L+E)$ time.

The memoized strings use $O(E)$ total space, and the dictionary plus recursion stack use $O(k)$ space. Auxiliary space is therefore $O(E+k)$. The dependency depth is at most $k\le10$.

## Alternatives and edge cases

- **Repeated global replacement:** Repeatedly searching all strings for resolvable placeholders can rescan already processed text and duplicate dependency work.
- **Topological sorting:** Building the dependency graph and expanding keys in topological order is also valid, with the same output-sensitive bound, but requires explicit graph bookkeeping.
- **Expansion without memoization:** This is correct on an acyclic graph but may repeatedly expand a shared dependency for several parents.
- **Forward references:** Replacement list order has no semantic meaning; recursive lookup resolves a dependency even when its entry appears later.
- **Repeated placeholder:** Multiple appearances of the same dependency reuse one memoized expansion while still copying its text at every required position.
- **Literal-only mapping:** A value with no percent sign is copied directly and becomes an immediate memo base case.
- **Deep dependency chain:** Acyclicity guarantees termination, and the maximum stack depth is bounded by the ten keys.
- **Branching dependency graph:** A key may feed several parents; memoization ensures its expanded value is computed once.
- **Underscores in `text`:** They are ordinary literal separators and are preserved exactly.
