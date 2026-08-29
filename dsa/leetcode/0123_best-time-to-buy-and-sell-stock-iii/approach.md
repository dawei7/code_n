## General

At most two transactions create four chronological actions:

1. buy the first share;
2. sell the first share;
3. buy the second share; and
4. sell the second share.

The selected solution scans prices once and stores the best cash balance possible after each of those actions. It does not need to remember the actual days because every state summarizes all valid schedules in the processed prefix.

**Interpreting the four values**

After processing some prefix of days:

- `f1` is the maximum cash balance after the first buy, while holding one share;
- `f2` is the maximum cash after the first sale, while holding no share;
- `f3` is the maximum cash after the second buy, while holding one share; and
- `f4` is the maximum cash after the second sale, while holding no share.

Assume starting cash is zero. Buying at price $p$ changes cash by $-p$; selling changes it by $+p$. The state value is not the stock price or profit of only the most recent transaction. It is total cash after all actions represented by that state.

Holding and non-holding states alternate, so the representation cannot buy twice without a sale between those purchases.

**Why the first-day initialization works**

The contract guarantees a nonempty `prices` list. On day zero, buying produces balance `-prices[0]`, so both holding states initialize to that value.

Initializing `f3` this way may look as though a second buy occurred without a first sale. Because the problem allows at most two transactions, states are permitted to represent fewer actions. It is equivalent to treating the first transaction as a zero-profit no-op before the useful buy.

Both sale states begin at zero, representing no completed transaction. This ensures the final result is never negative: doing nothing is always available.

**Updating the first transaction**

For current `price`, `f1 = max(f1, -price)` chooses between keeping the best earlier first purchase and buying for the first time today.

Then `f2 = max(f2, f1 + price)` chooses between keeping an earlier completed first transaction and selling the best first holding state today.

Because `f1` represents the strongest balance while holding, adding today's price considers every possible earlier buy in one comparison.

**Updating the second transaction**

`f3 = max(f3, f2 - price)` either keeps an earlier second purchase or buys today after the best first-sale result. The earlier profit offsets the cost of this second share, which is why `f2` is subtracted from price through the cash expression rather than tracked separately.

Finally, `f4 = max(f4, f3 + price)` either preserves an earlier two-transaction result or sells the second holding today.

Every transition is either “do nothing today” by retaining the old state or “perform the state's action today” from the preceding state.

**Why update order does not create illegal profit**

The assignments occur from `f1` through `f4`, so a later state can use an earlier state updated with the same price. This permits zero-duration handoffs such as buying and selling at the same price or selling the first share and buying the second at that same price.

Such paired actions add zero cash and never create extra profit. They can be removed, or adjacent transactions can be merged, without decreasing the result. The state still never holds two shares because each sale state is non-holding before the next buy state.

If a formulation requires every action on a strictly later day, copying old states before updates produces the same maximum profit under this no-fee contract.

**Why the states capture every valid schedule**

Consider a valid schedule restricted to the processed days. Its last action is one of the four stages, or it used fewer actions and is represented through the initialized no-op possibilities.

If it does nothing on the current day, its value was already present in the state. If its last action happens today, removing that action leaves a valid schedule represented by the preceding state from this day or an earlier day. Adding or subtracting the current price reconstructs its balance.

Taking the maximum therefore retains the best balance for every stage. Conversely, every transition follows the required buy-sell-buy-sell order, so no stored balance comes from overlapping holdings.

After all days, `f4` is the best cash with at most two completed sales. Initialization allows zero or one actual transaction to occupy that state, so returning `f4` answers “at most two,” not “exactly two.”

**Tracing the two profitable regions**

For `[3,3,5,0,0,3,1,4]`, the first completed profit can reach two by buying at three and selling at five, but later the machine can choose a better arrangement for two transactions.

Buying at zero and selling at three makes the first useful profit three. The second holding state can then buy at one with effective cash `3 - 1 = 2`. Selling at four produces `2 + 4 = 6`.

The states retain all competing possibilities, including a single transaction from zero to four worth four, and choose six.

**Exact Python source details**

The loop uses `prices[1:]`. Python creates a new list containing all but the first element before iteration begins. That allocation is linear in input length even though the four-state algorithm itself needs only scalar memory.

The annotation uses `List[int]` without importing `List`. A standalone source needs `from typing import List`.

The nonempty constraint makes indexing `prices[0]` safe. An empty list outside the contract would raise `IndexError`.

## Complexity detail

Let $n$ be the number of prices. Each day performs a constant number of comparisons and arithmetic operations, so time is $O(n)$. Creating the slice also takes $O(n)$ time, which does not change the total bound.

The four DP states are $O(1)$ algorithmic workspace. However, the exact `prices[1:]` slice allocates $O(n)$ references, so this protected Python source has $O(n)$ peak auxiliary space.

The manifest's $O(1)$ claim describes the intended state machine when iterating by index, `iter(prices)`, or an iterator slice. It does not account for the concrete list slice in this file.

The answer is one integer and uses constant output space. The input itself is not modified.

## Alternatives and edge cases

- **Direct iteration without slicing:** Initialize from the first item and loop over indices one through $n-1$, preserving the four-state logic with true $O(1)$ auxiliary space.
- **Start holding states at negative infinity:** Process every price, including the first, through the uniform recurrence. This also handles an empty input by returning zero if desired.
- **Prefix and suffix profits:** Precompute the best one-transaction profit ending on the left and starting on the right, then combine split points. It uses $O(n)$ space.
- **General $k$-transaction DP:** Maintain buy and sell states for each transaction count. It runs in $O(kn)$ time and $O(k)$ space; here $k=2$.
- **Brute-force split and rescan:** Try every division between the transactions and solve both sides repeatedly, leading to quadratic time without prefix preprocessing.
- **One day:** No sale is possible, so both sale states remain zero.
- **Strict decrease:** Holding balances improve as prices fall, but no sale produces positive cash; result is zero.
- **Strict increase:** One transaction from first to last is optimal, and the at-most-two states preserve it.
- **Only one profitable interval:** `f4` can represent the same profit through a no-op transaction.
- **Two separated rises:** The second buy uses the first realized profit while maintaining non-overlap.
- **Same-day state chaining:** Adds no artificial profit because buying and selling at one price cancel.
- **Zero prices:** Holding states can become nonnegative, and later sales produce the full price as profit.
- **Nonempty precondition:** The exact initialization indexes the first element.
- **Missing typing import:** `List` must be supplied.
- **Slice allocation:** Replace `prices[1:]` to make the manifest's constant-space claim exact.
