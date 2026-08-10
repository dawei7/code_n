## General

**Use prefix states so every pattern choice becomes a table transition**

Define

$$
DP[i][j] = \text{whether } s[:i] \text{ is matched completely by } p[:j].
$$

`i` and `j` are lengths, not direct character indices. Therefore the newest string character is `s[i - 1]`, and the newest pattern character is `p[j - 1]`.

The desired answer is `DP[len(s)][len(p)]`. This definition includes empty prefixes at row `0` and column `0`, which are essential for describing zero occurrences of starred elements.

The selected `Solution` stores only three table rows in a ring:

```python
k = 3
result = [[False ...] for i in range(k)]
```

Logically the recurrence is the normal full two-dimensional DP. Physically, row `i` is stored at `i % 3`, because transitions need only the current text row and the immediately preceding one.

**Initialize how patterns match the empty string**

Two empty prefixes match:

```python
result[0][0] = True
```

A non-empty pattern can match an empty string only if every pattern element can occur zero times. The initialization scans pattern-prefix lengths from `2` onward:

```python
if p[i - 1] == '*':
    result[0][i] = result[0][i - 2]
```

If the prefix ends with `x*`, it can discard that pair and inherit whether the shorter prefix matched empty. Thus `"a*"`, `"a*b*"`, and `".*"` initialize to true, while `"a"` and `"a*b"` do not.

The pattern validity guarantee ensures every `*` has a preceding element, so subtracting two is meaningful.

**Transition for a normal literal or dot**

When `p[j - 1] != '*'`, the newest pattern element must consume exactly the newest string character. Two conditions are required:

1. the shorter prefixes already matched: `DP[i - 1][j - 1]`;
2. the current characters match: `s[i - 1] == p[j - 1]` or `p[j - 1] == '.'`.

The rolling-row code is

```python
result[i % k][j] = (
    result[(i - 1) % k][j - 1]
    and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
)
```

The dot still consumes exactly one character; it merely relaxes the equality test.

**Transition for a starred element**

When `p[j - 1] == '*'`, the repeated element is `p[j - 2]`. There are two exhaustive ways for the prefix match to end.

The star can represent zero copies. Remove `element*` from the pattern without consuming string input:

$$
DP[i][j-2].
$$

That state lies two columns earlier in the same current row, which has already been computed because `j` increases from left to right.

Alternatively, the star can account for the newest string character. This requires that `s[i - 1]` match the repeated literal or dot, and that the shorter string prefix already match the same full starred pattern:

$$
DP[i-1][j] \land \text{matches}(s[i-1],p[j-2]).
$$

Keeping the pattern length at `j` permits the star to consume additional characters. Combining the choices gives the exact assignment:

```python
result[i % k][j] = result[i % k][j - 2] or (
    result[(i - 1) % k][j]
    and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
)
```

Zero and one-or-more occurrences cover every possible repetition count.

**Why rolling rows do not lose needed information**

For a normal element, row `i` needs `DP[i - 1][j - 1]`. For a star, it needs `DP[i - 1][j]` and `DP[i][j - 2]`. No transition reads row `i - 2` or earlier.

The modulo ring keeps row `i - 1` distinct from row `i`. Three rows are more than sufficient—two would also work—but three still uses $O(n)$ pattern-width storage and makes every required previous row available.

Every column `j >= 1` in the current physical row is overwritten during the inner loop. Same-row `j - 2` entries have already been overwritten for this logical `i`, so stale data from an older row reuse cannot leak into the recurrence.

Column zero represents matching a non-empty string prefix with an empty pattern and must be false. Newly allocated rows `1` and `2` already contain false there. Before physical row zero is reused for `i >= 3`, the code executes

```python
if i > 1:
    result[0][0] = False
```

which removes the original empty/empty true value. All later reuses retain the correct false base.

**Trace the essential choices for `"aab"` and `"c*a*b"`**

- On the empty-string row, `c*` can be skipped, so its prefix is true; then `a*` can also be skipped, so `c*a*` is true for empty.
- For the first `a`, the `a*` state uses its consume branch: the preceding empty string matched `c*a*`, and `a` matches the repeated `a`.
- For the second `a`, the same column uses the previous text row and consumes another occurrence.
- When `b` arrives, `a*` cannot consume it, but the later literal `b` uses the diagonal normal transition from the state where `c*a*` matched both `a` characters.
- The final table state is true, so the pattern covers the complete string.

The DP does not commit greedily to a repetition count. The zero-copy and consume transitions preserve every count that can lead to a successful prefix.

**Why the final cell is exact**

The empty-prefix initialization is correct by direct inspection. Assume all states needed by `(i, j)` are correct. A normal element has exactly one legal way to finish: match the newest characters and rely on the shorter prefixes. A starred element has exactly the zero-copy and positive-copy cases encoded by the recurrence. These cases are mutually sufficient for the pattern grammar.

Filling rows by increasing `i` and columns by increasing `j` ensures every dependency is available. Therefore each stored state has the declared prefix meaning, and the final cell answers whether the whole pattern matches the whole string.

## Complexity detail

Let $m = \lvert s\rvert$ and $n = \lvert p\rvert$.

- **Time complexity: $O(mn)$.** The nested loops compute one state for every non-empty string prefix and non-empty pattern prefix. Empty-row initialization adds $O(n)$ work. Each transition performs constant comparisons and boolean operations.
- **Space complexity: $O(n)$.** The ring contains exactly three rows of `n + 1` booleans, for $3(n+1) = O(n)$ storage. Loop indices and `k` use constant additional space. The full logical DP has $O(mn)$ states, but earlier text rows are discarded once they can no longer be dependencies.

The extra `Solution2`, `Solution3`, and `Solution4` classes do not affect the selected entry point. `Solution2` uses a full $O(mn)$ table, while the others use different iterative/backtracking strategies.

## Alternatives and edge cases

- **Top-down memoized recursion:** Define suffix states and cache `(i, j)`. It mirrors the grammar clearly and takes $O(mn)$ time, but retains an $O(mn)$ cache and recursion stack.
- **Full bottom-up table (`Solution2`):** Easiest iterative form to visualize because logical and physical rows coincide. It uses $O(mn)$ space instead of rolling storage.
- **Uncached recursive matching (`Solution4`):** Direct but can revisit the same suffix combinations exponentially often and creates string slices.
- **Manual backtracking (`Solution3`):** Tracks starred fallback points explicitly. It is more difficult to prove and maintain than the DP recurrence.
- **Empty string prefix with `x*` chains:** The row-zero initialization repeatedly skips starred pairs, allowing patterns such as `a*b*` to match empty.
- **Empty pattern with non-empty string:** Column zero is false for every `i > 0`, enforcing full coverage.
- **Pattern with no stars:** Only diagonal transitions are possible; lengths and characters must align one for one, except that dot matches any character.
- **Zero star occurrences:** `DP[i][j-2]` skips the pair without consuming text.
- **Many star occurrences:** Repeated use of `DP[i-1][j]` consumes one matching character at a time while retaining the star.
- **Dot under a star:** `.*` can consume any number of characters because every current input character satisfies the repeated-element test.
- **Literal mismatch under a star:** The consume branch fails, but the zero-occurrence branch may still allow the rest of the pattern to match.
- **Whole-string requirement:** Only the cell containing both complete prefix lengths is returned; no successful internal or partial cell is enough.
- **Valid pattern guarantee:** A star never appears without `p[j-2]`, so no malformed-pattern branch is needed.
