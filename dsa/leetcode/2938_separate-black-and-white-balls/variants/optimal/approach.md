## General

**A misplaced pair must cross.** Consider a black ball that currently appears
to the left of a white ball. The final arrangement requires their order to be
reversed. Because a step swaps only adjacent balls, those two balls must cross
each other at least once. Thus every pair `(i, j)` with $i<j$,
`s[i] == "1"`, and `s[j] == "0"` contributes an unavoidable step.

**Count those pairs while scanning.** Keep the number of black balls already
seen. When the next ball is black, increment that count. When it is white, it
forms one misplaced pair with every earlier black ball, so add the current
count to the answer. This counts every black-before-white pair exactly once,
at its white endpoint.

**The lower bound is attainable.** Repeatedly move each white ball left across
the earlier black balls. Each adjacent swap removes exactly one counted
inversion and never creates another one. After all inversions are removed, no
black ball precedes a white ball, so all whites are on the left and all blacks
are on the right. The construction uses exactly the number of steps counted by
the scan, proving that count is the minimum.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The scan examines each ball once, taking
$O(n)$ time. It stores only the running black-ball count and accumulated
answer, so auxiliary space is $O(1)$. The answer may be quadratic in $n$, even
though computing it is linear.

## Alternatives and edge cases

- **Count white balls from right to left:** Symmetrically, each black ball contributes the number of white balls to its right; this also takes $O(n)$ time and $O(1)$ space.
- **Sum target-position displacements:** Match each black ball with its final position and sum how far it moves right; this is linear but requires more careful index bookkeeping.
- **Enumerate every pair:** Testing all $i<j$ and counting `10` pairs is correct but takes $O(n^2)$ time.
- **Simulate adjacent swaps:** Bubbling white balls left produces the minimum arrangement directly, but performs one operation per inversion and can therefore take $O(n^2)$ time.
- **Already separated or one color only:** There are no black-before-white pairs, so the answer is zero.
- **Large result:** With many black balls followed by many white balls, the minimum can be proportional to $n^2$, so the running total must support values beyond 32-bit signed range.

