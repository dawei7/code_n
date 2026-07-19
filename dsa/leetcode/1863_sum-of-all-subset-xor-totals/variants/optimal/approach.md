## General
**Count one bit across all subsets**

Consider a bit that is set in at least one array element, and choose one index
whose value contains that bit. Pair every subset that omits this chosen index
with the subset obtained by adding it. The chosen bit is toggled between the
two XOR totals, so exactly one member of every pair has that bit set. Therefore
the bit contributes to exactly $2^{n-1}$ subset XOR totals.

If a bit is absent from every input value, no subset can contain it in its XOR.
Thus the bits that contribute are precisely those set in the bitwise OR of all
elements. Multiplying that OR by $2^{n-1}$ adds each contributing bit's value
the correct number of times:

$$
\text{answer}
=
\left(\bigvee_{x \in \texttt{nums}} x\right)2^{n-1}.
$$

Compute the OR in one pass, then shift it left by $n-1$. The pairing is based
on indices, so it remains valid when multiple positions hold equal values.

## Complexity detail
The OR pass inspects all $n$ values once and the final shift is constant time,
giving $O(n)$ time. Only the accumulated bit mask is stored, so auxiliary space
is $O(1)$.

## Alternatives and edge cases
- **Backtracking over subsets:** carrying the current XOR through include/skip
  branches is correct but takes $O(2^n)$ time.
- **Bitmask enumeration:** evaluating every mask is iterative but still
  exponential and may spend another factor of $n$ rebuilding each XOR.
- The empty subset contributes zero and therefore does not change the sum.
- Equal-valued elements at different indices create separately counted
  subsets even when their selected value lists look identical.
- For a one-element array, the answer is the element itself.
