## General

**Reduce validity to one inequality.** Sort the three positive lengths as $a \le b \le c$. The sums $a+c$ and $b+c$ are automatically greater than the remaining positive side. Therefore only $a+b>c$ can fail. If $a+b\le c$, the sides are degenerate or disconnected and the required result is `"none"`.

**Classify the equality pattern.** Once validity is known, sorted order makes the categories direct. If $a=c$, transitivity gives $a=b=c$, so the triangle is equilateral. Otherwise, equality of either adjacent pair means exactly two lengths agree and the triangle is isosceles. If neither pair agrees, all three lengths differ and the triangle is scalene. These tests are mutually exclusive and cover every valid triangle.

## Complexity detail

The contract always supplies exactly three values. Sorting and the fixed number of arithmetic comparisons therefore take $O(1)$ time and $O(1)$ auxiliary space. The legal domain is too tightly bounded for an honest scaling benchmark, so a bounded-domain certificate verifies this constant-work claim across every legal array.

## Alternatives and edge cases

- **Check all three inequalities:** This is correct, but after sorting positive lengths the two inequalities involving the largest side in a sum are automatic, so only `a + b > c` is material.
- **Count distinct lengths first:** Equality alone cannot establish that a triangle exists; validity must be checked before returning a category.
- **Degenerate equality:** When the two smaller lengths sum exactly to the largest, the result is `"none"`, not a triangle category.
- **Unsorted input:** Sorting ensures that any permutation of the same three lengths receives the same validity test and classification.
- **All sides equal:** Three positive equal lengths always satisfy the strict inequality and must return `"equilateral"` before the two-equal check.
- **Very thin isosceles triangle:** `[1, 100, 100]` is valid because $1+100>100$, despite the large difference between its base and equal sides.
