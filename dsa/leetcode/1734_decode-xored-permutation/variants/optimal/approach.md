## General
**Recover the XOR of the complete permutation**

Because `perm` contains every integer from $1$ through $n$ exactly once, XORing that entire range gives the XOR of every unknown permutation entry. The order is irrelevant because XOR is associative and commutative.

**Cancel every value except the first**

XOR the encoded entries at odd zero-based indices: `encoded[1] ^ encoded[3] ^ ...`. These entries expand to

$$
(\texttt{perm[1]} \mathbin{\oplus} \texttt{perm[2]})
\mathbin{\oplus} \cdots \mathbin{\oplus}
(\texttt{perm[n-2]} \mathbin{\oplus} \texttt{perm[n-1]}),
$$

so they contain every permutation value except `perm[0]` exactly once. XORing this result with the XOR of $1$ through $n$ cancels all those shared values and leaves `perm[0]`. Odd $n$ is essential: it makes the remaining $n-1$ positions pair up in this pattern.

**Decode every following value**

Once the first value is known, invert the encoding relation from left to right with `perm[i + 1] = perm[i] ^ encoded[i]`. Each recovered value supplies the next one, so one pass reconstructs the unique permutation.

## Complexity detail
The range XOR, odd-index XOR, and forward reconstruction each perform linear total work, giving $O(n)$ time. The returned permutation contains $n$ integers and therefore uses $O(n)$ space; aside from that required output, the algorithm keeps only constant-size XOR accumulators.

## Alternatives and edge cases
- **Try every possible first value:** Decoding and validating a permutation for each candidate can take $O(n^2)$ time.
- **Gaussian elimination over bits:** The adjacent XOR equations are linear, but generic elimination ignores the permutation and odd-length structure and is unnecessarily expensive.
- **Smallest legal length:** For $n=3$, the single odd-index encoded entry still identifies the first value correctly.
- **Unordered permutation:** No assumption is made about increasing, decreasing, or random order.
- **Repeated encoded values:** Adjacent XOR results need not be unique even though permutation values are unique.
- **Large integer boundary:** Values up to $n$ participate directly in bitwise XOR without arithmetic overflow in Python.
