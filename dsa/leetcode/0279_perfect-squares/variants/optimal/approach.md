## General

**View the problem as an unbounded minimum-combination problem**

The usable values are the positive perfect squares no larger than `n`:

$$
1^2,2^2,3^2,\ldots,\left\lfloor\sqrt n\right\rfloor^2.
$$

Each square may be used any number of times. For example, the optimal representation of 12 uses `4` three times. This is the same structure as unbounded coin change, except the goal is to minimize the number of selected values rather than count combinations or minimize monetary coins.

The exact protected source solves this with a two-dimensional dynamic-programming table. The manifest describes a different number-theory algorithm with $O(\sqrt n)$ time and constant space. This explanation follows the actual table implementation and states its true bounds.

**Define the table state precisely**

Let

$$
m=\left\lfloor\sqrt n\right\rfloor.
$$

The source builds `f` with `m + 1` rows and `n + 1` columns. State `f[i][j]` means:

> the minimum number of square terms needed to make sum `j` when the allowed square values are only $1^2,2^2,\ldots,i^2$.

The row dimension controls which square types are allowed. The column dimension is the target subtotal. This definition makes the final answer `f[m][n]`, because row `m` permits every positive perfect square no larger than the requested target.

**Initialize impossible states and the empty sum**

Every table entry begins as positive infinity. Infinity means that the subtotal has not been shown reachable with the currently permitted square types.

The one reachable state with zero square types is

$$
f[0][0]=0.
$$

Making sum zero requires choosing no terms, so its minimum count is zero. Any positive sum is impossible without square values and remains infinity in row zero.

This fictional empty-sum base case is what allows a perfect square to be recognized cleanly. When processing square $i^2$ and subtotal $j=i^2$, the include transition uses `f[i][0] + 1 = 1`, proving that one term is sufficient.

**At each state, separate exclusion from inclusion**

For square type $i^2$ and target subtotal $j$, an optimal representation falls into one of two exhaustive cases.

It may use no copy of $i^2$. Then it is composed entirely from smaller squares and has cost `f[i - 1][j]`. The source begins by assigning this exclusion value to `f[i][j]`.

Alternatively, it may use at least one copy of $i^2$. Remove one such copy. The remaining sum is $j-i^2$, and because more copies of $i^2$ are still allowed, the remainder's state is in the current row: `f[i][j - i * i]`. Adding back the removed square costs one term, giving

$$
f[i][j-i^2]+1.
$$

When $j\ge i^2$, the recurrence is therefore

$$
f[i][j]
=
\min\left(
f[i-1][j],
f[i][j-i^2]+1
\right).
$$

When $j<i^2$, inclusion is impossible, so only the exclusion value applies.

Using the current row in the inclusion term is crucial. If the source used `f[i - 1][j - i * i]`, each square type could be selected at most once, turning the problem into a 0/1 choice and incorrectly rejecting representations such as `4 + 4 + 4`.

**Why subtotals are scanned upward**

For a fixed `i`, the inner loop visits `j = 0, 1, ..., n`. When computing `f[i][j]`, the include transition reads column `j - i * i`, which is smaller than `j`. Because columns increase, that current-row state has already been computed.

This order intentionally allows repeated use of $i^2$. Once the row learns how to make a subtotal with one copy, later columns can build on it with a second copy, then a third, and so forth. Scanning downward would prevent those updates from chaining within the same row and would implement the wrong 0/1 recurrence.

**Why the recurrence gives the minimum**

Assume earlier rows and smaller columns of the current row already hold their stated minimum values. Any valid representation of `j` either contains no $i^2$ or contains at least one. In the first case, its best possible count is exactly the exclusion state. In the second case, removing one $i^2$ leaves a representation covered by the smaller current-row subtotal; choosing its minimum and adding one gives the best count among representations that use $i^2$.

Taking the smaller of these cases covers every representation and chooses the best one. The initialized base state starts the induction, so all filled states are correct. Since square 1 is available from the first real row, every subtotal from 0 through `n` eventually becomes reachable, and the final answer is finite.

**Trace `n = 12`**

Here $m=3$, so the available squares are 1, 4, and 9.

With square 1 alone, every subtotal `j` needs `j` copies. When square 4 is introduced, upward scanning produces:

$$
f[2][4]=1,
\qquad
f[2][8]=f[2][4]+1=2,
\qquad
f[2][12]=f[2][8]+1=3.
$$

These states correspond to one, two, and three copies of 4. Introducing square 9 can make 12 as `9 + 1 + 1 + 1`, requiring four terms, which does not beat the existing three. The table returns 3 for `4 + 4 + 4`.

For `n = 13`, the square-9 row evaluates its include choice as `f[3][4] + 1`. The remainder 4 needs one square, so the total is two, representing `9 + 4`. No one-term option exists because 13 is not itself square, and the answer is 2.

**Why table order does not count arrangements separately**

The task asks only for a minimum count, not a list of ordered decompositions. Processing square types row by row groups all uses of one type together. Representations `4 + 9` and `9 + 4` are the same multiset choice for this optimization and lead to the same count. The recurrence compares counts rather than enumerating term orders, avoiding exponential permutation work.

## Complexity detail

There are $m=\lfloor\sqrt n\rfloor$ real square rows and $n+1$ subtotal columns. Each cell performs constant work, so the exact time complexity is

$$
O(mn)=O(n\sqrt n).
$$

The table contains $(m+1)(n+1)$ numeric entries, giving exact auxiliary space

$$
O(mn)=O(n\sqrt n).
$$

These bounds differ from the manifest's $O(\sqrt n)$ time and $O(1)$ space, which describe the four-square/three-square theorem classification rather than this source.

Only the previous row and current row are needed, so a rolling two-row version would use $O(n)$ space. Because the recurrence's current-row dependency points to an already processed smaller column, it can be compressed further into one array of length $n+1$, updated upward for every square, also using $O(n)$ space. The protected source retains the complete two-dimensional table.

The result itself is one integer and uses $O(1)$ output space. Under the stated $n\le10^4$ constraint, floating-point `sqrt` identifies the small integer limit safely; an integer-square-root routine would avoid precision concerns in a generalized much larger domain.

## Alternatives and edge cases

- **Number-theory classification:** Lagrange's four-square theorem bounds the answer by four, and Legendre's three-square theorem identifies forced four-square cases; checking one and two squares distinguishes the rest. This achieves the manifest's $O(\sqrt n)$ time and $O(1)$ space but relies on deeper mathematical theorems and is not the exact source.
- **One-dimensional DP:** Initialize `dp[0] = 0`, then for each square update subtotals upward with `dp[j] = min(dp[j], dp[j-square] + 1)`. It preserves the unbounded recurrence while reducing space to $O(n)$.
- **Remainder BFS:** Treat each remainder as a node and subtract every usable square. The first level reaching zero gives the minimum term count. It is conceptually direct but requires a queue and visited-state storage.
- **Naïve recursion:** Trying every next square recomputes the same remainders many times and grows exponentially without memoization.
- **`n = 1`:** The square set contains 1, and `f[1][1]` becomes `f[1][0] + 1 = 1`.
- **`n` already a perfect square:** At row $i=\sqrt n$, the include transition from subtotal zero sets the answer to one.
- **Repeated square required:** The same-row transition and upward column order allow unlimited copies, which is essential for 12 as `4 + 4 + 4`.
- **Square larger than the subtotal:** The inclusion branch is skipped, preventing a negative column index and correctly carrying the smaller-square answer forward.
- **Infinity arithmetic:** Adding one to an unreachable infinity state remains infinity, so impossible partial choices cannot become falsely optimal.
- **Square 1 guarantees reachability:** Even if no larger square helps, `n` copies of 1 form `n`; the returned value is never infinity for legal positive input.
- **Positive-input guarantee:** The contract begins at 1. If zero were passed, the table would return `f[0][0] = 0`, which is the natural minimum empty sum.
- **Downward subtotal iteration:** This would block reuse of the current square within the same row and solve a different problem where each square is available once.
