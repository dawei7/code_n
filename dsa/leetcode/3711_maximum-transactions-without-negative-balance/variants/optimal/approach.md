## General

The transactions must remain in their original order, but any of them may be skipped. The source greedily keeps every transaction first. Whenever the selected balance becomes negative, it removes the smallest selected amount—the most harmful transaction seen so far.

The data structure `st` is a `SortedList` containing all currently selected transaction amounts in ascending order. Its first element is always the minimum.

The variable `s` is the sum of the currently selected amounts, and `ans` starts as the total number of transactions. Every removal decrements `ans`, so the final value is the number still selected.

**Tentatively selecting every transaction**

For current amount `x`, the source performs:

`s += x`

`st.add(x)`.

This preserves the original order conceptually: the current transaction is appended after every previously retained index. `st` sorts only the **values used for choosing a removal**; it does not reorder the actual subsequence.

If `s >= 0`, the selected sequence remains feasible through the current position. Keeping `x` increases its cardinality by one, so there is no reason to skip it.

Positive receipts and zero transactions can never cause the first violation. A negative outgoing transaction may.

**Repairing a negative balance**

When `s < 0`, at least one currently selected amount is negative. The source removes:

`y = st.pop(0)`,

the smallest value. Among all possible single removals, deleting the minimum increases the remaining sum the most.

It updates:

`s -= y`.

Because `y` is negative, subtracting it raises the balance.

The source uses a `while` loop, but after one newly added transaction causes a previously feasible selection to go negative, one removal is enough. Let the prior nonnegative balance be $S$ and current amount be $x$. The minimum selected value satisfies $y\le x$, so:

$$
S+x-y\ge S\ge0.
$$

The loop nevertheless expresses the general requirement directly and remains correct.

**Why removing an earlier negative preserves prefix feasibility**

The removed minimum may be an earlier transaction rather than the current one.

If the current transaction is removed, the selected sequence returns to the previously feasible sequence.

If an earlier negative amount is removed, all selected-prefix balances before that transaction remain unchanged. Every balance at or after its old position increases by `-y`. Thus no earlier feasible prefix becomes negative, and the repaired final balance is nonnegative.

The remaining indices still appear in original order, so they form a legal subsequence.

**Why the most negative amount is the right exchange**

Once a violation occurs, not all tentatively selected transactions can remain: their total balance is negative, so at least one must be skipped.

Removing any one transaction restores the same cardinality—one less than the tentative set. Deleting the smallest amount leaves the largest possible balance among these one-removal choices. A larger remaining balance can only make future transactions easier to accept; it can never reduce future feasibility.

Suppose another one-removal repair deletes a larger amount `z > y`. Its final balance is smaller by `z - y`. The greedy choice has already been shown prefix-feasible after removing negative `y`, and future transactions are appended only after the processed prefix. Starting that future with the larger repaired balance cannot make any later acceptance harder.

This exchange principle is applied whenever necessary: preserve as many processed transactions as possible, and among equal-cardinality choices retain the one with the greatest useful balance by discarding the most harmful value.

**Prefix optimality**

After processing each input prefix, the maintained subsequence has maximum feasible cardinality for that prefix.

Assume the previous prefix had a maximum selection of $c$ transactions.

- If adding the current transaction stays feasible, the source obtains $c+1$. No solution can use more because only one new index was introduced.
- If adding it makes the best retained balance negative, a $c+1$ selection is impossible: such a selection would need the current transaction plus $c$ feasible earlier transactions, and the greedy exchange state is at least as well funded as any equal-cardinality earlier choice. The source removes one amount and retains a feasible selection of size $c$.

The minimum-removal exchange also maximizes the remaining financial cushion among maximum-cardinality choices, which supplies the condition needed for the next induction step.

At the final prefix—the complete array—the maintained cardinality is the requested maximum.

**Tracing the first example**

For `[2, -5, 3, -1, -2]`:

- keep $2$, balance $2$;
- tentatively keep $-5$, balance $-3$; remove the smallest value $-5$, restoring balance $2$;
- keep $3$, balance $5$;
- keep $-1$, balance $4$;
- keep $-2$, balance $2$.

Four transactions remain, forming `[2,3,-1,-2]`.

**Why `ans` equals the final selected size**

`ans` begins at $n$, treating every transaction as selected. Each `pop` permanently rejects exactly one transaction and decrements `ans` once. No other operation changes membership count.

Therefore, `ans` always equals `len(st)` after each repair and returns the final maximum cardinality. The source could return `len(st)` directly, but its explicit decrement tracks removals.

## Complexity detail

Let $n$ be the number of transactions.

Each value is inserted into `SortedList` once. Insertion costs $O(\log n)$. A value can be removed at most once, and removing index zero also costs $O(\log n)$ in the balanced block structure used by `SortedList`.

There are at most $n$ insertions and $n$ removals, giving $O(n\log n)$ total time.

The sorted collection may retain $O(n)$ values. All other state is scalar, so auxiliary space is $O(n)$.

The running balance can have magnitude up to $10^{14}$. Python integers handle it; a fixed-width implementation should use 64-bit arithmetic.

## Alternatives and edge cases

- **Min-heap:** A standard heap supports insertion and removal of the minimum in $O(\log n)$ and is sufficient because no other sorted operation is needed.
- **Skip every transaction that immediately fails:** Rejecting only the current value can be suboptimal when an earlier, more negative transaction should be exchanged out instead.
- **Dynamic programming by balance:** Balances span an enormous range, making a value-indexed DP infeasible.
- **All negative transactions:** Each tentative selection is repaired by removing a negative value, and the final answer is zero.
- **All transactions feasible:** No removal occurs and the method returns $n$.
- **Zero transaction:** It neither helps nor hurts balance but increases cardinality, so it should always be kept.
- **Repeated amounts:** `SortedList` preserves multiplicity; each occurrence represents a distinct transaction index.
- **Removing an earlier item:** Deleting a negative earlier transaction only raises later prefix balances and preserves relative order of all retained indices.
- **Several severe negatives:** The loop formulation can remove as many minima as needed, while each stored occurrence is popped at most once overall.
- **Negative final total of all transactions:** A large feasible subsequence may still exist after discarding the most damaging negative amounts.
