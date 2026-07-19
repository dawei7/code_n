## General
**Store deficits, with negative counts representing surplus**

Initialize `balance[char]` to its multiplicity in `t` and `missing = len(t)`, the number of required occurrences not yet supplied. When the right edge includes character `c`, decrement `missing` only if `balance[c] > 0`, because only then does this copy satisfy a deficit. Decrement `balance[c]` afterward in all cases.

A zero balance means the window has exactly enough copies; a negative balance means surplus. This representation handles duplicate requirements without separately tracking how many distinct character types are satisfied.

**Once valid, contract until removing one more required copy breaks validity**

Whenever `missing = 0`, the current window covers all multiplicities. Record it if shorter, then remove its left character: increment that character's balance and advance `left`. If the restored balance becomes positive, the removed copy was required rather than surplus, so increment `missing` and stop contracting. Otherwise the window remains valid and contraction continues.

This loop tests every valid left boundary for the current right edge and leaves the next expansion starting from the first invalid boundary.

**Balance and `missing` describe the window exactly**

For every character, its balance equals required multiplicity minus occurrences in the current window. `missing` is the sum of positive deficits across all characters. Therefore `missing = 0` is exactly the cover condition. Surplus copies may make individual balances negative but never make `missing` negative.

**Trace surplus copies and the final contraction**

In `ADOBECODEBANC` for `ABC`, the first valid window is `ADOBEC`. Shrinking and later expansion progressively improves it; near the end, the window contracts to `BANC`, and removing `B` would break coverage.

**Shrinking isolates the shortest cover for each right endpoint**

The balance counts certify validity only when every required character multiplicity is present. While valid, advancing the left boundary considers progressively shorter windows ending at the same right position; the first removal that breaks a requirement proves no later left boundary can remain valid for that endpoint.

Thus the loop records the shortest valid window for every right endpoint that can cover `t`. Every globally minimum window has one such endpoint and is considered in this contracted form. Since recording occurs only under full multiplicity coverage, the shortest recorded candidate is exactly the answer.

## Complexity detail
Both pointers move only forward through `s`, so each character enters and leaves at most once, yielding $O(|s| + |t|)$ time. The frequency map stores only alphabet characters.

## Alternatives and edge cases
- **Check every substring:** requires quadratic candidates and repeated frequency work.
- **Restart a scan from every left endpoint:** can take $O(|s|^2)$ even with incremental counts.
- **Use sets instead of counts:** loses required multiplicity information for patterns such as `AABC`.
- If `len(t) > len(s)`, no window can cover the required occurrences. If no valid window is ever recorded, return the empty string.
- Characters not present in `t` acquire negative balances and are removable surplus; they never change `missing`.
