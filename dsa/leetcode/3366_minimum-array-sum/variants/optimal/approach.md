## General

Each index offers at most five outcomes: leave its value unchanged, apply only operation 1, apply only operation 2 when eligible, or apply both operations in either legal order. Once one outcome is chosen, the index no longer interacts with later values except through the two shared operation budgets. This makes the numbers of operations already used sufficient dynamic-programming state.

Let `dp[a][b]` be the minimum sum contributed by the processed prefix after using operation 1 exactly $a$ times and operation 2 exactly $b$ times. Begin with `dp[0][0] = 0`; every other state is unreachable. For the next value $x$, enumerate its legal outcomes and transfer each reachable state to a fresh table with the corresponding operation counts and transformed value added.

The two combined outcomes must be calculated separately. Dividing first yields $\lceil x/2\rceil-k$ only if the halved value is at least $k$. Subtracting first yields $\lceil(x-k)/2\rceil$ only if $x\ge k$. These expressions can differ, so retaining both is necessary.

Inductively, after each processed prefix, every table entry is the minimum among exactly all legal assignments with its recorded counts: the base represents the empty assignment, and the transition appends every and only legal outcome for the next index. Therefore the minimum over the final table covers every assignment within both budgets and returns the global optimum.

## Complexity detail

Let $n$ be the array length. There are $(\texttt{op1}+1)(\texttt{op2}+1)$ states per layer and at most five constant-time transitions per state. The time complexity is $O(n\cdot\texttt{op1}\cdot\texttt{op2})$. Keeping only the previous and next layers requires $O(\texttt{op1}\cdot\texttt{op2})$ auxiliary space.

The benchmark defines `size` as $n$, sets both budgets to $n$, and makes all five per-index outcomes legal. The dynamic program is polynomial in the state dimensions. A correct exhaustive baseline that assigns every legal outcome to every index explores exponentially many combinations and is separated by the scaling verdict.

## Alternatives and edge cases

- **Top-down memoization:** Caching `(index, remaining_op1, remaining_op2)` has the same time complexity but retains all $n$ layers and therefore uses $O(n\cdot\texttt{op1}\cdot\texttt{op2})$ space.
- **Exhaustive operation assignment:** Trying every outcome for every index is correct but takes exponential time without memoization.
- **Greedy largest current reduction:** Spending the locally best operation first can prevent a better combined transformation or waste a scarce operation needed elsewhere.
- **Operation order:** Applying both operations requires testing both orders with eligibility checked against the intermediate value.
- **Upward rounding:** Compute $\lceil x/2\rceil$ as `(x + 1) // 2`, including for odd values.
- **At-most budgets:** The answer is the minimum over every final state, not only the state that exhausts both budgets.
- **Zero `k`:** Operation 2 changes nothing and need not be used.
- **Ineligible subtraction:** Operation 2 cannot be applied when the current value is below `k`, including after halving.
