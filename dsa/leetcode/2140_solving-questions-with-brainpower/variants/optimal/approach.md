## General

At each question, exactly two decisions are available: solve it and jump over a required number of later questions, or skip it and move to the next question. A choice affects only which suffix of the exam remains available. That repeated suffix structure makes dynamic programming appropriate.

**Define one state with a complete meaning**

Let `dfs(i)` be the maximum points obtainable from questions at indexes `i` through the end, assuming question `i` is the next one on which a decision may be made.

This definition includes every consequence of earlier choices. The function does not need to remember which earlier question caused a jump, because reaching index `i` already means all skipped restrictions have been honored.

If `i >= len(questions)`, no questions remain. The only possible additional score is zero, so the base case returns `0`. Using `>=` rather than equality is important because solving a question may jump beyond the first index after the array.

**Evaluate the solve decision**

The current pair is unpacked as `p, b = questions[i]`. Solving it immediately earns `p` points. The next `b` questions, at indexes `i + 1` through `i + b`, become unavailable. The first index where a new decision may be made is therefore

`i + b + 1`.

The best total under the solve choice is `p + dfs(i + b + 1)`. The recursive call is allowed to skip that next available question too; `dfs` means the best plan for the suffix, not a promise to solve its first question.

**Evaluate the skip decision**

Skipping question `i` earns nothing now and leaves question `i + 1` available. Its best total is `dfs(i + 1)`.

There are no other legal decisions. The recurrence is consequently

$$
\operatorname{dfs}(i)=\max\left(
p_i+\operatorname{dfs}(i+b_i+1),
\operatorname{dfs}(i+1)
\right).
$$

The exact code returns this maximum directly.

For `[[3,2],[4,3],[4,4],[2,5]]`, solving index zero contributes three and moves to index three, where solving contributes another two, for five. Skipping index zero exposes other alternatives, but their best score does not exceed five. The recurrence compares these possibilities at each suffix rather than committing greedily to the largest immediate point value.

**Cache every suffix result**

Without memoization, many decision paths ask for the same `dfs(i)`. For instance, one branch may skip to an index while another may arrive there after solving an earlier question. Recomputing both subtrees would cause exponential work.

The `@cache` decorator stores the result for each integer argument `i`. The first call computes the state; later calls with the same index return its saved value. There are only $n$ in-range indexes plus possible beyond-end base-case indexes reached by jumps.

Different oversized indexes can technically create several cached base cases, but each originates from one of the $n$ questions, so the number of cached arguments is still $O(n)$.

**Why the recurrence is correct**

Consider any state `dfs(i)`. Every valid plan either solves question `i` or skips it.

If it solves, `p` is forced into the score and no decision before `i+b+1` is legal. By definition, `dfs(i+b+1)` is the best possible continuation, so the solve term is optimal among all plans that solve `i`.

If it skips, the remaining problem is exactly the suffix beginning at `i+1`, whose optimum is `dfs(i+1)`. Taking the maximum selects the better of two exhaustive categories. The base case is correct for an empty suffix, so this argument applies backward to every reachable index, including `dfs(0)` for the full exam.

**Why a local greedy rule fails**

The largest point value may carry a large brainpower penalty, while a smaller question may allow several later questions to be solved. Similarly, the best ratio of points to skipped questions does not capture the exact future combinations. The DP compares complete optimal suffix values, which is the information local rules omit.

## Complexity detail

Let $n$ be the number of questions. Each in-range state `dfs(i)` is evaluated at most once because of `@cache`. Its work outside recursive calls is constant: unpack one pair, compute two indexes, add, and take a maximum. The number of cached beyond-end states is also at most linear. Total time is $O(n)$.

The cache stores $O(n)$ state-result pairs. The recursive skip path can call `dfs(0)`, `dfs(1)`, and so on before unwinding, so call-stack depth may reach $O(n)$. Total auxiliary space is $O(n)$.

Python’s usual recursion limit is much smaller than the legal maximum of $10^5$ questions. The exact recursive source therefore relies on a runtime that raises the limit or otherwise accommodates deep recursion; in a default Python environment, a long skip chain may raise `RecursionError`. A bottom-up DP avoids that practical risk.

## Alternatives and edge cases

- **Bottom-up suffix DP:** Fill an array from right to left using the same solve-versus-skip recurrence. It keeps $O(n)$ time and space and avoids recursion depth, making it safer for the maximum input size.
- **Forward score propagation:** Track the best score reaching each index and propagate skip and solve transitions. This can also be linear but needs careful handling of jump destinations and the final maximum.
- **Greedy by points:** Taking the question with the most immediate points can block a more valuable combination later.
- **Greedy by brainpower:** Always choosing the smallest skip penalty ignores how many points are earned.
- **One question:** `dfs(0)` compares its positive points with skipping to zero, so it solves the question.
- **Jump beyond the array:** The `i >= len(questions)` base case returns zero for any oversized destination without special clamping.
- **All large brainpower values:** Each solved question may end the exam, but skip branches still let the DP choose the best later standalone question.
- **Positive points:** Solving the final available question always beats skipping it, though the general recurrence needs no special final-element case.
- **Repeated state:** Memoization ensures different paths that reach the same suffix share one computation.
- **Cache scope:** The nested function and its cache are created for one method call, so results from a different input cannot leak into this run.
- **Deep recursion:** The mathematical complexity is linear, but default Python stack limits are a material implementation constraint at $n=10^5$.
- **Input preservation:** The algorithm reads question pairs and stores cached integers without changing `questions`.
