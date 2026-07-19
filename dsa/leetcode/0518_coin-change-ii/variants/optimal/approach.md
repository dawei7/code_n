## General
**Let each DP entry count completed totals**

Maintain `ways[value]`, the number of combinations forming `value` using only denominations processed so far. Initialize `ways[0] = 1`: choosing no coins is the unique combination for total zero. All positive totals initially have no combinations.

**Process denominations outside totals**

For one `coin`, scan totals upward from `coin` through `amount` and add `ways[value - coin]` into `ways[value]`. Each source combination becomes a new combination by appending one copy of the current denomination. The upward direction permits that same coin to be reused because the source may already include it.

**Why combinations are counted once rather than permuted**

After finishing a denomination, `ways[value]` counts exactly the combinations whose allowed coin types come from the processed prefix. A combination is introduced when its largest-by-processing-order denomination is the current coin, independent of the order in which its physical coins could be arranged. Thus `[1, 2]` and `[2, 1]` contribute one combination, while different denomination counts remain distinct.

**Why no valid combination is missed**

Partition combinations for a total into those using zero current coins and those using at least one. The old `ways[value]` retains the first group. Removing one current coin from every combination in the second group gives a unique combination counted by the already updated `ways[value - coin]`; adding that value therefore accounts for the second group bijectively.

## Complexity detail
Each of `abs(coins)` denominations scans at most `amount` totals, for $O(amount \cdot |coins|)$ time. The one-dimensional table contains `amount + 1` integers, giving $O(amount)$ space.

## Alternatives and edge cases
- **Two-dimensional unbounded-knapsack table:** uses the same recurrence and time but $O(amount \cdot |coins|)$ space.
- **Try every count of each coin per state:** is correct but adds another factor proportional to `amount`.
- **Memoized choose-or-skip recursion:** has $O(amount \cdot |coins|)$ states but uses cache and call-stack space.
- **Totals outermost:** counts ordered sequences when it lets every coin extend each total, solving a different problem.
- **Zero amount:** has one empty combination regardless of available coins.
- **Unreachable amount:** remains at count zero.
- **Coin larger than amount:** contributes no transition.
