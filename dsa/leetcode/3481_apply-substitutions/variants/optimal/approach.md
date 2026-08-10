## General

**Interpret replacement values as recursively expandable text.** The source first creates dictionary `d` from each key to its raw replacement value. It then calls nested function `dfs` on the complete `text`.

`dfs(s)` searches for the first percent sign. If none exists, `s` contains no placeholder and is returned unchanged. It then searches for the next percent sign. Under the valid-input guarantee, these two delimiters surround one key. If a closing delimiter is unexpectedly absent, the source conservatively returns the text unchanged.

The key is extracted with `s[i + 1:j]`. Before inserting its value, the code recursively evaluates `dfs(d[key])` because that replacement may contain further placeholders. The source then concatenates:

- the literal prefix `s[:i]` before the placeholder;
- the fully expanded replacement; and
- `dfs(s[j + 1:])`, the fully expanded remainder after the closing percent sign.

This decomposition processes the first placeholder and delegates all later placeholders in the same string to the suffix recursion.

For `text = "%A%_%B%"`, the first call extracts `A`, expands `abc` directly, and recursively handles suffix `_%B%`. That suffix preserves its leading underscore, expands `B` to `def`, and returns `_def`. Concatenation gives `abc_def`.

For key `C` mapped to `abc%B%`, expanding `C` finds `B` inside its value, recursively obtains `ace`, and returns `abcace`. The top-level call can then place that completed value wherever `%C%` occurs.

**Acyclic dependencies guarantee termination.** View each key as a node with edges to keys mentioned in its replacement. The statement guarantees that this dependency graph has no cycle. Every nested replacement call therefore moves along a finite path and eventually reaches values without placeholders. Suffix recursion also consumes at least one complete placeholder from its current string. Together, these facts ensure recursion terminates for valid input.

If cycles were allowed, such as `A -> %B%` and `B -> %A%`, the function would recurse indefinitely because it has no visiting-state detection. Correctness relies on the explicit acyclic guarantee.

**Why every placeholder is replaced correctly.** Induct on dependency depth. A value with no placeholders is returned exactly. Assume all referenced keys at smaller depth expand to their correct completed values. For a string at the current depth, `dfs` preserves the literal prefix, replaces the first placeholder with the inductively correct expansion, and recursively expands every placeholder in the remaining suffix. The concatenation is therefore the fully substituted string. Applying the argument to `text` proves the returned result contains no placeholders and has every key occurrence replaced by its defined value.

Occurrences are handled independently. If `%A%` appears several times, each occurrence receives the same recursively computed characters, although the source recomputes them rather than sharing a cached result.

**The protected source does not memoize keys.** The manifest summary says each key's expansion is memoized. There is no cache or expanded-value dictionary in this implementation. Every call to `dfs(d[key])` expands that raw value again, even if the same key was expanded earlier elsewhere.

This distinction matters when one key is referenced many times or dependencies branch. For example, if several values each contain two occurrences of the next key, the recursive expansion tree can contain many repeated calls despite having only a few distinct keys. The constraints cap the mapping at ten keys, so the source can still be adequate, but its behavior is not the linear dependency-graph traversal advertised by the manifest.

**String construction is also material work.** Python strings are immutable. Slicing and `+` concatenation allocate and copy characters. The returned text itself may be much longer than the raw mapping because one placeholder can expand into a value containing several placeholders, each of which expands again. Any honest complexity description must account for this produced output rather than only the compact input graph.

The source does not modify `d` after construction, so raw replacement definitions remain available for every repeated expansion.

## Complexity detail

Let $R$ be the final output length, $C$ the number of placeholder occurrences visited in the full recursive expansion tree including repeated expansions of the same key, and $D$ the maximum dependency depth. At minimum, producing the answer requires $\Omega(R+C)$ work.

Because the source has no memoization, $C$ can be much larger than the number of distinct dependency edges. Immutable slicing and concatenation copy generated characters at successive recursion levels. A useful output-sensitive upper description is $O(DR)$ character-copy work plus the scans and slices used across the $C$ calls; in unfavorable concatenation shapes, repeated processing within a source string can approach quadratic work in that expanded piece. With at most ten dependency levels and very short raw values, these factors are bounded by the problem constraints, but the manifest's simple $O(L+E)$ memoized bound does not describe the exact source.

The final returned string requires $O(R)$ space. The recursion stack is proportional to nested dependency depth plus outstanding suffix-placeholder calls, and temporary expanded strings can add output-proportional memory. Peak auxiliary memory is therefore output-sensitive, commonly $O(R+C)$ under these small constraints, rather than merely $O(E+k)$ for a cached dependency graph.

A memoized implementation would expand each distinct key once and reuse its completed value, substantially reducing repeated dependency work. That is an alternative, not this protected code.

## Alternatives and edge cases

- **Memoize expansion by key:** This matches the manifest summary and avoids recomputing shared dependencies, but the protected source does not do it.
- **Topologically expand the dependency graph:** A dependency order can resolve each key once without recursion and detect cycles explicitly.
- **Repeated global string replacement:** Repeatedly scanning all keys and all text may do unnecessary work and requires careful termination logic.
- **Cycle detection:** It is unnecessary only because the input guarantees no cyclic dependencies; the source would otherwise recurse indefinitely.
- **Repeated key occurrence:** Every occurrence is expanded correctly but recomputed independently.
- **Several placeholders in one value:** The first-placeholder split plus suffix recursion expands all of them in left-to-right order.
- **Literal underscores:** They contain no percent signs and are preserved by prefix and suffix slicing.
- **Value without placeholders:** The first `find` returns $-1$, so it is returned immediately.
- **Nested dependencies:** `dfs(d[key])` completes the inner value before inserting it into its caller.
- **Unknown key:** Dictionary lookup would fail, but the statement guarantees every placeholder names a mapped key.
- **Unmatched percent sign:** The source returns the current string unchanged; valid inputs never require this fallback.
- **Output growth:** Branching replacements can make the result much larger than the raw input, so output size must appear in realistic complexity analysis.
- **Input preservation:** The mapping is copied into `d` and the immutable input text is never modified.
