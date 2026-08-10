## General

**The first bit of every row must be one in an optimum**

Each row is interpreted as an `n`-bit binary number. The first column is the most significant bit, worth:

$$
2^{n-1}.
$$

All remaining bit weights together sum to:

$$
2^{n-2}+\cdots+2^0=2^{n-1}-1.
$$

Therefore, changing a row's leading bit from 0 to 1 gains more value than the maximum possible loss from toggling every lower bit in that row. Any optimal solution must make every first-column entry one.

Rows can be flipped independently, so the source flips exactly each row whose first bit is zero.

**Apply the forced row flips**

For row `i` with `grid[i][0] == 0`, every entry is toggled through:

`grid[i][j] ^= 1`.

XOR with one converts zero to one and one to zero.

After this phase, the entire first column contains ones. Rows originally beginning with one remain unchanged because flipping them would make their most significant bit zero and cannot be optimal.

This fixes the row decisions. What remains is choosing column flips.

**Columns can now be optimized independently**

Flipping a column toggles that bit in every row but does not affect any other column. The total matrix score is the sum over columns of:

`number of ones in column * that column's binary weight`.

For column `j`, let `cnt` be its current number of ones. If left unchanged, it contributes `cnt` ones. If flipped, its zeros become ones, giving `m-cnt` ones.

The optimal count is:

`max(cnt, m - cnt)`.

No column choice affects another column, so taking the local maximum in every column gives the global maximum once row orientation is fixed.

**Column weight**

Column `j` from the left has binary weight:

`1 << (n - j - 1)`,

which equals `2^{n-j-1}`.

The code adds:

`max(cnt, m-cnt) * weight`

to `ans`.

It does not need to physically flip columns, because only the maximum resulting number of ones is required to calculate the score.

**Why row-first greedy and column greedy are compatible**

One might worry that a later first-column flip could undo row decisions. But after row normalization, first-column count is `m`. Its choice `max(m,0)` keeps it unchanged.

For lower columns, choosing their majority orientation does not change the leading bits. Thus, all column improvements preserve the mandatory first-column condition.

**Trace the main example**

For:

`[[0,0,1,1],[1,0,1,0],[1,1,0,0]]`,

the first row begins with zero and is toggled to `[1,1,0,0]`. Other rows remain.

Now count ones by column and choose majority orientation:

- first column already has three ones, contributing `3*8=24`;
- second column has two ones, contributing `2*4=8`;
- third column has one one, so flipping yields two ones, contributing `2*2=4`;
- fourth column has zero ones, so flipping yields three, contributing `3*1=3`.

Total is 39.

**Why the result is correct**

The most significant-bit argument proves every optimal matrix belongs to the set where all first-column bits are one. The row phase reaches one such matrix without excluding any optimum.

Within that set, column moves are independent, and each column's contribution is maximized by choosing the larger of its one and zero counts. Summing these individually maximal weighted contributions produces the maximum possible total score.

This reasoning covers every permitted sequence of moves because repeated flips of the same row or column cancel in pairs; only whether each row and column is flipped an odd or even number of times matters.

## Complexity detail

For an `m \times n` matrix, the row phase may toggle every cell once, taking `O(mn)` time. The column phase scans every cell once to count ones, also `O(mn)`. Total time is `O(mn)`.

The algorithm modifies `grid` in place and stores only dimensions, counters, and the answer, so auxiliary working space is `O(1)`.

The returned value is scalar. The input matrix storage is not counted as extra space.

## Alternatives and edge cases

- **Try every subset of row and column flips:** There are `2^{m+n}` possibilities, unnecessary because bit significance and column independence force greedy choices.

- **Compute row flips virtually:** Treat cell `grid[i][j]` as toggled when its first bit is zero, avoiding input mutation. It has the same time and `O(1)` space.

- **All first bits already one:** No row is toggled; column optimization still applies.

- **Column tied between zeros and ones:** Flipping or not gives the same contribution; `max` handles either.

- **One-row matrix:** Make its first bit one, then every column can independently be made one, producing all binary ones.

- **One-column matrix:** Every zero row is flipped, so all entries become one and score is `m`.

- **Lower-bit loss during a row flip:** It can never outweigh gaining the leading bit.

- **First column during column phase:** Its all-one count makes leaving it unchanged optimal.

- **Binary guarantee:** XOR toggling and majority complement counts rely on cells being 0 or 1.

- **Input mutation:** Rows beginning with zero are changed in place; callers observe the normalized matrix.
