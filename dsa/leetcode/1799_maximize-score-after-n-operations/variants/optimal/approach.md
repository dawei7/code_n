## General

**Why choices need subset state**

Every operation removes two array elements, and an element's index can be used only once. The score of a chosen pair also depends on when it is chosen because operation $r$ multiplies its GCD by $r$.

A locally largest GCD is not automatically best to choose first. Large GCD values often deserve larger multipliers in later operations, and using one element prevents pairing it elsewhere. The algorithm must explore both pairing and ordering choices.

With at most $2n=14$ elements, a bitmask can represent exactly which indices have already been selected. The protected solution uses a forward dynamic program over all masks.

**Precompute pair GCD values**

Let $m=\texttt{len(nums)}$. Matrix `g` has $m$ rows and $m$ columns. For every pair $i<j$, the solution stores

`g[i][j] = gcd(nums[i], nums[j])`.

Only the upper-triangular entries are needed because later loops always use `j > i`. Precomputation avoids repeating the Euclidean algorithm in many DP transitions.

**Meaning of the DP state**

`f[mask]` is the maximum score obtainable after selecting exactly the indices whose bits are one in `mask`.

Only masks with an even number of set bits are valid because every operation selects two indices. The empty mask has `f[0] = 0` by array initialization.

For a mask `k`, the code computes `cnt = k.bit_count()`. When `cnt` is even, that state contains

$$
r=\frac{\texttt{cnt}}{2}
$$

selected pairs, so its most recent pair was chosen in operation $r$.

**Build a state by deciding its last pair**

For every set bit $i$ and every later set bit $j$, treat indices $i$ and $j$ as the pair selected last in mask `k`. Removing those bits gives the predecessor

`k ^ (1 << i) ^ (1 << j)`.

Because both bits are known to be one, XOR clears them. The predecessor has two fewer selected indices and was therefore completed after $r-1$ operations.

Appending pair $(i,j)$ as operation $r$ adds

$$
r\cdot\gcd(\texttt{nums}[i],\texttt{nums}[j]).
$$

The transition is

`f[k] = max(f[k], f[previous] + cnt // 2 * g[i][j])`.

Every predecessor mask is numerically smaller than `k` because clearing set bits decreases the integer. The outer loop visits masks from zero upward, so the required predecessor value is already available.

**Why choosing the last pair captures operation order**

The mask records only the selected set, not a sequence. The operation number is nevertheless determined by its population count. When the transition removes a proposed last pair, `f[previous]` already contains the best ordering of all earlier pairs. Adding the current pair with multiplier $r$ evaluates one complete ordering of this state's elements.

Trying every possible last pair covers every possible ordering recursively. Any schedule has a definite final pair; remove it, and the remaining schedule is represented by the predecessor. This is the same decomposition that makes many subset DPs possible.

**Following the four-element example**

For `nums = [3, 4, 6, 8]`, one optimal schedule pairs 3 with 6 first and 4 with 8 second.

The mask containing indices 0 and 2 has two bits, so its operation number is one and its score can become `1 * gcd(3, 6) = 3`.

The full mask has four bits. Taking indices 1 and 3 as its last pair uses the prior mask and adds `2 * gcd(4, 8) = 8`, giving 11. Other final-pair choices are also tested, and none gives a larger full-mask value.

**Why odd masks can be ignored**

No legal sequence selects an odd number of elements because every operation adds exactly two. The code computes `bit_count` for every integer mask but enters pair transitions only when that count is even.

Odd entries remain zero, yet they are never used as predecessors of an even state: clearing two bits from an even-popcount mask leaves another even-popcount mask.

**Why the returned full-mask value is correct**

Use induction on $r$, the number of selected pairs. The empty state's value zero is correct. Assume every state with $r-1$ pairs stores its optimal score.

Take a state with $r$ pairs. Any legal schedule for it has some last pair $(i,j)$. Its earlier score is no greater than the optimal predecessor value, and its last contribution is exactly $r\cdot g[i][j]$. The DP tests this pair, so it reaches at least that schedule's score. Conversely, every DP transition appends an unused pair to a valid predecessor schedule, so every candidate is achievable. Taking the maximum gives the exact optimum for the state.

The final entry `f[-1]` is Python's last list element, corresponding to mask `(1 << m) - 1` with every bit set. It therefore stores the optimal score after all $n$ required operations.

## Complexity detail

Let $m=2n$ and let $A$ be the maximum input value. Precomputing all pair GCDs uses $O(m^2\log A)$ time under the Euclidean algorithm and $O(m^2)$ space.

There are $2^m$ masks. For each even mask, the nested index loops can examine $O(m^2)$ pairs, so DP time is $O(m^2 2^m)$. Combining both phases gives

$$
O(m^2\log A+m^2 2^m).
$$

The exponential DP term is the manifest's stated $O(m^2 2^m)$ and dominates with respect to $m$; the exact multi-parameter bound also records GCD precomputation.

Array `f` uses $O(2^m)$ space and matrix `g` uses $O(m^2)$, for total $O(2^m+m^2)$ auxiliary space, matching the manifest. With $m\leq14$, at most 16,384 mask entries are needed.

## Alternatives and edge cases

- **Memoized recursive bitmask DP:** Choose the next pair and cache by mask. It explores the same state graph but uses recursion and computes operation number from selected bits.
- **Unmemoized backtracking:** It recomputes identical remaining-index states through many pair orders and grows far faster.
- **Greedy largest GCD:** It ignores element conflicts and multiplier timing; saving a large GCD for a later operation can be better.
- **Recompute GCD per transition:** It preserves correctness but repeats the same pair calculation across many masks.
- **Pair-value sorting:** A globally sorted GCD list cannot enforce that each original index appears in only one pair.
- **Two elements:** The full mask has one pair and returns their GCD with multiplier one.
- **Duplicate values:** Indices remain distinct mask bits, so equal numbers can still be paired or used in separate pairs.
- **All GCDs equal:** Every complete pairing and order has the same weighted sum, and the DP returns that shared value.
- **Large common factors:** Precomputed GCDs retain them exactly; Python integer arithmetic avoids overflow.
- **Even-mask invariant:** Only states representing whole operations receive transitions.
- **Ascending mask order:** Clearing two set bits always reaches a smaller mask, ensuring predecessor values are ready.
- **Upper-triangular matrix:** `g[j][i]` is left zero, but transitions always enforce `i < j` and read initialized entries.
- **Full-mask indexing:** `f[-1]` deliberately means the last mask, not an error sentinel.
- **Input preservation:** The algorithm reads `nums` and stores derived GCDs without removing or reordering elements.
