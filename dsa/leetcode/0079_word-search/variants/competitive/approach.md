## General

**Keep board contents separate from path visitation**

The source allocates a Boolean matrix `visited` with the same dimensions as `board`. A true entry means that the corresponding cell is already used by the current recursive path. The characters themselves are never overwritten, so board values remain available for comparison and the input board is preserved.

Every board cell is tried as a possible location for `word[0]`. The recursive call receives `cur`, the index of the next word character to match, plus candidate coordinates `(i, j)`. Starting from all cells is necessary because the first letter can occur more than once and only some occurrences may have a legal continuation.

**Check completion before rejecting the next coordinates**

`existRecu` first tests `cur == len(word)`. This means all word characters were already matched by earlier calls. It returns true without inspecting `(i, j)`.

This ordering is intentional. After a call matches the final character, it recursively tries a neighbor with `cur + 1 == len(word)`. That neighbor may be outside the board, but no additional cell is actually required; the path was complete at the previous cell. Checking the success state first lets completion propagate without demanding a nonexistent extra coordinate.

For any call that still needs a character, the combined rejection condition checks row bounds, column bounds, prior visitation, and character equality. Logical `or` short-circuits from left to right, so `visited[i][j]` and `board[i][j]` are accessed only after the coordinates have been proved safe.

**Choose the current cell and explore every direction**

Once a candidate is valid, `visited[i][j] = True` chooses it for the current path. The four recursive calls try down, up, right, and left for `word[cur + 1]`. Diagonals are never generated.

They are connected with logical `or`, so Python stops evaluating as soon as one direction succeeds. If a direction succeeds, its true value becomes `result`; if none succeeds, `result` is false. Short-circuiting saves work but does not alter completeness because unexplored directions are irrelevant after existence has been proved.

After the expression finishes, the source always executes `visited[i][j] = False`, even when `result` is true. It then returns the saved Boolean. This cleanup order is a strong backtracking property: the visit mark belongs only to the current call's active path and never leaks into a sibling branch, later starting cell, or the caller after success.

**Why the visited matrix prevents every kind of reuse**

It is not enough to prevent only an immediate move back to the preceding cell. A longer path could loop around and revisit a cell from several steps earlier. Since every active ancestor remains true in `visited`, the rejection check blocks any cell already on the full current path.

When recursion returns, clearing the mark makes the cell available to alternative paths. The rule is “at most once per candidate path,” not “at most once across the entire search.” A global permanent visited mark would incorrectly reject paths starting elsewhere or reaching the cell through a different prefix.

**A recursive invariant and proof**

On entry to a call with character index `cur`, exactly the cells chosen for `word[:cur]` are marked, they form an orthogonally adjacent path, and no marked cell is repeated. If `cur` equals the word length, that path spells the entire word and success is correct.

Otherwise, invalid coordinates, an already marked cell, or a character mismatch cannot legally extend the path. For a valid candidate, marking it extends the path with the correct next character. The four recursive calls cover every allowable next direction. Their disjunction is true exactly when at least one continuation completes the word.

Cleanup restores the entry visitation state before returning, preserving the invariant for the caller's remaining directions. The outer loops test every possible first cell, so if any legal path exists, its sequence of neighbor choices is explored. Conversely, every true result corresponds to matched characters on distinct orthogonally adjacent cells.

**Trace why cleanup still runs on success**

Suppose the downward recursive call finds the rest of the word. Because of `or`, the other three calls are skipped, but evaluation assigns true to `result` and continues with the statements after the expression. The current cell is unmarked before `result` is returned. Each ancestor performs the same cleanup as true unwinds. The final board and visited matrix are clean.

This is safer than returning directly inside the first successful direction, which would bypass unmarking unless cleanup were handled separately.

**The space declaration overlooks the visited matrix**

Although backtracking depth depends on the word length, this source also materializes one Boolean per board cell before searching. That storage exists even when the word is very short. It cannot be ignored as constant auxiliary state.

## Complexity detail

Let the board have $mn$ cells and let the word length be $L$. Each cell can be a start. The first level has up to four choices and subsequent levels have at most three immediate forward choices because the preceding cell is visited. Worst-case time is $O(mn\cdot3^L)$ after constant factors, matching the manifest.

The recursion stack and active path depth use $O(L)$ space. The explicit `visited` matrix uses $O(mn)$ additional space. Exact auxiliary space is therefore $O(mn+L)$, not the manifest's $O(L)$ bound. Achieving only $O(L)$ auxiliary space requires marking the board in place or storing only the active path positions in a set of size at most `L`.

## Alternatives and edge cases

- **In-place sentinel marking:** Temporarily replace a chosen board character and restore it after recursion. This removes the full visited matrix and reaches $O(L)$ stack space if cleanup is guaranteed.
- **Active-path coordinate set:** Store only visited coordinates on the current path. It uses $O(L)$ entries but has hashing overhead.
- **Frequency pruning:** Compare board and word character counts before DFS to reject impossible multiplicities quickly.
- **Rarer-end start:** Reverse `word` when its final character occurs less often than its first, reducing the number of promising starts.
- **One-character word:** A matching start marks its cell, reaches the completion base case on the first recursive neighbor call, cleans up, and returns true.
- **Word longer than board area:** Reuse is forbidden, so success is impossible; an explicit length precheck could avoid search.
- **Out-of-bounds after final match:** Completion is checked before coordinate validity, correctly recognizing that no next cell is needed.
- **Short-circuit directions:** Later directions are skipped only after one complete path has already been found.
- **Repeated characters:** The visited matrix distinguishes cells even when their character values are equal.
- **Board preservation:** Only `visited` changes, and every chosen entry is cleared before return.
- **Nonempty constraints:** Allocation reads `board[0]`, which is safe because both dimensions are guaranteed positive.
- **Manifest discrepancy:** The allocated matrix makes exact auxiliary space dimension-dependent even though the active recursion alone is $O(L)$.
