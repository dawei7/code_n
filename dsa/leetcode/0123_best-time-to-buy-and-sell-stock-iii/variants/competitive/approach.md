## General

The competitive source is a four-state dynamic program compressed into scalar variables. It processes every price and retains the best balance after the first buy, first sale, second buy, and second sale.

The names `hold1`, `release1`, `hold2`, and `release2` describe whether a share is held and how many transaction stages have been reached.

**Cash-balance meaning**

Starting with zero cash:

- `hold1` is the best balance while holding after the first purchase;
- `release1` is the best balance while not holding after at most one sale;
- `hold2` is the best balance while holding after a second purchase;
- `release2` is the best balance while not holding after at most two sales.

A buy subtracts the current price from a prior non-holding balance. A sale adds the current price to a prior holding balance.

This cash interpretation keeps profits from the first transaction automatically available when paying for the second purchase.

**Initialization makes impossible holdings harmless**

`hold1` and `hold2` start at negative infinity. Before any price exists, it is impossible to hold a legitimately purchased share, so these states must not compete with real balances.

Both release states start at zero, representing no transaction. Because the objective permits fewer than two transactions, zero is a valid baseline for every processed prefix.

The loop can therefore process all prices uniformly, including the first, without indexing or a special case.

**First buy and sale**

`hold1 = max(hold1, -i)` decides whether to keep an earlier first purchase or buy today from starting cash zero.

`release1 = max(release1, hold1 + i)` decides whether to keep an earlier one-transaction profit or sell today.

After these assignments, the two variables summarize every way to use at most one transaction within the processed prefix.

**Second buy and sale**

`hold2 = max(hold2, release1 - i)` either preserves an earlier second holding or buys today using the best cash after the first sale.

`release2 = max(release2, hold2 + i)` either retains the prior final answer or sells that second holding today.

The transitions always alternate hold and release, so they cannot represent simultaneous shares. A second purchase is reachable only from a state that has released the first share.

**Why current-day updated states are safe**

Assignments occur in action order, and later assignments can read values updated at the same price. This allows a buy followed by sale at that price, or first sale followed by second buy at the same price.

Each same-day pair changes cash by zero. It cannot manufacture profit and can be deleted from the represented schedule. Allowing these no-op transitions is useful because it lets an “at most” state inherit a solution using fewer actual transactions.

The maximum result is therefore the same as a version that snapshots yesterday's four values before all updates.

**Why no possible schedule is omitted**

For each state after a day, an optimal schedule either performed no corresponding action that day or did perform it that day.

The first argument to each `max` covers doing nothing. The second argument takes the best valid predecessor stage and applies today's buy or sale. Those cases exhaust the possibilities.

Inductively, each variable equals the best balance for its stage over the complete processed prefix. Every constructed transition respects action order, so stored values are feasible; every feasible schedule appears in one of the cases, so none is missed.

At the end, `release2` is the maximum non-holding cash after at most two sales. It is the requested profit.

**Tracing the main example conceptually**

During the early `[3,3,5]` segment, `release1` can reach two. When price zero appears, `hold1` improves to zero, representing a first purchase at no cost.

Selling at three makes `release1` three. A later price one lets `hold2` become two because the first profit three pays for the second share. At final price four, `release2` reaches six.

This corresponds to transactions zero-to-three and one-to-four. The machine also retains single-transaction and no-transaction candidates throughout.

**Active class selection**

The file contains `Solution2`, a general two-transaction array-state implementation, and `Solution3`, a prefix/suffix implementation. The selected entry point is the first `Solution.maxProfit`.

Those alternatives do not contribute arrays or costs to the active method. Complexity and explanation must follow the four scalar states actually executed.

## Complexity detail

For $n$ prices, the loop runs $n$ times. Each iteration performs four constant-time maximum transitions, so time is $O(n)$.

Only four DP numbers and the current price are retained. Auxiliary space is $O(1)$, matching the manifest.

Unlike the Optimal source, this method loops directly over `prices` and creates no slice. Its constant-space claim is exact for ordinary Python list input.

The method returns one integer and never modifies the input.

## Alternatives and edge cases

- **Cost-and-profit formulation:** Track minimum first cost, maximum first profit, effective second cost, and maximum second profit. It is algebraically equivalent to these cash states.
- **Prefix/suffix arrays:** Combine best one-transaction profits on both sides of every split. It is intuitive but uses linear space.
- **General transaction-count states:** Arrays of holding and released balances support arbitrary $k$ with $O(kn)$ time and $O(k)$ space.
- **Brute-force transaction days:** Four nested choices are infeasible for $10^5$ prices.
- **Empty input outside constraints:** The loop is skipped and returns zero, making this source more defensive than first-element initialization.
- **One price:** Holding states update, but release states remain zero.
- **All falling:** No profitable sale occurs, so `release2` stays zero.
- **All rising:** The single full rise is retained even though two transactions are allowed.
- **One useful transaction:** No-op stage transitions let `release2` represent it.
- **Two useful transactions:** `hold2` incorporates `release1`, enforcing that the first share was sold.
- **Zero-cost buy:** A hold balance may equal prior released profit.
- **Same-day transitions:** They are zero-profit conveniences, not overlapping holdings.
- **At most versus exactly two:** Zero initialization is what permits doing fewer transactions.
- **No fee or cooldown:** Additional rules would require modified transitions.
- **Alternative classes:** `Solution2` and `Solution3` are inert relative to the selected `Solution`.
- **Input preservation:** Only scalar states change.
