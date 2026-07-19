## General
**Evaluate the correct precedence separately.** Parse the digit operands and
operators. Maintain the product of the current multiplication group; when `+`
appears, add that product to the total and begin the next group. This produces
the unique five-point value without relying on arbitrary evaluation.

**Enumerate all parenthesized values with interval DP.** Let `possible[i][j]`
be the set of results obtainable by fully parenthesizing operands `i` through
`j`. A single operand contributes itself. For every longer interval, try each
operator as the final split, combine every left and right result with that
operator, and retain values no larger than $1000$, since submitted answers
cannot exceed that bound.

Every full binary parenthesization has one final operator separating a left
and right subexpression, so the corresponding split reconstructs its result
from smaller DP intervals. Conversely, each DP combination corresponds to a
valid parenthesization using the original operator order. The final set
therefore contains exactly the plausible two-point values. Grade each answer
by checking the correct value first, then membership in that set.

## Complexity detail
There are $O(M^2)$ operand intervals and $O(M)$ splits per interval. Each split
can combine up to $V^2$ value pairs, giving $O(M^3V^2)$ DP time; grading adds
$O(A)$. Storing up to $V$ results per interval uses $O(M^2V)$ space. In legal
inputs $M\le16$ and $V=1001$, while actual set sizes depend strongly and
non-monotonically on the operators and digits.

## Alternatives and edge cases
- **Enumerate parenthesization trees:** Generating every Catalan-structured
  evaluation repeats identical subexpressions and grows exponentially.
- **Use unrestricted `eval`:** It can obtain the correct precedence value but
  neither enumerates mistaken parenthesizations nor provides an appropriate
  parser boundary.
- Correct answers always receive five points, even if also reachable through
  a wrong operation order.
- Duplicate submissions are graded separately and multiply their points.
- Zero can collapse many multiplication results, so DP sets must deduplicate
  values rather than paths.
