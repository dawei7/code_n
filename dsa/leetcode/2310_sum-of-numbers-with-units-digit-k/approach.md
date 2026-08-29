## General

**The number of chosen integers determines the final units digit**

Suppose a valid collection contains exactly `i` positive integers, and every one has units digit `k`. Each such integer can be written as

`k + 10q`

for some nonnegative integer `q` when `k > 0`. Adding `i` numbers gives

`i \cdot k + 10(q_1 + q_2 + \cdots + q_i)`.

Therefore a count `i` can produce `num` only if `num - i \cdot k` is both nonnegative and divisible by 10. The code names this difference `t` and checks exactly:

`t >= 0 and t % 10 == 0`.

The nonnegative test says the unavoidable units-digit contributions `i \cdot k` have not already exceeded the target. The divisibility test says the remaining amount can be supplied in whole tens without changing any chosen integer's units digit.

For `k > 0`, these conditions are also sufficient. Start with `i` copies of the positive integer `k`. Their sum is `i \cdot k`. Since `t` is a nonnegative multiple of 10, add all of `t` to any one copy. Every number remains positive, every units digit remains `k`, and the total becomes `num`.

This necessity-and-sufficiency observation turns a problem about choosing actual values into a much smaller problem about choosing only their count.

**Test counts in increasing order**

The loop considers `i = 1, 2, 3, ...`. For each count, the assignment expression

`t := num - k * i`

both computes the remainder and makes it available to the rest of the condition. If `t` is nonnegative and ends in zero, `i` is feasible and the method immediately returns it.

Because all smaller positive counts were tested first and rejected, the first returned `i` is necessarily the minimum possible size. There is no need to construct the actual integers because the arithmetic proof above guarantees that a collection exists whenever the condition succeeds.

For `num = 58` and `k = 9`, count `1` gives `t = 49`, which is not divisible by 10. Count `2` gives `t = 40`, which is nonnegative and divisible by 10, so the method returns `2`. One construction is to begin with `9 + 9` and add all 40 remaining units, in tens, to one number, producing `49 + 9 = 58`.

**Handle the empty collection before positive counts**

The statement defines the sum of an empty collection as zero. Thus when `num == 0`, the minimum size is `0` regardless of `k`. The early return handles this unique case before the loop starts at one.

Without that branch, the method would either return a positive count for some `k` or return `-1`, both of which would miss the explicitly permitted empty solution. For every positive `num`, an empty collection is impossible, so testing begins correctly at count one.

**Why the search limit is sufficient**

The exact loop is `range(1, num + 1)`, so it tests at most `num` positive counts. When `k > 0`, every chosen integer is at least one. Any collection of positive integers summing to `num` therefore has size at most `num`. No feasible minimum can lie beyond the loop.

When `k = 0`, each valid positive integer must end in zero and is therefore at least 10. A positive target is feasible exactly when it is itself a positive multiple of 10; in that case one number equal to `num` is already a solution, and the first iteration returns `1`. If `num` is not divisible by 10, no sum of numbers all divisible by 10 can produce it, so reaching the end and returning `-1` is correct.

This also explains a subtle point about writing an integer as `k + 10q`. For `k = 0`, choosing `q = 0` would give zero, which is not positive. The exact algorithm never incorrectly returns a count based on such zero terms: any feasible positive target with `k = 0` is settled at count one using the positive number `num`, and an infeasible target is rejected.

**Only count residues matter mathematically, although the code scans farther**

The divisibility part depends on `i` through `i \cdot k` modulo 10. These residues repeat after at most 10 increments. If a feasible count greater than 10 existed for `k > 0`, subtracting 10 from that count would preserve the units-digit congruence and would increase `t` by `10k`, keeping it nonnegative. A smaller feasible count would therefore already exist. Consequently, any feasible answer is found among the first ten positive counts.

The exact implementation nevertheless loops up to `num`. This makes no difference to correctness, and with `num <= 3000` it remains tightly bounded. It does mean that an infeasible input—especially `k = 0` with a target not divisible by 10—can execute more than ten iterations. An explanation of the exact code should distinguish the mathematical ten-residue observation from the literal loop bound.

**Why returning minus one is justified**

If the loop finishes, every possible count from one through `num` has failed at least one necessary condition. Counts beyond `num` cannot form a positive-integer sum of `num`. The zero-count case was already handled separately. Therefore no valid collection size exists, and `-1` is the required sentinel.

## Complexity detail

Let `N` denote the numeric value of `num`. The exact loop performs at most `N` iterations, each with constant-time arithmetic under the bounded integer sizes in the problem. Its parameterized running time is therefore `O(N)`. Because the source contract permanently caps `num` at 3000, this is also a fixed upper bound and is reported by the variant manifest as `O(1)` with respect to unbounded input size.

There is also a tighter algorithmic observation: feasibility residues repeat every ten counts, so a modified implementation could test only counts one through ten and have an unconditional constant iteration count. The current solution does not use that shortened loop, so the distinction matters when describing literal operations even though both forms are constant under the official domain.

The method stores only `i` and `t` in addition to its input parameters. It allocates no array, set, recursion stack, or collection of candidate numbers, so auxiliary space is `O(1)`.

Python integers safely represent all intermediate values. Under the stated bounds, `k * i` is small, but correctness would not rely on fixed-width overflow behavior even for larger values.

## Alternatives and edge cases

- **Check only counts one through ten:** The units-digit pattern repeats modulo 10, and any feasible larger count implies a feasible count ten smaller. This is a cleaner unconditional `O(1)` loop, but it is not the literal range used by the exact solution.
- **Dynamic programming for a minimum coin count:** Treat every positive number ending in `k` up to `num` as a coin. This can solve the task but creates many redundant denominations and spends roughly `O(num^2)` time where a congruence condition is sufficient.
- **Breadth-first search over reachable sums:** Each edge adds a number ending in `k`. The state graph is far larger than needed and still requires generating candidate addends; arithmetic characterizes reachability directly.
- **Checking only `num % 10 == k`:** That recognizes a possible one-number solution but misses valid multiple-number solutions, such as `58` with `k = 9`, where two units digits sum to the needed residue.
- **Checking divisibility without `t >= 0`:** A negative multiple of 10 passes `t % 10 == 0` in Python but cannot be distributed as nonnegative tens. Both parts of the condition are necessary.
- **Starting the loop at zero for positive `num`:** Count zero cannot sum to a positive target. The one legitimate empty case is clearer and safer as the explicit `num == 0` branch.
- **Target zero:** The empty collection is permitted and has minimum size zero, even if one could discuss positive numbers whose residues match; no positive collection can improve on zero items.
- **`k = 0` with a positive multiple of ten:** One integer equal to `num` has units digit zero, so the first iteration returns one.
- **`k = 0` with a target not divisible by ten:** Every allowed integer is divisible by ten, as is every sum of them, so the method eventually returns `-1`.
- **`num < k`:** Even one smallest positive number ending in `k` would exceed the target. The first remainder is negative and all later ones are smaller, so no count succeeds.
- **A feasible count with zero remainder:** If `num = i \cdot k`, then `t = 0` is a valid multiple of ten. For `k > 0`, `i` copies of `k` provide the required construction.
- **Repeated values:** The problem permits multiple instances of the same integer, so the sufficiency construction may use repeated copies of `k`. Treating the collection as a mathematical set with uniqueness would change the problem.
- **Positivity of members:** For `k > 0`, the baseline copies of `k` are positive. The separate `k = 0` reasoning avoids mistakenly using zero as an allowed member.
- **First feasible count:** Immediate return is correct only because counts are tried in strictly increasing order. Reversing the loop would find a feasible size but not necessarily the minimum one.
