## General

**The top-left corner is fixed.** Every counted submatrix must contain `grid[0][0]`. With axis-aligned submatrices inside the grid, any such rectangle must begin at row zero and column zero. It is therefore uniquely determined by its bottom-right cell $(i,j)$.

Instead of considering four independent boundaries, the algorithm considers each of the $RC$ possible bottom-right corners and asks for the numbers of X and Y characters in prefix rectangle

$$
[0..i]\times[0..j].
$$

**Store two two-dimensional prefix counts.** `s[i][j][0]` is the number of X characters in the first `i` rows and first `j` columns, while `s[i][j][1]` is the analogous Y count. Row and column zero of `s` are padding, so grid cell `grid[i-1][j-1]` corresponds to prefix coordinate `s[i][j]`.

For each letter channel `q`, the standard two-dimensional inclusion-exclusion formula is

$$
s[i][j][q]
=s[i-1][j][q]+s[i][j-1][q]-s[i-1][j-1][q]+\textit{cellContribution}.
$$

The top prefix and left prefix cover the desired rectangle except for the current cell, but their overlapping top-left portion was counted twice, so it is subtracted once.

The source first computes this formula without a cell contribution for both channels. If the current character is not a dot, it increments one channel.

**Decode the compact character-to-channel mapping.** ASCII/Unicode code point `ord("X")` is $88$, which is even, so `ord("X") & 1` equals zero. `ord("Y")` is $89$, which is odd, so its result is one. Therefore

`s[i][j][ord(x) & 1] += 1`

adds X to channel zero and Y to channel one. Dots are excluded by `if x != "."` and add nothing.

This is concise but depends on the exact character codes. An explicit comparison would be clearer and less fragile if the allowed symbols changed.

**Test the two required frequency conditions.** After cell $(i-1,j-1)$ is incorporated, `s[i][j]` describes exactly the anchored rectangle ending there. It qualifies when:

- `s[i][j][0] == s[i][j][1]`, so X and Y frequencies are equal;
- `s[i][j][0] > 0`, so at least one X occurs.

Once the counts are equal, requiring a positive X count also implies at least one Y. It excludes all-dot rectangles, whose counts are both zero but which fail the stated at-least-one-X condition.

Each qualifying bottom-right corner increments `ans` once. Because every eligible submatrix has a unique bottom-right corner, there is neither duplication nor omission.

**Why the prefix table remains correct.** Padding entries represent empty regions with zero occurrences. Assume the already computed neighboring prefixes hold correct counts. Inclusion-exclusion combines them into the count for the larger rectangle and then the current cell contributes to exactly its matching channel. Row-major traversal ensures all three referenced prefix cells are available. Induction over the traversal establishes correctness for the entire table.

For `[["X","Y","."],["Y",".","."]]`, prefixes ending at cells that enclose one X and one Y qualify, as do larger anchored rectangles that retain equal totals. The source evaluates those counts in constant time per bottom-right corner rather than rescanning their contents.

For an all-dot grid, both channels stay zero everywhere. The equality holds, but the strict positive-X test rejects every prefix, returning zero.

## Complexity detail

Let $R$ be the number of rows and $C$ the number of columns. Every grid cell is visited once, with constant work for two prefix channels, so time is $O(RC)$.

The exact source allocates $(R+1)(C+1)$ entries, each containing two counters. Its auxiliary space is $O(RC)$. This materially contradicts the manifest, which states $O(C)$ space and describes maintaining vertical balances. A rolling-row or column-accumulator implementation can achieve $O(C)$, but `solution.py` retains the full two-dimensional table.

At maximum $1000\times1000$ dimensions, the asymptotic distinction is important in Python because the nested lists and small list objects have substantial overhead beyond two raw integers per cell.

The grid is read only and the answer can be as large as $RC$, which Python represents exactly.

## Alternatives and edge cases

- **One rolling prefix row:** Keep previous and current rows for both channels, reducing space to $O(C)$ while preserving $O(RC)$ time.
- **Column accumulators plus horizontal totals:** Update per-column X/Y counts as each new row arrives and scan their prefix across columns. This also achieves the manifest's $O(C)$ space.
- **Balance plus X-presence:** Store X as $+1$, Y as $-1$, dot as zero, along with either an X count or Boolean presence. Balance zero plus presence is equivalent to two counts.
- **Rescan every anchored rectangle:** There are $RC$ corners and each rectangle may contain $RC$ cells, leading to much worse time.
- **All dots:** Equality alone is insufficient; `X > 0` correctly rejects them.
- **Equal positive counts:** Any value $q\ge1$ for both channels qualifies, regardless of dot count.
- **More X than Y or vice versa:** The prefix is rejected even if it contains both symbols.
- **`grid[0][0]` is a dot:** Larger anchored rectangles may still qualify; containing the top-left cell does not require it to be X or Y.
- **Single-cell grid:** X alone and Y alone have unequal counts; dot has no X, so the answer is zero in every one-cell case.
- **Character-code trick:** `ord(x) & 1` is correct specifically for uppercase X and Y. Explicit branches are safer for maintenance.
- **Padding row and column:** They remove boundary condition branches from the recurrence.
- **Input preservation:** Only the separate prefix table is written.
- **Manifest mismatch:** Attribute $O(C)$ space only to a compressed alternative; the exact artifact is $O(RC)$ space.
