## General
**Accumulate one customer at a time.** Initialize a running maximum to zero, which is below or equal to every possible positive wealth. For each row, start a fresh total and add every balance in that row exactly once.

**Retain only the best total.** After finishing a row, compare its sum with the running maximum and keep the larger value. The individual row total is no longer needed once that comparison is complete, so totals for all customers do not need to be stored.

**Why the maximum is exact.** The inner scan includes every account belonging to the current customer, so its total is exactly that customer's wealth. After processing the first $k$ rows, the running value is the maximum wealth among precisely those $k$ customers. Extending this fact one row at a time shows that after all rows are processed, the stored value is the richest wealth over the entire matrix.

## Complexity detail
Every one of the $S=mn$ balances is read and added once, giving $O(S)$ time. Only the current row total and running maximum are stored beyond the input, so auxiliary space is $O(1)$. Inspecting all cells is necessary in the worst case because increasing any unexamined balance can make its customer the richest.

## Alternatives and edge cases
- **Built-in row sums:** Computing `max(map(sum, accounts))` expresses the same linear scan concisely, though the explicit loops make the constant-space accumulation visible.
- **Store every wealth:** Building a separate array of row sums also works but consumes $O(m)$ avoidable space.
- **Sort row totals:** Sorting can identify the largest total, but it adds $O(m\log m)$ work after the required matrix scan.
- A one-customer, one-bank matrix returns its only balance.
- Multiple customers may tie for the maximum; only the wealth value is returned.
- The richest customer may appear in any row, including the first or last.
- Rectangular matrices need not be square, but every row has the same number of banks.
- Different balance distributions can have the same row sum and are treated as equal wealth.
