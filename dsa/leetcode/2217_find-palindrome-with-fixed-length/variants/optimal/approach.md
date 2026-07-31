## General

**A prefix determines the whole palindrome**

For length $\ell$, let $h=\lceil\ell/2\rceil$. The first $h$ digits uniquely determine the palindrome: mirror the entire prefix when $\ell$ is even, or mirror all but its last digit when $\ell$ is odd. Increasing this prefix by one increases the resulting palindrome, so prefix order is exactly palindrome order.

**Translate a rank into a prefix**

The smallest legal $h$-digit prefix is $10^{h-1}$. Therefore, one-based query rank $k$ corresponds to prefix $10^{h-1}+k-1$. A prefix reaching $10^h$ has too many digits, proving that the requested palindrome does not exist and must produce `-1`.

For an in-range prefix, convert it to decimal text and append the appropriate reversed portion. This creates exactly $\ell$ digits, preserves a nonzero leading digit, and is palindromic by construction. Because the rank-to-prefix mapping is consecutive and order-preserving, it returns precisely the requested smallest-order palindrome.

## Complexity detail

Let $q=\lvert\texttt{queries}\rvert$ and $\ell=\texttt{intLength}$. Each query mirrors $O(\ell)$ digits, for $O(q\ell)$ total time.

The returned list uses $O(q)$ space and one temporary decimal representation uses $O(\ell)$ space, giving $O(q+\ell)$ including output.

## Alternatives and edge cases

- **Enumerate integers:** Testing successive $\ell$-digit numbers for palindromicity is prohibitively slow because most numbers are not palindromes.
- **Generate all palindromes first:** Materializing the complete prefix range can use far more time and memory than the requested ranks require.
- **Build each rank from the first:** Advancing through every preceding prefix separately for each query is correct but quadratic in large query ranks.
- **Odd length:** The center digit is mirrored only once.
- **Even length:** Every prefix digit participates in both halves.
- **One digit:** Prefixes `1` through `9` are the only results; rank ten is out of range.
- **Oversized query:** It returns `-1` independently without affecting other answers.
