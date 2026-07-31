## General

**Represent a row by its interior joints**

Build every sequence of allowed brick widths whose total is exactly `width`.
Whenever a brick ends before the right boundary, set the corresponding bit in
a seam mask. The brick widths are unique, and the ordered seam positions
determine every brick width between successive boundaries, so each completed
layout produces one distinct mask.

Two rows may be adjacent exactly when their masks have no common set bit.
Precompute, for every current mask, the indices of all predecessor masks whose
bitwise intersection with it is zero.

**Count walls one row at a time**

For the first row, assign one way to every valid mask. For each remaining
height, the number of walls ending in mask $m$ is the sum of the previous
counts for all masks compatible with $m$. Reduce each count modulo $10^9+7$.
After the final row, sum the counts for every possible last mask.

The first-row initialization represents every one-row wall once. Assuming the
counts are correct through some height, appending each compatible mask creates
every sturdy next row and rejects exactly those additions sharing a joint
with the preceding row. Each wall has a unique final-row mask and predecessor,
so no wall is duplicated. Induction therefore establishes the final count.

## Complexity detail

Let $R$ be the number of valid row masks and $E$ the number of ordered
compatible mask pairs. Testing every pair costs $O(R^2)$ time. Each of the
remaining $h-1$ rows traverses the compatible edges, costing $O(hE)$ time, for
$O(R^2+hE)$ overall. The compatibility lists contain $E\le R^2$ entries and
the two DP layers contain $O(R)$ counts, so space is $O(R^2)$.

Because `width` is at most ten, masks use only the nine possible interior
joint positions.

## Alternatives and edge cases

- **Enumerate complete walls:** Try every sequence of row layouts and test
  adjacent masks. This is correct but can require $O(R^h)$ combinations.
- **Check every predecessor during every layer:** Omitting compatibility lists
  uses $O(R)$ DP space but spends $O(hR^2)$ time repeating the same mask tests.
- If no brick sequence totals exactly `width`, there are no valid rows and the
  answer is zero.
- A brick whose width equals the wall creates a zero seam mask and is
  compatible with every row, including itself.
- For `height = 1`, every valid row layout is a sturdy wall because there is
  no adjacent-row constraint.
- Only interior joints matter; the shared left and right wall boundaries are
  explicitly permitted.
- Different brick orders are distinct row layouts even when they use the same
  multiset of widths.
