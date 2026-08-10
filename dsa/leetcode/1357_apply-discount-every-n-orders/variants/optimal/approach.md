## General

The cashier object must preserve two kinds of state across calls: the catalog price for each product identifier and the position of the current customer within a repeating block of `n` customers. Each bill can then be computed independently from the product quantities, with the discount applied exactly when the customer counter wraps around.

**Build a direct product-to-price map**

The constructor creates `self.d = {a: b for a, b in zip(products, prices)}`. The two input arrays are parallel, so each zipped pair contains a product ID and its price. Product IDs are unique, making the dictionary a one-to-one catalog lookup.

Using a dictionary means the price of a bill item can be found by its ID without searching the catalog array. The constraints guarantee every ID supplied to `getBill` exists in the constructor’s product list.

The object also stores `self.n` and `self.discount`. `self.i` begins at zero and represents the number of customer positions advanced modulo `n`.

**Advance the customer cycle once per bill**

At the start of every `getBill` call, the statement
`self.i = (self.i + 1) % self.n` advances the persistent counter.

Beginning from zero, the sequence is one, two, and so on through `n - 1`, then zero on the `n`th call. Consequently, `self.i == 0` is true precisely for customer numbers `n`, `2n`, `3n`, and so forth.

For `n = 3`, the first three calls produce counter values one, two, and zero. Only the third receives the discount. The next three calls repeat the same pattern, so the sixth also receives it.

The counter is updated per call rather than per product line. A customer buying many different products is still one order and advances the cycle once.

**Compute the undiscounted subtotal**

`zip(product, amount)` pairs each purchased product ID with its quantity. The generator expression multiplies `self.d[a]`, the unit price, by quantity `b` for every pair. `sum` adds those line totals into `x`.

The input arrays have equal lengths, and product IDs within one bill are unique. No line is accidentally truncated by `zip` under the contract, and no duplicate line needs consolidation.

**Apply a percentage only on the wrap call**

When `self.i == 0`, the method returns
`x - (self.discount * x) / 100`. The second term is the percentage amount removed from the subtotal. Algebraically, this is

$$
x\left(1-\frac{\texttt{discount}}{100}\right)
=x\frac{100-\texttt{discount}}{100},
$$

which is the required final bill.

The division operator produces a floating-point result in Python, matching the method’s return contract. On non-discounted calls, returning integer `x` is also acceptable because Python numeric results compare correctly with the expected double value.

The counter condition and subtotal calculation are independent. Every call computes the full price first, and only the periodic customer receives the stored percentage reduction.

For a concrete first bill with product IDs one and two, prices one hundred and two hundred, and quantities one and two, the generator contributes `100 * 1` and `200 * 2`. Their subtotal is five hundred. If this is customer one in a three-customer cycle, `self.i` is one and the method returns five hundred unchanged. On customer three, the counter becomes zero; with a fifty-percent discount, the same subtotal would return two hundred fifty.

Applying the discount after summing all lines is equivalent to discounting every line by the same percentage, but it requires only one percentage calculation and follows the stated bill formula directly.

## Complexity detail

Let $P$ be the number of catalog products and $L$ the number of line items in one bill.

The constructor’s dictionary comprehension processes every product-price pair once, taking $O(P)$ expected time and $O(P)$ persistent space.

One `getBill` call performs $L$ expected constant-time dictionary lookups and multiplications, so it takes $O(L)$ time. Counter advancement and discount arithmetic are $O(1)$. The generator and `sum` do not build an additional list, so per-call auxiliary working space is $O(1)$ beyond the stored price dictionary.

Across construction and one bill, the combined work is $O(P+L)$. Across many bills, add the lengths of all their item lists.

## Alternatives and edge cases

- **Catalog arrays with linear search:** Correct but makes each bill line cost $O(P)$ instead of expected $O(1)$ lookup.
- **Countdown counter:** Initialize a counter to `n`, decrement per bill, apply the discount at zero, then reset. It expresses the same cycle without modulo.
- **One-based total customer count:** Increment an unbounded count and test `count % n == 0`. The checked-in counter keeps only the remainder.
- **`n == 1`:** Every increment wraps to zero, so every customer receives the discount.
- **Zero percent discount:** Discounted customers pay the same subtotal, but the cycle still advances normally.
- **One hundred percent discount:** Every designated customer pays zero.
- **Single bill line:** The same zipped subtotal formula handles it without a special case.
- **Different product order:** Dictionary lookup uses IDs, so bill lines need not follow catalog order.
- **Unique bill product IDs:** The contract prevents repeated IDs within one call, though summing repeated lines would still produce the same total quantity cost.
- **Floating-point tolerance:** Percentage division may produce a non-integer result; the accepted error tolerance covers normal floating arithmetic.
- **Persistent object state:** Creating a new `Cashier` resets the customer cycle, while repeated calls on the same object continue it.
- **Counter updated before the subtotal:** With valid input this changes only which customer number the current call represents. The first call correctly becomes customer one rather than customer zero.
