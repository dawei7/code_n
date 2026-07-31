## General

The first `min(need1, need2)` units are required on both sides. Each such shared unit can be bought either as one combined item for `costBoth` or as one item of each single type for `cost1 + cost2`. Since purchases do not interact, use the cheaper price independently for every shared unit.

After those units, only one requirement can remain. If type 1 has the excess need, each remaining unit can come from a type-1 item or a combined item; oversupplying type 2 is allowed, so its cheapest price is `min(cost1, costBoth)`. The symmetric rule uses `min(cost2, costBoth)` when type 2 has the excess.

These two regions cover every required unit. Replacing any chosen unit with its more expensive alternative cannot improve feasibility, so the sum of the locally cheapest prices is globally minimal.

## Complexity detail

The calculation uses a fixed number of comparisons and arithmetic operations, taking $O(1)$ time and $O(1)$ auxiliary space. The result can be as large as $10^{15}$, so it requires an integer representation wider than signed 32-bit.

## Alternatives and edge cases

- **Enumerate combined-item counts:** Try every number from zero through `max(need1, need2)` and buy single items for each deficit. This is correct but takes $O(\max(\texttt{need1},\texttt{need2}))$ time.
- **Both needs zero:** Buying nothing gives cost `0`.
- **One need zero:** A combined item may still be cheaper than the corresponding single item because oversupply is permitted.
- **Combined versus separate:** For shared units, compare `costBoth` with the sum `cost1 + cost2`, not with either price alone.
- **Unequal needs:** Combined items may remain optimal after the smaller need is already satisfied.
- **Large result:** Maximum costs and requirements produce totals beyond 32-bit range.
