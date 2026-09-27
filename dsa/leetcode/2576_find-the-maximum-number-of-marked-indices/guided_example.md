# Guided Example: Find the Maximum Number of Marked Indices

## 1. Marked indices arrive two at a time

Every allowed operation chooses two *different* indices $i$ and $j$ that are both unmarked, requires $2\,\texttt{nums}[i] \le \texttt{nums}[j]$, and marks both. Three facts follow before any algorithm is chosen.

- The answer is always **even**. Each operation marks exactly two indices, so the maximum number of marked indices is $2k$ where $k$ is the maximum number of operations, that is, the maximum number of disjoint valid index pairs.
- Inside a valid pair the two values cannot be equal in role. Since $\texttt{nums}[i] \ge 1 > 0$, the condition $2\,\texttt{nums}[i] \le \texttt{nums}[j]$ forces $\texttt{nums}[i] < \texttt{nums}[j]$; a value can never be paired with itself.
- Since no index can be marked twice, $k \le \lfloor n/2 \rfloor$ and therefore the answer never exceeds $2\lfloor n/2 \rfloor$. It is often strictly smaller, because the doubling condition can fail for every candidate pairing.

Terminology for the rest of the lesson: in a pair $(i,j)$ with $2\,\texttt{nums}[i] \le \texttt{nums}[j]$, call index $i$ the **small role** and index $j$ the **large role**. Allowing the doubling slack means the small value at most halves the large value; slack of exactly zero, as in `2` paired with `4`, is permitted because the inequality is $\le$ and not $<$.

## 2. Sorting first: only values matter

The condition depends on values only, never on positions, so the order of the input cannot change which pairings are legal. Sorting ascending therefore loses nothing and creates the structure the method needs: after sorting, the small roles of a good solution sit on the left side of the array and the large roles on the right side.

The instance used for the full trace is the first official one:

- Input: `nums = [3, 5, 2, 4]`
- Sorted array: `[2, 3, 4, 5]`
- Required output: `2`

| Sorted position | Value | Role in the scan |
|---|---|---|
| 0 | 2 | candidate small role, never scanned as a large |
| 1 | 3 | candidate small role, never scanned as a large |
| 2 | 4 | scanned as a large role |
| 3 | 5 | scanned as a large role |

With $n = 4$, the split index is $\lceil n/2 \rceil = 2$: positions `0` and `1` may only serve as small roles, and positions `2` and `3` are scanned in increasing order as candidates for the large role. The reason the small roles can be confined to the lower half is the subject of section 4; the reason the scan must start at the split is that any valid pair occupies two distinct positions and a pair with both positions in the lower half could always be replaced by a pair reaching further right.

## 3. Executing the greedy scan

The scan keeps one pointer $i$, initially $0$, into the lower half, and walks the upper half from left to right. For each scanned value $x$, if the smallest still-unmatched candidate satisfies $2\,\texttt{nums}[i] \le x$, the pair $(\texttt{nums}[i], x)$ is accepted and $i$ advances; otherwise $x$ is skipped and $i$ stays. Each accepted pair marks exactly two indices.

| Scanned position | Value $x$ | Smallest unmatched candidate | Test applied | Decision | Pairs so far |
|---|---|---|---|---|---|
| 2 | 4 | `nums[0] = 2` | $2 \cdot 2 = 4 \le 4$ | accept, $i$ becomes 1 | `(2, 4)` |
| 3 | 5 | `nums[1] = 3` | $2 \cdot 3 = 6 \le 5$ fails | reject, $i$ stays 1 | `(2, 4)` |

After the scan the pointer stands at $i = 1$, so $k = 1$ pair was formed and the answer is $2k = 2$. Throughout the scan the invariant is that $i$ equals the number of pairs accepted so far and that the accepted small roles are exactly the positions $0, 1, \dots, i-1$, so the smallest unmatched candidate is always $\texttt{nums}[i]$. The rejection is the informative part of this instance: the pair `(3, 5)` looks plausible because both values are close to the middle of the array, but doubling the smaller value overshoots the larger one, and that index pair can never be marked together. The only legal pair in this array is `(2, 4)`, which is exactly the one the greedy takes, using index `2` and index `3` of the original array. No legal pairing marks more than these two indices.

Notice also what the greedy did *not* do: it did not try pairing the larger candidate `5` with the smaller value `2`, which would have been legal, because doing so would waste the smallest value and leave `3` unable to reach anything. Taking candidates in increasing order and pairing each with the smallest value that can still afford it is the discipline that section 5 justifies.

## 4. Why the small roles are the smallest elements

The first structural claim is an exchange argument about the multiset of roles.

**Claim.** If some $k$ disjoint valid pairs exist, let $a_1 \le a_2 \le \dots \le a_k$ be their small values and $b_1 \le b_2 \le \dots \le b_k$ their large values. Then $2a_t \le b_t$ for every $t$.

**Proof.** Suppose $2a_t > b_t$ for some $t$. The $t$ smallest large values $b_1, \dots, b_t$ are then all strictly below $2a_t$. Each of them is matched, in the hypothetical solution, to a small value $a_s$ satisfying $2a_s \le b_j < 2a_t$, hence $a_s < a_t$. Distinct large values have distinct partners, so this produces $t$ distinct small values strictly below $a_t$, but only $a_1, \dots, a_{t-1}$ — that is, $t-1$ values — can be strictly below $a_t$. Contradiction. $\square$

Two monotonicity facts then transfer the claim from the role multisets to the sorted array itself.

- The $t$-th smallest array element is no larger than the $t$-th smallest small value: $\texttt{nums}[t-1] \le a_t$, because the small values are a subset of the array.
- The $t$-th smallest large value is no larger than the $(n-k+t)$-th smallest array element: $b_t \le \texttt{nums}[n-k+t-1]$. At most $t-1$ of the $k$ large values are below $b_t$, and at most $n-k$ array elements are not large values at all, so fewer than $n-k+t$ elements of the array can lie strictly below $b_t$.

Chaining the three inequalities for every $t = 1, \dots, k$:

$$2\,\texttt{nums}[t-1] \;\le\; 2a_t \;\le\; b_t \;\le\; \texttt{nums}[n-k+t-1].$$

This is the canonical form of any $k$-pair solution: the $k$ smallest array elements can take the small roles, the $t$-th of them paired with the array element at position $n-k+t-1$. In particular the $k$ smallest elements are the ones the greedy consumes, in increasing order, which is precisely what the pointer $i = 0, 1, \dots, k-1$ does.

## 5. Why the left-to-right scan finds the maximum

The second structural claim shows that no solution can beat the greedy.

**Claim.** If $k$ pairs exist, the scan accepts at least $k$ times.

**Proof.** Let $r_j = n-k+j-1$ be the position of the $j$-th required large value in the canonical form, for $j = 1, \dots, k$. Because $k \le \lfloor n/2 \rfloor$, every $r_j$ satisfies $r_j \ge n-k \ge \lfloor n/2 \rfloor$, so all of them lie inside the scanned upper half and are visited in increasing order. Induct on $j$: assume that by the time the scan passes position $r_{j-1}$ it has accepted at least $j-1$ pairs. If it has already accepted $j$ or more pairs, the claim holds for $j$. Otherwise it has accepted exactly $j-1$ pairs, all of them at positions at most $r_{j-1} < r_j$; since the greedy always consumes the smallest unmatched candidate, those $j-1$ pairs used values $\texttt{nums}[0], \dots, \texttt{nums}[j-2]$, so at position $r_j$ the smallest unmatched candidate is $\texttt{nums}[j-1]$. Section 4 gives $2\,\texttt{nums}[j-1] \le \texttt{nums}[r_j]$, so the test succeeds at position $r_j$ at the latest and the accepted count reaches $j$. $\square$

The greedy therefore accepts at least as many pairs as any legal solution, and since every pair it accepts is legal and disjoint, it accepts exactly the maximum $k$. Two details keep the argument airtight: the candidate pointer never leaves the lower half, because at most $\lfloor n/2 \rfloor$ pairs can be accepted and the indices consumed are $0, \dots, k-1$ with $k-1 < \lceil n/2 \rceil$, so a scanned position can never be reused as a small role; and both pointers move only forward, so no index is ever considered twice.

A second official instance shows the greedy reaching a perfect matching where the pairs cross in the original order:

| Scanned position | Value $x$ | Smallest unmatched candidate | Test applied | Decision | Pairs so far |
|---|---|---|---|---|---|
| 2 | 5 | `nums[0] = 2` | $2 \cdot 2 = 4 \le 5$ | accept, $i$ becomes 1 | `(2, 5)` |
| 3 | 9 | `nums[1] = 4` | $2 \cdot 4 = 8 \le 9$ | accept, $i$ becomes 2 | `(2, 5)`, `(4, 9)` |

For `nums = [9, 2, 5, 4]` the sorted array is `[2, 4, 5, 9]`, both scans succeed, $k = 2$, and the answer is `4` — every index is marked. The pair `(2, 5)` uses original indices `1` and `2`, while `(4, 9)` uses original indices `3` and `0`, so the two pairs interleave in the unsorted array; any method that pairs neighbouring positions of the input, or that greedily pairs each element with the next one large enough, has no reason to find this matching.

## 6. Boundaries and traps

| Input | Expected output | Reading of the reasoning |
|---|---|---|
| `[1]` | `0` | one index cannot form a pair, and the scanned upper half is empty |
| `[3, 3]` | `0` | equal values fail because $2 \cdot 3 = 6 > 3$; the answer is even but not automatic |
| `[5, 10]` | `2` | exact doubling satisfies the inequality with equality |
| `[5, 9]` | `0` | the ratio is below $2$, so no pair exists |
| `[7, 6, 8]` | `0` | sorted `[6, 7, 8]`; the only scanned candidate `8` would need a small value at most `4`, and the smallest value is `6` |
| `[3, 5, 2, 4]` | `2` | one pair `(2, 4)`; `(3, 5)` fails because $2 \cdot 3 = 6 > 5$ |
| `[9, 2, 5, 4]` | `4` | both pairs exist, so the maximum equals $2\lfloor n/2 \rfloor$ |
| `[1, 1, 2, 2]` | `4` | duplicates at both ends: each `1` pairs with a `2` at exact doubling |
| `[1, 2, 4]` | `2` | odd length; the candidate `4` consumes the smallest value `1` and value `2` stays unmarked |
| `[1, 500000000, 1000000000, 1000000000]` | `4` | maximum magnitudes: $2 \cdot 500000000 = 10^9$ exactly reaches the second maximum |
| a dense 26-element instance | `26` | all 26 indices can be paired, so the answer reaches $2\lfloor n/2 \rfloor$ |

| Trap | Symptom | Correction |
|---|---|---|
| Working on the unsorted array | scanning left to right in the original order misses pairings such as `(4, 9)` after `(2, 5)` | sort ascending first; positions in the answer's pairing need not be ordered |
| Letting the candidate pointer enter the scanned half | an index could then serve as both a small and a large role | consume candidates only from the lower half; there are at most $\lfloor n/2 \rfloor$ of them, one per possible pair |
| Rejecting a pair that meets the bound exactly | `(2, 4)` or `(5, 10)` are legal | the contract uses $2\,\texttt{nums}[i] \le \texttt{nums}[j]$, so equality is allowed |
| Reporting the number of pairs | values such as `1` for `[3, 5, 2, 4]` instead of `2` | the answer counts marked *indices*, so each pair contributes two |
| Assuming the whole array can always be marked | `[3, 5, 2, 4]` has $n = 4$ but the answer is `2`, not `4` | the doubling condition must hold for every pair; $2\lfloor n/2 \rfloor$ is only an upper bound |
| Overflowing when doubling | $2\,\texttt{nums}[i]$ can reach $2 \cdot 10^9$ | that value still fits a signed 32-bit integer (limit `2147483647`), but the comparison must not be rewritten as a division that truncates |

The scan itself is linear, but two other methods are worth knowing:

| Approach | Time | Space | Tradeoff |
|---|---|---|---|
| Sort plus one greedy two-pointer scan | $\Theta(n \log n)$, dominated by the sort | $O(1)$ beyond the sort | the method derived here; the scan is a single pass over the upper half |
| Sort plus binary search on the number of pairs $k$ | $\Theta(n \log n)$ for the searches after the sort | $O(1)$ | uses the section 4 criterion $2\,\texttt{nums}[t-1] \le \texttt{nums}[n-k+t-1]$ for $t = 1..k$, which is monotone in $k$; correct but performs more comparisons |
| Matching inside the unsorted array | no bound | no bound | fails outright, since a legal matching may pair positions that are far apart and interleaved |

## 7. Time and auxiliary space

- **Sorting** the array ascending costs $\Theta(n \log n)$ comparisons and is the dominant term. It is necessary here because the greedy argument is stated in terms of sorted positions; no linear-time method is available for arbitrary values, and comparison sorting is optimal for this much information.
- **The scan** visits exactly $\lfloor n/2 \rfloor$ candidates, one per position of the upper half, and performs a constant amount of work at each: one doubling, one comparison, and possibly one pointer increment. It costs $\Theta(n)$ and therefore does not change the total bound.
- **Total time** is $O(n \log n)$, which is optimal for this problem because the greedy decision depends on the sorted order of the values.
- **Auxiliary space** is $O(1)$ for the scan, which keeps only the pointer $i$ and the current candidate. The sort is performed in place by the canonical solution's library routine; a merge-based implementation of that routine may use up to $\Theta(n)$ transient memory, which is the only non-constant storage in the method.