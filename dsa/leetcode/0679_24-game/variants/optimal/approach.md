## General
**Reduce any chosen pair to one exact result**

Every fully parenthesized binary expression has a final operation joining the results of two subexpressions. Reversing that view, choose any pair of current values, replace it with the result of one legal operation, and recurse on the shorter multiset. Addition and multiplication need one ordering; subtraction and division need both because they are not commutative. Division by zero is skipped.

**Use rational arithmetic and canonical states**

Represent every value as an exact fraction, avoiding tolerance choices and floating-point drift in expressions such as $8 / (3 - 8 / 3)$. Sort each remaining multiset into a tuple before memoization. Pair-selection orders that produce the same rational values then share one cached state.

**Why pair reduction covers every expression**

Consider any legal expression tree. Its lowest internal node combines two original cards, so one backtracking branch can choose that pair and operation first. Repeating this argument on the contracted expression reaches the tree's final value. Conversely, every recursive reduction applies one permitted binary operation to disjoint card-derived values and therefore describes a legal parenthesized expression using each card once. Reaching the singleton fraction 24 is thus equivalent to the existence of a solution.

## Complexity detail
The public contract fixes both the card count at four and every card value to a bounded range, so the complete search has a finite constant upper bound: $O(1)$ time and $O(1)$ space with respect to input size. For a generalized `M`-card version, the pair-and-operation search is exponential, while memoization limits repeated work to distinct rational multisets. Recursion depth is three for this contract.

## Alternatives and edge cases
- **Floating-point backtracking:** follows the same pair reduction and accepts values within an epsilon of 24, but exact fractions avoid both false tolerances and accumulated error.
- **Enumerate permutations, operators, and parenthesis shapes:** is finite for four cards, but duplicates many commutative and structurally equivalent expressions.
- **Unmemoized exact backtracking:** is correct and still constant for the fixed contract, though it revisits identical intermediate multisets reached in different orders.
- Both operand orders must be tried for subtraction and division.
- A zero intermediate value is legal, but it cannot be used as a divisor.
- Duplicate card values still represent separate cards and must all be consumed.
