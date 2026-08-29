## General

The array has at most 19 elements, so the source enumerates which elements belong to B. For each B choice, all remaining elements must be split between A and C.

The difficult inner split is reduced to a maximum subset-XOR problem through a bitwise identity, then solved with a linear XOR basis.

**Precompute XOR and AND for every subset**

There are `2^n` masks. For each nonzero `mask`:

- `bit = mask & -mask` extracts one selected element;
- `previous = mask ^ bit` removes it;
- `index` identifies the corresponding array value.

Then:

`subset_xor[mask] = subset_xor[previous] ^ nums[index]`.

For AND, the first element must initialize the value because the problem defines empty AND as zero:

`nums[index] if previous==0 else subset_and[previous] & nums[index]`.

Thus both aggregate values are available in constant time for any later mask.

**Enumerating B through its complement**

The loop variable `outside_b` is the set of elements not assigned to B. It is exactly `A union C`.

The actual B mask is:

`b_mask = full_mask ^ outside_b`.

Because `full_mask` has all n low bits set, XOR here computes the subset complement.

This enumeration includes empty B and empty outside-B, matching the permission for all three subsequences to be empty.

**Fix B and simplify the A/C objective**

For a fixed `outside_b`, let:

- `T = XOR(A union C) = subset_xor[outside_b]`;
- `X = XOR(A)`.

Since A and C partition the outside set:

`XOR(C) = T ^ X`.

The two XOR contributions are:

`X + (T ^ X)`.

Consider one bit.

- If T's bit is 1, X and `T^X` have opposite bits, contributing exactly one at that bit regardless of X.
- If T's bit is 0, both expressions have X's bit, contributing twice that bit's value when X has 1.

Therefore:

$$
X+(T\oplus X)=T+2\bigl(X\mathbin{\&}\lnot T\bigr).
$$

For fixed outside set, T is constant. Maximizing the A/C split only requires maximizing X on bit positions where T has zero.

**The keep-bit mask**

All input values are below `2^30`. `value_mask=(1<<30)-1` contains thirty 1 bits.

`keep_bits = value_mask ^ total_xor`

is the 30-bit complement of T: it has 1 exactly where T has 0.

For any chosen A:

$$
XOR(A)\ \&\ keep\_bits
=
XOR\bigl(\{nums[i]\ \&\ keep\_bits:i\in A\}\bigr).
$$

Masking each vector before XOR therefore preserves exactly the projected value that must be maximized.

**Building a linear XOR basis**

The source inserts every masked value from `outside_b` into a 30-slot basis. `basis[p]`, when nonzero, has highest set bit p.

To insert `value`:

- inspect its highest set bit `pivot`;
- if a basis vector already owns that pivot, XOR it away;
- otherwise store the value at that pivot and stop.

If the value reduces to zero, it is XOR-dependent on existing vectors and adds no new achievable subset XOR.

The resulting basis spans exactly all XOR values obtainable by choosing a subset A of the outside elements.

**Extracting the maximum subset XOR**

Starting from zero, pivots are considered from bit 29 down to 0. The source replaces the current value by its XOR with a basis vector only when that makes the integer larger.

At each highest undecided bit, this greedily chooses whether to set it without disturbing any higher bit already optimized. The final `best_projected_xor` is the largest achievable projected `XOR(A)`.

The elements selected for A need not be reconstructed because only the maximum numeric value is requested. Every unselected outside element belongs to C.

**Combining all three parts**

For this B choice, the best objective is:

`subset_and[b_mask] + total_xor + 2*best_projected_xor`.

The first term is AND(B). The other terms come from the XOR identity. Taking the maximum over every `outside_b` examines every possible B and optimizes every A/C split, so it covers every legal partition.

**Empty-subsequence behavior**

If B is empty, `subset_and[0]=0` as required. If outside-B is empty, T and the basis maximum are zero, corresponding to A and C both empty.

Within a nonempty outside set, the linear basis includes the empty A subset producing XOR zero; C then receives all outside elements. It also permits A to receive all elements and C to be empty.

**Following a conceptual fixed-B example**

Suppose outside-B has total XOR T. Bits where T is one contribute T's bit exactly once to `XOR(A)+XOR(C)` regardless of the split. Only zero bits of T can contribute twice, and the basis chooses A to maximize those doubled positions.

This explains why maximizing raw `XOR(A)` would be wrong: a large bit already set in T cannot improve the sum, because assigning it to A merely removes it from C.


Every partition maps to exactly one B mask and one A subset of its complement. For that fixed B, the identity rewrites the objective without approximation. The basis enumerates the linear span of all possible A XORs and greedily returns its maximum under the exact relevant-bit projection.

Thus the computed candidate is at least every partition with that B and is achievable by some A/C split. Maximizing candidates over all B masks yields exactly the global optimum.

## Complexity detail

Let `n<=19` and `W=30` bit positions.

Subset aggregate preprocessing costs `O(2^n)` time and stores two arrays of length `2^n`.

For each of `2^n` outside masks, up to `n` values are inserted into a basis, with up to `W` eliminations each. Basis maximization costs `O(W)`. The faithful bound is:

$$
O(Wn2^n),
$$

which is `O(n2^n)` when the 30-bit width is treated as constant. The manifest's `O(n^2 2^n)` is a looser bound rather than the exact fixed-width operation count.

The subset arrays use `O(2^n)` space. Each iteration's basis has 30 integers, so total auxiliary space is `O(2^n)`.

## Alternatives and edge cases

- **Enumerate all three assignments:** There are `3^n` partitions; the B-mask plus basis method is substantially smaller.
- **Enumerate A submasks for every B:** This also approaches `3^n` total submask work.
- **Linear basis without projection:** It can maximize XOR(A) but not necessarily the sum `XOR(A)+XOR(C)`; masking out T's one bits is essential.
- **B empty:** AND contributes zero by contract.
- **A empty:** Its XOR is zero and C receives the outside set.
- **C empty:** A receives the whole outside set.
- **Outside-B empty:** Both XOR terms are zero and only AND(B) remains.
- **Single element:** Enumeration can place it in whichever subsequence gives the largest valid contribution.
- **Dependent masked values:** Basis insertion reduces them to zero, correctly recognizing they add no new XOR possibilities.
- **Duplicate values:** They may cancel under XOR and are handled by linear dependence.
- **Thirty-bit bound:** `value_mask` is correct because values are at most `10^9 < 2^30`.
- **Empty AND initialization:** The special first-element recurrence avoids incorrectly ANDing from zero.
- **No reconstruction:** The source returns only the best value, not the chosen partition.
- **Input preservation:** It precomputes subset data without modifying `nums`.
