## General

**Focus on boundaries between adjacent characters**

The final string is all equal exactly when every adjacent pair is equal.

For each boundary $i$ between positions $i-1$ and $i$, the initial boundary is:

- satisfied when `s[i - 1] == s[i]`;
- mismatched when the two characters differ.

The solution charges each mismatched boundary independently.

**What one prefix inversion changes**

Inverting prefix positions zero through $i-1$ costs $i$.

Inside that prefix, both endpoints of every internal adjacent pair are inverted, so their equality or inequality does not change. Outside it, neither endpoint changes.

Only the boundary between $i-1$ and $i$ has exactly one endpoint inverted. Therefore this operation toggles precisely boundary $i$.

**What one suffix inversion changes**

Inverting suffix positions $i$ through $n-1$ costs $n-i$.

Again, internal suffix pairs have both characters inverted and outside pairs have neither. Only boundary $i$ has one endpoint changed.

Thus either the prefix ending at $i-1$ or suffix starting at $i$ can toggle the same boundary, with respective costs $i$ and $n-i$.

**Why a differing boundary must be toggled oddly**

If two adjacent bits begin different, they must end equal.

Inverting exactly one endpoint toggles their equality state. An odd number of boundary toggles changes different to equal, while an even number leaves it different.

At least one toggle is necessary. More than one odd toggle adds avoidable positive cost, so an optimum toggles that boundary once using the cheaper operation.

**Why an equal boundary needs no charge**

An initially equal pair already has the desired final relation.

It needs an even number of toggles; zero is the cheapest even number. Paying to toggle it twice cannot improve any other boundary because each permitted operation toggles only its own endpoint boundary relation.

Therefore equal boundaries contribute zero.

**Derive the exact sum**

For every $i$ from one through $n-1$, if adjacent characters differ, the minimum cost to fix that boundary is:

$$
\min(i,n-i).
$$

The code adds that quantity to `ans`.

No dynamic state about the current flipped string is necessary because boundary effects are independent and compose by parity.

**Trace `"0011"`**

Only boundary $i=2$ differs: positions one and two are zero and one.

The two possible costs are prefix length two and suffix length two. The formula adds two.

Inverting the suffix beginning at index two changes `"11"` to `"00"`, yielding `"0000"`.

**Trace alternating length six**

In `"010101"`, every boundary differs.

The costs are:

$$
\min(1,5)+\min(2,4)+\min(3,3)+\min(4,2)+\min(5,1)
=1+2+3+2+1=9.
$$

The sum matches the example's achievable sequence.

**Why independent boundary choices produce a valid string**

Apply one chosen prefix or suffix operation for every initially differing boundary.

Each such operation toggles only its associated adjacency relation. Consequently every differing boundary becomes equal and every initially equal boundary remains equal.

When all adjacent pairs are equal, transitivity means every character in the binary string is the same, though the common final bit may be either zero or one.

This remains true even when two chosen operations overlap across many character positions. Overlap may invert an individual character several times, but it does not create hidden interference between boundaries: for any boundary other than an operation's endpoint, either both adjacent characters belong to that operation or neither does. Their equality relation is therefore preserved. Thinking in terms of relations, instead of the temporary character values, is what makes the apparently global operations independent.

**Lower bound and construction prove optimality**

Every differing boundary requires at least one operation that toggles it, costing at least the cheaper of its prefix and suffix options.

Summing gives a lower bound because one operation cannot toggle two distinct boundaries.

Choosing the cheaper operation once for each differing boundary achieves exactly that sum and makes all boundaries equal. The lower bound is attainable, so it is the minimum.

**Why the target bit need not be chosen**

One might try two separate calculations: make everything zero or make everything one.

The boundary formulation avoids this. The goal only requires equality, and fixing all adjacent relations automatically yields one of those two constant strings at the globally minimum cost.

## Complexity detail

The loop examines each of the $n-1$ boundaries once and performs constant arithmetic. Total time is $O(n)$.

Only `ans`, `n`, and the loop index are stored, so auxiliary space is $O(1)$. The immutable input string is not changed.

## Alternatives and edge cases

- **Dynamic programming for target zero and one:** Can solve the problem but stores more state than the independent-boundary proof needs.
- **Simulate greedy flips on characters:** Risks repeatedly touching long prefixes or suffixes and obscures cost optimality.
- **Length one:** No boundary exists, so cost is zero.
- **Already all equal:** No boundary differs and the sum is zero.
- **One transition:** Pay the shorter side length.
- **Middle boundary:** Prefix and suffix costs may tie; either operation is optimal.
- **Near-left boundary:** Prefix inversion is usually cheaper.
- **Near-right boundary:** Suffix inversion is usually cheaper.
- **Alternating string:** Every boundary contributes.
- **Final common bit:** Need not be predetermined.
- **Binary alphabet:** Inverting one endpoint always toggles equality for a pair.
- **Input preservation:** The method computes cost without applying operations to `s`.
