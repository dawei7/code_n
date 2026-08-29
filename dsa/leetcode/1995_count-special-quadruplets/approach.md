## General

**Enumerate index quadruplets directly**

The exact source uses four nested loops. Each loop starts after the index chosen by the previous loop:

- `a` ranges up to `n - 4`;
- `b` starts at `a + 1`;
- `c` starts at `b + 1`;
- `d` starts at `c + 1`.

This construction guarantees `a < b < c < d` without an extra ordering test. Every increasing four-index combination appears exactly once.

For each combination, the code evaluates

`nums[a] + nums[b] + nums[c] == nums[d]`.

If true, it increments `ans`. Since quadruplets are defined by indices, equal values at different positions still produce distinct valid quadruplets, and the loops naturally count them separately.

**Why the loop bounds are chosen carefully**

The first index must leave room for three later positions, so its final possible value is $n-4$. Python's `range(n - 3)` stops just before $n-3$ and reaches exactly that endpoint.

Likewise, `b` must leave two later positions and `c` must leave one. The ranges become empty automatically when insufficient positions remain, though the outer bounds already prevent such states.

These bounds avoid invalid access and unnecessary iterations while retaining every legal tuple.

**Trace repeated values**

For `[1,1,1,3,5]`, the first three ones with index three form one valid quadruplet because $1+1+1=3$.

For right endpoint four, value five can be formed by choosing value three at index three and any two of the three earlier ones. There are three index pairs, so three additional quadruplets are counted.

The answer is four. A value-frequency set would risk collapsing these different index choices, while direct enumeration preserves them.

**Why the result is correct**

Every increment corresponds to four strictly increasing indices and a tested equality, so no invalid quadruplet is counted.

Conversely, every valid quadruplet has some unique ordered indices $(a,b,c,d)$. The four nested ranges eventually choose those exact indices in that exact nesting, evaluate the true equality, and increment once. No other iteration represents the same ordered index tuple.

Therefore `ans` equals the number of distinct valid index quadruplets.

**Simplicity versus the claimed optimal bound**

The direct method is easy to audit and is feasible for the small limit $N\le50$: there are at most

$$
\binom{50}{4}=230300
$$

quadruplets, which is modest.

However, four nested index loops are asymptotically $O(N^4)$. The manifest labels this branch $O(N^2)$ time and $O(V)$ space, but those bounds describe a different counting method, not the concrete source.

**How a quadratic method would reorganize the equation**

The equality can be rearranged as

$$
\texttt{nums}[a]+\texttt{nums}[b]
=
\texttt{nums}[d]-\texttt{nums}[c].
$$

A quadratic scan can maintain counts of left-side pair sums while advancing the boundary between $b$ and $c$, then query matching right-side differences. The update order must enforce $a<b<c<d$.

That method explains the manifest's value-frequency storage and $O(N^2)$ goal, but it is not implemented in this `solution.py`. An exact explanation must not attribute its performance to the four-loop source.

**Why no auxiliary structure is used**

The source keeps only loop indices, `n`, and `ans`. It reads values directly from `nums`. This gives constant auxiliary space and avoids subtle frequency-update ordering, trading memory and asymptotic speed for a straightforward exhaustive proof.

**No early pruning is needed**

All values are positive, but the source does not sort the array because index order is semantically important. Sorting would destroy the original $a<b<c<d$ relationship. Without sorting, value-based break conditions are not generally safe, so the exact method tests each combination.

## Complexity detail

Let $N$ be the array length. The number of iterations is $\binom{N}{4}$, which is $\Theta(N^4)$ in the asymptotic worst case. Each equality check is constant-time under the bounded integer values, so exact time is $O(N^4)$.

Auxiliary space is $O(1)$: the implementation stores counters and indices only. This differs from the manifest's $O(N^2)$ time and $O(V)$ space, which correspond to pair-sum/difference counting.

## Alternatives and edge cases

- **Pair-sum frequency scan:** Rearrange to `nums[a] + nums[b] = nums[d] - nums[c]` and maintain only pairs satisfying the index boundary, achieving $O(N^2)$ time with frequency storage.
- **Triple loops plus value lookup:** Can reduce one index search, but multiplicity and the position-after-$c$ condition must be maintained carefully.
- **Sort the array:** Incorrect because quadruplets depend on original index order, not only multiset values.
- **Exactly four elements:** The loops test the sole possible quadruplet once.
- **Duplicate values:** Different index choices remain distinct and are correctly counted separately.
- **No satisfying equality:** `ans` remains zero.
- **Several right endpoints:** Each appears in its own `d` iterations.
- **Positive values:** Bound arithmetic but do not justify reordering indices.
- **Loop ordering:** Starting each index after its predecessor enforces strict inequalities automatically.
- **Maximum length 50:** Makes the exact $\binom{N}{4}$ enumeration practical despite its $O(N^4)$ asymptotic class.
- **Manifest mismatch:** The exact source is exhaustive, not the quadratic pair-count approach.
- **Input preservation:** The array is neither sorted nor modified.
