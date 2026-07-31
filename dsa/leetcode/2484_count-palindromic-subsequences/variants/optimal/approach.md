## General

**Split every palindrome at its center.** Any length-five palindrome has the digit pattern $a,b,c,b,a$. Once an index is chosen for the center digit $c$, the other four indices consist of an ordered pair $(a,b)$ in the prefix and the reversed ordered pair $(b,a)$ in the suffix. The center's value does not restrict either pair, so all $100$ possibilities for $(a,b)$ can be counted together.

**Maintain ordered-pair counts on both sides.** For each pair of digits $(x,y)$, `left_pairs[x][y]` counts choices of two increasing indices before the current center whose digits are $x,y$. The analogous right table counts pairs after the center. Single-digit frequency arrays make each pair table easy to update when the sweep boundary crosses one character.

The right table is initialized for the entire string. Before using a position as the center, remove that occurrence from the right singles and remove every right pair in which it was the first index. The suffix state then represents only positions strictly after the center. For every $(a,b)$, multiply `left_pairs[a][b]` by `right_pairs[b][a]`; each product independently chooses the two prefix indices and two suffix indices of a valid palindrome.

After counting the current center, append its digit to the left state. Existing left singles form every new ordered pair ending at this position, and then the position becomes available as a single for later centers. Thus the left table always contains exactly the pairs strictly before the next center, while the right table contains exactly the pairs strictly after it. Every valid five-index tuple has one unique center and is counted once.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Initialization and the center sweep each inspect a constant $10$ or $100$ digit combinations per character, so the running time is $O(100n) = O(n)$. Four arrays of at most $10 \times 10$ counters use $O(100) = O(1)$ auxiliary space because the decimal alphabet is fixed.

## Alternatives and edge cases

- **Prefix and suffix pair tables at every position:** Precomputing all split states also gives $O(n)$ time, but stores $O(100n)$ counters instead of updating two constant-size states.
- **Interval dynamic programming:** Counting length-three palindromes inside every possible equal outer pair can be organized in $O(n^2)$ time and $O(n)$ space, but it is unnecessarily slow for $n=10^4$.
- **Enumerate five indices:** Directly checking every five-position subsequence takes $O(n^5)$ time and is infeasible.
- **Repeated values:** Equal digit strings produced from different index tuples must all be counted; pair counts retain their multiplicities.
- **Short strings:** When $n<5$, no center has two indices on each side, so every pair product is zero.
- **Modulo arithmetic:** Reducing the accumulated answer after each center keeps values bounded without changing the final residue.
