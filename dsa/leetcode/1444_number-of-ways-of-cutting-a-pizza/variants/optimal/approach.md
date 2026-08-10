## General

**Describe what remains after each cut.** Every horizontal cut gives away the upper piece, and every vertical cut gives away the left piece. Therefore the piece that stays on the table is always a rectangle anchored at the original pizza's bottom-right corner. It can be described completely by the row `i` and column `j` of its top-left cell. Its cells are all rows from `i` through `m - 1` and all columns from `j` through `n - 1`.

This fixed orientation is what makes dynamic programming possible. The history of earlier cuts does not matter once the remaining rectangle and the number of cuts still required are known. The memoized function `dfs(i, j, k)` means: count the valid ways to divide the remaining bottom-right rectangle beginning at `(i, j)` when exactly `k` more cuts must be made.

The parameter named `k` inside `dfs` shadows the outer input name, but its meaning is narrower: it is the number of remaining cuts, not the requested number of people or pieces. The initial call is `dfs(0, 0, k - 1)` because creating `k` pieces requires exactly `k - 1` cuts.

**Make every apple test constant-time.** A transition must know whether the piece being handed away has at least one apple. Scanning all of that piece's cells for every possible cut would repeat a great deal of work. The matrix `s` is a two-dimensional prefix sum. `s[r][c]` stores the number of apples in the rectangle consisting of the first `r` rows and first `c` columns, with the lower and right boundaries excluded.

The extra zero row and zero column make boundary calculations uniform. While reading pizza cell `(i - 1, j - 1)`, the recurrence adds the apple counts above and to the left, subtracts their double-counted overlap, and adds one if the current character is `'A'`. Thus `s[i][j]` becomes the apple count in the top-left rectangle ending just before row `i` and column `j`.

The apple count in any rectangle can then be obtained by inclusion-exclusion. For the current retained rectangle, the code uses `s[m][n] - s[i][n] - s[m][j] + s[i][j]`. Start with all apples in the full pizza, remove the rows above `i`, remove the columns left of `j`, then add back the top-left overlap that was removed twice.

**The base case represents the last person.** When the local `k` equals zero, no more cuts are allowed. There is exactly one possible action: give the entire remaining rectangle to the final person. That action is valid if the rectangle contains at least one apple and invalid otherwise. The expression inside `int(...)` tests whether its apple count is positive, converting `True` to `1` and `False` to `0`.

It would be wrong to return one unconditionally when no cuts remain. Earlier cuts guarantee that every already distributed piece contains an apple, but the retained final piece has not yet been checked. The base case performs precisely that final validation.

**Try every legal horizontal first cut.** A horizontal boundary `x` can lie after any row from `i` through `m - 2`, so the code iterates `x` from `i + 1` to `m - 1`. The upper piece being given away consists of rows `i` through `x - 1` and columns `j` through `n - 1`. Its apple count is `s[x][n] - s[i][n] - s[x][j] + s[i][j]`.

If that count is positive, the cut is allowed. The bottom piece remains on the table, begins at `(x, j)`, and needs one fewer cut, so the code adds `dfs(x, j, k - 1)`. If the upper piece has no apple, no continuation could repair it after it has been handed away, so that cut is skipped immediately.

**Try every legal vertical first cut.** A vertical boundary `y` ranges from `j + 1` through `n - 1`. The handed-away left piece contains rows `i` through `m - 1` and columns `j` through `y - 1`. Its apple count is `s[m][y] - s[i][y] - s[m][j] + s[i][j]`. A positive count permits the transition `dfs(i, y, k - 1)`, whose rectangle is the right-hand remainder.

The code checks only the handed-away piece at a transition. That is sufficient. The remainder is not forgotten; the recursive state is responsible for cutting it into all remaining pieces, and its base case eventually checks the final one. An impossible remainder simply contributes zero.

**Why memoization is essential.** Different sequences of earlier cuts can produce the same retained rectangle with the same number of cuts remaining. From that point onward, the number of valid completions is identical. The `@cache` decorator stores the result for each `(i, j, k)` triplet, so the complete transition work for that state happens only once. Repeated paths retrieve the already computed integer.

**A small conceptual trace.** Suppose the current rectangle begins at `(0, 0)` and two cuts remain. If a horizontal cut after row `1` gives away an apple-containing top strip, the problem becomes `dfs(1, 0, 1)`. That child tries every horizontal and vertical cut within the smaller bottom rectangle. If instead the first cut is vertical after column `2`, the resulting state is `dfs(0, 2, 1)`. The two first cuts are distinct ways and their valid completion counts should be added.

For each valid first cut, the recursive result counts all and only valid ways to finish that specific remainder. First cuts have distinct directions or boundary positions, so their sets of cutting sequences do not overlap. Summing their results counts every valid sequence exactly once.

**Why the recurrence is correct.** Consider any state. With zero cuts left, the base case gives one precisely when the last piece satisfies the apple rule. With at least one cut left, every legal solution has a unique first cut: it is horizontal at one particular row boundary or vertical at one particular column boundary. The algorithm enumerates all such boundaries, rejects exactly those whose distributed piece lacks an apple, and recursively counts every valid continuation for the remainder. Assuming smaller-cut states are correct, each accepted transition contributes exactly its valid continuations. Induction on the number of cuts proves that `dfs(0, 0, k - 1)` is the required count.

The answer can be enormous, so each completed state's total is reduced modulo `10**9 + 7`. Addition respects modular arithmetic, meaning reducing a subtotal does not change the final answer modulo the required number.

## Complexity detail

Let `m` be the number of rows, `n` the number of columns, and `k` the requested number of pieces. Building the prefix-sum matrix visits each cell once, taking `O(mn)` time and `O(mn)` space.

There are at most `k m n` memo states because the remaining-cut count has `k` possible values and the retained rectangle has at most `m n` top-left positions. For a non-base state, the code considers up to `m - 1` horizontal boundaries and `n - 1` vertical boundaries. Every apple test is constant time because of `s`. The total time is therefore `O(kmn(m + n))`, matching the manifest.

The cache can store one integer for each of `O(kmn)` states. The prefix matrix adds `O(mn)`, which is absorbed by `O(kmn)` because `k` is at least one. Recursion depth is at most `k` because each call decrements the remaining-cut count. Total auxiliary space is `O(kmn)`.

The modulo operation occurs once after accumulating a state's transitions. Python may temporarily hold an integer larger than the modulus, but the number of additions is bounded by `m + n` per state, and this does not alter the asymptotic analysis.

## Alternatives and edge cases

- **Bottom-up three-dimensional DP:** Fill states by increasing number of cuts instead of using recursion and `@cache`. It has the same `O(kmn(m + n))` time and `O(kmn)` space and avoids recursive calls, but often requires more initialization.
- **Rolling DP layers:** A bottom-up formulation needs only the previous cut-count layer to build the next one. It can reduce DP storage to `O(mn)` while retaining the same transition time; the stored memoized source keeps every reached layer.
- **Scan each candidate piece directly:** This avoids a prefix matrix but can spend `O(mn)` on one apple test, multiplying the already large transition cost. Constant-time rectangle counts are the key preprocessing improvement.
- **Count apples only in the remainder:** A suffix-sum matrix is another natural representation because every state is bottom-right anchored. The stored top-left prefix sums are equally correct when inclusion-exclusion formulas use the proper boundaries.
- **Fewer than k apples:** It is impossible for all `k` pieces to receive an apple. The recurrence naturally returns zero because some distributed piece or the final remainder must fail an apple test.
- **Exactly one requested piece:** The initial call has zero remaining cuts. It returns one if the whole pizza has an apple and zero if it does not.
- **No apples:** Every possible handed-away piece fails, and the zero-cut base state also fails, so the result is zero for every positive `k`.
- **One row:** No horizontal cut boundary exists. The horizontal loop is empty, and only vertical cuts are considered.
- **One column:** No vertical cut boundary exists. The algorithm correctly relies only on horizontal cuts.
- **Apple-free strip before an apple:** A cut cannot hand away that empty strip, even if the retained piece has many apples. The positive-count guard rejects it.
- **Remainder lacks enough apples:** The current cut may hand away a valid piece while leaving an impossible remainder. The recursive call returns zero, so the cut contributes nothing without requiring a separate lookahead rule.
- **Different cut orders:** A horizontal-then-vertical sequence and a vertical-then-horizontal sequence are different cutting ways when the distributed pieces differ. The state recurrence counts them through different first-cut branches.
- **Boundary indexing:** `x` and `y` are cut boundaries, not included cells of the handed-away top or left piece. Using half-open ranges is what makes the prefix formulas and recursive top-left coordinates align.
- **Modulo requirement:** Apply `10**9 + 7`, not `10^9 + 7` as a bitwise or language-specific expression. In Python, `10**9 + 7` constructs the intended integer.
