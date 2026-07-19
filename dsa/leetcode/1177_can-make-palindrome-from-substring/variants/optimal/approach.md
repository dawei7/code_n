## General
**Keep only frequency parity.** Rearrangement makes character order irrelevant. A palindrome can pair every character occurrence except possibly one center occurrence, so only the characters with odd frequencies matter. If a substring has $x$ odd-frequency character types, one replacement can turn two odd frequencies even by changing an occurrence of one type into another. The minimum replacements is therefore $\lfloor x/2\rfloor$.

**Encode a prefix in 26 bits.** Assign one bit to each lowercase letter. Begin with prefix mask `0`; for every character, XOR its bit into the previous mask. A bit is set exactly when that character has appeared an odd number of times in the prefix.

**Cancel the part before each query.** For `[left, right, k]`, compute `masks[right + 1] ^ masks[left]`. Equal prefix parities cancel under XOR, leaving precisely the odd-frequency bits in the inclusive substring. `bit_count()` yields $x$, and the answer is whether `x // 2 <= k`. The string remains unchanged, so the same prefix masks answer every query.

## Complexity detail
Building $n+1$ prefix masks takes $O(n)$ time. Each query uses a constant number of integer bit operations over the fixed 26-letter alphabet, so all queries take $O(q)$ time. The total is $O(n+q)$ time and the prefix array uses $O(n)$ auxiliary space; the returned answers are output storage.

## Alternatives and edge cases
- **Count each queried substring directly:** This is correct but costs time proportional to every substring length and can take $O(nq)$ overall.
- **Twenty-six prefix-count arrays:** Subtracting counts per letter also gives $O(n+q)$ time because the alphabet is fixed, but uses more storage and operations than parity masks.
- **Odd-length substring:** One odd-frequency character may occupy the center without any replacement.
- **Even-length substring:** Every frequency must ultimately be even, which is still captured by `x // 2` because $x$ is even for an even total length.
- **Single character:** It is already a palindrome, even with `k = 0`.
- **Large budget:** A budget at least half the substring length always suffices.
- **Independent queries:** A replacement considered for one answer never modifies `s` for a later query.
