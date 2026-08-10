## General

The competitive solution keeps the cheapest price observed so far and the best profit observed so far. For each current price, it first updates the minimum and then measures the profit from that minimum to the current day.

This one-pass state compresses every possible earlier purchase into one number. A more expensive earlier purchase can never be better for the same selling day.

**What `min_price` summarizes**

After `min_price = min(min_price, price)`, it is the minimum among all prices from the first day through the current day.

For any future selling price, buying at this minimum is at least as profitable as buying at any other observed price. Earlier prices larger than the minimum can be discarded from the decision state without losing an optimal transaction.

Positive infinity is a convenient initial value because the first real price always replaces it.

**Why including the current day does not violate chronology**

The contract requires buying on a different earlier day before selling. This source updates `min_price` with the current price before calculating `price - min_price`.

If the current price does not become the minimum, `min_price` comes from an earlier day, so the candidate is a valid transaction.

If the current price does become the minimum, the computed candidate is exactly zero because it subtracts the price from itself. That same-day candidate cannot increase `max_profit`, which is initialized to zero and never decreases.

Therefore every positive candidate necessarily uses an earlier minimum. Allowing a harmless zero candidate does not alter the maximum valid nonnegative profit.

**The loop invariant after a day**

After processing day $j$:

- `min_price` is the smallest price in days zero through $j$; and
- `max_profit` is the best nonnegative profit from all valid earlier-buy/later-sell pairs whose sale is no later than day $j$.

The minimum assignment establishes the first statement. The profit assignment compares the previous best with the best candidate selling today. If today's minimum was first seen today, that candidate is zero; otherwise it uses an earlier day and is the best sale-today transaction.

Those cases cover all possibilities, so the invariant holds after each iteration. At the end, it describes the complete array.

**Why the best purchase alone is sufficient**

For a fixed sale price $p$, profit from buy price $b$ is $p-b$. Making $b$ smaller can only increase or preserve the result.

The algorithm does not need the second-smallest price, every valley, or a list of candidate days. The one minimum dominates all other processed purchase prices for every future sale.

The specific index of the minimum is also unnecessary when only the profit amount is returned. Chronological processing guarantees it is not from the future.

**Tracing `[7, 1, 5, 3, 6, 4]`**

At seven, the minimum becomes seven and the candidate is zero. At one, the minimum becomes one and the candidate is again zero.

At five, the minimum remains one and profit four becomes the best. Price three offers two. Price six offers five and replaces the best. Price four offers three.

The final result is five, corresponding to the earlier minimum one and later price six.

**Why falling prices return zero**

Each new falling price becomes `min_price` before subtraction, producing zero for that day. No positive candidate appears, so `max_profit` remains its initial zero.

This correctly chooses no transaction instead of a loss. The method never returns a negative profit.

**Exactly one transaction**

The state never adds profits from separate rises. It always computes a single difference between one observed minimum and one current price. Thus even if the array contains several profitable waves, only the best single buy-sell pair is returned.

The method has no type annotation or external dependency and is self-contained under ordinary Python. It reads but does not mutate `prices`.

## Complexity detail

For $n$ days, the loop performs one iteration per price. Each iteration has two constant-time minimum or maximum comparisons and one subtraction. Total time is $O(n)$.

`max_profit`, `min_price`, and `price` are scalar state, so auxiliary space is $O(1)$. The answer is one integer.

No sorting is allowed or needed. Sorting would destroy the chronological relation between buy and sell days unless original indices were also retained, and it would be slower than the scan.

The $O(n)$ time is optimal in the comparison/input model because an unseen final price could change the answer.

## Alternatives and edge cases

- **Profit-before-minimum order:** Evaluate the current sale against only strictly earlier prices, then admit today as a future purchase. It makes chronology explicit and produces the same answer.
- **Nested buy-sell loops:** Enumerates every valid pair but takes quadratic time.
- **Track maximum future price from right:** Scan backward or build suffix maxima and evaluate each day as a purchase. A backward scalar scan can also achieve $O(n)$ time and $O(1)$ space.
- **Maximum subarray of daily changes:** A profitable buy-sell interval equals a positive-sum contiguous range of day-to-day differences.
- **One price:** The only candidate is same-day zero, which leaves the result zero.
- **All prices equal:** Every difference is zero.
- **Strict decrease:** Each day becomes the new minimum, and no positive profit appears.
- **Strict increase:** The first minimum persists and the final price produces the best result.
- **Repeated minimum:** Any earlier occurrence can serve as the purchase; profit amount is unchanged.
- **Price zero:** It becomes the strongest possible purchase because prices are nonnegative.
- **Same-day candidate:** It is always zero and cannot create an invalid positive maximum.
- **Several profitable segments:** Profits are not accumulated because only one transaction is allowed.
- **No-transaction option:** Initializing `max_profit` to zero is necessary to avoid reporting a loss.
- **Chronological order:** The left-to-right scan is what makes `min_price` an observed, never-future purchase.
- **Input values:** The algorithm uses exact integer subtraction and cannot overflow in Python.
