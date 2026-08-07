## Description

Initially, you have a bank account balance of **100** dollars.

You are given an integer `purchaseAmount` representing the amount you will spend on a purchase in dollars, in other words, its price.

When making the purchase, first the `purchaseAmount` **is rounded to the nearest multiple of 10**. Let us call this value `roundedAmount`. Then, `roundedAmount` dollars are removed from your bank account.

Return an integer denoting your final bank account balance after this purchase.

**Notes:**

- 0 is considered to be a multiple of 10 in this problem.

- When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** purchaseAmount = 9

**Output:** 90

**Explanation:**

The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.

</div>
#### Example 2

<div class="example-block">
**Input:** purchaseAmount = 15

**Output:** 80

**Explanation:**

The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.

</div>
#### Example 3

<div class="example-block">
**Input:** purchaseAmount = 10

**Output:** 90

**Explanation:**

10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.

</div>
### Constraints

- $0 \le purchaseAmount \le 100$