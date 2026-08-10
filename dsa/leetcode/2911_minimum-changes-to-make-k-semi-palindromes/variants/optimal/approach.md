## General

The task contains two nested choices. First, the string must be cut into exactly $k$ nonempty contiguous substrings. Second, each chosen substring must be changed into a semi-palindrome using the best proper divisor for that substring's length. Trying cuts and divisor patterns together would repeat the same substring calculations many times.

The solution separates those decisions:

1. Precompute `g[i][j]`, the minimum changes needed to turn substring `s[i-1:j]` into a semi-palindrome.
2. Use another dynamic program, `f[i][j]`, to choose exactly $j$ semi-palindromic pieces covering the first $i$ characters.

Both tables use one-based string boundaries even though Python strings are zero-based. In `g[i][j]`, $i$ and $j$ are inclusive one-based endpoints. The corresponding Python character at local offset $l$ is `s[i - 1 + l]`.

**What a divisor does inside one substring**

Let a substring have length $m$, and choose a proper divisor $d$, meaning $1\le d<m$ and $m\bmod d=0$. Taking characters whose local indices have the same remainder modulo $d$ creates $d$ sequences. For remainder $t$, the sequence contains local positions

$$
t,\ t+d,\ t+2d,\ \ldots,\ t+\left(\frac{m}{d}-1\right)d.
$$

The substring is semi-palindromic for this $d$ when each of these $d$ sequences is a palindrome.

The code visits every local index $l$. Its group is determined by `l % d`, and its position within that group is `l // d`. If a group has $m/d$ characters, the mirror of group position `l // d` is

$$
\frac{m}{d}-1-\left\lfloor\frac{l}{d}\right\rfloor.
$$

Converting that mirrored group position and the unchanged remainder back to a local string index gives the exact expression in the solution:

`r = (m // d - 1 - l // d) * d + l % d`.

This formula can look mysterious until its two components are separated. The multiplication by $d$ selects the mirrored step within the residue-class sequence, while `l % d` returns to the same residue class.

**Count the changes required by one divisor**

For every mirrored pair of positions $l$ and $r$, no change is needed if their characters already match. If they differ, changing either character makes that pair match, so exactly one change is necessary and sufficient.

The loop stops when `l >= r`. All earlier iterations have $l<r$ and count each unordered mirrored pair once. At $l=r$, the character is the center of an odd-length group and already mirrors itself. Once $l>r$, the pairs would be duplicates in reverse order.

The variable `cnt` is therefore the exact minimum number of character replacements needed for this particular divisor $d$. The solution tries every proper divisor of $m$ and keeps the smallest count in `g[i][j]`.

Lengths with no proper divisor remain at infinity. In particular, a substring of length $1$ cannot be semi-palindromic under the definition because there is no integer $d$ with $1\le d<1$. The table deliberately leaves such entries invalid. A length of at least $2$ always has divisor $1$, so it gets a finite repair cost.

**Why pairwise mismatch counting is globally optimal for a fixed divisor**

The palindrome requirements partition positions into disjoint mirror pairs, plus possibly unpaired centers. A character position belongs to only one pair for the chosen $d$. Each mismatching pair forces at least one change, because leaving both characters unchanged would preserve their inequality. Conversely, changing one endpoint of every mismatching pair satisfies every equality. Since the pairs do not compete for characters, their individual lower bounds add exactly. That proves `cnt` is optimal for $d$, and taking the minimum over all allowed divisors makes `g[i][j]` optimal for the substring.

**Partition prefixes after all substring costs are known**

The second table has the meaning

$$
\texttt{f}[i][j]
=
\text{minimum changes needed to split the first }i\text{ characters into exactly }j\text{ valid pieces}.
$$

All entries begin at infinity, representing an impossible state. The sole initial state is `f[0][0] = 0`: an empty prefix uses zero substrings and needs zero changes.

To compute `f[i][j]`, choose $h$ as the endpoint of the preceding prefix. Then:

- the first $h$ characters must already be divided into $j-1$ semi-palindromes, costing `f[h][j - 1]`;
- characters $h+1$ through $i$ form the final substring, costing `g[h + 1][i]`.

This yields the transition

$$
\texttt{f}[i][j]
=
\min_{0\le h<i}
\left(
\texttt{f}[h][j-1]+\texttt{g}[h+1][i]
\right).
$$

The exact code loops over every `h in range(i - 1)`, so $h$ runs from $0$ through $i-2$. This intentionally ensures the final part has length at least $2$. Allowing $h=i-1$ would create a length-one part, whose `g` value is infinity anyway, but excluding it avoids a useless transition.

Infinity also propagates safely from impossible earlier partitions. Adding a finite cost to infinity remains infinity, so the code does not need separate reachability branches.

**Why the partition recurrence finds the global optimum**

Take any valid partition of the first $i$ characters into $j$ pieces. Its last cut occurs after some $h<i$. The portion before that cut is a valid $(j-1)$-piece partition, so its cost cannot be below `f[h][j-1]`. Its final piece cannot cost less than the already optimized `g[h+1][i]`. Therefore the transition considers a value no greater than the cost of this arbitrary partition.

Conversely, every finite transition combines an achievable prefix partition with an achievable repaired final substring. Their ranges are adjacent and disjoint, so together they form a valid $j$-piece partition of the first $i$ characters. The minimum is thus neither an underestimate nor an overestimate: it is exact. The required answer is `f[n][k]`.

## Complexity detail

Let $n$ be the string length.

There are $O(n^2)$ substrings. For a substring of length $m$, the implementation tests every integer $d$ from $1$ through $m-1$, performs a divisibility check, and scans $O(m)$ positions for each divisor that divides $m$. A coarse bound is $O(n^4)$, but accounting for the number of divisors gives the tighter bound used by the Optimal manifest.

For one length $m$, the character work over valid divisors is $O(m\,\tau(m))$, where $\tau(m)$ is the number of divisors of $m$. There are $O(n)$ substrings of each length, and the standard aggregate divisor bound contributes the logarithmic factor. Across all substrings, the preprocessing is bounded by $O(n^3\log n)$ in the arithmetic-operation model.

The partition table has $O(kn)$ states. Each state may test $O(n)$ cut positions, giving $O(kn^2)$ time. The combined time is

$$
O(n^3\log n+kn^2).
$$

Table `g` stores $O(n^2)$ costs, and `f` stores $O(kn)$ costs. Hence auxiliary space is $O(n^2+kn)$. Loop variables require only constant additional storage.

## Alternatives and edge cases

- **Enumerate all partitions first:** There are combinatorially many ways to place $k-1$ cuts. Prefix dynamic programming collapses partitions with the same prefix length and piece count into one best state.
- **Recompute substring repair costs inside the partition DP:** This gives the right answer but repeats expensive divisor and mirror work whenever multiple partition states use the same final substring. The `g` table computes each interval once.
- **Use only divisor $1$:** That would force every substring itself to be an ordinary palindrome. A different proper divisor can require fewer changes because it asks several interleaved sequences to be palindromes instead.
- **Length-one pieces:** They are not semi-palindromes because they have no proper divisor. The infinity initialization of `g` and the cut range prevent them from being used.
- **Exactly $k$ pieces:** The state dimension counts pieces explicitly. A cheaper split into fewer or more substrings cannot leak into `f[n][k]`.
- **Already semi-palindromic substring:** At least one divisor produces zero mismatched mirror pairs, so its `g` cost is zero.
- **Several equally good divisors:** Only the minimum number of changes matters. The algorithm does not need to remember which divisor achieved it.
- **Odd residue-class length:** A center character mirrors itself and costs nothing. Stopping at `l >= r` handles that center and prevents double counting.
- **One-based table indices:** `g[h + 1][i]` corresponds to Python slice `s[h:i]`. Confusing these coordinate systems would shift substring boundaries.
- **Impossible intermediate states:** Infinity is a deliberate sentinel, not a large guessed number. It lets minimum and addition operations preserve impossibility without risking collision with a legal cost.
- **Simultaneous character requirements:** For a fixed divisor, residue classes are disjoint and every position has one mirror partner at most. Therefore repairing one pair never invalidates another pair's equality.
