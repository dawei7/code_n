## Function Contract

**Inputs**

- `nums`: The array from which any subset of indexed elements may be removed.
- `target`: The required XOR of the elements that remain.

Removing elements preserves the relative order of those retained, but XOR is order-independent. Equal values at different indices remain separate choices.

Let $n=\lvert\texttt{nums}\rvert$ and let $b=14$, the number of bits needed to represent every legal value and target. Every attainable subset XOR lies in $[0,2^b)$.

**Return value**

Return the smallest number of removed indices whose complementary retained subset has XOR `target`. Return `-1` when no retained subset—including the empty subset—has that XOR.
