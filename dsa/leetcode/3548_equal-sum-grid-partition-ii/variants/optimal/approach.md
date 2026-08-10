## General

**For a fixed cut, only one value can repair unequal sums**

Consider a horizontal cut after row `i`. Let:

- `s1` be the sum above the cut;
- `s2` be the sum below the cut.

If `s1=s2`, no discount is needed and the cut is immediately valid.

If `s1>s2`, discounting a cell from the smaller bottom side would make the imbalance worse. The cell must come from the top and must have value exactly:

`diff = s1-s2`.

Then `s1-diff=s2`.

The symmetric rule applies when `s2>s1`. Because every grid value is positive, no other deletion value or side can equalize the sums. This turns the numerical part of each cut into one membership lookup.

**Maintain both side sums and value frequencies**

At the start of `check(g)`:

- `s1=0` and `cnt1` is empty for the top side;
- `s2` is the total grid sum and `cnt2` counts every cell for the bottom side.

The scan moves one complete row at a time from side two to side one. After row `i` is moved:

- `s1` and `cnt1` describe rows zero through `i`;
- `s2` and `cnt2` describe rows `i+1` through `m-1`.

The loop stops at `m-2`, so both sections are always non-empty.

Frequency dictionaries are necessary because the same value may occur several times. Decrementing `cnt2[x]` as cells move ensures a lookup refers to the correct side of the current cut.

**Connectivity is automatic for a true rectangle**

If a section has at least two rows and at least two columns, deleting any one cell leaves it connected under four-direction movement.

Intuitively, a missing cell can be bypassed through an adjacent row or column. Even the smallest two-by-two rectangle leaves three cells forming a connected L shape. Larger rectangles contain enough alternate routes around one removed vertex.

Therefore, when the larger-sum side has both dimensions greater than one, the source needs only `cnt[diff] > 0`. Any occurrence of the required value is safe to discount.

**A one-dimensional section allows only endpoint deletion**

A section with one row is a path of cells. Removing an interior cell splits that path into left and right pieces. Removing its first or last cell leaves the remainder connected.

A section with one column is the same path geometry vertically: only its top or bottom endpoint may be removed.

The protected source handles these cases explicitly rather than assuming every matching cell is valid.

**Check deletion from the bottom side**

When `s1<s2`, the source first requires `cnt2[diff]`.

Let bottom height be `m-i-1`:

- if bottom height is greater than one and `n>1`, it is a true rectangle and any matching cell works;
- if bottom height is one, its only row is `g[i+1]`, and a matching value must be at column zero or column `n-1`;
- if `n=1`, the bottom is one vertical path from row `i+1` through `m-1`, and a matching value must be at `g[i+1][0]` or `g[-1][0]`.

These are exactly the three conditions in the first branch.

**Check deletion from the top side**

When `s1>s2`, `cnt1[diff]` must be positive.

Top height is `i+1`:

- if it is greater than one and `n>1`, any matching cell is safe;
- if it is one, only the first or last cell of row zero can be removed;
- if `n=1`, only top endpoint `g[0][0]` or bottom endpoint `g[i][0]` of that vertical path can be removed.

The source's conditions mirror the bottom logic.

**Why equal sums need no connectivity test**

When `s1=s2`, the source returns true before considering a cell. Discounting is optional—“at most one”—so it chooses no deletion. Both rectangular sections created by a straight cut are connected and non-empty by construction.

**Transpose to cover vertical cuts**

`check(grid)` examines every horizontal boundary. The transpose:

`list(zip(*grid))`

turns original columns into rows. A horizontal cut in this transposed matrix corresponds exactly to a vertical cut in the original grid. Cell values and four-neighbor connectivity are preserved by transposition.

The final expression:

`check(grid) or check(transpose)`

short-circuits if a horizontal solution exists and otherwise examines every vertical cut.

**Why the membership and endpoint rules are complete**

For any valid unequal partition, positivity forces discounting exactly `diff` from the larger side. If that side is at least two-by-two, its matching cell is covered by the frequency lookup. If it is one-dimensional, connectedness forces the cell to be an endpoint, which the explicit comparisons test.

Conversely, any successful branch identifies a matching cell on the correct larger side and verifies that deleting it preserves connectivity. Its value removes exactly the sum imbalance, so the two sections become equal.

Thus every returned true corresponds to a legal cut and every legal cut is found.

## Complexity detail

Let `N=mn`. One `check` first scans all `N` cells to initialize bottom counts, then moves each cell at most once while testing cuts. It takes `O(N)` expected time with hash-table operations.

The transpose contains `N` references and takes `O(N)` time and space. At most two checks run, so total time is `O(mn)`.

`cnt1` and `cnt2` may contain one entry per distinct cell value, up to `O(mn)`. Together with the transpose, auxiliary space is `O(mn)`, matching the manifest.

## Alternatives and edge cases

- **Rotate four times as in the editorial:** It also covers cut orientation and deletion side. The protected source checks both larger-side branches directly and needs only one transpose.
- **Use only a set:** Counts are needed while rows move between sides; a value may remain below after one copy moves above.
- **Ignore connectivity:** This falsely accepts deleting an interior cell from a one-row or one-column section.
- **Run graph connectivity after every candidate deletion:** Correct but far too expensive. Rectangle geometry reduces connectivity to a dimension/endpoint rule.
- **Equal section sums:** No deletion is selected, so connectivity remains automatic.
- **Required diff absent:** That cut cannot be repaired by one discount.
- **Required value occurs only at an unsafe interior path cell:** Frequency membership succeeds but endpoint checks correctly reject it.
- **Two-by-two section:** Removing any single cell leaves three connected cells.
- **One-cell section:** Its only cell is both endpoints; discounting it would leave the section empty. Could the source accept this? For a one-cell larger side, deleting its sole positive value would make its sum zero while the other non-empty side has positive sum, so equality is impossible; `diff` cannot equal that sole value when the other sum is positive.
- **Single-row original grid:** The first check has no horizontal cut; transposition converts vertical cuts into a multirow one-column case.
- **Single-column grid:** Endpoint rules apply directly to horizontal sections.
- **Duplicate values:** Side-specific counts ensure presence is tracked after row transfers.
- **Positive values:** They guarantee the larger side and exact positive difference determine the only possible discount.
