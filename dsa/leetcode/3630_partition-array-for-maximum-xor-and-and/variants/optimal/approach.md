## General

**Choose the AND subsequence first.** Enumerate a mask $U$ containing exactly the elements that do not belong to `B`; its complement uniquely specifies `B`. Precompute the XOR and AND of every subset so the contribution `AND(B)` and the total XOR of $U$ are available in constant time. The empty `B` mask keeps the problem-defined AND value zero.

**Reduce the two XOR groups to one projected subset XOR.** For fixed $U$, let $T$ be the XOR of all its elements and let $x$ be `XOR(A)`. Because `C` contains the remaining elements, `XOR(C) = T xor x`. Bit by bit,

$$
x + (T \mathbin{\mathrm{xor}} x)
= T + 2\bigl(x \mathbin{\mathrm{and}} \mathord{\sim}T\bigr).
$$

Bits set in $T$ contribute exactly once regardless of which XOR group receives them. Only bits absent from $T$ can contribute twice, so maximizing the split is equivalent to maximizing `x & ~T`.

**Use a linear basis for every fixed complement of B.** Mask every value in $U$ by the bits absent from $T$. Masking commutes with XOR, so the possible projected values are precisely the subset XORs of these masked numbers. Insert them into a binary linear basis, then greedily combine basis vectors from the highest pivot downward to obtain the maximum projected XOR.

For this $U$, add `AND(B)`, $T$, and twice that maximum. Every partition appears once because its elements outside `B` define one enumerated mask and its choice of `A` is represented in the linear span; `C` is then forced. Taking the maximum therefore considers all valid partitions.

## Complexity detail

Let $n$ be the number of elements. There are $2^n$ choices for the elements outside `B`. Building a basis inserts at most $n$ values and each insertion can eliminate against at most $n$ pivots, giving $O(n^2 2^n)$ time. The fixed 30-bit greedy basis scan is absorbed by this bound.

The two subset-aggregate tables use $O(2^n)$ space. The basis and other per-mask state use $O(n)$ additional space, so total auxiliary space is $O(2^n)$.

For benchmarking, $S=2^n$. The accepted method is $O(n^2S)$, whereas assigning every element directly to one of three groups takes $O(n3^n)$ time.

## Alternatives and edge cases

- **Enumerate all three-way assignments:** This is a direct and reliable correctness baseline, but its $3^n$ state count grows too quickly.
- **Enumerate A inside every complement of B:** Trying every submask separately also totals $3^n$ work; the linear basis compresses all attainable XORs.
- **Dynamic programming over aggregate values:** Values reach $10^9$, so a table indexed by XOR or AND values has no practical bounded range.
- **Empty subsequences:** Empty XOR and empty AND are both zero under this contract and must not use the usual all-bits-set AND identity.
- **Duplicate values:** Equal elements remain distinct partition choices even though XOR may cancel them.
- **One element:** Assigning it to any one nonempty group produces its value, while the other two groups contribute zero.
- **Large result:** The sum can exceed a signed 32-bit integer even though each input value does not.
