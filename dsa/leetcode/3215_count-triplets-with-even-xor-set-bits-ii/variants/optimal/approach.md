## General

**Compress each integer to popcount parity.** The arrays can each contain $10^5$ values, so enumerating all index triplets would be impossible. The condition does not require the exact XOR value; it asks only whether that value has an even number of set bits.

Define

$$
p(x)=\operatorname{popcount}(x)\bmod2.
$$

The source computes this as `x.bit_count() & 1`. Result zero means even popcount, and result one means odd popcount. Each entire array can be summarized by two frequencies.

`cnt1`, `cnt2`, and `cnt3` are `Counter` objects holding those frequencies for `a`, `b`, and `c`. Regardless of input size, each has at most keys zero and one.

**Prove parity distributes through XOR.** Popcount parity is the XOR of all individual bits in a number. For two values,

$$
p(x\mathbin{\mathrm{XOR}}y)=p(x)\mathbin{\mathrm{XOR}}p(y).
$$

At each bit position, XOR is addition modulo two. Summing those result bits modulo two is the same as adding the parity contributions from both inputs; duplicated one bits cancel.

Applying the identity to three values gives

$$
p(x\mathbin{\mathrm{XOR}}y\mathbin{\mathrm{XOR}}z)
=p(x)\mathbin{\mathrm{XOR}}p(y)\mathbin{\mathrm{XOR}}p(z).
$$

The final XOR has even popcount exactly when the number of odd-popcount operands is even: zero or two.

**Enumerate eight parity triples.** The nested loops consider each `i,j,k` in $\{0,1\}^3$. Only four patterns qualify:

$$
(0,0,0),\quad(0,1,1),\quad(1,0,1),\quad(1,1,0).
$$

For a qualifying pattern, the number of indexed triplets is

`cnt1[i] * cnt2[j] * cnt3[k]`.

This multiplication applies the product rule: choose any matching index from the first array, independently any matching index from the second, and any from the third. Equal numeric values at different indices remain separate choices because their frequency contributes multiplicatively.

**Decode the source's condition.** It writes:

`if (i + j + k) & 1 ^ 1:`

Python evaluates bitwise AND before bitwise XOR, so this means

`((i + j + k) & 1) ^ 1`.

`& 1` obtains the sum parity. XOR with one flips it: even becomes integer one, which is truthy, and odd becomes zero, which is false. The body therefore executes exactly for the four patterns above.

An explicit comparison to zero would be easier to read, but the exact expression is correct under Python's precedence rules.

**Why the frequency sum is exact.** Every value has exactly one parity class, so every index triplet belongs to exactly one of the eight loop combinations. The parity identity proves it is valid exactly when its combination is among the four added. The classes are disjoint, preventing double counting, and exhaustive, preventing omissions.

For `a=[1]`, `b=[2]`, and `c=[3]`, popcounts are one, one, and two, giving parity pattern $(1,1,0)$. It qualifies. Their XOR is zero, whose popcount is zero; zero is even.

In `a=[1,1]`, the two equal values contribute frequency two to the odd class. A qualifying product containing that class counts both possible `a` indices, explaining why duplicate-looking numeric triplets can correspond to separate indexed answers.

**Why this version scales.** The “II” constraints allow up to $10^5$ values per array and values up to $10^9$. The method never loops over pairs or triplets of elements. It scans each array once and then performs exactly eight constant-size combinations.

## Complexity detail

Let

$$
N=\lvert a\rvert+\lvert b\rvert+\lvert c\rvert.
$$

Each input value is visited once. Values are at most $10^9$, so `bit_count` examines a fixed bounded number of machine-word bits and is constant-time under the problem model. Building all counters takes $O(N)$ time. The final eight iterations are $O(1)$, giving total $O(N)$ time.

Each counter has at most two keys, so auxiliary space is $O(1)$. The answer can reach $\lvert a\rvert\lvert b\rvert\lvert c\rvert$, up to $10^{15}$ under the constraints. Python integers represent it exactly.

For unbounded arbitrary-precision integers, bit counting would additionally depend on bit length, but that is outside the stated value range.

## Alternatives and edge cases

- **Closed four-product expression:** Name even/odd counts and directly sum `Ea*Eb*Ec + Ea*Ob*Oc + Oa*Eb*Oc + Oa*Ob*Ec`. It is equivalent and removes the compact parity-loop condition.
- **Combine two parity distributions first:** Convolve the two two-element parity counts, then match even pair parity with even `c` and odd pair parity with odd `c`. This generalizes cleanly to more arrays.
- **Enumerate all triplets:** $O(|a||b||c|)$ time is infeasible at the II constraints.
- **Count exact XOR values:** A frequency map of full values retains far more state than the one parity bit needed.
- **XOR result zero:** Its set-bit count is zero, which is even, so it qualifies.
- **All three classes even:** Every index triplet qualifies.
- **All three classes odd:** Three odd parities combine to odd, so no triplet qualifies.
- **Exactly one odd class:** The XOR popcount parity is odd, so those products are skipped.
- **Exactly two odd classes:** Their parity cancels to even, so the product is added.
- **Duplicate values:** Indices define choices; counters preserve multiplicity rather than deduplicating values.
- **Missing parity key:** `Counter` returns zero, so all eight combinations can be evaluated without membership checks.
- **Value zero:** `0.bit_count()` is zero and belongs to the even class.
- **Large result:** The count can far exceed 32-bit range even though individual values are small.
- **Operator precedence:** Rewriting the condition without preserving parentheses can invert or otherwise change its meaning.
- **Input preservation:** The method only iterates over all three arrays and does not mutate them.
