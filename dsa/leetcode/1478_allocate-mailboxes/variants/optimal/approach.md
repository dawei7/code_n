## General

**Sort houses so optimal mailbox groups are contiguous.** On a line, houses served by one mailbox in an optimal assignment can be taken as a consecutive block in sorted order. If two mailbox service regions crossed, exchanging assignments removes the crossing without increasing distance.

The source sorts `houses` in place. From then on, the problem is to partition the ordered positions into exactly `k` contiguous groups and place one mailbox optimally for each group.

**One mailbox belongs at a median.** For sorted houses from index `i` through `j`, the sum of absolute distances is minimized by any median position. Matrix `g[i][j]` stores that minimum one-mailbox cost.

The recurrence `g[i][j] = g[i+1][j-1] + houses[j] - houses[i]` peels off the two outer houses. A median optimal for the inner interval lies between the outer positions, so their combined distance to it is exactly the outer difference. Repeating inward gives the full median cost.

Lower-triangle and single-house entries start at zero, supplying base cases when indices meet or cross. The fill order decreases `i` and increases `j`, so `g[i+1][j-1]` is ready.

For houses one, four, and eight, the inner one-house cost is zero and the outer contribution is seven, matching a mailbox at four: three plus zero plus four.

**Define the partition DP.** `f[i][j]` is the minimum distance for the first `i + 1` sorted houses using exactly `j` mailboxes. With one mailbox, all those houses form one group, so `f[i][1] = g[0][i]`.

For more mailboxes, choose `p` as the final index served by the first `j - 1` mailboxes. Houses `p + 1` through `i` form the last group and cost `g[p+1][i]`. The transition adds this to `f[p][j-1]` and minimizes over all `p < i`.

The mailbox-count loop reaches at most `i + 1` because no nonempty prefix of that many houses can use more nonempty groups, and it never exceeds `k`.

**Why exactly k groups are enough.** Every house is assigned to its nearest mailbox in the objective. Once optimal mailbox locations are ordered, their served houses can be partitioned into contiguous regions. Empty mailboxes are unnecessary; since `k <= n`, an optimal arrangement can give each mailbox a nonempty group.

**Trace a partition decision.** For sorted houses `[1,4,8,10,20]` and three mailboxes, consider a final group containing only house twenty. Choosing `p = 3` combines the best two-mailbox solution for houses through ten with `g[4][4] = 0`. Another split might group ten and twenty together, but its last-group cost is `g[3][4] = 10`. The minimum transition decides using total prefix cost, not merely the cheapest final group.

This illustrates why greedily placing a mailbox at the largest gap is not a complete general proof. Every split changes both the final group and how many mailboxes remain for the prefix. Dynamic programming evaluates that interaction exactly.
The median argument makes every `g` entry optimal for one contiguous group. Any optimal partition of the first `i + 1` houses has a unique last group beginning after some `p`, and the recurrence considers that split. Conversely, every transition joins a valid optimal prefix partition to a valid last group. Induction over mailbox count and prefix length proves `f[-1][k]` is globally minimal.

The method returns only the total distance; mailbox coordinates need not be reconstructed.

## Complexity detail

Sorting takes `O(N log N)`. Filling `g` visits `O(N^2)` intervals with constant work. The DP has `O(kN)` states and considers up to `N` split points each, taking `O(kN^2)` time overall.

Matrix `g` uses `O(N^2)` space and `f` uses `O(kN)`. Since `k <= N`, total space is `O(N^2)`, matching the manifest.

The input list is mutated by sorting. Python's sort may also use linear temporary workspace, absorbed by the quadratic DP storage.

Infinity marks unreachable states and cannot beat a finite candidate.

## Alternatives and edge cases

- **Compute group cost on demand:** Median prefix formulas can avoid storing all `g` entries, but repeated queries need careful optimization.
- **Top-down memoization:** Cache the first unserved house and mailboxes remaining; it uses the same contiguous-group principle.
- **One mailbox:** The answer is `g[0][N-1]`, the total distance to a median.
- **k equals N:** Give every house its own mailbox and obtain zero.
- **Two-house group:** Any mailbox between them has cost equal to their distance, exactly the recurrence's outer difference.
- **Odd group size:** The unique middle house is an optimal mailbox position.
- **Even group size:** Any point between the two middle houses is optimal; the cost recurrence remains valid.
- **Unsorted input:** Sorting is essential for median intervals and contiguous partitions.
- **Unique house positions:** No duplicate-coordinate special case is needed.
- **Large gaps:** Absolute-distance cost is captured directly by coordinate differences.
- **Input mutation:** The caller observes sorted `houses` after the method.
- **No reconstruction:** Only minimum cost is stored, not split choices or mailbox coordinates.
- **Exactly k:** DP index `j` represents an exact count, not at most `j`.
- **Contiguous service regions:** Sorting plus the uncrossing argument ensures no optimal solution is lost by interval partitioning.
- **Transition split p:** The first `j-1` mailboxes serve through `p`, and the last mailbox serves every house after it through `i`.
