## General

**Separate rightward and downward visibility**

A person may see only along the same row to the right or along the same column below. These two directions are independent: no person can be both strictly right and strictly below while sharing the required row or column.

The helper `f(nums)` solves the one-dimensional problem of how many people each position can see to its right. The main method applies it to every row, then applies it to every top-to-bottom column and adds the downward counts.

**Scan a line from the far end**

For a one-dimensional list, `f` processes indices from right to left. When position `i` is handled, every possible person to its right has already been summarized by a monotonic stack.

The stack contains a strictly decreasing sequence of representative heights from farther positions at the bottom to nearer relevant positions at the top. People already proven to be blocked for every future position are removed, so the stack is a visibility frontier rather than a copy of the suffix.

**See and remove every shorter frontier person**

Let current height be `nums[i]`. While the nearest frontier height `stk[-1]` is strictly smaller, the current person can see that person, so `ans[i]` increases and the height is popped.

The popped person cannot block the current person's view because the current person is taller. Popping may expose another farther frontier person. That person is also visible if it is still shorter: all relevant people between them that could block have already been represented and removed in increasing visibility order.

Each popped height counts as one visible person. It is removed because the current, taller and nearer person will dominate it as a blocker for positions farther left.

**Count the first height that is at least as tall**

When the shorter-pop loop stops, a remaining stack top has height greater than or equal to the current height. The current person can see this first such person, so `ans[i]` increases once.

That person blocks everyone behind it from the current person's view. For a farther person to be visible, everyone between must be shorter than both endpoints; this at-least-as-tall blocker is not shorter than the current endpoint. Therefore, the code counts one blocker but does not scan beyond it.

If the stack is empty, no additional person exists on the frontier and nothing is added.

**Remove equal representatives before pushing**

After counting the blocker, the code removes stack entries equal to `nums[i]` and then pushes the current height.

This duplicate handling is essential. For a future taller person to the left, two equal-height people cannot both be visible: the nearer equal person blocks the farther one because an intervening height equal to the farther endpoint is not shorter than both. Replacing an older equal representative with the current, nearer one ensures future scans count only the visible equal.

If the blocker is strictly taller, it remains in the stack and the current shorter height is pushed above it. This preserves decreasing order from bottom to top.

**Trace one row**

For heights `[3, 1, 4, 2, 5]`, scan from five toward three:

- Height five has nobody to its right.
- Height two sees five as the first taller blocker.
- Height four pops and sees two, then sees five as its taller blocker.
- Height one sees four as its first taller blocker.
- Height three pops and sees one, then sees four as its taller blocker.

The rightward counts are `[2, 1, 2, 1, 0]`.

**Apply the helper to rows**

`ans = [f(row) for row in heights]` builds the initial output matrix. Entry `ans[i][j]` now counts people visible to the right of `(i,j)`.

Each row is processed independently because a rightward line of sight never changes row.

**Apply the helper to columns**

For each column `j`, the list comprehension `[heights[i][j] for i in range(m)]` extracts heights from top to bottom. Running `f` on this list counts visibility toward increasing row indices, which means downward in the grid.

The inner loop adds `add[i]` to `ans[i][j]`. Since rightward and downward target sets are disjoint, ordinary addition gives the total requested count.

**Why the stack frontier is correct**

After processing a suffix, the stack retains exactly the height changes that can become visible from some position farther left, with equal redundant blockers collapsed. For a new current height, every shorter top is visible until it is dominated and removed. The first remaining taller-or-equal height is visible and blocks everything beyond.

These are exactly the people satisfying “everyone between is shorter than both endpoints.” The update then produces the correct frontier for the next position. By induction, `f` returns exact one-direction counts, and applying it to both permitted axes returns the grid answer.

## Complexity detail

Let the grid have `m` rows and `n` columns. In one call to `f`, each height is pushed once and popped at most once, including equal-removal pops. Its time is linear in the line length.

All row calls total `O(mn)`, and all column calls total another `O(mn)`. Extracting columns and adding their results are also `O(mn)`. Total time is `O(mn)`.

The returned answer matrix uses `O(mn)` space. Excluding required output, one helper result, extracted column, and stack use at most `O(\max(m,n))` temporary space. Including the returned structure, the bound is `O(mn)` as in the manifest.

The input matrix is not modified.

## Alternatives and edge cases

- **Scan every person ahead:** Checking all rightward and downward pairs can take `O(mn(m+n))` time.
- **Nearest-greater arrays alone:** A person can see several shorter people before the first blocker, so only storing one greater neighbor is insufficient.
- **Monotonic stack without equal removal:** A future taller person could incorrectly count multiple equal-height people even though the nearer equal blocks the farther one.
- **Process rows only:** It omits all downward visibility.
- **Transpose the matrix:** It can reuse row logic for columns but requires another matrix-sized structure; direct column extraction is simpler.
- **One row:** Only rightward counts contribute.
- **One column:** Only downward counts contribute.
- **Single cell:** Both scans return zero for that person.
- **Strictly increasing line:** Each person sees only the immediate taller person to the right.
- **Strictly decreasing line:** A taller left person can see a chain of successively exposed shorter frontier people.
- **Equal adjacent heights:** The nearer equal is visible and blocks the farther suffix for that current person.
- **Several equal heights:** Duplicate collapse retains only the nearest representative for future observers.
- **First taller blocker:** It is counted once, then traversal stops beyond it.
- **Right and below overlap:** No distinct target position can satisfy both same-row-right and same-column-below, so counts add without duplication.
- **Input preservation:** Column lists and answer rows are new objects; `heights` remains unchanged.
