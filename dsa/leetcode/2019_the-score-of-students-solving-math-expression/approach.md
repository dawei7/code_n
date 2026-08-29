## General

**Compute the one officially correct value**

Helper `cal` evaluates multiplication before addition without using general expression evaluation.

`pre` stores the current multiplication term. On `'*'`, the next digit multiplies `pre`. On `'+'`, the completed term is added to `res` and `pre` resets to the next digit. Adding the final term after the loop produces the standard-precedence result `x`.

For `"7+3*1*2"`, seven is committed when plus appears, while three remains in `pre` and is multiplied by one and two. The final addition gives $7+6=13$, demonstrating that multiplication is completed before its term joins the sum.

Operands are single digits at even string indices and operators are at odd indices, so stepping by two parses the expression exactly.

**Enumerate results from every parenthesization**

A student's correct arithmetic with wrong operation order corresponds to some full parenthesization that preserves the original numbers and operator sequence.

Let `f[i][j]` be the set of values obtainable by parenthesizing operands `i` through `j` in every possible way.

For a single operand, the only result is that digit. For a longer interval, choose the final top-level split `k`. Combine every value from `f[i][k]` with every value from `f[k+1][j]` using the original operator between operands `k` and `k+1`.

Trying every split covers every binary parenthesization because every expression tree has one root operator that separates a left and right interval.

**Fill dependencies in a valid order**

The outer index `i` decreases. For a fixed `i`, `j` increases.

At split `k`, left interval `f[i][k]` has a smaller right endpoint and was computed earlier in the same row. Right interval `f[k+1][j]` has a larger starting index and was computed during an earlier outer iteration.

Thus every set is ready before it is read.

**Deduplicate equal arithmetic results**

Different parenthesizations can yield the same number. A set stores it once because grading asks whether an answer is possible, not how many erroneous evaluation orders produce it.

The source retains only results at most 1000, the maximum submitted answer. Operations and operands are nonnegative. Values above the grading range generally cannot become a relevant positive in-range sum; multiplication by zero can yield zero, and equivalent parenthesizations that combine the zero earlier preserve that reachable zero.

**Score answer multiplicities efficiently**

`Counter(answers)` groups equal submissions. Every occurrence of exact correct value `x` earns five, contributing `cnt[x] * 5`.

For every other distinct submitted value, membership in `f[0][m-1]` earns two per occurrence. The condition `k != x` preserves grading priority: a value that is both correct and obtainable through a wrong order still receives five, not two.

`v << 1` is exactly `2 * v`.

**Trace `"3+5*2"`**

Correct precedence computes $3+(5\cdot2)=13$.

Interval DP also tries split after the second operand, producing $(3+5)\cdot2=16$. Both 13 and 16 belong to the possible-parenthesization set, but submissions of 13 receive five because it equals `x`. Submissions of 16 receive two.

Values such as ten that no parenthesization produces receive zero.

**Why the interval DP is complete and sound**

Every inserted value comes from two recursively valid subexpressions joined by the actual operator, so it corresponds to a legal parenthesization with correct arithmetic.

Conversely, take any legal parenthesization. Its root split is tried, and by induction its left and right results are in their interval sets, so their combination is inserted. Therefore the full set contains exactly the relevant wrong-order results within the scoring range.

## Complexity detail

Let $M$ be the number of operands, $V$ the maximum number of retained values in an interval set, and $A$ the number of answers. There are $O(M^2)$ intervals, $O(M)$ splits per interval, and up to $V^2$ value pairs per split.

Time is $O(M^3V^2+A)$ and space is $O(M^2V)$ for the interval sets, matching the manifest. Here $V\le1001$ due to the retained range.

## Alternatives and edge cases

- **Recursive memoization by interval:** Computes the same value sets top-down; iterative order avoids recursion.
- **Use `eval` for the correct value:** Unsafe and unnecessary; the small parser handles exactly the allowed grammar.
- **Enumerate parenthesization strings:** Repeats equal results and allocates much more data than result sets.
- **Only multiplication or only addition:** Every parenthesization has the same result, so only the correct answer earns points.
- **Correct value also in DP set:** Award five because `k != x` excludes it from the two-point pass.
- **Duplicate student answers:** Counter multiplicity awards each student independently.
- **Answer outside every result:** Earns zero.
- **Operand zero:** Multiplication can produce zero and the DP includes it.
- **Single-digit operands:** Even-index parsing relies on this explicit guarantee.
- **Values over 1000:** Not submitted and are pruned from interval sets.
- **Operator order:** Parenthesization may change evaluation order but never reorder operands or operators.
- **Bit shift for points:** `v << 1` multiplies the answer frequency by two.
- **Input preservation:** The expression and answers are read without modification.
