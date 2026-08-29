## General

**Each column sum determines its possible shape**

A binary column with two rows has only three cases:

- sum zero forces `[0,0]`;
- sum two forces `[1,1]`;
- sum one must be either `[1,0]` or `[0,1]`.

The two-row answer is initialized entirely to zero. The algorithm processes columns once, filling forced columns and greedily assigning sum-one columns while treating `upper` and `lower` as remaining row quotas.

**Forced sum-two columns**

For `v == 2`, both cells must be one. The code assigns both entries and decrements both row quotas.

No alternative exists. If either quota becomes negative, the requested row has already been forced to contain more ones than allowed, so no matrix can exist.

**Flexible sum-one columns**

A sum-one column contributes one remaining one to exactly one row. The code gives it to the row with the larger current quota:

- if `upper > lower`, place it in the upper row;
- otherwise, place it in the lower row.

When quotas tie, choosing lower is arbitrary; a symmetric choice of upper would also work.

The goal is to consume the larger outstanding requirement first and keep the residual quotas balanced. Future sum-two columns affect both quotas equally, so they do not change which quota is larger. Future sum-one columns supply the remaining individual choices.

**Why the greedy choice is safe**

Focus on the flexible columns. Ultimately, exactly `upper` of the remaining sum-one columns must be assigned to the upper row and exactly `lower` to the lower row after forced contributions are accounted for.

At a sum-one decision, suppose the upper remaining quota is larger. Any valid completion must assign at least as many of the remaining flexible ones to upper as its quota demands. Giving the current one to upper cannot take an opportunity uniquely needed by lower, because every future sum-one column is interchangeable: each can be assigned to either row.

An exchange argument makes this explicit. If some valid completion assigns the current column to the smaller-quota row while later assigning another flexible column to the larger-quota row, swap those two column assignments. Column sums remain one, row totals stay unchanged, and the greedy current choice is realized.

**The negative-quota check**

After every column, the code checks `upper < 0 or lower < 0`. A negative value means too many ones have already been placed in that row. Later columns can only add ones, never remove them, so returning an empty list is immediately correct.

This check also catches an excessive number of forced sum-two columns as soon as the contradiction appears.

**Final quota check**

After all columns, `ans` automatically satisfies every column sum because each case was filled according to `v`. It satisfies the requested row sums exactly only if both residual quotas are zero.

`return ans if lower == upper == 0 else []` performs that final test. A positive leftover means too few column ones were available to reach a requested row total.

**Following the first example**

For `upper = 2`, `lower = 1`, and three sum-one columns:

- the first goes upper because 2 is greater than 1, leaving quotas 1 and 1;
- the second goes lower on the tie, leaving 1 and 0;
- the third goes upper, leaving zero and zero.

The produced matrix is `[[1,0,1],[0,1,0]]`. Other assignments are accepted because only totals matter.

**Why separate `if` statements are safe**

The code uses one `if` for `v == 2` and another for `v == 1` rather than `elif`. A column sum cannot equal both values, and sum zero matches neither, so at most one block runs.


After processing a prefix of columns, every filled column has the required sum, and `upper` and `lower` equal the numbers of ones still needed in each row. Forced columns are uniquely correct. The greedy flexible assignment preserves the existence of a completion whenever one existed, by the exchange argument.

Negative quotas prove impossibility. If processing finishes with both quotas zero, all column and row constraints hold, making `ans` valid. If either is nonzero, no unprocessed column remains to supply it, so no solution exists.

## Complexity detail

Let \(n=\lvert\texttt{colsum}\rvert\). Initializing the two output rows takes \(O(n)\), and the loop performs constant work per column, giving \(O(n)\) time.

The returned matrix contains \(2n\) values and requires \(O(n)\) space. Excluding required output, the algorithm uses only scalar quotas and loop variables, or \(O(1)\) auxiliary space.

## Alternatives and edge cases

- **Process all sum-two columns first:** Subtract their forced contributions, then distribute sum-one columns according to the residual upper count. This is equally linear and can simplify the feasibility formula.
- **Closed-form feasibility test:** After forced twos, require nonnegative quotas and require their sum to equal the number of ones in `colsum`.
- **All column sums zero:** A solution exists only when both requested row sums are zero.
- **Too many sum-two columns:** A quota becomes negative and the method returns empty.
- **Too few available ones:** Residual quota remains positive at the end and the final check fails.
- **Tied quotas:** Either row can receive the current flexible one; the exact source chooses lower.
- **Multiple valid matrices:** The contract permits any, so greedy need not reproduce an example’s layout.
- **Maximum length:** The one-pass method handles \(10^5\) columns without recursion.
- **Output space:** \(O(n)\) is unavoidable because a valid matrix itself contains \(2n\) entries.
- **Column values restricted to zero, one, or two:** The case analysis relies on this guarantee.
