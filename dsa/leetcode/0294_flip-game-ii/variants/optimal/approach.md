## General
**Minus signs reveal the game's structure**

A minus sign never becomes plus again, so play in one maximal run of pluses cannot affect another run. The board is
therefore a sum of independent impartial games rather than one indivisible string state.

**What a move does to one run**

Consider a plus run of length $L$. Flipping the pair beginning after $i$ pluses leaves two independent runs:

- a left run of length $i$;
- a right run of length $L - i - 2$.

These are every possible move from the run. Runs of length zero or one have no move.

**Turn the recurrence into Grundy numbers**

Let $g(L)$ be the Grundy value for a run of length $L$. A move at split $i$ reaches the combined value
$g(i) \oplus g(L - i - 2)$. Collect these values for all $i$, then set $g(L)$ to their minimum excluded nonnegative
integer (mex). Because every child run is shorter than $L$, the table can be filled from small lengths upward.

For example, $g(2) = 1$: its only move reaches two empty runs with xor zero. A four-plus run can reach xor values zero
and one, so its mex is two.

**Decide the entire board with xor**

Sprague-Grundy theory combines independent games by xor. Xor `grundy[length]` for every plus run. A zero total is
losing; a nonzero total is winning because a move exists that makes the total zero. Thus `++--++` loses—the two
identical value-one games cancel—while `++++--++` wins.

## Complexity detail
Let $n$ be the longest plus-run length and let $m$ be the complete state length. Building Grundy values through $n$
examines $O(n^2)$ split positions, and discovering and combining the runs takes $O(m)$ time, for $O(m + n^2)$ total
time. The runs, Grundy table, and one reachable set use $O(m + n)$ space, which is $O(m)$ because $n \le m$.

## Alternatives and edge cases
- **Memoized complete strings:** avoids duplicate recursion but still distinguishes exponentially many combinations
  of flipped pairs.
- **Unmemoized minimax:** revisits the same board states and grows even faster.
- **Short runs:** lengths zero and one have no legal move and therefore Grundy value zero.
- **Separated identical runs:** their equal Grundy values cancel under xor, a semantic distinction that a single
  longest-run check would miss.
