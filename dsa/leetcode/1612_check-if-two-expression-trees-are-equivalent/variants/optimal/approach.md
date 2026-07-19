## General
**Flatten algebraically rather than structurally.** Parenthesization and left/right placement do not affect a sum because addition is associative and commutative. What does affect the expression is the coefficient of each variable, which is exactly the number of leaves carrying that letter.

**Accumulate one signed frequency map.** Traverse `root1`, adding one for every variable leaf. Traverse `root2`, subtracting one for every variable leaf. At `+` nodes, recursively visit both children without recording the operator itself. After both traversals, every zero balance means the two expressions have identical coefficients.

If all balances are zero, evaluation under any variable assignment produces the same linear combination in both trees. Conversely, if one variable has nonzero balance, assigning that variable 1 and every other variable 0 makes the two evaluated results differ. The frequency condition is therefore both sufficient and necessary.

## Complexity detail
Each node in both trees is visited once, so the running time is $O(n_1+n_2)$. Recursive calls use $O(h)$ stack space, and the frequency map stores $u$ variables, for $O(h+u)$ total auxiliary space. Since variables are lowercase English letters, $u$ is also bounded by 26.

## Alternatives and edge cases
- **Collect and sort both leaf lists:** Comparing sorted variable sequences is correct but takes $O((n_1+n_2)\log(n_1+n_2))$ time.
- **Remove each first-tree leaf from a second-tree list:** This preserves multiplicity and is correct, but repeated linear searches and removals can take quadratic time.
- **Compare tree shapes and corresponding nodes:** This incorrectly rejects equivalent expressions whose variables are regrouped or reordered.
- A one-leaf tree is equivalent only to an expression with the same single variable multiplicity.
- Duplicate variables matter; equality of distinct-variable sets is insufficient.
- Different shapes and different left-to-right orders can still be equivalent.
- Internal `+` nodes affect grouping only and do not contribute a symbol to the variable counts.
