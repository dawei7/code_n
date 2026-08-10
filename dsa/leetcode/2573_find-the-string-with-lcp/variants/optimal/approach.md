## General

**A positive LCP forces equal first characters**

`lcp[i][j]` is positive exactly when the suffixes beginning at $i$ and $j$ share at least their first character. Therefore,

$$
\texttt{lcp[i][j]}>0
\quad\Longrightarrow\quad
\texttt{word[i]}=\texttt{word[j]}.
$$

These positive entries impose equality classes among string positions. The construction phase assigns one letter per implied class, choosing letters in the order `a` through `z`.

This condition alone is necessary but not sufficient. Equal first characters constrain an LCP to be at least one, but the exact LCP length depends on all following characters. The solution therefore constructs the lexicographically smallest candidate and then validates every matrix entry.

**Assign the earliest unfilled class the smallest letter**

The list `s` initially contains an empty string at every position. Variable `i` points to the earliest still-unassigned position. For the current letter `c`, the inner loop assigns `c` to every position $j\ge i$ with `lcp[i][j]` nonzero.

In a valid matrix, those positions must share their first character with position $i$. Assigning them together satisfies that required equality. Position $i$ itself should have `lcp[i][i] = n-i > 0`, so it is also assigned.

Before using the next letter, the `while` loop advances `i` past all positions already assigned. The next class representative is again the earliest unfilled position.

**Why this is lexicographically smallest**

At position zero, any valid string may rename its equality classes without changing the LCP matrix, because LCP depends on character equality rather than the particular letter names. Giving the first class `a` is therefore optimal.

After all positions in earlier classes are fixed, the earliest unassigned position must differ from those classes wherever its LCP entry with their representatives is zero. The smallest new letter available is the next alphabet letter. Assigning it there makes the earliest possible differing position as small as any valid string can make it.

Repeating this reasoning gives the lexicographically smallest canonical labeling of the equality classes.

If more than 26 distinct classes are required, the loop runs out of lowercase letters. Some entry of `s` remains empty, and `if "" in s` returns the required empty failure result.

**The exact LCP recurrence**

For any candidate string, suffixes at $i$ and $j$ obey:

$$
\operatorname{LCP}(i,j)=
\begin{cases}
0,&\text{if }\texttt{s[i]}\ne\texttt{s[j]},\\
1,&\text{if }\texttt{s[i]}=\texttt{s[j]}\text{ and an index is }n-1,\\
1+\operatorname{LCP}(i+1,j+1),&\text{otherwise.}
\end{cases}
$$

If the first characters differ, the common prefix has length zero immediately. If they agree, one character is shared, and matching continues with the two next suffixes. At the final row or column, only that one shared character remains, so the LCP must be exactly one.

**Validate every cell from bottom right**

The nested loops move both indices from $n-1$ down to zero. When validating `lcp[i][j]` for equal characters away from a boundary, `lcp[i+1][j+1]` is already an input value and does not need to be computed, but reverse order mirrors the recurrence and makes its dependency clear.

If candidate characters agree:

- a boundary entry must equal one;
- an interior entry must equal `lcp[i + 1][j + 1] + 1`.

If candidate characters differ, the matrix entry must be zero. Any violation returns an empty string immediately.

Checking every pair catches malformed diagonals, asymmetry, non-transitive equality claims, values that run past a suffix boundary, and exact-length inconsistencies. The construction phase may overwrite a character under contradictory positive relations, but validation rejects the resulting candidate rather than trusting those relations.

**Why validation proves existence**

If validation succeeds, the recurrence holds for every pair of suffix starts with correct boundary values. Starting at the bottom and following the diagonal recurrence shows that each matrix entry equals the actual number of consecutive equal candidate characters before the first mismatch or string end. Thus the candidate's true LCP matrix is exactly the input.

If the constructed candidate fails validation, could a differently named string work? No. The construction gives the canonical smallest labels to all equality relations forced by positive entries. Renaming letters cannot repair a contradiction in zero-versus-positive relations or in recurrence lengths. More than 26 forced classes also cannot be represented with lowercase English letters. Returning empty is therefore correct.

For the alternating sample, positive relations group positions $0$ and $2$, and positions $1$ and $3$. The first class receives `a` and the second `b`, producing `"abab"`. The recurrence then confirms all exact LCP lengths.

## Complexity detail

Let $n$ be the matrix dimension. The construction considers at most 26 letters and scans suffix positions for each new class, taking $O(26n)=O(n)$ under the fixed alphabet. The validation examines all $n^2$ matrix entries and dominates at $O(n^2)$ time.

The character list `s` uses $O(n)$ space and becomes the returned string. Apart from this output-building storage, only loop variables are used. The input matrix itself already occupies $O(n^2)$ space but is not copied or modified.

## Alternatives and edge cases

- **Union-find equality classes:** Positive entries can union positions, after which classes can be labeled. Full recurrence validation is still necessary, and the direct row-based construction is simpler here.
- **Trust only positive entries:** This misses exact LCP lengths and zero contradictions; construction without validation is insufficient.
- **Build an LCP matrix from the candidate:** Explicitly allocating another $n^2$ table works but is unnecessary because each input entry can be checked against its diagonal successor.
- **Invalid diagonal:** Every valid `lcp[i][i]` equals $n-i$. The recurrence checks this implicitly and rejects values such as a last diagonal entry greater than one.
- **Asymmetric matrix:** True LCP is symmetric. Contradictory entries cannot both satisfy the candidate recurrence, so validation rejects them.
- **More than 26 classes:** No lowercase string can represent them; an empty position after the letter loop signals failure.
- **Single character:** The only valid matrix is `[[1]]`, producing `"a"`.
- **All suffixes begin equally:** The construction uses one letter, and validation determines whether exact continuation lengths match an all-equal string.
- **Empty return ambiguity:** An empty string denotes impossibility; input length is at least one, so it is never a valid constructed word.
- **Lexicographic labels:** Actual letter identities do not affect equality, so assigning classes `a`, `b`, and onward in first-position order is minimal.
