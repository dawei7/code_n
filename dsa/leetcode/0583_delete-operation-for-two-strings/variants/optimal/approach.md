## General

Only deletions are allowed. We cannot reorder characters, replace one character, or insert a missing character. After deletions, each original string leaves behind a subsequence, and the two remaining subsequences must be identical.

The solution uses dynamic programming directly on string prefixes. Define:

$$
f[i][j]
=
\text{the minimum deletions needed to make }
\texttt{word1[:i]}
\text{ and }
\texttt{word2[:j]}
\text{ equal}.
$$

The prefix lengths $i$ and $j$ range from zero through $m$ and $n$. Thinking in prefix lengths rather than raw indices gives clean empty-string base cases: the last character of a nonempty length-$i$ prefix is `word1[i - 1]`.

**Base cases**

If the second prefix is empty, every character in the first prefix must be deleted, so

$$
f[i][0]=i.
$$

Likewise,

$$
f[0][j]=j.
$$

The table is initially filled with zeros. The first loop writes the first column, and the second writes the first row. `f[0][0]` remains zero, which is correct because two empty strings already match.

These boundaries are not just initialization mechanics. Later states depend on cells above, left, and diagonally above-left, so the empty-prefix answers anchor the entire recurrence.

**When the final characters match**

For a state `f[i][j]`, the nested loops name the final characters `a = word1[i - 1]` and `b = word2[j - 1]`. If `a == b`, both strings can retain that shared final character. The earlier prefixes must then be made equal, costing `f[i - 1][j - 1]`:

```python
f[i][j] = f[i - 1][j - 1]
```

No new deletion is necessary for the equal pair. Keeping both is never worse than deleting one of them: a common final character can be appended to any equal result obtained from the shorter prefixes. Thus an optimal solution exists that preserves both matching characters.

**When the final characters differ**

If `a != b`, the two final characters cannot both remain as the final character of one common result. At least one must be deleted.

- Delete `a` from the first prefix. That costs one operation, leaving the problem represented by `f[i - 1][j]`.
- Delete `b` from the second prefix. That also costs one operation, leaving `f[i][j - 1]`.

The better choice gives:

$$
f[i][j]
=
1+\min\bigl(f[i-1][j],f[i][j-1]\bigr).
$$

There is no replacement branch because replacement is not an allowed step. There is also no need to delete both immediately: doing so is covered by taking one deletion now and allowing the chosen smaller state to make its own optimal next decision.

**Why the table is filled in this order**

The outer loop advances through `word1` and the inner loop advances through `word2`. Before computing `f[i][j]`:

- `f[i - 1][j]` belongs to the completed previous row;
- `f[i][j - 1]` was computed earlier in the current row;
- `f[i - 1][j - 1]` belongs to the previous row and column.

Every dependency is therefore ready. `enumerate(word1, 1)` conveniently yields prefix length `i` alongside character `a`, starting from one; the same applies to `word2`.

**Tracing `"sea"` and `"eat"`**

The dynamic program discovers that the common sequence `"ea"` can remain. Conceptually, deleting `s` from `"sea"` costs one and deleting `t` from `"eat"` costs one, for total two. The table does not need to reconstruct `"ea"`; it records only the smallest operation count needed for every prefix pair. The bottom-right cell `f[3][3]` is two.

For completely disjoint strings of lengths $m$ and $n$, no character can be kept in both, so all $m+n$ characters must be deleted. For identical strings, every diagonal comparison matches and the result remains zero.

**Why the recurrence is correct**

The base cases are forced because a nonempty string can equal an empty string only after deleting all of its characters.

For nonempty prefixes, consider their final characters. If equal, preserving the common character reduces the task to the two shorter prefixes without additional cost, and an optimal common result can include it. If unequal, any valid final equality must delete at least one of them. Deleting the first gives exactly the subproblem above; deleting the second gives exactly the subproblem to the left. Taking one plus the smaller covers the first deletion of every possible valid solution and selects the best one.

By induction over increasing $i+j$, each cell stores its defined minimum. Therefore, `f[m][n]` is the minimum deletions for the complete strings.

The same result can be connected to longest common subsequence length $L$: retaining an LCS means deleting $m-L$ characters from one string and $n-L$ from the other, totaling $m+n-2L$. The direct DP reaches that number without separately computing $L$.

## Complexity detail

There are $(m+1)(n+1)$ table cells. Initialization takes $O(m+n)$ time, and the nested loops compute $mn$ interior cells with constant work each. Total time is $O(mn)$.

The exact source allocates the full matrix `f` with $(m+1)(n+1)$ integers, so its auxiliary space is $O(mn)$. This differs from the manifest’s $O(\min(m,n))$ space declaration. That smaller bound is achievable with rolling rows, because each state needs only the previous row and current row, but the exact protected implementation does not perform that compression. Its actual space must be documented as $O(mn)$.

At the maximum lengths 500 and 500, the table has 251,001 cells, which is reasonable for the stated constraints even though Python integer/list overhead is larger than a raw numeric array in lower-level languages.

## Alternatives and edge cases

- **Rolling-row dynamic programming:** Keep only the previous and current row, arranging the shorter string along the row dimension. This retains $O(mn)$ time and achieves the manifest’s $O(\min(m,n))$ space.
- **One array updated in place:** Preserve the old diagonal value in a temporary variable while overwriting a single DP row. It uses even less constant overhead but is easier to implement incorrectly.
- **Longest common subsequence:** Compute LCS length $L$ and return $m+n-2L$. It has the same core recurrence and gives another useful proof of the formula.
- **Memoized recursion:** Express the same prefix decisions top-down. It avoids computing unreachable states in some inputs but uses a cache and recursion stack and can be less predictable in Python.
- **Naive recursion:** Branching whenever characters differ repeats the same prefix states exponentially and is unsuitable at length 500.
- **Identical strings:** Every corresponding final pair matches, so zero deletions are needed.
- **No common characters:** Every character in both strings is deleted, giving $m+n$.
- **One-character strings:** Equal characters cost zero; unequal characters require deleting both eventually, costing two.
- **Repeated characters:** The DP considers ordering through prefixes and chooses which occurrences to retain; a frequency-only method would be wrong because subsequence order matters.
- **Deletion only:** A mismatch costs one now and another later if necessary. Treating it as a one-step replacement would solve a different edit-distance problem.
- **Empty-prefix states:** Although the public constraints make complete inputs nonempty, empty prefixes are indispensable subproblems and must be initialized correctly.
- **Space-claim fidelity:** The two-dimensional list visible in the source is decisive evidence of $O(mn)$ space; rolling-space complexity belongs only to an alternative implementation.
