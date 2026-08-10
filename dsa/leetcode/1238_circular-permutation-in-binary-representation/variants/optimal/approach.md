## General

**Start with the standard reflected Gray-code cycle**

A Gray-code ordering lists every \(n\)-bit number exactly once while consecutive numbers differ in one bit. The standard formula for the Gray code of integer \(i\) is

\[
G(i)=i\oplus(i\mathbin{\text{>>}}1),
\]

where \(\oplus\) is bitwise XOR.

The list comprehension

`g = [i ^ (i >> 1) for i in range(1 << n)]`

evaluates this formula for every integer from zero through \(2^n-1\). `1 << n` is \(2^n\), so the list has exactly the required number of entries.

**Why every value appears exactly once**

The Gray transformation is invertible. The most significant binary bit of \(i\) equals the most significant bit of \(G(i)\). Moving downward, each original bit can be reconstructed from the preceding reconstructed bit and the corresponding Gray bit. Therefore, two different integers cannot produce the same Gray code.

There are \(2^n\) inputs and exactly \(2^n\) possible \(n\)-bit outputs. An injective mapping between these equally sized sets is a permutation, so `g` contains every value from zero through \(2^n-1\) once.

**Why consecutive Gray values differ in one bit**

When incrementing \(i\) to \(i+1\), suppose \(i\) ends in \(t\) one-bits. The increment changes those \(t\) trailing ones to zeros and changes the next zero to one. Thus `i ^ (i + 1)` has its lowest \(t+1\) bits set.

In the shifted values, the analogous XOR has its lowest \(t\) bits set. Since

\[
G(i)\oplus G(i+1)
=
\bigl(i\oplus(i+1)\bigr)
\oplus
\bigl((i\mathbin{\text{>>}}1)\oplus((i+1)\mathbin{\text{>>}}1)\bigr),
\]

the two low-bit runs cancel except for bit \(t\). The result has exactly one set bit, proving adjacent Gray values differ in exactly one binary position.

**Why the standard ordering is already circular**

The first Gray value is \(G(0)=0\). For \(i=2^n-1\), the \(n\)-bit representation is all ones, while its right shift has ones in the lower \(n-1\) positions. XOR leaves only the highest bit:

\[
G(2^n-1)=2^{n-1}.
\]

That differs from zero in exactly one bit. Therefore, the last and first entries also satisfy the adjacency rule.

**Rotate the cycle to begin at `start`**

Because `g` is a permutation, `start` occurs exactly once. `j = g.index(start)` finds its position. The return expression

`g[j:] + g[:j]`

moves the suffix beginning at `start` in front of the earlier prefix. The first returned value is consequently `start`.

Rotation does not destroy a cycle’s adjacency. Within each slice, neighboring pairs keep their original order. At the join between `g[-1]` and `g[0]`, the original circular edge is used. The new returned last value is `g[j - 1]`, which was adjacent to `g[j]` in the original sequence; that becomes the required wraparound edge back to the new first element.

**Following the two-bit example**

For \(n=2\), the generated codes are:

- \(G(0)=0\), binary `00`;
- \(G(1)=1\), binary `01`;
- \(G(2)=3\), binary `11`;
- \(G(3)=2\), binary `10`.

The cycle is `[0,1,3,2]`. If `start = 3`, its index is two, and rotation returns `[3,2,0,1]`. The binary sequence `11,10,00,01` changes one bit at each step, including `01` back to `11`.

**Why no search or backtracking is needed**

Constructing an arbitrary Hamiltonian cycle of the \(n\)-dimensional hypercube could be expressed as graph search, but Gray code gives one directly. Rotation makes any requested vertex the start without changing the cycle.

The output itself has \(2^n\) numbers, so a method returning an explicit list cannot asymptotically beat the linear-in-output construction time.

## Complexity detail

Let \(N=2^n\). Building `g` takes \(O(N)\) time. `g.index(start)` scans up to \(N\) entries. The two slices and concatenation copy \(N\) references overall. Total time is \(O(2^n)\).

`g` stores \(N\) integers. Slicing creates two additional lists and concatenation creates the returned list; peak memory is still \(O(N)\), or \(O(2^n)\). The output alone requires that much space.

## Alternatives and edge cases

- **Direct rotated Gray formula:** XOR every standard Gray value with `start`. Because XOR preserves Hamming distance and `G(0)=0`, `[start ^ G(i)]` is also a valid cycle beginning at `start`, avoiding the index search and slices while retaining \(O(2^n)\) output work.
- **Backtracking on the hypercube:** It can find a valid cycle but explores a large search space unnecessarily.
- **Minimum \(n=1\):** The standard cycle `[0,1]` or its rotation has one-bit adjacency in both directions.
- **Start equals zero:** `j` is zero, and the return reproduces the standard Gray list.
- **Start at the final Gray entry:** Rotation moves that entry first and preserves both join edges.
- **Every value unique:** Invertibility of the Gray transform guarantees `g.index(start)` finds exactly one occurrence.
- **Wraparound requirement:** Ordinary adjacent Gray-code proof is not enough by itself; the first and last standard codes differ in the highest bit, establishing circularity.
- **Output size:** At \(n=16\), the list contains 65,536 integers, which is within the stated bound but inherently requires linear output memory.
- **Bit-width:** All generated values are below \(2^n\) because XOR of \(n\)-bit quantities stays within \(n\) bits.
