## General

**The legal states follow Gray-code order**

The bit-changing rules look unusual because a higher bit can flip only when the bit immediately below it is one and every still-lower bit is zero. These conditions generate the standard reflected Gray-code path.

A Gray-code sequence lists non-negative integers so consecutive encoded values differ in exactly one bit. The standard encoding of ordinary index `r` is:

$$
G(r)=r\oplus(r\mathbin{\texttt{>>}}1).
$$

Under the problem’s stricter operation condition, the transitions from `G(r)` to `G(r+1)` flip exactly the bit that is legal at that state. The reflected construction alternates the rightmost bit and permits a higher-bit flip only at the required lower-bit pattern.

The operations are reversible: if a bit may be flipped from one state to the next, flipping it again returns to the previous state under the corresponding condition. Thus reducing state `n` to zero requires finding the ordinary index `r` whose Gray encoding is `n`. That index is the distance from `G(0)=0` along the unique legal Gray-code path.

The exact source performs this inverse Gray-code conversion.

**Inverting the Gray encoding**

Suppose the Gray bits of `n` from most significant to least significant are $g_m,g_{m-1},\ldots,g_0$, and the desired ordinary answer bits are $b_m,\ldots,b_0$.

From the encoding:

$$
g_k=b_{k+1}\oplus b_k,
$$

where a nonexistent bit above the most significant position is zero. Solving from the top gives:

$$
b_k=g_m\oplus g_{m-1}\oplus\cdots\oplus g_k.
$$

Each answer bit is the XOR of the input’s bit at that position and every more significant input bit.

**Why XORing shifted copies computes those prefixes**

The loop starts `ans = 0`. On each iteration it performs `ans ^= n` and then `n >>= 1`.

Across the full loop, the final expression is:

$$
\text{original }n
\text{ XOR }(n\mathbin{\texttt{>>}}1)
\text{ XOR }(n\mathbin{\texttt{>>}}2)
\cdots
$$

until the shifted value becomes zero.

At answer bit position `k`, the unshifted term contributes original bit `k`, the one-step term contributes original bit `k+1`, and so on. Their XOR is exactly the prefix-parity formula for inverse Gray code.

No operator precedence ambiguity occurs in the source because the operations are separate assignments.

**A trace for six**

Six is binary `110`.

- Start `ans = 000`. XOR with `110` gives `110`. Shift `n` to `011`.
- XOR `110` with `011` to get `101`. Shift `n` to `001`.
- XOR `101` with `001` to get `100`. Shift `n` to zero.

Binary `100` is four, matching the minimum four operations in the example.

For three, binary `11` XOR shifted `1` equals `10`, which is two operations.

**Why zero works without a branch**

If the input is zero, the `while n` condition is false immediately. `ans` remains zero and is returned. Zero already needs no operation.

**Connection to the recurrence**

Another derivation considers the most significant set bit at position `k`. Reducing the pure power $2^k$ takes $2^{k+1}-1$ operations. If lower bits form remainder `r`, they represent progress along that reflected path, producing:

$$
A(n)=2^{k+1}-1-A(r).
$$

Processing bits from least significant to most significant can evaluate this recurrence iteratively. The inverse-Gray XOR formula is its compact bit-parallel form: every set bit toggles how lower contributions reflect.

**Why this is the minimum, not just a valid count**

The reflected Gray sequence enumerates the states in the exact order permitted by the operation constraints, beginning at zero. Each move changes one legal bit. A state’s inverse Gray index therefore supplies a sequence of that many reverse moves to zero.

Because the legal transition structure follows this path, reaching zero in fewer moves would place the same state at a smaller index, contradicting the one-to-one Gray encoding. The decoded index is the minimum operation count.

## Complexity detail

Let $B=\lfloor\log_2 n\rfloor+1$ be the number of bits when $n>0$.

Each loop iteration right-shifts `n` once, so there are exactly $B$ iterations. Under the conventional fixed-width integer model, XOR and shift are constant-time operations, giving $O(\log n)$ time.

The source stores only `ans` and the progressively shifted `n`, so auxiliary space is $O(1)$ under the same model. With arbitrary-precision bit-cost accounting, early XORs touch $O(B)$ bits and total bit-operation cost is higher, but the package and interview model treats bounded integers as constant-size words.

## Alternatives and edge cases

- **Most-significant-bit recursion:** Use $A(n)=2^{k+1}-1-A(n\oplus2^k)$. It is educational but can take $O(\log^2 n)$ time if each recursive call rescans for its highest bit.
- **Iterative reflected recurrence by bit position:** Scan set bits from low to high and update `ans = (1 << (k + 1)) - 1 - ans`. It runs in $O(\log n)$ time and expresses the same mathematics.
- **Breadth-first search over integers:** It can find shortest paths for tiny values but explores an enormous state space and ignores the Gray-code structure.
- **Greedily clear the highest set bit:** A high bit may not be legally flippable until lower bits reach a precise pattern, so ordinary popcount reasoning fails.
- **Input zero:** The loop does not execute and returns zero.
- **Power of two:** Inverse Gray decoding returns $2^{k+1}-1$, the full reflected traversal needed to clear that bit.
- **All low bits set:** Successive XORed shifts alternate prefix parity and correctly reflect the recursive subtractions.
- **Operation reversibility:** It justifies measuring distance from zero to `n` instead of explicitly reducing `n` to zero.
- **Destructive local shift:** The parameter variable `n` is reduced to zero inside the method, but integers are immutable objects passed by value reference; the caller’s integer is unaffected.
- **Fixed-width assumption:** The stated $O(1)$ space and word-operation costs follow standard analysis for values bounded by $10^9$.
- **No simulation output:** The method returns only the minimum count, so it does not reconstruct the actual sequence of flipped bits.
- **XOR versus addition:** Prefix parity requires XOR; adding shifted copies would introduce carries and produce unrelated values.
