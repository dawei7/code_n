## General

**Every request is an accept-or-reject choice**

There are at most 16 requests. That small bound allows enumeration of every subset. A bitmask with $M$ bits represents one choice:

- bit `i` equals one if request `i` is accepted;
- bit `i` equals zero if it is rejected.

Integers from zero through `(1 << M) - 1` cover all $2^M$ subsets exactly once.

The method tests whether each chosen subset leaves every building’s net employee change at zero and records the largest number of accepted requests among valid subsets.

**Computing a subset’s balance**

The helper `check(mask)` creates `cnt = [0] * n`. For an accepted transfer from building `f` to building `t`, it performs:

`cnt[f] -= 1`

`cnt[t] += 1`.

Thus `cnt[b]` equals employees entering building `b` minus employees leaving it across the selected requests. The sign convention could be reversed without changing the zero test, but the source consistently uses incoming as positive.

After scanning all requests, `all(v == 0 for v in cnt)` returns true exactly when every building has equal incoming and outgoing counts. That is the achievability condition.

A request from a building to itself subtracts and adds at the same index, for net zero. Such a request never harms feasibility and may increase the selected count.

**Counting selected requests**

For each mask, `mask.bit_count()` returns the number of one bits, which is exactly the number of accepted requests in that subset.

The source calls `check(mask)` only when `ans < cnt`. If the subset selects no more requests than the best valid subset already found, it cannot improve the maximum, so validating its building balances would be wasted work.

The strict inequality is sufficient because only the maximum count is requested. Equal-size valid subsets do not change `ans`.

If a larger subset is balanced, `ans = cnt` records its size. Starting `ans` at zero is valid because the empty subset always has zero net change.

**Why every possible solution is represented**

Any selection of requests corresponds to one unique mask: set exactly the bits for the accepted requests. The outer range visits that mask. `check` adds precisely the transfers in the selection and tests the given zero-net rule.

Therefore, every achievable request set is recognized unless its size is already no larger than `ans`, in which case skipping it cannot affect the maximum. Every update comes from a balanced subset. The final `ans` is both achievable and at least as large as every achievable subset, so it is the requested maximum.

**A cycle interpretation**

Selected transfers can be viewed as directed edges. Zero net change means every vertex has equal selected indegree and outdegree. Such edges decompose into directed cycles, including self-loops.

For example, transfers zero to one, one to two, and two to zero form a balanced cycle and all three may be accepted. An isolated transfer three to four creates negative balance at three and positive balance at four, so a subset containing only that edge is invalid.

The algorithm does not need to construct the cycles. The balance array is a complete algebraic test for whether a decomposition is possible.

**Why exhaustive enumeration is appropriate**

The building count can reach 20, but the request count—not the building count—controls the subset space and is capped at 16. At most 65,536 masks are considered, which is practical.

A greedy choice based on individual requests cannot guarantee balance because usefulness is collective. A request that looks unbalanced alone may complete a large cycle with later requests, while accepting a locally appealing pair could prevent a larger feasible subset only if choices were prematurely fixed. Enumeration avoids that issue.

## Complexity detail

Let $N$ be the number of buildings and $M$ the number of requests.

There are $2^M$ masks. `bit_count` is constant time here because $M\le16$. For every mask that can beat `ans`, `check` allocates and initializes $N$ counters, scans all $M$ requests, and scans up to $N$ counters in `all`. In the worst case, pruning does not remove the exponential order, so exact time is:

$$
O\left(2^M(M+N)\right).
$$

The package’s shorter $O(N2^M)$ description suppresses the request scan or treats the bounded $M$ factor as small. The source explicitly scans both dimensions.

The iterative implementation stores one length-$N$ balance array inside a check plus scalar loop state. Its actual auxiliary space is $O(N)$, not recursive $O(N+M)$ stack space. The requests and masks are not copied.

## Alternatives and edge cases

- **Recursive backtracking:** Accept or reject each request while mutating one shared balance array, then undo accepted changes. It has the same exponential search and uses $O(N+M)$ space including recursion.
- **Meet in the middle:** Splitting requests into halves can combine balance vectors and may help for larger $M$, but the bound of 16 makes direct enumeration simpler.
- **Greedy acceptance:** Individual transfers do not reveal whether they participate in a balanced cycle, so local choices cannot ensure a maximum subset.
- **Check masks in descending bit count:** This can return after the first balanced size is found, though ordering or grouping masks adds complexity. The source uses a simple ascending numeric scan with size pruning.
- **Empty subset:** It is always balanced and justifies initializing `ans = 0`.
- **All requests achievable:** The all-ones mask passes and updates `ans` to $M$.
- **Self-transfer:** Its decrement and increment cancel, so it never changes feasibility and contributes one accepted request.
- **Duplicate requests:** Each is a distinct employee request and has its own bit. Multiplicity is handled correctly.
- **Disconnected cycles:** Each balanced component contributes zero net change independently, so their union passes.
- **One unmatched edge:** It creates two nonzero building balances and fails.
- **Buildings absent from every request:** Their counters remain zero and do not affect validity.
- **Subset-size pruning:** A mask with count equal to `ans` is skipped because it cannot improve the numerical answer.
- **Generator short-circuit:** `all` may stop at the first nonzero building, improving typical work without changing the worst-case bound.
- **Exact source space:** No recursion is used; only the current balance list grows with $N$.
