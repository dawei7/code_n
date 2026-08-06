## General

**Number theory reduces the answer to four classified cases**

Lagrange guarantees that every positive integer needs at most four squares. First test whether `n` is one square.
Remove factors of four, then Legendre's theorem says a remainder congruent to seven modulo eight requires exactly four
squares.

Removing factors of four does not change whether the minimum is four: a representation of $n / 4$ scales every root
by two, and squares modulo four force the reverse implication. The reduced $n \bmod 8 = 7$ test therefore identifies
precisely the four-square case.

**Exhaustively test the two-square case**

Try each square $a^2 \le n$ and check whether $n - a^2$ is also a square. A match gives two; if no match and the
four-square condition did not apply, the answer is three.

**Exhausting cases in minimality order determines the answer**

The direct square test identifies exactly answer one. The loop considers every possible first square $a^2$, so a
perfect-square remainder exists exactly when answer two is possible. Legendre's necessary-and-sufficient form
identifies answer four. If none of those classifications applies, Lagrange still guarantees an answer no larger than
four; excluding one, two, and four leaves exactly three.

## Complexity detail

Removing factors of four takes $O(\log n)$ divisions. The dominant loop tests at most
$\lfloor \sqrt{n} \rfloor$ roots with constant-time integer-square checks under the source's bounded integer contract,
giving $O(\sqrt{n})$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming through $n$:** takes $O(n\sqrt{n})$ time and $O(n)$ space.
- **Breadth-first search over remainders:** also explores up to $n$ states and can require $O(n\sqrt{n})$ work and
  $O(n)$ storage.
- **A perfect square:** must be returned as one before the two-square loop can pair it with the zero remainder.
- **Four-square form:** after all factors of four are removed, a remainder congruent to seven modulo eight forces the
  answer to be four without scanning roots.
- **Integer arithmetic:** `isqrt` avoids floating-point rounding at square boundaries.
