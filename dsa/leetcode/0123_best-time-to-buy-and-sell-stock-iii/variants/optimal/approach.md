## General
**Four balances represent the only legal action stages**

Maintain the best balance after the first buy, first sale, second buy, and second sale. A balance is cash after executing that stage, with a buy state also representing one currently held stock.

Initialize buy states to negative infinity because no buy has occurred before any day, and sale states to zero because doing no transaction is allowed. A first buy transitions from zero cash; a second buy transitions only from a completed first sale, enforcing nonoverlap.

**Each price offers one transition or the choice to keep an earlier state**

For price `p`, apply:

```text
buy1  = max(buy1, -p)
sell1 = max(sell1, buy1 + p)
buy2  = max(buy2, sell1 - p)
sell2 = max(sell2, buy2 + p)
```

Keeping the prior value models taking no action. In-place left-to-right updates may allow a sale and following buy at the same price on one day, but that zero-profit boundary is equivalent to holding stages across adjacent days and cannot create illegal positive profit.

**Every state retains only the dominant history for its stage**

After each day, every state is the maximum balance achievable at its transaction/holding stage using only processed prices. A lower balance at the same stage can never outperform a higher one under identical future prices, so retaining only the maximum loses no optimal schedule.

**Trace two profitable nonoverlapping intervals**

In `[3,3,5,0,0,3,1,4]`, the first completed transaction can earn `2`, and after buying again at `0` or `1`, the second can raise total profit to `6`.

**Four stages enumerate every legal two-transaction schedule**

Any valid history moves in order through first buy, first sell, second buy, and second sell, possibly skipping arbitrarily many days between actions. Each state update either retains the best earlier history for that stage or performs today's action from the immediately preceding stage.

Those are the only legal ways to end a day in each stage. Keeping only the maximum balance discards histories that can never outperform it under identical future actions. After all prices, the second-sell state is therefore the best profit using at most two completed transactions.

## Complexity detail
Each of `n` prices performs four constant-time updates, giving $O(n)$ time. Four scalar balances give $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every split day with separate scans:** takes $O(n^2)$ without prefix/suffix preprocessing.
- **General `k`-transaction DP:** is flexible but stores more state than needed for fixed $k=2$.
- **Sum every positive rise:** allows unlimited transactions and can overstate the answer.
- Fewer than two profitable opportunities naturally leave `sell2` equal to the best zero- or one-transaction result.
- Empty or decreasing inputs return zero through the sale-state initialization.
