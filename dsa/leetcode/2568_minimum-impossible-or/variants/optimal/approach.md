## General

**OR can add bits but can never remove them**

The bitwise OR of selected numbers has a one in every bit position that is one in at least one selected number. Once an unwanted bit appears, no later OR operation can turn it back to zero.

This makes powers of two special. The number $2^k$ has exactly one set bit, at position $k$. To express exactly $2^k$, every chosen number must contain no set bit outside position $k$, and at least one chosen number must contain bit $k$. Because all input numbers are positive, the only number satisfying both conditions is $2^k$ itself.

Therefore:

$$
2^k\text{ is expressible if and only if }2^k\text{ appears in }\texttt{nums}.
$$

Combining other numbers cannot manufacture a missing single-bit value. Any number carrying bit $k$ plus some additional bit would make the OR larger and different from $2^k$.

**Why the first missing power of two is the answer**

Suppose $2^k$ is the first power of two absent from the array. It is impossible to express by the single-bit argument above.

Now consider any positive integer $x<2^k$. Its binary representation uses only bit positions $0$ through $k-1$. Because $2^k$ is the first missing power, all values

$$
1,2,4,\ldots,2^{k-1}
$$

are present in `nums`. Select the power of two corresponding to each set bit of $x$. ORing those selected values reconstructs $x$ exactly.

For example, if $x=13$, its binary representation is `1101`, so

$$
13=8\mathbin{|}4\mathbin{|}1.
$$

If $1$, $4$, and $8$ are present, $13$ is expressible. This construction works for every smaller positive value. Hence the first missing power of two is not merely impossible; every positive integer below it is possible. It is exactly the minimum impossible OR.

**How the implementation finds that power**

The code builds `s = set(nums)`, allowing expected $O(1)$ membership tests. It then generates powers `1 << i` for $i$ from $0$ through $31$ and returns the first one not in the set:

`next(1 << i for i in range(32) if 1 << i not in s)`.

Left-shifting one by $i$ places its only set bit at position $i$, producing $2^i$. The generator tests powers in strictly increasing order, so `next` returns the smallest missing one without generating later candidates.

For `nums = [2,1]`, both $1$ and $2$ are present. Their OR expresses $3$. Power $4$ is absent and cannot be assembled without also introducing some other bit, so the answer is $4$.

For `nums = [5,3,2]`, power $1$ is not an array element. Although both $5$ and $3$ contain their least-significant bit, each also contains another bit. OR cannot remove those extras, so neither can express $1$. The answer is immediately $1$.

**Why 32 tested bit positions are enough**

Every input value is at most $10^9$, which is less than $2^{30}$. Therefore no input can equal $2^{30}$ or a larger power. Even in the extreme case where every smaller relevant power from $2^0$ through $2^{29}$ appears, $2^{30}$ is guaranteed missing.

The range through index $31$ includes that guaranteed candidate, so the generator can never run out without returning. The two extra positions beyond the necessary upper boundary are harmless.

**Subsequence order does not matter for OR**

The definition speaks of a subsequence, which requires increasing indices. However, bitwise OR is associative and commutative. Any chosen set of distinct array occurrences can be listed in their existing index order, producing a valid subsequence with the same OR. The proof can therefore reason about which powers are present without tracking their positions.

Duplicates also add no expressive ability for OR: `x | x == x`. The set discards duplicates because membership of each exact power is the only information the solution needs.

**Why arbitrary non-power values are irrelevant to the minimum**

Numbers with multiple set bits may help express some composite values, but they cannot affect whether a single-bit power is expressible. Once the first absent power is identified, it already supplies an impossible candidate; the presence of all smaller powers separately proves every smaller integer expressible. No further analysis of composite input numbers is needed.

This is why a problem that appears to ask about exponentially many subsequences collapses to checking a short sequence of individual values.

## Complexity detail

Let $n$ be the number of input values. Building `set(nums)` takes expected $O(n)$ time and $O(n)$ space. The generator checks at most 32 powers, which is $O(1)$ time under the fixed integer bound. Total expected time is $O(n)$.

The manifest lists $O(1)$ space, but the exact checked-in implementation stores every distinct input value in a set, so its code-accurate auxiliary space is $O(n)$ in the worst case. A 32-bit presence mask could achieve true $O(1)$ space by recording only input values that are powers of two.

## Alternatives and edge cases

- **Bit-presence mask:** Record bit $k$ only when an input equals $2^k$. This preserves the proof and achieves $O(1)$ auxiliary space under the fixed 32-bit domain.
- **Enumerate subsequence OR values:** Maintaining all reachable OR results is much more expensive and unnecessary because the minimum answer is controlled by powers of two.
- **Sort the array:** Sorting does not help; exact membership of a few powers is enough, and a set supplies it directly.
- **Missing one:** If literal value $1$ is absent, the answer is always $1$, even when other numbers have their lowest bit set.
- **All small powers present:** Their subsequences express every number below the first missing higher power by selecting the set-bit components.
- **Duplicates:** Repeated copies do not change OR expressibility and are collapsed by the set.
- **Composite values:** They may express other composites but can never replace a missing single-bit power.
- **Guaranteed generator result:** The value $2^{30}$ exceeds the input maximum and is necessarily absent, so checking 32 positions is sufficient.
- **Expected set behavior:** The $O(n)$ time statement uses normal expected constant-time Python hash membership.
