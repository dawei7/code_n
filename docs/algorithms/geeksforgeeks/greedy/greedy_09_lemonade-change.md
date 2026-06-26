# Lemonade Change

| | |
|---|---|
| **ID** | `greedy_09` |
| **Category** | greedy |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) |

## Problem statement

At a lemonade stand, each lemonade costs `5`. Customers are standing in a queue to buy from you, and order one at a time.
Each customer will only buy one lemonade and pay with either a `5`, `10`, or `20` bill. You must provide the correct change to each customer so that the net transaction is exactly `5`.
You start with NO change in your cash register.
Return `true` if you can provide every customer with correct change, or `false` otherwise.

**Input:** An integer array `bills` where `bills[i]` is either 5, 10, or 20.
**Output:** A boolean.

## When to use it

- To demonstrate the simplest possible application of a Greedy choice involving denomination breakdown.
- Often used as a warm-up question before transitioning to harder DP Coin Change problems.

## Approach

We simply simulate the process of serving customers while tracking the count of `5` and `10` bills in our register. (We don't need to track `20` bills because we will never use them as change).

**1. The 5 Bill:**
If the customer gives `5`, we just accept it. No change needed. Increment our `5` count.

**2. The 10 Bill:**
If the customer gives `10`, we OWE them `5` in change.
We MUST give them one `5` bill. If we don't have one, we immediately return `False`.
If we do, we decrement our `5` count and increment our `10` count.

**3. The 20 Bill (The Greedy Choice):**
If the customer gives `20`, we OWE them `15` in change.
There are two mathematical ways to make `15`:
1. One `10` bill and one `5` bill.
2. Three `5` bills.

**The Greedy Decision:** Which way is strictly better?
A `5` bill is far more versatile than a `10` bill! A `5` bill can be used to make change for a `10` OR a `20`. A `10` bill is useless for making change for a `10`!
Therefore, we should **always greedily get rid of our 10 bills first!**
If we have a `10` and a `5`, we give them that.
If we don't have a `10`, we are forced to give three `5` bills.
If we don't have either combination, we return `False`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_09: Lemonade Change.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(bills, n):
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
```

</details>

## Walk-through

`bills = [5, 5, 5, 10, 20]`.
`fives = 0`, `tens = 0`.

1. Customer 1 (5): `fives = 1`.
2. Customer 2 (5): `fives = 2`.
3. Customer 3 (5): `fives = 3`.
4. Customer 4 (10):
   - Owe 5. We have it!
   - `fives = 3 - 1 = 2`.
   - `tens = 1`.
5. Customer 5 (20):
   - Owe 15.
   - Do we have a 10 and a 5? Yes! (`tens=1, fives=2`).
   - `tens = 0`. `fives = 1`.

Queue finished. Return `True`. ✓

*(Contrast: If we didn't use the Greedy rule and gave three 5s to Customer 5 instead, it would still work here. But if `bills = [5, 5, 10, 20, 10]`, giving three 5s to the `20` would leave us with `tens=2, fives=0`, causing us to immediately fail on the final `10`!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

We iterate through the `bills` array exactly once, performing $O(1)$ constant-time arithmetic checks at each step. Time complexity is strictly $O(N)$.
Space complexity is O(1)$ because we only track two integer variables (`five_count`, `ten_count`) regardless of how large the input array is.

## Variants & optimizations

- **Any Denomination Change:** If the bills were arbitrary values `[1, 5, 10, 25, 50]`, the Greedy logic (always returning the largest possible bill that fits in the owed amount) works ONLY if the denomination system is "Canonical" (like US currency). If the system is non-canonical (e.g., `[1, 3, 4]`), Greedy fails and you must use Dynamic Programming (`dp_05`).

## Real-world applications

- **Vending Machines:** Standard algorithmic logic running on the microcontrollers of physical vending machines and cash registers to dispense the minimum number of physical coins to a customer, reducing the frequency the machine needs to be refilled.

## Related algorithms in cOde(n)

- **[greedy_10 - Minimum Coins](greedy_10_minimum-coins.md)** — The generalized mathematical version of this exact problem using standard currency denominations.
- **[dp_05 - Coin Change Problem](../dynamic/dp_05_coin-change.md)** — The Dynamic Programming variant required when the Greedy logic fails due to non-standard denominations.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
