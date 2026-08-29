## General

**Translate the table into one total per customer**

Each inner list in `accounts` belongs to one customer. Its entries are the amounts that customer holds in different banks. The problem defines wealth as the sum across all those entries, so for a row `v` the exact wealth is `sum(v)`.

Once every customer has one row sum, the richest wealth is simply the largest of those sums. The source expresses both levels directly:

`max(sum(v) for v in accounts)`.

The generator visits the customer rows one at a time. For the current row, `sum` visits all bank balances and produces that customer’s total. `max` compares each produced total with the largest one seen so far and ultimately returns the greatest.

**Why a generator is enough**

There is no need to remember every customer’s total after comparing it. If the first processed customer has wealth six, the running maximum is six. If the next has wealth ten, the running maximum becomes ten. A later total of eight cannot change it. At every point, only the greatest wealth among the rows processed so far matters.

The generator expression supplies totals lazily to `max` instead of constructing a separate list such as `[sum(v) for v in accounts]`. That avoids storing one additional number per customer. Each row already exists in the input; only its scalar sum is temporarily produced.

The constraints guarantee at least one customer, so `max` always receives at least one value. No default value or empty-input branch is needed.

**A trace**

For `accounts = [[1, 5], [7, 3], [3, 5]]`:

- the first row yields `1 + 5 = 6`, so the current maximum is six;
- the second yields `7 + 3 = 10`, replacing the current maximum;
- the third yields `3 + 5 = 8`, which is smaller than ten.

The returned answer is ten. The index or identity of the customer does not need to be returned, so the implementation stores only the wealth value.

For `[[1, 2, 3], [3, 2, 1]]`, both row sums are six. `max` returns six regardless of which tied customer is considered first. This matches the contract: it asks for the wealth of a richest customer, not for a unique customer ID.

**Why the result is correct**

For each customer `i`, the inner `sum` adds every `accounts[i][j]` exactly once and adds no amount belonging to a different row. It therefore computes precisely the definition of that customer’s wealth.

After processing any prefix of customer rows, `max` retains the greatest total in that prefix. This is true after the first row, and processing another row either preserves the old greatest total or replaces it with the new larger total. By induction, after the final row it holds the greatest wealth among all customers. That is exactly the requested result.

**Why every account must be read**

Even though the code is short, its linear work is necessary. Before an account balance is examined, it could be large enough to make its owner the richest customer. In the general case, no correct algorithm can ignore arbitrary cells. The method performs the minimum conceptual work: one addition per balance and one comparison per customer total.

The positivity guarantee makes every wealth positive, but the logic would also correctly find the maximum for zero or negative entries because `max` initializes itself from an actual generated row sum rather than from an assumed value such as zero.

## Complexity detail

Let `m` be the number of customers, let customer `i` have `n_i` accounts, and define

$$
S = \sum_{i=0}^{m-1} n_i,
$$

the total number of cells. Every cell participates in exactly one row sum, so summation takes $O(S)$ time. Comparing the `m` row totals adds $O(m)$ work, which is contained in $O(S)$ because every row is nonempty. Total time is $O(S)$, or $O(mn)$ for the rectangular `m \times n` grid.

The generator does not materialize all row sums. Apart from iterator and accumulator state used by Python’s built-ins, it keeps only the current total and running maximum, so auxiliary space is $O(1)$. The input grid itself is not copied or modified.

Python integers can grow beyond fixed machine width, though the stated bounds keep every sum small. Each addition is treated as constant time under ordinary problem-model arithmetic.

## Alternatives and edge cases

- **Explicit nested loops:** Maintain `current_wealth` for each row and `best` globally. This is longer but exposes the same $O(S)$ time and $O(1)$ space mechanics.
- **List comprehension of row sums:** `max([sum(v) for v in accounts])` is correct but allocates an $O(m)$ temporary list that the generator avoids.
- **Sort customer totals:** Sorting can identify the largest value but costs $O(m\log m)$ after the sums and stores all totals, neither of which is needed for one maximum.
- **Tied richest customers:** Only the wealth is returned, so equal maximum totals need no tie-breaking rule.
- **One customer:** The only row sum is necessarily the maximum and is returned.
- **One bank per customer:** Every row sum equals its single entry, so the operation reduces naturally to finding the largest balance.
- **All balances equal:** Row lengths are equal in the rectangular input, so all wealth totals tie and that common total is returned.
- **Positive-input guarantee:** It permits an explicit-loop version to initialize a maximum to zero, but the exact built-in expression does not rely on that detail.
- **Nonempty-grid guarantee:** Without at least one row, `max` would raise an exception; the stated `m >= 1` makes the call safe.
- **No customer index returned:** Tracking which row produced the maximum would be extra state for information the contract does not request.
