## General

**The next match always comes from the best opposite price**

A buy order can match only the cheapest sell order, and only when that sell price is at most the buy price. A sell order symmetrically checks the most expensive buy order and requires that buy price to be at least the sell price.

The solution maintains two priority queues:

- `sell` is a normal min-heap of `(price, amount)`, so its first entry has the lowest sell price;
- `buy` stores `(-price, amount)`, turning Python's min-heap into a max-heap by price.

Each input row is a batch of independent orders. Storing one tuple with its remaining amount is equivalent to storing that many identical orders, but is vastly more efficient for amounts up to $10^9$.

**Process a buy batch**

For a buy batch with price `p` and remaining amount `a`, matching continues while three facts hold: `a` is positive, the sell heap is nonempty, and the cheapest sell price `sell[0][0]` is no greater than `p`.

The cheapest sell tuple `(x, y)` is removed.

- If `a >= y`, the current buy batch executes all `y` sell orders. The solution subtracts `y` from `a`, and that sell tuple is exhausted.
- If `a < y`, the buy batch executes completely. The solution pushes back `(x, y - a)` for the unexecuted sell remainder and sets `a = 0`.

When no further match is possible, any positive remaining `a` is pushed into `buy` as `(-p, a)`.

**Process a sell batch symmetrically**

For a sell batch, the best opposite order is at `buy[0]`. Its real price is `-buy[0][0]`. Matching is allowed while that price is at least the current sell price.

The same amount subtraction either exhausts the older buy tuple or exhausts the current sell batch and pushes back a reduced buy remainder. Any unmatched current sell amount finally enters `sell` as `(p, a)`.

The two cases mirror the execution rules exactly; only heap direction and price inequality change.

**Why batch subtraction preserves individual order semantics**

All orders within a batch have the same type and price, and the next input batch arrives only after all of them. Executing `min(a, y)` units between compatible batches produces the same backlog as matching those unit orders one by one.

Amounts influence only how many matches occur, not which price has priority. The heaps preserve the required price choice, while arithmetic skips repeated identical operations.

**Following the first example**

Five buys at price 10 enter `buy`. Two sells at 15 cannot match because the highest buy price is below 15, so they enter `sell`. One sell at 25 also enters.

The final buy batch has price 30 and amount 4. It first pops the cheapest sell tuple at 15 and consumes both units, leaving buy amount 2. It then pops the price-25 tuple and consumes its one unit, leaving amount 1. No sells remain, so one buy at 30 enters the backlog.

The original five buys at 10 plus that one buy total six.

**Why each heap choice is correct**

For a buy, if the minimum sell price exceeds `p`, every other sell price is at least as large and no match is legal. If the minimum is compatible, the rules require choosing it before any more expensive sell. The min-heap supplies exactly this decision. The max-heap gives the symmetric proof for sells.

After matching as much of the current batch as possible, either it is exhausted or the opposite heap has no compatible price. In the latter case its remainder must enter the backlog. Processing input rows in order therefore reproduces every specified execution, and the final heap amounts are exactly the unexecuted orders.

**Compute the final amount**

After all batches, the solution concatenates the heap lists for summation and adds the amount field `v[1]` from every tuple. Heap order is irrelevant at this stage.

The modulo $10^9+7$ is applied only to the final total. Matching decisions require exact amounts, so reducing stored amounts modulo the constant earlier would be incorrect. Python integers retain the full values safely.

## Complexity detail

Let $n$ be the number of input batches. Each batch is pushed at most once as a new backlog tuple. Fully exhausted tuples are popped once. A partial match can pop and reinsert one opposite tuple, but it exhausts the current incoming batch, so there is at most one such partial event per input batch. Total heap operations are therefore $O(n)$.

Each heap operation costs $O(\log n)$, giving $O(n\log n)$ time. The final concatenation and sum are $O(n)$.

The two heaps contain at most $O(n)$ tuples. The expression `buy + sell` also creates a temporary combined list of $O(n)$ references during summation. Total auxiliary space is $O(n)$. These bounds match the manifest.

## Alternatives and edge cases

- **Store unit orders:** Amounts reach $10^9$, so expanding a batch into individual heap entries is impossible.
- **Sorted lists:** Finding the best price is easy, but inserting arbitrary prices can cost $O(n)$ per batch.
- **Ordered price map:** A balanced tree keyed by price can aggregate equal prices and support extreme-price matching in $O(\log n)$, but Python has no built-in ordered map.
- **Aggregate identical heap prices:** It may reduce tuple count, though correctness does not require merging equal-price batches.
- **Equal prices:** Buy and sell prices satisfy both inclusive inequalities and must match.
- **No opposite backlog:** The entire incoming amount is stored on its own side.
- **Incompatible best price:** If the best opposite price cannot match, no worse heap entry can match either.
- **Current batch larger than top backlog batch:** The top is exhausted and matching continues with the next best price.
- **Current batch smaller than top backlog batch:** The current batch ends and the reduced opposite amount is pushed back.
- **Exact exhaustion:** Both amounts disappear when equal, and no zero tuple is pushed.
- **Same-price tuples:** Heap tie-breaking may use amount, but identical prices are interchangeable.
- **Modulo timing:** Apply it after exact matching, never to intermediate quantities.
- **Large total backlog:** Python's unbounded integers prevent overflow before the final modulo.
- **Input order:** Batches must be processed sequentially; sorting `orders` would change execution semantics.
- **Input preservation:** The loop unpacks values and changes only local `a`, leaving the input rows unchanged.
