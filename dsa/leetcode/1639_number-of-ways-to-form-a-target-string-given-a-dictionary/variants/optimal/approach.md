## General

**Compress each dictionary column into character counts**

Once a source column is used, all earlier columns become unavailable across every word. Therefore the important global order is the column index, not which word was chosen previously.

For each column `j`, the source counts how many dictionary words contain each lowercase letter there. `cnt[j][c]` is the number of distinct choices for taking character code `c` from column `j`.

The nested preprocessing loops visit every character of every word. If five words contain `'a'` at column 3, then choosing column 3 for an `'a'` target character has five different ways, one for each word. After that choice, future characters may come from any word at later columns, including the same word, exactly as the contract allows.

This frequency compression removes the word identity from the dynamic-programming state while preserving the number of choices.

**Define a suffix-counting state**

The cached function `dfs(i, j)` counts ways to form target suffix `target[i:]` using only dictionary columns from `j` onward.

This state captures everything future decisions need:

- `i` says which target character must be formed next;
- `j` says the first still-usable source column.

Past word selections do not matter because each later column can again choose from all words. Past source columns do not matter because they are permanently forbidden and summarized by `j`.

**Base cases**

If `i >= m`, every target character has been formed. There is exactly one way to complete the remaining task: choose nothing else. The source returns 1.

This success check comes before checking whether columns are exhausted. That order correctly handles the state where the target finishes exactly as `j` reaches `n`.

If the target is unfinished but `j >= n`, no usable column remains, so the source returns 0.

**Choice 1: use the current column**

To use column `j` for `target[i]`, one must select a word whose character at that column matches. The number of such word choices is

`cnt[j][ord(target[i]) - ord('a')]`.

After using the column, both indices advance: the next target character is `i + 1`, and every source column through `j` is forbidden, so the next available column is `j + 1`. `dfs(i + 1, j + 1)` counts the ways to complete after one particular matching choice.

Multiplying the suffix count by the frequency counts all combinations of the current word choice with every valid later construction:

`dfs(i + 1, j + 1) * matching_count`.

If no word has the needed character in this column, the matching count is zero and this branch contributes nothing.

**Choice 2: skip the current column**

The algorithm may choose not to use any character from column `j`. The target index stays `i`, while the available source index advances to `j + 1`. This contributes `dfs(i, j + 1)` ways.

Use and skip are disjoint: a construction either selects a character from column `j` for the current target position or never uses column `j`. They are also exhaustive, so their counts are added.

The source reduces the sum modulo `10**9 + 7` before caching and returning it.

**A small recurrence view**

The state obeys

$$
F(i,j)=F(i,j+1)+
\textit{count}(j,\textit{target}[i])F(i+1,j+1).
$$

The first term skips column $j$. The second uses it and multiplies by the number of matching word rows.

For `words = ["acca","bbbb","caca"]` and target beginning with `'a'`, column 0 contains two `a` characters, so the use branch at `(0,0)` receives a factor of two. The recursive suffix then chooses only columns 1 and later. The skip branch explores constructions whose first chosen column is later than zero.

**Why memoization matters**

Many different sequences of earlier skips and uses reach the same remaining indices. Without caching, the recursion would recompute those suffix counts exponentially many times.

`@cache` stores each completed `(i,j)` result. A later call with the same pair returns it immediately, turning the branching recursion into a dynamic program over a rectangular state space.

**Why the recurrence counts every way exactly once**

Consider any valid construction represented by strictly increasing chosen columns. At state `(i,j)`, either its next chosen column equals `j` or is greater than `j`.

If it equals `j`, the construction belongs uniquely to the use branch; its chosen word is one of the counted matching rows, and its remainder is counted by `dfs(i+1,j+1)`. If it is greater, the construction belongs uniquely to the skip branch and remains valid in `dfs(i,j+1)`.

No construction belongs to both cases, and every construction belongs to one. With the success and failure base cases, induction proves that `dfs(0,0)` returns exactly the desired count modulo the required prime.

## Complexity detail

Let $W$ be the number of words, $L$ their common length, and $T$ the target length.

Building `cnt` visits $WL$ characters and costs $O(WL)$ time. There are at most $(T+1)(L+1)$ distinct cached `dfs(i,j)` states. Each uncached state performs constant work beyond its recursive calls and frequency lookup, so the DP costs $O(TL)$ time. Total time is

$$
O(WL+TL),
$$

matching the manifest.

The frequency table has $26L$ integer entries, or $O(L)$ space under the fixed alphabet. However, the exact source's `@cache` may store $O(TL)$ state results, and the recursion stack can reach $O(L)$ depth because every call advances `j`. Therefore actual auxiliary space is $O(TL+L)$, which simplifies to $O(TL)$ in the worst case.

This differs from the manifest's `O(L+T)` space, which would describe a rolling bottom-up DP rather than the checked-in two-dimensional memoization cache. The explanation follows the exact source.

With $L$ up to 1000, the recursive skip chain can also approach Python's default recursion-depth boundary. The algorithmic recurrence is correct, but an iterative implementation is operationally safer at the maximum constraint if the runtime has not raised that limit.

## Alternatives and edge cases

- **One-dimensional bottom-up DP:** Process columns left to right and update target positions right to left. It retains the same $O(WL+TL)$ time while reducing DP storage to $O(T)$ and avoiding recursion depth.
- **Two-dimensional tabulation:** Fill skip/use recurrence iteratively in an $(L+1)\times(T+1)$ table. It matches the cache's $O(LT)$ space but avoids call overhead.
- **Try individual words inside every state:** This repeats work across identical column characters. Precomputed frequencies collapse $W$ equivalent choices into one multiplication.
- **Target longer than word columns:** Strictly increasing chosen columns cannot supply enough characters, so the recursion eventually exhausts `j` and returns zero.
- **No matching character in a column:** The use factor is zero; only skipping contributes.
- **Target completes at the last column:** The success base case is checked first and returns one even when `j == n`.
- **Using several characters from one word:** This is allowed because each column independently counts all word choices; only column indices must increase.
- **Changing words between target characters:** Also allowed. Multiplication counts independent row choices at successive columns.
- **Modulo timing:** Cached values are reduced after adding use and skip contributions, keeping later states bounded while preserving the required remainder.
- **Lowercase alphabet:** Subtracting `ord('a')` maps characters to indices 0 through 25. A different alphabet would require a different frequency representation.
- **Recursive depth near 1000:** The exact source may depend on the platform's recursion configuration. Iterative DP removes this implementation risk.
- **Memoized-space claim:** `@cache` retains a result for many `(i,j)` pairs, so it is not a rolling $O(L+T)$ solution despite the manifest entry.
