## General
**Keep one state for each legal end-of-day position**

Let `cash` be the best profit after the processed days while holding no share. Let `hold` be the best profit while holding one share, with the purchase cost already subtracted. Initially cash is zero and holding means buying at the first price.

**Update the no-stock state**

On a new price, either remain out of the market with the old `cash` or sell the held share for `hold + price - fee`. Take the better result.

**Update the holding state**

Either keep the old share or buy today using the previous no-stock profit, producing `previous_cash - price`. Using the saved previous cash makes the two transitions describe decisions from the same prior day.

**Why two values contain the complete history**

Every valid strategy ends each day in exactly one of these two states. For each state, the recurrence considers every legal final action—do nothing, buy, or sell—and combines it with the best compatible prior state. Induction therefore preserves the best profit for both positions. A completed strategy cannot finish with more usable profit by holding a share, so final `cash` is the answer.

## Complexity detail
The state machine performs constant work for each of the `n` prices, taking $O(n)$ time. It stores only the two state values and one saved previous value, using $O(1)$ extra space.

## Alternatives and edge cases
- **Greedy effective purchase price:** track the cheapest fee-adjusted entry and realize profit when price rises beyond it; it is also linear but its state reinterpretation is less direct.
- **Full DP table:** store cash and hold for every day; it exposes the recurrence visually but uses $O(n)$ space.
- **Try every earlier buy for each sell day:** combine each transaction with prior optimal profit; it is correct but takes $O(n^2)$ time.
- A single day or monotonically decreasing prices produce zero profit.
- A fee larger than every possible rise makes every transaction unprofitable.
- Multiple transactions may outperform one long transaction when prices fall enough between profitable rises.
- The fee is charged once per completed transaction, not on both buying and selling.
