## General
**Minus signs reveal the game's structure**

A minus sign never becomes plus again, so play in one maximal run of pluses cannot affect another run. The board is therefore a sum of independent impartial games rather than one indivisible string state.

**What a move does to one run**

Consider a plus run of length `L`. Flipping the pair beginning after `i` pluses leaves two independent runs:

- a left run of length `i`;
- a right run of length $L - i - 2$.

Those are every possible move from the run. Runs of length zero or one have no move.

**Turn the recurrence into Grundy numbers**

Let $g(L)$ be the Grundy value for a run of length $L$. A move at split $i$ reaches the combined value
$g(i) \oplus g(L-i-2)$. Collect these values for all $i$, then set $g(L)$ to their minimum excluded nonnegative integer (mex). Because every child run is shorter than $L$, the table can be filled from small lengths upward.

For example, $g(2) = 1$: its only move reaches two empty runs with xor zero. A four-plus run can reach xor values zero and one, so its mex is two.

**Decide the entire board with xor**

Sprague-Grundy theory combines independent games by xor. Xor `g[length]` for every plus run. A zero total is losing; a nonzero total is winning because a move exists that makes the total zero. Thus `++--++` loses—the two identical value-one games cancel—while `++++--++` wins.

## Complexity detail
Computing all run lengths through `n` examines $O(n^2)$ split positions. The Grundy table and the reachable-value set for one length use $O(n)$ space.

## Alternatives and edge cases
- Memoizing complete strings avoids duplicate recursion but still distinguishes exponentially many combinations of flipped pairs.
- Unmemoized minimax revisits those states and grows even faster.
- Runs of length zero or one contribute Grundy value zero; an input without `++` is therefore losing immediately.
