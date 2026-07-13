# Apply Discount Every n Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1357 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [apply-discount-every-n-orders](https://leetcode.com/problems/apply-discount-every-n-orders/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/apply-discount-every-n-orders/).

### Goal
Design a cashier that knows product prices and applies a percentage discount to every `n`th customer order. Other orders are charged at full price.

### Function Contract
**Inputs**

- `n`: every nth order receives the discount.
- `discount`: discount percentage.
- `products`: product ids known by the cashier.
- `prices`: prices parallel to `products`.
- `orders`: list of `[product, amount]` pairs passed to `getBill`.

**Return value**

List of order totals after applying the scheduled discount when applicable.

### Examples
**Example 1**

- Input: `n = 3, discount = 50, products = [1,2], prices = [100,200], orders = [[[1],[1]]]`
- Output: `[100.0]`

**Example 2**

- Input: `n = 3, discount = 50, products = [1,2], prices = [100,200], orders = [[[1],[1]], [[2],[2]]]`
- Output: `[100.0, 400.0]`

**Example 3**

- Input: `n = 3, discount = 50, products = [1,2], prices = [100,200], orders = [[[1],[1]], [[2],[2]], [[1,2],[1,1]]]`
- Output: `[100.0, 400.0, 150.0]`

---

## Solution
### Approach
Hash map lookup with an order counter. Store product prices by id, increment the counter on each bill, compute the subtotal, and multiply by `(100 - discount) / 100` only when the counter is divisible by `n`.

### Complexity Analysis
- **Time Complexity**: `O(p)` to initialize `p` products and `O(k)` per bill with `k` line items.
- **Space Complexity**: `O(p)`

### Reference Implementations
<details>
<summary>python</summary>

```python
class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.price_by_product = dict(zip(products, prices))

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        total = sum(self.price_by_product[item] * count for item, count in zip(product, amount))
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return float(total)


def solve(
    n: int,
    discount: int,
    products: list[int],
    prices: list[int],
    orders: list[tuple[list[int], list[int]]],
) -> list[float]:
    cashier = Cashier(n, discount, products, prices)
    return [cashier.getBill(product, amount) for product, amount in orders]
```
</details>
