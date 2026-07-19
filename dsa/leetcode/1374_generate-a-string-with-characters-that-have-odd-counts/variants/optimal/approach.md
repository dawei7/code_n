## General
**Use parity to choose the number of characters.** If `n` is odd, repeating one letter exactly `n` times already gives an odd frequency. If `n` is even, reserve one position for a second letter and fill the other $n-1$ positions with the first letter. Both $n-1$ and $1$ are odd.

The construction therefore returns `"a" * n` for odd `n`, and `"a" * (n - 1) + "b"` for even `n`. Its length is exactly `n`, it uses only lowercase English letters, and every character it includes has an odd count, so it satisfies the full contract.

## Complexity detail
Creating the returned string writes `n` characters, so the time is $O(n)$. The returned string occupies $O(n)$ space; apart from that output, the construction uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Distribute several odd counts:** Any collection of positive odd frequencies summing to `n` is valid, but it adds bookkeeping without improving the bound.
- **Repeated concatenation:** Adding one character in each loop can repeatedly copy an immutable string and take $O(n^2)$ time.
- **Odd `n`:** A single repeated character is sufficient because its total count is already odd.
- **Even `n`:** One character cannot occur an even total number of times, so split the length into $n-1$ and $1$.
- **Minimum input:** For `n = 1`, returning `"a"` is valid.
- **Non-uniqueness:** The examples and reference use `a` and `b`, but the problem accepts any lowercase construction with the required frequencies.
