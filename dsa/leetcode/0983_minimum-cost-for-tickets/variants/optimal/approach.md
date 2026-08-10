## General

**Define the state by the first travel day not covered yet**

The difficult part is not checking whether one pass covers one day. It is choosing a pass whose price and duration interact with all later travel days. A cheaper short pass may lead to more purchases, while a more expensive long pass may cover several future trips. This is an optimization problem with repeated suffixes, which makes dynamic programming appropriate.

The recursive state `dfs(i)` is defined as:

> the minimum additional cost needed to cover every travel day from index `i` through the end of `days`, assuming earlier travel days are already covered.

This definition contains exactly the information future choices need. Past ticket details no longer matter once the algorithm knows the first uncovered travel day.

**Why a new pass can begin on `days[i]`**

Let `d = days[i]` be the earliest uncovered travel day. Any valid continuation must buy some pass that covers `d`. If that pass were bought on an earlier non-travel day, shifting its purchase forward to `d` would cost the same, would still cover `d`, and would extend rather than shorten its coverage on the future side. Therefore, there is always an optimal continuation whose next pass begins exactly on `days[i]`.

This observation removes the need to try all 365 possible purchase dates. At each state, the code only decides which duration to buy at the current uncovered travel day.

**Try all three legal ticket types**

The list `valid = [1, 7, 30]` is aligned with `costs`:

- `costs[0]` buys one day;
- `costs[1]` buys seven consecutive days;
- `costs[2]` buys thirty consecutive days.

The loop `for c, v in zip(costs, valid)` pairs each price `c` with the corresponding duration `v`. Since there are exactly three entries in each list, every legal first decision is considered once.

If a duration-`v` pass is bought on day `days[i]`, it covers the half-open interval

`[days[i], days[i] + v)`.

For example, a seven-day pass bought on day two covers days two through eight. Day nine, equal to `2 + 7`, is the first day not covered. Expressing coverage as a half-open interval avoids off-by-one ambiguity.

**Use binary search to jump over all covered travel days**

The travel days are strictly increasing. Therefore,

`j = bisect_left(days, days[i] + v)`

finds the first index whose day is greater than or equal to the pass's expiration boundary. Every travel day at an index from `i` through `j - 1` is smaller than that boundary and is covered by this pass. Index `j` is the next uncovered travel day.

If the pass covers all remaining trips, `bisect_left` returns `n`. If it covers only `days[i]`, it returns `i + 1`. Since every duration is positive and `days[i]` itself is below `days[i] + v`, `j` is always greater than `i`. Recursion therefore moves strictly toward the base case and cannot cycle.

The total cost of this choice is

`c + dfs(j)`:

- `c` pays for the pass chosen now;
- `dfs(j)` optimally covers exactly the suffix left after that pass expires.

The minimum of the three totals is stored in `ans` and returned.

**The base case represents an empty suffix**

When `i >= n`, there are no travel days left to cover. The minimum additional cost is zero, so `dfs` returns `0`. This allows a pass that covers the rest of the schedule to contribute only its own price.

The initial call `dfs(0)` asks for the minimum cost beginning with the first travel day, so it is the answer to the whole problem.

**Memoization prevents repeated suffix work**

Different pass choices can arrive at the same next index. For instance, a one-day pass from one state and a seven-day pass from an earlier state might both leave the same later travel day uncovered. Without caching, `dfs` would solve that identical suffix repeatedly and build an exponential recursion tree.

The `@cache` decorator stores the returned value for every index `i`. Subsequent calls with the same index immediately reuse the result. There are only `n + 1` possible indices, so the exponential choice tree collapses into a small directed acyclic graph of suffix states.

**Trace the first example**

For `days = [1, 4, 6, 7, 8, 20]` and `costs = [2, 7, 15]`, consider suffixes from right to left:

- At day twenty, the cheapest choice is a one-day pass, so `dfs(5) = 2`.
- At day eight, a one-day pass followed by the day-twenty cost gives `2 + 2 = 4`, cheaper than a seven-day pass plus day twenty or a thirty-day pass. Thus `dfs(4) = 4`.
- At day four, a seven-day pass covers travel days four, six, seven, and eight. Binary search jumps to day twenty, giving `7 + dfs(5) = 9`. Buying successive one-day passes costs more, so `dfs(1) = 9`.
- At day one, a one-day pass costs `2 + dfs(1) = 11`. A seven-day pass covers days one, four, six, and seven, then leaves day eight; that option is `7 + dfs(4) = 11`. A thirty-day pass costs fifteen. The minimum is eleven.

The algorithm need not reconstruct which of the tied eleven-dollar plans was chosen because the contract asks only for the minimum cost.

**Why taking the minimum produces the global optimum**

Consider any state `dfs(i)`. Every valid plan for this suffix must choose one of the three ticket types to cover `days[i]`, and, by the shifting argument, an equally good plan can buy that ticket on `days[i]`. The loop examines all three possibilities.

Once a particular pass is selected, it deterministically covers indices `i` through `j - 1`. The remaining decision is exactly the subproblem `dfs(j)`. By memoized recursion, that value is the cheapest way to cover the remaining suffix. Thus `c + dfs(j)` is the cheapest complete plan whose first pass is the chosen type.

Taking the minimum compares the cheapest plan from every possible first ticket. No valid first decision is omitted, so the result is the cheapest valid plan for state `i`. The base case is correct for an empty suffix, and the argument applies backward to `dfs(0)`, proving the returned total is globally minimal.

## Complexity detail

Let `N` be the number of travel days. Memoization evaluates each state `i` at most once, so there are `O(N)` computed states. Each state considers exactly three ticket types. The protected implementation performs one `bisect_left` over the length-`N` sorted array for each type, costing `O(\log N)` apiece. Its precise time complexity is therefore `O(N \log N)`.

The cache stores at most `N + 1` results. Recursion moves to a strictly larger index and can have depth at most `N + 1`, so cached state plus call-stack space is `O(N)`. Binary search itself uses constant auxiliary space.

Because the calendar is limited to 365 days, these bounds are small in absolute terms. A version that precomputes each next index with moving pointers can reduce the asymptotic transition work to linear time, but that is not what the exact solution code shown here executes.

## Alternatives and edge cases

- **Calendar-day dynamic programming:** Compute the minimum cost for every day from one through the final travel day. It is straightforward and runs in `O(K)` for last travel day `K <= 365`, but it creates states for non-travel days that the index-based method skips.
- **Precomputed next indices:** For each duration, advance a monotonic pointer across `days` and store where coverage ends. The dynamic program can then run in `O(N)` time at the cost of extra preprocessing arrays and bookkeeping.
- **Bottom-up suffix DP:** Fill `dp[i]` from `N - 1` down to zero using the same binary-search transitions. It avoids recursion while preserving the same recurrence and asymptotic complexity.
- **Naive recursion without `@cache`:** It tries the correct choices but recomputes identical suffixes and can grow exponentially.
- **Greedy cheapest-per-day selection:** Always buying the lowest-priced pass or the lowest cost-per-day pass is not reliable because unused calendar days and irregular travel gaps change which coverage is valuable.
- **Pass expiration boundary:** A duration-`v` pass bought on `d` covers through `d + v - 1`. Searching for `d + v` with `bisect_left` correctly makes a trip exactly on that boundary uncovered.
- **Pass covers every remaining trip:** Binary search returns `n`, and the base case adds zero.
- **Only one travel day:** All three transitions reach `n`, so the algorithm returns the least of the three ticket prices.
- **Large gaps between trips:** Binary search skips covered indices, not calendar dates. If the next trip falls after expiration, it correctly becomes the next state regardless of how many non-travel days lie between.
- **Strictly increasing input:** Sorted unique travel days are essential to the binary-search boundary and ensure that a state advances. The contract guarantees this ordering.
- **A longer pass cheaper than a shorter pass:** No dominance assumption is made. All three costs are tested at every state, so unusual but legal pricing is handled correctly.
- **Tied optimal plans:** `min` may choose any equal numeric total; since only the minimum amount is returned, no tie-breaking rule is needed.
