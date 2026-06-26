# Minimum Coins (Greedy Variant)

| | |
|---|---|
| **ID** | `greedy_10` |
| **Category** | greedy |
| **Complexity (required)** | $O(V)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/) |

## Problem statement

Given an integer `V` representing a target value, and an array of coin denominations representing the standard currency system of a country (e.g., Indian Rupee `[1, 2, 5, 10, 20, 50, 100, 500, 1000]`).
Find the absolute minimum number of coins required to make exactly value `V`. You have an infinite supply of each coin denomination.

**Input:** Target value `V`, array of integer denominations `coins`.
**Output:** An integer representing the minimum number of coins, or a list of the specific coins used.

## When to use it

- When the denominations given are "Canonical" (like US Dollars, Indian Rupees, Euros).
- *Critical Constraint:* If the denominations are NON-Canonical (e.g., `[1, 3, 4]`), this Greedy approach mathematically FAILS, and you must use Dynamic Programming (`dp_05`).

## Approach

**1. The Greedy Philosophy:**
If you want to minimize the *count* of physical coins in your hand, you should obviously use the highest value coins possible!
Why use ten `10` bills when you can just use one `100` bill?

**2. The Canonical Guarantee:**
In a standard currency system, the Greedy choice works perfectly because every larger coin is strictly superior to any combination of smaller coins it replaces. You will never encounter a bizarre edge case where using a smaller coin unlocks a more efficient global combination.

**3. The Algorithm:**
1. Sort the `coins` array in descending order (if not already sorted).
2. Iterate through the `coins`.
3. While the current `coin` is \le the remaining target `V`, greedily subtract it from `V`!
   - (Optimized math: Instead of `while` loop subtraction, use integer division: `count = V // coin`, and update `V = V % coin`).
4. Keep going until `V` reaches 0.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_10: Minimum Coins.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        if c <= 0:
            continue
        while amount >= c:
            amount -= c
            count += 1
        if amount == 0:
            break
    if amount == 0:
        return count
    return -1
```

</details>

## Walk-through

`V = 43`. `coins = [1, 2, 5, 10, 20, 50, 100]` (Already sorted descending: `[100, 50, 20, 10, 5, 2, 1]`).

1. `coin = 100`: 100 \le 43 False.
2. `coin = 50`: 50 \le 43 False.
3. `coin = 20`: 20 \le 43 True!
   - `count = 43 // 20 = 2`.
   - `ans` gets two `20`s. `ans = [20, 20]`.
   - `V = 43 % 20 = 3`.
4. `coin = 10`: 10 \le 3 False.
5. `coin = 5`: 5 \le 3 False.
6. `coin = 2`: 2 \le 3 True!
   - `count = 3 // 2 = 1`.
   - `ans` gets one `2`. `ans = [20, 20, 2]`.
   - `V = 3 % 2 = 1`.
7. `coin = 1`: 1 \le 1 True!
   - `count = 1 // 1 = 1`.
   - `ans` gets one `1`. `ans = [20, 20, 2, 1]`.
   - `V = 1 % 1 = 0`.
8. Loop terminates because V=0.

Result `[20, 20, 2, 1]`. (Count = 4). ✓

*Why it fails on Non-Canonical `[1, 3, 4]`, `V=6`:*
Greedy takes `4`. Remainder `2`. Takes `1`, `1`. Total coins = 3 (`[4, 1, 1]`).
Optimal DP takes `3`, `3`. Total coins = 2 (`[3, 3]`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(C)$ | $O(1)$ |
| **Average** | $O(C)$ | $O(1)$ |
| **Worst** | $O(C)$ | $O(1)$ |

Where C is the number of coin denominations available (e.g., 9 in the Indian Rupee system).
Because we use math (`//` and `%`) instead of a `while` loop, processing each coin denomination takes $O(1)$ time regardless of how massive V is! Therefore, the time complexity is strictly bounded by the size of the denominations array $O(C)$.
Since C is usually a small constant like 10, the algorithm runs in $O(1)$ constant time.
Space complexity is $O(1)$ if returning just the count, or $O(\text{Answer Count})$ if returning the specific list of coins.

## Variants & optimizations

- **Coin Change II (Combinations):** Finding the minimum coins is one thing, but what if you want to find the TOTAL number of unique ways to make value V? That is strictly a DP problem (`dp_04`) and cannot be solved greedily.

## Real-world applications

- **Cash Registers / ATMs:** The exact algorithm running on the microprocessor of an ATM calculating which physical bills to dispense when a user requests an odd withdrawal amount like `$380`.

## Related algorithms in cOde(n)

- **[greedy_09 - Lemonade Change](greedy_09_lemonade-change.md)** — A hard-coded application of this exact logic restricted specifically to 5, 10, and 20 bills.
- **[dp_05 - Coin Change Problem](../dynamic/dp_05_coin-change.md)** — The mathematically generalized DP solution that correctly handles non-canonical (bizarre) currency systems.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
