## General

**Store the best path sum ending in each previous-row column**

After processing a row, `f[j]` represents the minimum sum of a valid falling path that has selected column `j` in that row. To extend into the next row at column `i`, the preceding column may be anything except `i`.

Therefore the recurrence is

$$
g[i]=\texttt{row}[i]+\min_{\substack{0\le j<n\\j\ne i}} f[j].
$$

The code creates `g = row[:]` so every entry starts with the current cell value, then adds the minimum valid previous sum.

**Initialize the first row through a zero virtual row**

Before any real row, `f` is an array of $n$ zeroes. For $n>1$, the minimum excluding any column is still zero, so after the first iteration `g` equals the first grid row. This correctly represents choosing any first-row cell with no earlier cost.

For $n=1$, the exclusion generator is empty. `min(..., default=0)` supplies zero, so the single-cell grid returns its value. This default is needed because there is no alternative previous column in that special case.

**Use only the previous DP row**

Each `g[i]` reads exclusively from unchanged `f`, not from other entries being computed in `g`. After the full row is ready, `f = g` makes it the previous-row state for the next iteration.

Copying `row[:]` is important because it avoids mutating the input grid and gives an independent current DP array.

For the $3$ by $3$ example, after the first row `f = [1,2,3]`. For second-row column zero, the best allowed previous value is two, producing six. For column one, the best allowed previous value is one, producing six. For column two, the best allowed value is one, producing seven. Thus `f = [6,6,7]`. Processing the last row yields a minimum of thirteen.

**Why the recurrence is correct**

Every valid path ending at current column `i` has some previous column `j != i`. Removing the current cell leaves a valid optimal-subproblem path represented by at least `f[j]`. The cheapest such predecessor is the minimum over all allowed $j$, so no valid path can cost less than the recurrence.

Conversely, selecting the predecessor that attains that minimum and appending current cell `row[i]` creates a valid path because the columns differ. Hence `g[i]` is achievable and optimal.

Induction over rows proves every DP entry. After the final row, a complete path may end in any column, so `min(f)` is the global answer.

Negative grid values cause no problem. Dynamic programming compares complete prefix sums, and using the locally smallest cell without context is not assumed.

**The exact source rescans the previous row for every column**

For each current column `i`, the generator iterates through all $n$ previous columns and filters out `i`. This is clear and directly mirrors the recurrence, but it repeats similar minimum work $n$ times per row.

An optimized implementation can store the smallest and second-smallest previous values plus the column of the smallest. Then every current column chooses one of those in constant time. The shipped source does not perform that optimization.

## Complexity detail

There are $n$ rows and $n$ current columns per row. For each of those $n^2$ cells, the `min` generator scans $n$ previous columns. Exact time is therefore $O(n^3)$.

This differs from the manifest's $O(n^2)$ claim, which describes the minimum-and-second-minimum optimization. The exact code remains practical only for smaller $n$ than that optimized bound suggests; here $n\le200$.

Arrays `f` and `g` each contain $n$ values. During a row both coexist, so auxiliary space is $O(n)$. The generator is lazy and does not allocate a separate list. The input is not modified.

## Alternatives and edge cases

- **Track two minima:** Find the smallest and second-smallest previous DP values and the smallest's column once per row. This reduces time to $O(n^2)$ and keeps $O(n)$ or even constant DP summary space.
- **Full two-dimensional DP:** Store every row's states. It has the same cubic transition time as the exact recurrence and uses $O(n^2)$ space.
- **Top-down memoization:** Memoize row-column states, but scanning all next columns still gives $O(n^3)$ time and adds recursion overhead.
- **Greedy smallest cell per row:** This can force the same column on adjacent rows and is not valid; even choosing the smallest allowed current cell can harm future rows.
- **Single-cell grid:** The empty predecessor set uses default zero, returning that cell.
- **Negative values:** The recurrence remains correct and may favor very negative cells while respecting column changes.
- **Tied predecessor minima:** Any minimum in a different column is sufficient; the generator handles ties naturally.
- **Input preservation:** `row[:]` prevents DP updates from overwriting grid rows.
- **Adjacent rows only:** A column may be reused after one intervening row; the recurrence excludes only the immediately previous column.
- **Final choice:** Taking `min(f)` is necessary because the path may optimally end in any last-row column.
