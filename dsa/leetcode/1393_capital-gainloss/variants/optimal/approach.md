## General

**Treat every transaction as signed cash flow**

Buying a stock sends money out, so a buy price contributes a negative amount. Selling brings money in, so a sell price contributes a positive amount. Once each row has the correct sign, a stock's total capital gain or loss is simply the sum of all its signed transactions.

The exact expression

`IF(operation = 'Buy', -price, price)`

returns negative `price` for a buy and positive `price` otherwise. The table's enum guarantees the only other operation is `'Sell'`, so the else branch represents sales exactly.

This avoids pairing each buy row with a particular later sell row. Pairing is unnecessary for total net result because addition is associative:

$$
\sum(\text{sell prices}-\text{buy prices})
=
\sum\text{sell prices}-\sum\text{buy prices}.
$$

The guarantees about earlier buys and later sells ensure the data describes valid trading sequences, but chronological order does not affect the final net cash flow.

**Group independently by stock**

`GROUP BY 1` groups by the first expression in the `SELECT` list, which is `stock_name`. Each stock receives its own aggregation group, so transactions belonging to different names never mix.

Within one group, `SUM(...)` adds all signed prices and names the result `capital_gain_loss`. A positive value is a net gain, a negative value a net loss, and zero means buys and sells balance exactly.

Using the column position is legal MySQL syntax, although `GROUP BY stock_name` would be more explicit and less fragile if the select-list order later changed.

**Following the sample**

Leetcode has a buy at 1000 and a sell at 9000. Their signed contributions are $-1000$ and $+9000$, totaling 8000.

Handbags contributes $-30000+7000=-23000$, so the negative output correctly represents a capital loss.

Corona Masks contributes

$$
-10+1010-1000+500-1000+10000=9500.
$$

This equals the sum of the three separately described trade gains, but the query never needs to discover or materialize those pairs.

**Why `operation_day` is unused**

The output asks only for the total gain or loss per stock, not per trade, day, or holding period. Once the input guarantees valid buy-before-sell relationships, transaction day does not change a row's monetary sign. It remains part of the table's primary key and data semantics but is irrelevant to this aggregate.

**Why the result needs no ordering**

The contract allows rows in any order. `GROUP BY` does not promise alphabetical or insertion order, and the query intentionally omits `ORDER BY` because no presentation order is required.

**Why the query is correct**

For any stock, every buy price is included once with a negative sign and every sell price once with a positive sign. Their sum is precisely total sale proceeds minus total purchase costs, which is the definition of accumulated capital gain or loss. Grouping performs this calculation separately for every stock name. Therefore each output row has the correct net value, and every stock present in the table receives one row.

**Why transaction pairing is not required**

Suppose a stock is bought several times and later sold several times. The Reference guarantees a valid sequence, but the total result depends only on the aggregate money spent and received. Reordering additions or choosing a different conceptual pairing leaves the sum unchanged. This is why a single conditional aggregate is both simpler and more general than self-joining buys to sells.

## Complexity detail

Let $N$ be the number of transaction rows and $K$ the number of distinct stock names. A hash-aggregation plan reads each row once, computes one signed value, and updates one group total, giving expected $O(N)$ time. The hash table stores one accumulator per stock, using $O(K)$ space. These bounds match the manifest.

A database may instead sort by `stock_name` before aggregating, which can cost $O(N\log N)$ time, or exploit an index that already groups rows. SQL is declarative, so the physical plan depends on indexes and optimizer statistics. Output contains $K$ rows and is normally excluded from auxiliary-space accounting.

## Alternatives and edge cases

- **`CASE` expression:** Use `CASE WHEN operation = 'Buy' THEN -price ELSE price END`. It is standard and often more portable than MySQL `IF`.
- **Separate buy and sell aggregates:** Sum buys and sells in separate expressions and subtract. It is correct but repeats conditions and is longer.
- **Pair transactions with window functions:** This is unnecessary for net gain and adds assumptions about matching individual trades.
- **Self-join buys to sells:** It risks multiplicative matches when a stock trades several times and is much harder to make correct.
- **One buy-sell pair:** The aggregate reduces directly to sell price minus buy price.
- **Several trading cycles:** All signed flows combine correctly regardless of conceptual pairing.
- **Net loss:** A negative sum is returned as-is; no absolute value should be applied.
- **Zero net result:** Equal total buys and sells produce zero.
- **Operation domain:** The else branch assumes every non-buy row is `Sell`, guaranteed by the enum. Unexpected values would be incorrectly treated as sales.
- **Transaction order:** `operation_day` is unnecessary for the total, though it establishes valid chronological semantics.
- **Positional grouping:** `GROUP BY 1` means the first selected expression, `stock_name`; explicit naming is more maintainable.
- **Any result order:** The lack of `ORDER BY` is intentional.
- **Null prices outside the contract:** `SUM` would ignore null contributions, so valid data must provide the stated integer price.
