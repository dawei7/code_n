## Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$.

Each candidate split index satisfies $0\le i<n-1$, ensuring that both the prefix and suffix contain at least one character. A letter `c` contributes `ord(c) - ord("a") + 1` to its substring's score.

**Return value**

Return `true` if the score of `s[0..i]` equals the score of `s[(i + 1)..(n - 1)]` for at least one legal `i`; return `false` if no legal split balances the scores.
