# Maximize Amount After Two Days of Conversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3387 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-amount-after-two-days-of-conversions](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/).

### Goal
Given an initial amount of a starting currency, calculate the maximum possible amount of that same currency you can obtain after two days of trading. On each day, you are provided with a list of currency pairs and their corresponding exchange rates. You start with the initial currency on Day 1, convert it through various pairs to maximize the amount of a target currency, and then on Day 2, use those proceeds to perform further conversions to maximize the final amount of the starting currency.

### Function Contract
**Inputs**

- `initialCurrency`: A string representing the starting currency.
- `pairs1`: A list of lists where each inner list contains two strings (currency A, currency B) and a float (rate).
- `rates1`: A list of floats representing the exchange rate from currency A to currency B for `pairs1`.
- `pairs2`: A list of lists where each inner list contains two strings (currency A, currency B) and a float (rate).
- `rates2`: A list of floats representing the exchange rate from currency A to currency B for `pairs2`.

**Return value**

- A float representing the maximum possible amount of `initialCurrency` obtainable after two days of conversions.

### Examples
**Example 1**

- Input: `initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0, 3.0], pairs2 = [["JPY","USD"],["USD","EUR"]], rates2 = [0.5, 0.5]`
- Output: `1.5`

**Example 2**

- Input: `initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["EUR","NGN"]], rates2 = [6.0]`
- Output: `54.0`

**Example 3**

- Input: `initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"],["JPY","USD"]], rates2 = [1.0, 1.0]`
- Output: `1.0`

---

## Solution
### Approach
The problem is modeled as a directed graph where currencies are nodes and exchange rates are edge weights. Since we want to find the maximum conversion rate between any two currencies, we can use the Bellman-Ford algorithm or simply perform a Breadth-First Search (BFS) / Depth-First Search (DFS) from the source node to all reachable nodes, keeping track of the maximum product of rates found so far.

### Complexity Analysis
- **Time Complexity**: O(N + M), where N is the number of pairs in day 1 and M is the number of pairs in day 2. We perform a traversal (BFS/DFS) on the graph constructed from each day's rates.
- **Space Complexity**: O(V), where V is the number of unique currencies, used to store the adjacency list and the maximum rates found during traversal.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict, deque

def solve(initialCurrency, pairs1, rates1, pairs2, rates2):
    def get_max_rates(pairs, rates, start_node):
        graph = defaultdict(list)
        for (u, v), r in zip(pairs, rates):
            graph[u].append((v, r))
            graph[v].append((u, 1.0 / r))

        max_rates = {start_node: 1.0}
        queue = deque([start_node])

        while queue:
            curr = queue.popleft()
            for neighbor, rate in graph[curr]:
                if max_rates.get(neighbor, 0) < max_rates[curr] * rate:
                    max_rates[neighbor] = max_rates[curr] * rate
                    queue.append(neighbor)
        return max_rates

    # Day 1: Find max conversion from initialCurrency to all others
    day1_rates = get_max_rates(pairs1, rates1, initialCurrency)

    # Day 2: For every currency reached in Day 1, find max conversion back to initialCurrency
    max_final_amount = 1.0

    # We need to check all currencies reachable from initialCurrency in Day 1
    # and see how much they can convert back to initialCurrency in Day 2
    for intermediate_currency, amount_after_day1 in day1_rates.items():
        day2_rates = get_max_rates(pairs2, rates2, intermediate_currency)
        if initialCurrency in day2_rates:
            final_amount = amount_after_day1 * day2_rates[initialCurrency]
            if final_amount > max_final_amount:
                max_final_amount = final_amount

    return float(max_final_amount)
```
</details>
