## General
**Translate smashes into signed weights:** Smashing replaces $y$ and $x$ by $y-x$, so the eventual result can be viewed as assigning every original weight a positive or negative sign and taking the absolute signed sum. Equivalently, divide the stones into two groups and minimize the absolute difference between their sums.

**Search only up to half the total:** If one group has sum $A$, the other has sum $S-A$ and their difference is $lvert S-2A\rvert$. The best $A$ may therefore be chosen as the greatest reachable subset sum not exceeding $lfloor S/2\rfloor$.

**Build reachable subset sums:** Start with only sum zero reachable. For each stone, add its weight to every sum reachable before processing that stone. A set update based on the prior contents ensures each stone is used at most once. After all stones, select the greatest reachable value at most half the total and return `total - 2 * best`.

Every stored sum is produced by a real subset, and every subset sum is generated when its members are processed. Thus the chosen $A$ is the closest achievable value to half of $S$. Any smaller reachable sum gives a no smaller difference, while sums above half correspond symmetrically to their complementary groups, proving optimality.

## Complexity detail
There are at most $S+1$ distinct subset sums. Processing each of the $N$ stones can inspect or create $O(S)$ sums, giving $O(NS)$ time. The reachable-sum set stores $O(S)$ integers.

## Alternatives and edge cases
- **Boolean knapsack array:** Mark reachable sums in descending order for each stone. It has the same $O(NS)$ time and $O(S)$ space.
- **Meet in the middle:** Enumerate subset sums of two halves and binary-search complements near $S/2$; this is useful when weights are huge but $N$ is small.
- **Enumerate every subset:** Checking all $2^N$ assignments is exact but exponential.
- **Recompute reachability for every target:** Solving a separate subset-sum problem for each target up to $S/2$ repeats work and adds a factor of $S$.
- **Single stone:** Its weight is the only possible result.
- **Perfect partition:** If a reachable subset sums to $S/2$, the answer is zero.
- **Odd total:** A zero result is impossible, and the minimum difference is at least one.
- **Repeated weights:** Equal values represent distinct stones and may be assigned to different groups.
