## General

**Discard transaction history after netting accounts**

Subtract each amount from its giver and add it to its recipient. Once all $n$ records have been processed, only the final balance of each of the $p$ participants matters: any settlement that cancels those balances also settles the original history. Remove zero balances and place the remaining $k$ values in `balances`; their sum is zero.

**Settle the first unfinished balance completely**

At recursion position `start`, skip balances that earlier transfers have reduced to zero. If none remain, the current branch has settled everyone. Otherwise, pair `balances[start]` with every later balance of the opposite sign. One transaction can clear the first balance completely; adding it to the partner records whatever amount that partner still owes or is owed. The recursion therefore continues at `start + 1`, and restoring the partner afterward makes the mutation local to that branch.

This branching is complete because the first unfinished account must transact with an opposite-signed account in any settlement. Choosing its counterparty determines exactly the residual balance represented by the mutation, so one branch models the first transaction of every potentially optimal settlement. A same-signed transfer cannot clear the first account and is unnecessary.

**Remove equivalent branches without changing the answer**

Partners holding the same balance create identical residual multisets, so `tried` explores that value only once at the current depth. If a partner exactly cancels the first balance, an exchange argument guarantees an optimal settlement containing that direct transaction: any settlement that routes the two equal-and-opposite obligations through other accounts can redirect that amount between this pair without adding an edge among the remaining accounts. After evaluating the exact-cancellation branch, the loop can therefore stop. The minimum over the remaining distinct branches is the optimal transaction count.

## Complexity detail

Building the net-balance map costs $O(n)$ time and $O(p)$ space. In the worst case, the backtracking tree explores factorially many counterparty orders, so total time is $O(n + k!)$. The balance list and recursion use $O(k)$ space. Each active recursion frame also owns a `tried` set; across a depth-$k$ call path these sets can hold $O(k^2)$ values in total, giving $O(p + k^2)$ auxiliary space.

## Alternatives and edge cases

- **Bitmask subset dynamic programming:** can maximize the number of disjoint zero-sum groups in exponential state space, but requires a larger state table.
- **Unpruned backtracking:** remains correct, but repeatedly explores equal partner balances and continues after an exact cancellation; those redundant branches cause the benchmark control to exceed the runtime limit.
- **Greedily match the largest debt and credit:** produces a valid settlement but can use more transactions than necessary.
- **All balances cancel during aggregation:** leaves `balances` empty and correctly returns zero.
- **Repeated equal balances:** are interchangeable at one recursion depth, which is why value-based symmetry pruning is safe.
- **Sparse person identifiers:** belong in a map rather than an array sized by the largest identifier.
