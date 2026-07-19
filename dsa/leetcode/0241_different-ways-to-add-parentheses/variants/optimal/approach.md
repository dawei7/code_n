## General
**Every expression tree chooses one final operator**

Every full parenthesization has one root operator. Split at each operator, recursively obtain every left and right result, and combine their Cartesian product using that operator.

For `2*3-4*5`, choosing the subtraction as the root combines every interpretation of `2*3` with every interpretation of `4*5`. Choosing either multiplication instead covers the trees whose final operation is that multiplication. No precedence rule is imposed because the parenthesization itself determines evaluation order.

**Cache the complete multiset for each interval**

Different split choices request the same subexpressions repeatedly. Cache the complete result list for each substring so its parenthesizations are generated once.

The cached value must remain a list rather than a set. Distinct parenthesizations may evaluate to the same integer, and the output requires one entry for each structure. A substring containing no operator is the base case and contributes its parsed integer once.

**Root decomposition generates every parenthesization exactly once**

For any cached interval, consider a complete parenthesization tree. Its root is one specific operator in that interval; its left and right children are complete parenthesizations of the corresponding two substrings. The recursion reaches that split, and the Cartesian product includes exactly that child pair.

Conversely, selecting an operator and one valid result structure from each side creates a valid full parenthesization with that operator as its unique root. Different root splits or child structures represent different trees, so the generated multiset is neither missing structures nor inventing invalid ones.

## Complexity detail
With `n` operators there are Catalan-number `C_n` output structures, each requiring combination work across its tree, giving output-sensitive $O(C_n \cdot n)$ time and stored results of the same order.

## Alternatives and edge cases
- **Recursion without memoization:** recomputes identical substrings.
- **Precedence evaluation:** produces only one interpretation, not all trees.
- A number-only expression has one result; multi-digit numbers and duplicate results must be preserved.
