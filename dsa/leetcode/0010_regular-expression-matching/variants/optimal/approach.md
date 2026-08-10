## General

**Match suffixes, not isolated characters**

The match must cover all of `s`. It is not enough for the pattern to match a prefix or a substring. A useful state is therefore:

$$
\texttt{dfs}(i,j) = \text{whether } s[i:] \text{ is matched completely by } p[j:].
$$

The original question is `dfs(0, 0)`. Every recursive transition consumes characters from the front of one or both remaining suffixes. A state is identified only by the two indices; no substring copies are needed.

The two wildcard rules affect different units:

- `.` replaces exactly one input character;
- `*` does not stand alone—it modifies the immediately preceding pattern element and allows that element to occur zero or more times.

The pattern validity guarantee means that whenever the code sees `p[j + 1] == '*'`, `p[j]` is the valid repeated element.

**The exhausted-pattern base case enforces full coverage**

The first condition is

```python
if j >= n:
    return i == m
```

If the pattern suffix is empty, the only successful situation is that the string suffix is also empty. If `i < m`, unmatched input remains, so the result is false. If both indices are at their ends, every character and pattern element has been accounted for.

This is the point that distinguishes whole-string matching from a search. A partial match cannot return true merely because the pattern ran out.

**A direct element matches one current character**

When the next pattern element is not followed by `*`, exactly one input character must be consumed. The current positions match when

```python
i < m and (s[i] == p[j] or p[j] == '.')
```

The `i < m` check appears first, so short-circuit evaluation prevents an out-of-range `s[i]` access. A literal pattern character must equal `s[i]`; `.` accepts any one lowercase input character.

If the current characters match, the remaining question advances both indices:

```python
dfs(i + 1, j + 1)
```

If they do not match, the `and` expression becomes false immediately. There is no alternative way for a non-starred element to disappear or consume a different number of characters.

**A starred element has exactly two meaningful choices**

The code recognizes a starred element by looking one position ahead:

```python
if j + 1 < n and p[j + 1] == '*':
```

The pair `p[j:j+2]` can match zero occurrences or at least one occurrence.

The zero-occurrence choice skips both the element and its star without consuming input:

```python
dfs(i, j + 2)
```

For example, `c*` can disappear while matching `""`, or while allowing the later pattern to handle the current input.

The one-or-more choice is possible only if `s[i]` matches `p[j]`. It consumes one input character but keeps `j` unchanged:

```python
i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j)
```

Keeping `j` at the same starred element is what permits another occurrence. On the next call, the algorithm again chooses between stopping the repetition and consuming another match. This single transition represents one, two, or any larger finite number of occurrences through repeated calls.

The branches are joined with `or`:

```python
dfs(i, j + 2) or (matches_current and dfs(i + 1, j))
```

The match succeeds if any legal repetition count lets the remaining pattern cover the remaining string.

**Why the zero-occurrence branch is tried first**

Python evaluates `or` from left to right. The implementation first asks whether the rest of the pattern can succeed with zero repetitions. If it can, the second branch is skipped. If not, a matching input character is consumed and the starred element remains available.

This ordering does not change correctness because both possibilities are represented. It can reduce work for patterns where a starred element should be empty. Caching ensures that repeated states reached through different repetition choices are still solved only once.

**Trace `s = "aab"`, `p = "c*a*b"`**

The significant decisions are:

1. `dfs(0, 0)` sees `c*`. The current `a` does not match `c`, so only zero occurrences work: move to `dfs(0, 2)`.
2. `dfs(0, 2)` sees `a*`. It may skip or consume. Skipping cannot make the later `b` cover `"aab"`, so consume one `a` and stay at pattern index `2`: `dfs(1, 2)`.
3. The second `a` matches the same starred element, so consume again: `dfs(2, 2)`.
4. Now the current input is `b`. It does not match `a`, so the repetition must stop by taking the zero-occurrence branch to `dfs(2, 4)`.
5. Pattern `b` directly matches input `b`, leading to `dfs(3, 5)`.
6. Both suffixes are exhausted, so the base case returns true.

The example shows why “zero or more” is not a greedy one-time choice. The same `a*` state can consume until another part of the pattern needs to take over.

**Memoization turns the branching recursion into dynamic programming**

Without caching, different repetition histories can reach the same `(i, j)` pair and recompute its entire subtree. The decorator

```python
@cache
```

stores the boolean result for each argument pair. A later call with the same indices returns the stored value.

There are only `(m + 1) * (n + 1)` possible index pairs, including end positions. Not every pair must be reached, but none is evaluated more than once.

**Why the recurrence covers every valid match**

At a non-starred element, the pattern grammar permits exactly one action: match one current character and advance both positions. At a starred element, every legal match uses either zero occurrences or at least one; the recurrence includes both exhaustive cases. Consuming one occurrence and retaining the star recursively represents every positive count.

Each branch reduces the remaining problem by increasing `i`, `j`, or both, and the base case evaluates the only empty-pattern situation correctly. Therefore every returned true corresponds to a complete legal interpretation of the pattern, and every legal full match has a corresponding sequence of recurrence choices.

## Complexity detail

Let $m = \lvert s\rvert$ and $n = \lvert p\rvert$.

- **Time complexity: $O(mn)$.** At most $(m+1)(n+1)$ memoized states exist. Each state performs constant work aside from calls whose results are themselves separately counted. Short-circuiting may visit fewer states, but the worst-case bound is quadratic in the two lengths.
- **Space complexity of this exact implementation: $O(mn)$.** The cache may retain one boolean for every reachable `(i, j)` pair. The recursion stack can additionally reach $O(m+n)$ depth along a path, which is dominated by $O(mn)$ when both dimensions grow.

The branch manifest declares $O(n)$ space, a bound attainable with a rolling-row bottom-up DP such as the Competitive variant. It does not describe this top-down cached source, whose memo table is two-dimensional. The explanation reports the actual implementation cost.

## Alternatives and edge cases

- **Bottom-up full DP table:** Define prefix or suffix states and fill all $O(mn)$ cells iteratively. It avoids recursion but still uses $O(mn)$ space.
- **Rolling-row DP:** Each prefix row depends on the current row and one previous text row, so storage can be reduced to $O(n)$ pattern columns. This matches the manifest but requires careful handling of `*` and empty-prefix initialization.
- **Uncached recursion:** It mirrors the grammar directly but can explore exponentially many repetition choices and repeatedly solve identical suffix pairs.
- **Backtracking with mutable pointers:** A manual stack can try repetition counts, but it is easier to miss cases or revisit states exponentially. Memoized indices make overlap explicit.
- **Pattern with no `*`:** Every successful step advances both indices, so the strings must have equal length and each position must match literally or through `.`.
- **`.*`:** The repeated dot can consume any number of characters, including zero, so it can match any complete string suffix.
- **Star uses zero occurrences:** Patterns such as `a*b` can match `"b"` by skipping `a*`.
- **Star uses many occurrences:** `a*` matches `"aaaa"` by repeatedly taking the consume branch and then the skip branch at the end.
- **Empty remaining string:** A suffix can still match when the remaining pattern consists entirely of skippable `element*` pairs; recursive zero-occurrence branches discover that path.
- **Pattern exhausted first:** Returns false unless the string is also exhausted, preserving whole-string semantics.
- **Literal mismatch before a star:** The starred pair may still be skipped; a literal mismatch without a star has no valid transition.
- **Valid-star guarantee:** Looking backward from `*` never encounters a missing preceding element, so the recurrence does not need malformed-pattern validation.
