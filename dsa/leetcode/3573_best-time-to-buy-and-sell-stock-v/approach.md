## General

At the end of a day, one of three position states is possible:

- flat: no transaction is open;
- long: a normal transaction has been opened by buying and still needs a later sale;
- short: a short transaction has been opened by selling and still needs a later buyback.

The source uses dynamic programming over day, transaction allowance, and these three states. Every transition comes only from the previous day, which enforces the rule that closing one transaction and starting another cannot happen on the same day.

**State meaning**

`f[i][j][state]` is the greatest accounting profit after processing days zero through `i` while using capacity for at most `j` transactions, with:

- state `0` flat;
- state `1` holding an open long position;
- state `2` holding an open short position.

Opening a position consumes one of the `j` transaction slots in the recurrence. Closing it keeps the same `j` because that slot was already reserved at opening.

For an open long, accounting profit includes the purchase payment as `-price`. For an open short, it includes the proceeds received on the initial sale as `+price`. The final answer must be flat so these temporary cash positions are eventually resolved.

**Day-zero initialization**

All flat states begin at zero, representing no transaction.

For every allowance `j \ge 1`:

- `f[0][j][1] = -prices[0]` opens a long by buying on day zero;
- `f[0][j][2] = prices[0]` opens a short by selling on day zero.

No position can close on day zero because the closing day must be later.

Entries with `j=0` remain zero. Their non-flat columns are not meaningful reachable positions, but the recurrence never uses them to close a zero-capacity transaction; new positions for `j=1` are opened only from `f[previous][0][0]`.

**Ending a day flat**

There are three ways to finish day `i` with no open position and allowance `j`:

1. remain flat and do nothing;
2. sell a previously opened long at `prices[i]`;
3. buy back a previously opened short at `prices[i]`.

This gives

`max(f[i-1][j][0], f[i-1][j][1] + prices[i], f[i-1][j][2] - prices[i])`.

Closing a long adds the sale proceeds. Closing a short subtracts the buyback cost.

**Ending with an open long**

Either the long was already open and remains untouched, or a new long begins today from a previously flat state with one fewer transaction slot:

`f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - prices[i])`.

The second transition pays today’s price. Because it reads day `i-1`, it cannot use a flat state created by closing another transaction on day `i`.

**Ending with an open short**

Similarly, either an old short remains open, or a new short begins today:

`f[i][j][2] = max(f[i-1][j][2], f[i-1][j-1][0] + prices[i])`.

Opening the short receives today’s sale amount, hence the addition.

**Why the DP covers every legal strategy**

Consider any legal strategy’s action on the final processed day. For each desired ending state, the recurrences list every possible last action: do nothing, open the matching position, or close the opposite open position into flat. No other legal action leads to that ending state.

The source takes the best previous-day profit for each possibility. By induction, earlier table entries already represent optimal legal strategies, so each new entry is optimal.

The previous-day dependency enforces strict ordering between open and close dates and prevents overlapping transactions. At most one position can be open because the state stores exactly one of flat, long, or short.

**Why f[n-1][k][0] is the answer**

The flat state guarantees every transaction has been completed. Returning an open-short cash balance would incorrectly count sale proceeds without the required buyback, and returning an open long would hold unsold stock.

The capacity `k` permits fewer transactions as well: doing nothing carries flat profit forward, and states do not have to use every slot. Therefore `f[n-1][k][0]` is the maximum for at most `k` complete transactions.

## Complexity detail

The table has `n(k+1)3` entries, and each transition examines a constant number of candidates. Time complexity is `O(nk)`.

The exact source allocates the complete three-dimensional table for every day, so space complexity is `O(nk)`. This contradicts the manifest’s `O(k)` claim.

Only day `i-1` is needed to compute day `i`, so a rolling array can reduce space to `O(k)`. The local editorial shows such an optimization, but the protected Optimal source here does not implement it and must be documented as `O(nk)`.

## Alternatives and edge cases

- **Rolling DP:** Keep only one day and iterate transaction capacity downward to avoid same-day reuse. This achieves the manifest’s `O(k)` space but is not the exact source.
- **Memoized recursion:** The same day/capacity/state recurrence can be evaluated top-down in `O(nk)` time and space, with recursion overhead.
- **Treat only normal transactions:** Standard Stock IV DP misses profitable downward moves; the short state is essential.
- **Unlimited-transactions shortcut:** Because same-day close/open is forbidden and both long and short trades exist, a specialized greedy derivation would need care. The bounded DP is direct and safe.
- **k equals one:** The table chooses the best single upward or downward price movement while ending flat.
- **Constant prices:** Every completed transaction has zero profit, so doing nothing returns zero.
- **Strictly increasing prices:** A long trade captures the useful movement; short trades cannot improve it.
- **Strictly decreasing prices:** A short sale followed by a lower buyback captures profit.
- **Open position at the end:** It is excluded by returning state zero.
- **Same-day reversal:** Impossible because all openings use a previous-day flat state rather than the newly computed current flat state.
- **Fewer than k transactions:** Flat carry transitions preserve those strategies.
- **Large prices:** Python integers avoid overflow in accumulated profits.
- **Minimum two days:** Initialization and later closure work normally; the constraints never supply an empty price list.
