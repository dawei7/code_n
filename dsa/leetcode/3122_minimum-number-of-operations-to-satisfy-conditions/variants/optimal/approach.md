## General

**Every final column must be uniform.** The vertical condition requires each cell to equal the cell below it. By transitivity, all $m$ cells in one column must have one common final value.

The horizontal condition then says adjacent columns must choose different common values. The two-dimensional cell problem becomes a sequence problem: choose one value for each column, make neighboring choices different, and minimize how many cells change.

**Cost of assigning one digit to a column.** Input values lie from 0 through 9. For column `i`, the source counts occurrences of each digit in `cnt`. If final digit is `j`, every cell already equal to `j` stays unchanged and every other cell requires one operation. The cost is:

`m - cnt[j]`.

Although an operation may assign any nonnegative number, it is sufficient to consider digits 0 through 9. A new outside value matches no existing cell and costs `m`. Among ten input-domain digits, at least one choice different from the previous column is available and costs at most `m`. An outside value can never be strictly better.

**Dynamic-programming state.** `f[i][j]` is the minimum operations needed for columns zero through `i` when column `i` is made entirely digit `j`.

For the first column there is no left neighbor, so:

`f[0][j] = m - cnt[j]`.

This directly uses the column assignment cost.

**Transition between columns.** For later column `i` ending in digit `j`, previous column digit `k` must differ. The source examines all ten possibilities and applies:

`f[i][j] = min(f[i][j], f[i - 1][k] + m - cnt[j])`

whenever `k != j`.

The prior DP value already optimally satisfies every earlier vertical and horizontal condition. Adding the current column cost and enforcing the one new boundary condition produces a valid prefix. Taking the minimum covers every possible prior digit.

**Why only the preceding chosen digit matters.** The current column's horizontal restriction involves only column `i-1`. All older constraints are fully summarized by `f[i-1][k]`. No earlier grid contents or selected digits need to be carried separately, which is the optimal-substructure property.

**Final answer.** The last column may use any digit, so `min(f[-1])` chooses the cheapest complete assignment.

**A trace for `[[1,1,1],[0,0,0]]`.** In every column, digit zero occurs once and digit one occurs once, so choosing either costs one. For column zero, both states cost one. Column one must choose the opposite digit from column zero and adds one. Column two switches again and adds one. Minimum total is three, producing a pattern such as 1, 0, 1 down the columns.

For one column `[[1],[2],[3]]`, choosing any of 1, 2, or 3 preserves one cell and changes two. There is no horizontal restriction, so the returned minimum is two.
For column zero, every `f[0][j]` is exactly the cost of the only possible uniform assignment to that digit. Assume row `i-1` stores optimal costs for every possible final digit. Any valid assignment through column `i` ending in `j` must previously end in some `k != j` and pays current cost `m-cnt[j]`. The transition checks that exact predecessor and cannot exceed its cost. Conversely, every transition combines a valid optimal prefix with a different current digit, so it constructs a valid assignment. Thus each state is exact, and the final minimum is globally optimal.

## Complexity detail

Counting values visits every one of the $mn$ cells once. For each of $n$ columns, the DP considers 10 current digits and 10 previous digits, adding $O(100n)$. Total time is:

$$
O(mn+100n)=O(mn)
$$

because 100 is constant and $m\ge1$.

The exact source allocates `f` as an $n$ by 10 table, so auxiliary space is $O(10n)=O(n)$. This contradicts the manifest's $O(1)$ space claim, which would require retaining only the previous and current ten-state rows. The implementation does not perform that rolling optimization.

## Alternatives and edge cases

- **Rolling two DP rows:** Preserve only ten previous and ten current costs to achieve true $O(1)$ auxiliary space under the fixed digit domain.
- **Maximize unchanged cells:** Use rewards `cnt[j]` instead of change costs and subtract the maximum reward from $mn$. Equivalent to the manifest wording.
- **Choose best digit per column independently:** Incorrect when adjacent columns choose the same digit.
- **One column:** No horizontal constraint; select its most frequent digit.
- **One row:** Vertical equality is automatic, but adjacent selected cell values must differ.
- **Already valid grid:** The corresponding digit sequence produces cost zero.
- **All columns identical:** Some columns must change because adjacent final values cannot match.
- **Tie between digits:** Either may be used; DP resolves later compatibility.
- **Outside-domain value:** Costs all $m$ cells and cannot beat every available digit choice.
- **Ten candidate digits:** Guaranteed sufficient by the input domain and inequality-only horizontal rule.
- **Operation cost:** Each changed cell costs one regardless of the new nonnegative value.
- **Full table:** Makes reconstruction possible in principle, although the source returns only cost.
- **Input preservation:** `grid` is counted but never modified.
- **Large dimensions:** $mn$ is at most one million cells, compatible with the linear scan.
- **Source/manifest space mismatch:** Exact table storage grows with the number of columns.
