## General

The operation looks flexible because any row or any column may be flipped any number of times. The useful first simplification is that flipping the same row or column twice has no net effect. Therefore, every possible sequence of operations is equivalent to choosing some rows to flip once and some columns to flip once.

**Turn the operations into a structural condition**

Let $r_i$ say whether row $i$ is flipped, and let $c_j$ say whether column $j$ is flipped. All values are binary, so flipping is the same as exclusive OR with $1$. The final value at position $(i,j)$ is

$$
\texttt{grid}[i][j] \mathbin{\mathrm{XOR}} r_i \mathbin{\mathrm{XOR}} c_j.
$$

For every final value to be zero, the original matrix must satisfy

$$
\texttt{grid}[i][j] = r_i \mathbin{\mathrm{XOR}} c_j.
$$

Compare any row $i$ with row $0$. For every column $j$, the column choice $c_j$ appears in both rows and cancels when the two original bits are compared:

$$
\texttt{grid}[i][j] \mathbin{\mathrm{XOR}} \texttt{grid}[0][j]
= r_i \mathbin{\mathrm{XOR}} r_0.
$$

The right side does not depend on $j$. Consequently, the relationship between row $i$ and the first row must be the same in every column. If the value is $0$, the two rows are identical everywhere. If it is $1$, every bit differs, so row $i$ is the bitwise complement of the first row. There is no third legal pattern.

This condition is also sufficient. If a row is the complement of the first row, flip that entire row; leave identical rows alone. Now every row equals the first row. For each column whose shared bit is $1$, flip that column. Every position then becomes $0$. Thus, checking whether every row is either the first-row pattern or its complement completely characterizes whether the goal is possible.

**Normalize rows so equivalent patterns become equal**

The exact solution does not separately compare each row with the first row and its complement. Instead, it gives every row a canonical, or normalized, orientation.

The bit `grid[0][0]` is used as the desired first bit of every normalized row. For a current `row`:

- if `row[0] == grid[0][0]`, the code keeps the row unchanged by converting it to `tuple(row)`;
- otherwise, it complements every bit with `x ^ 1` and converts the result to a tuple.

After this choice, every normalized row begins with the same bit. Suppose an original row is identical to the first row. Their first bits agree, so that row remains unchanged and becomes exactly the first-row tuple. Suppose it is the complement of the first row. Its first bit differs, so the solution complements the whole row and again obtains exactly the first-row tuple.

Now suppose a row is neither identical to nor the complement of the first row. Normalization may align its first bit, but at least one later column still disagrees. Its normalized tuple is therefore different. This is why checking only the first bits is not pretending that one cell proves the whole row: the first bit merely decides which orientation to create, while the complete tuple preserves and checks every column.

**Use one set to detect a disagreement**

Each normalized tuple `t` is inserted into `s`. If all rows are compatible, they all normalize to the same tuple and `len(s)` is exactly `1`. If any row violates the required relationship, its tuple differs, so the set contains at least two values. The final expression `len(s) == 1` therefore returns precisely the desired boolean.

For example, in `[[0,1,0],[1,0,1],[0,1,0]]`, the first and third rows remain `(0,1,0)`. The second row begins with the opposite bit, so complementing it also produces `(0,1,0)`. There is one normalized pattern, hence the answer is true. In `[[1,1,0],[0,0,0],[0,0,0]]`, complementing a zero row produces `(1,1,1)`, which differs from `(1,1,0)`. The second pattern exposes the impossibility.

The procedure never changes `grid`: unchanged rows are copied into tuples, and complemented rows are produced by a generator. This matters because the mathematical idea speaks about hypothetical row flips, but the implementation only compares normalized representations.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Every row is read across all $n$ columns to build a tuple. Even `tuple(row)` must copy the row’s $n$ references, while `tuple(x ^ 1 for x in row)` computes and stores $n$ complemented bits. Hashing a newly created length-$n$ tuple also takes $O(n)$ time. Across $m$ rows, the total time is $O(mn)$.

The exact code’s worst-case auxiliary space is $O(mn)$, not $O(1)$. The set may retain as many as $m$ distinct normalized tuples, and each tuple contains $n$ entries. A valid instance usually leaves only one distinct tuple, using $O(n)$ stored space, but complexity must cover invalid matrices too. The temporary tuple for the current row also occupies $O(n)$ space. The input matrix itself is not counted as auxiliary space.

There is a constant-extra-state way to implement the same criterion by comparing every cell directly against the first row and returning immediately on a mismatch. That is a useful alternative, but it is not what the exact stored Optimal solution does; its tuple set determines the stated implementation cost.

## Alternatives and edge cases

- **Direct cell comparison:** For each row, determine from its first bit whether it should match the first row or its complement, then verify every column immediately. This retains $O(mn)$ time and reduces auxiliary space to $O(1)$, but differs from the exact tuple-and-set implementation.
- **Simulating flips:** Actually flipping selected rows and columns can reach the result, but it performs unnecessary mutation and makes choosing operations seem harder than checking the invariant. The identical-or-complement condition gives the answer without constructing an operation sequence.
- **Trying every subset of rows and columns:** There are exponentially many flip selections, even though flipping twice cancels. Algebraically eliminating the column choices collapses that search to one deterministic matrix scan.
- **Checking only row counts:** Two rows can contain the same number of ones without being identical or complementary. Positions, not merely counts, determine whether one column-flip choice can satisfy every row.
- **Single row:** Every one-row binary matrix is valid. Its only normalized tuple enters the set once, and columns containing `1` could all be flipped to clear the row.
- **Single column:** Every row is necessarily identical to or the complement of the first one because there is only one bit to compare, so the method correctly returns true.
- **Already all zeroes or all ones:** All rows normalize to one pattern. An all-zero matrix needs no operations, while an all-one matrix can be cleared by flipping every column or every row.
- **Duplicate rows:** Repeated insertion does not increase the set’s size, exactly matching the fact that repeated compatible patterns introduce no new restriction.
- **Mixed compatible rows:** Any number of first-row copies and first-row complements is allowed. Each complement can be corrected with its own row flip before the shared column flips are applied.
- **First disagreement after column zero:** Aligning the first bit alone is not enough, but the full tuple catches any later mismatch. This is the material reason the code stores the complete normalized row.
- **Input preservation:** The code creates tuples and never assigns into `grid`, so callers observe the original matrix after the method returns.
