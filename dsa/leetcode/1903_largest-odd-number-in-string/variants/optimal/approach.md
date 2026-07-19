## General
**An odd substring must end at an odd digit.** Decimal parity depends only on the final digit. Scan `num` from right to left to locate the last occurrence of `1`, `3`, `5`, `7`, or `9`. If none exists, no nonempty odd substring is possible.

**Use the entire prefix through that digit.** For a fixed odd ending position, starting at index zero yields at least as many digits as any later start. Because the original string has no leading zero, a longer decimal representation has a larger numeric value than every shorter one. Among odd ending positions, the rightmost one gives the longest prefix. Therefore `num[:index + 1]` at the first odd digit encountered from the right is globally optimal.

This argument uses only digit positions; converting the potentially $10^5$-digit input to an integer is unnecessary.

## Complexity detail
The backward scan examines at most $n$ digits, and copying the returned prefix also takes at most $O(n)$ time, so total time is $O(n)$. The scan itself uses $O(1)$ auxiliary space. The returned string can contain $n$ characters, making total output-inclusive space $O(n)$.

## Alternatives and edge cases
- **Enumerate every substring:** Testing and comparing all candidates requires at least quadratic enumeration and unnecessary large-string work.
- **Convert `num` to an integer:** The input may exceed fixed-width limits, and numeric conversion does not help locate the optimal substring.
- **All digits even:** Return `""`; zero is not odd.
- **Last digit odd:** Return the complete input immediately.
- **Only the first digit odd:** The answer is that one-character prefix.
- **Internal zeros:** They remain ordinary digits inside the selected prefix and do not affect parity unless one is last.
