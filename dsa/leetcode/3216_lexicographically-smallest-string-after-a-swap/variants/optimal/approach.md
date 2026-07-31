## General

**Focus on the earliest changed position.** Lexicographic order is determined at the first position where two strings differ. Therefore, a beneficial swap beginning at an earlier index always beats every result whose first change occurs later. It is enough to inspect adjacent pairs from left to right.

**Recognize a beneficial legal pair.** A pair can be swapped only when both digits have the same parity. At a fixed index there is only one possible adjacent partner, and the swap improves the string exactly when the left digit is greater than the right digit. Thus the first same-parity inversion is the best possible operation: it decreases the earliest position at which any legal swap can decrease the string.

Convert the string to a mutable list, scan its adjacent pairs, and swap the first pair satisfying both conditions. Stop immediately because any later change would be lexicographically less important. If no such pair exists, leaving the string unchanged is optimal.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. The scan examines at most $n-1$ adjacent pairs, and constructing the returned string also takes $O(n)$ time. The mutable digit list and returned string use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate every legal swap:** Constructing and comparing a complete string for each same-parity pair is correct, but repeated string copies can require $O(n^2)$ time.
- **Swap the smallest later same-parity digit:** This is invalid because the operation permits only adjacent digits; a smaller digit farther away cannot be moved in one operation.
- Equal adjacent digits may be swapped legally, but doing so has no effect and must not prevent a later beneficial swap.
- Adjacent digits of different parity cannot be swapped even when they form an inversion.
- If several beneficial swaps exist, the leftmost one is optimal because it improves an earlier position.
- If no legal inversion exists, the original string is already the smallest reachable result.
