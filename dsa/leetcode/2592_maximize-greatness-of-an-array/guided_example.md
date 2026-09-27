# Guided Example: Maximize Greatness of an Array

## 1. The instance and what greatness actually counts

Take `nums = [1,3,5,2,1,3,1]`. We may lay the same seven values out in any order we like, calling the result `perm`, and greatness counts the slots where our value is **strictly** larger than the value the problem placed there:

$$
\text{greatness}(\texttt{perm}) = \bigl\lvert \{\, i : 0 \le i < 7 \ \text{and}\ \texttt{perm}[i] > \texttt{nums}[i] \,\} \bigr\rvert .
$$

Two structural facts govern everything that follows.

- The **target slot is frozen**. Index $i$ is always compared against `nums[i]`; no rearrangement moves the target.
- The **supply is a free multiset**. Because `perm` is a permutation of `nums`, the values $1, 1, 1, 2, 3, 3, 5$ are dealt one per slot, and any dealing is legal.

So this is not a question about magnitude but about routing: how many frozen slots can be covered by a strictly larger value taken from the very same pile? Index identity is immovable, value identity is fully under our control, and the answer is the largest number of slots that can be covered simultaneously.

## 2. A counting bound from the most frequent value

Before searching, census the pile. For each value, the entries able to beat it are exactly the pile entries strictly greater than it.

| Value | Copies in the pile | Pile entries strictly greater | Copies that can ever be beaten |
|:---:|:---:|:---:|:---:|
| 1 | 3 | 2, 3, 3, 5 (four entries) | at most 3 |
| 2 | 1 | 3, 3, 5 (three entries) | at most 1 |
| 3 | 2 | 5 (one entry) | at most 1 |
| 5 | 1 | none | 0 |

Let $m$ be the multiplicity of the most frequent value, here $v = 1$ with $m = 3$. Every beaten slot holding $v$ needs a partner strictly greater than $v$, and the pile contains only $n - m = 4$ such entries, all of them distinct positions. A slot holding $v$ cannot be beaten by another copy of $v$. This is the shape of the bound: $k \le n - m = 7 - 3 = 4$, so greatness 5, 6, or 7 is impossible before any pairing is attempted.

## 3. When can $k$ slots be won at all?

Sort the pile once, ascending. Write $a_t$ for the value at sorted position $t$.

| Sorted position $t$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $a_t$ | 1 | 1 | 1 | 2 | 3 | 3 | 5 |

A pairing of size $k$ uses $k$ beaten positions and $k$ distinct beater positions. Exchange arguments on the sorted order show that the best possible choice always takes the $k$ **smallest** entries as the beaten side and the $k$ **largest** entries as the beater side, matched in order. That reduces feasibility to a single test:

$$a_t < a_{\,n-k+t} \quad \text{for every } 0 \le t < k .$$

| $t$ | $a_t$ | Beater for $k = 4$: $a_{3+t}$ | feasible? | Beater for $k = 5$: $a_{2+t}$ | feasible? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | yes | 1 | **no** |
| 1 | 1 | 3 | yes | 1 | **no** |
| 2 | 1 | 3 | yes | 2 | yes |
| 3 | 2 | 5 | yes | 3 | yes |

The $k = 4$ column satisfies every row, so four wins are attainable. The $k = 5$ column already fails at $t = 0$: the smallest entry would have to be beaten by $a_2 = 1$, and $1 < 1$ is false. The failure is not an artifact of this split; feasibility is monotone, so once size 5 is impossible no larger size can be possible either. The maximum is therefore exactly 4, meeting the counting bound of section 2 with equality.

## 4. The frontier-pointer sweep on the real array

The test above tells us the maximum, but a sweep over the sorted array produces the pairing itself while needing no case analysis. Keep one pointer $p$ marking the frontier: the sorted position of the smallest entry that has not yet been beaten. Walk the sorted entries left to right as candidate beaters `x`. If `x > nums[p]`, then `x` beats the frontier entry, spend it, and advance the frontier; otherwise discard `x` and keep the frontier in place.

| Step | Candidate beater `x` | Frontier $p$ before | `nums[p]` | `x > nums[p]` | Pair recorded | Frontier $p$ after |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 1 | 0 | 1 | false | none | 0 |
| 2 | 1 | 0 | 1 | false | none | 0 |
| 3 | 1 | 0 | 1 | false | none | 0 |
| 4 | 2 | 0 | 1 | true | position 0 beaten | 1 |
| 5 | 3 | 1 | 1 | true | position 1 beaten | 2 |
| 6 | 3 | 2 | 1 | true | position 2 beaten | 3 |
| 7 | 5 | 3 | 2 | true | position 3 beaten | 4 |

The first three candidates die on the frontier because a 1 cannot beat a 1. The value 2 finally clears the frontier, and from there each remaining candidate clears the next frontier entry in turn. The pointer ends at $p = 4$, which is the greatness.

Notice which entries were beaten: sorted positions 0, 1, 2 (all value 1) and position 3 (value 2), beaten by 2, 3, 3, 5 respectively. The 5 is the only entry able to beat the 2, and it is used exactly once, which is why the four small entries cannot all be rescued.

## 5. Turning the pairing back into a permutation

The sweep matched values, and the permutation is reconstructed by sending each winning value to a slot whose original value it strictly exceeds. In the original indexing, the value 1 occupies slots 0, 4, 6 and the value 2 occupies slot 3, so those are the four slots the pairing can cover. The three leftover values $1, 1, 1$ take the remaining slots 1, 2, 5.

| Slot $i$ | `nums[i]` | Value placed at `perm[i]` | `perm[i] > nums[i]` | Counts toward greatness |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 2 | true | yes |
| 1 | 3 | 1 | false | no |
| 2 | 5 | 1 | false | no |
| 3 | 2 | 5 | true | yes |
| 4 | 1 | 3 | true | yes |
| 5 | 3 | 1 | false | no |
| 6 | 1 | 3 | true | yes |

The result is `perm = [2,1,1,5,3,1,3]`, whose multiset is again $1, 1, 1, 2, 3, 3, 5$, so it is a legal permutation, and it wins at slots 0, 3, 4, 6 for a greatness of 4. Other optimal arrangements exist, for instance the one that places 2 and 5 in the first two slots; the pairing fixes which values win, not which order the losing values appear in. What no arrangement can do is push past 4, because slots 1, 2, 5 hold values whose only strictly larger partner is the single 5.

## 6. Invariant and correctness of the frontier

**Invariant.** After the sweep has consumed the first $j$ sorted entries as candidate beaters, two things hold simultaneously: $p$ equals the maximum number of disjoint winning pairs that can be built using only those $j$ entries as beaters, and every winning pair uses one of the sorted positions $0, \dots, p-1$ as its beaten side.

Three consequences make the sweep safe.

- **The frontier is monotone.** $p$ never decreases, so each entry is considered as a target at most once and the scan is a single pass.
- **A failed candidate is genuinely useless.** All entries at or beyond the frontier are $\ge$ `nums[p]` in sorted order. If `x > nums[p]` is false, then `x` is no larger than every remaining frontier entry, so `x` could never beat any of them. Discarding it removes no feasible pair.
- **Using the earliest usable beater is never a loss.** Suppose some optimal pairing beats `nums[p]` with a beater $y$, while a smaller usable beater $x \le y$ (with `x > nums[p]`) sits unused or paired elsewhere. Swapping $x$ into the frontier pair keeps it valid, and wherever $x$ was used, $y$ still beats that target because that target was strictly below $x \le y$. The exchange changes no count, so an optimal pairing that uses the first usable beater always exists. Induction over the sweep steps upgrades this to: the greedy pairing is maximum.

**Completeness.** The sweep never terminates with an unused beater and an unbeaten frontier entry that it could have matched, since every entry is either spent or rejected for a proven reason. Combined with the exchange argument, the final $p$ is exactly the largest achievable number of winning pairs, and the counting bound $n - m$ from section 2 confirms the value independently: $7 - 3 = 4$.

## 7. Traps the instance exposes

| Strategy | Greatness on `[1,3,5,2,1,3,1]` | Greatness on `[1,1,1,2]` | Verdict |
|:---|:---:|:---:|:---|
| Count adjacent strict increases after sorting | 3 | 1 | Undercounts; duplicates force equal partners to stand next to each other |
| Split the sorted array in half and pair positionally | 3 | 1 | Also 3 here, but a run of duplicates straddling the split pairs equal values |
| Return $n - m$ from the frequency count | 4 | 1 | Correct total, yet it certifies no assignment of values to slots |
| Frontier-pointer sweep | 4 | 1 | Optimal on both instances and yields the pairing explicitly |
| Enumerate all $n!$ permutations | 4 | 1 | Correct but hopeless at $n = 10^{5}$ |

| Instance | $n$ | $m$ | Answer $n - m$ | Lesson it teaches |
|:---|:---:|:---:|:---:|:---|
| `[0]` | 1 | 1 | 0 | A lone element has no partner; its own slot cannot beat it |
| `[1,1]` | 2 | 2 | 0 | The comparison is strict, so equal values never win |
| `[10,10,10]` | 3 | 3 | 0 | Three free slots buy nothing when the pile holds one repeated value |
| `[1,1,1,2]` | 4 | 3 | 1 | One large value supports exactly one win however many small copies wait |
| `[0,0,1,2,3]` | 5 | 2 | 3 | The most frequent value need not be the smallest one |
| `[1000000000,0]` | 2 | 1 | 1 | Values near $10^{9}$ matter only through their order relations |

Two further traps are worth naming. First, the answer is unchanged if the input is shuffled, since the multiset is what the method inspects; a solution that depends on input order is testing the wrong property. Second, boundary values are not special: $0$ and $10^{9}$ are ordinary entries, and an entry equal to $0$ still cannot beat another $0$.

## 8. Time and auxiliary space complexity

Let $n = \texttt{nums.length}$ and $m$ the largest multiplicity of any single value.

- **Sorting dominates.** Ordering the pile costs $O(n \log n)$ comparisons, and every later step depends on that order.
- **The sweep is linear.** It visits each sorted entry once and only ever increments the frontier, so it adds $O(n)$ time. The total running time is therefore $O(n \log n)$, independent of the magnitude of the values.
- **Working state is constant.** The sweep keeps one frontier pointer and one counter, so its own auxiliary space is $O(1)$. The sorted copy is what costs space: $O(n)$ for a materialized copy, or $O(\log n)$ stack depth if the input may be reordered in place. With $n \le 10^{5}$ either choice is comfortable.

The frequency count that yields $n - m$ is itself $O(n)$ with a hash map, so it never becomes the bottleneck; it is a cross-check on the answer, not a replacement for the pairing.