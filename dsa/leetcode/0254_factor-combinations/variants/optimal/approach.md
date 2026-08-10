## General

A factor combination is a list of integers from `2` through `n - 1` whose product is the original `n`. The same multiplication can be written in many orders—for example, `2 * 2 * 3`, `2 * 3 * 2`, and `3 * 2 * 2`—but those are one combination, not three. The central design decision is therefore to generate factors only in nondecreasing order.

The exact solution performs depth-first backtracking. The shared list `t` contains the factors already chosen. A call `dfs(n, i)` has the following meaning:

- `n` is the product still not represented by `t`;
- every additional chosen factor must be at least `i`;
- the product of `t` times this remaining `n` equals the original input.

The minimum allowed factor `i` is what enforces nondecreasing order and eliminates permutations.

**The remaining quotient is already a complete ending**

At the beginning of every recursive call, if `t` is nonempty, the solution appends `t + [n]` to `ans`. This says: stop splitting now and use the entire remaining quotient as the final factor.

For example, after choosing `2` from `12`, the recursive state is `t = [2]`, `n = 6`, so `[2, 6]` is immediately a valid answer. The same call may continue splitting `6`, choosing another `2` and reaching `t = [2, 2]`, `n = 3`; that new state records `[2, 2, 3]`.

The top-level call has an empty `t`, so it deliberately does not append `[original_n]`. A one-element list containing `n` is excluded because factors must lie below `n`; the task asks for actual factorizations into at least two factors.

**Search only possible smaller factors**

Within `dfs(n, i)`, candidate `j` begins at `i` and continues while `j * j <= n`. If `j` divides `n`, then `n // j` is its paired quotient. Limiting `j` to the square root ensures

$$
j\le \frac{n}{j}.
$$

So choosing `j` keeps it no larger than the remaining quotient that may eventually become the last factor. Trying divisors above the square root would merely rediscover the same pair in reversed order.

When divisibility holds, the algorithm:

1. appends `j` to `t`;
2. recurses on quotient `n // j` with new minimum `j`;
3. pops `j` to restore `t` before trying the next candidate.

Passing `j` rather than `j + 1` allows repeated factors, which are necessary for combinations such as `[2, 2, 3]` and `[4, 4]`.

**Why the appended quotient respects ordering**

At a recursive state, every value already in `t` is at most the current minimum `i`. The state was reached by choosing some factor `j` with `j * j <= previous_remainder`, so its quotient—the new remaining `n`—is at least `j`. Therefore, appending `n` to `t` yields a nondecreasing list. The solution never emits a list such as `[3, 2, 2]`.

More formally, each chosen factor becomes the lower bound for all subsequent choices, and every chosen divisor is no greater than its paired quotient. Both the continuing path and the stop-now output preserve sorted order.

**Trace for `n = 12`**

The initial call is `dfs(12, 2)` with `t = []`, so no answer is recorded yet.

- Candidate `2` divides `12`. Append it and call `dfs(6, 2)`.
  - This state first records `[2, 6]`.
  - Candidate `2` divides `6`. Append it and call `dfs(3, 2)`.
    - This state records `[2, 2, 3]`.
    - No candidate satisfies `j * j <= 3`, so it returns.
  - Backtracking removes the second `2`; the call has no other divisor through $\sqrt6$ and returns.
- Back at the root, candidate `3` divides `12`. Append it and call `dfs(4, 3)`.
  - This state records `[3, 4]`.
  - Since `3 * 3 > 4`, no further split respects nondecreasing order.
- Candidate `4` is beyond $\sqrt{12}$, so the root loop ends.

The result contains exactly `[[2,6], [2,2,3], [3,4]]`, possibly in that depth-first order, which the contract permits.

**Why every emitted combination is valid**

Initially, the remaining product is the original input. Whenever `j` is selected, divisibility guarantees an integer quotient, and replacing remaining `n` by the factors `j` and `n // j` preserves the total product. The recursion maintains this product relation. Every emitted list includes the remaining quotient, has at least two entries because `t` is nonempty, and contains nondecreasing factors of at least two. Its product is exactly the original number.

**Why every valid combination appears once**

Sort any valid factor combination into nondecreasing order $f_0,f_1,\ldots,f_{k-1}$. At the root, $f_0$ divides the remaining product and cannot exceed its complementary product, so the loop reaches it. After choosing it, $f_1\ge f_0$ is permitted by the new lower bound and divides the new remainder. Repeating this follows a unique recursion path through all factors except the last; at that state, the remaining quotient equals $f_{k-1}$ and the combination is appended.

No second path can produce the same sorted list because its first chosen factor would have to be the same, then its second, and so on. The monotonic lower bound removes all reordered duplicates.

## Complexity detail

The cost is output-sensitive and depends strongly on the divisor structure of `n`. Let $F$ be the number of returned combinations, $P$ the total number of integers across all returned lists, and let

$$
W=\sum_{\text{visited states}}\text{number of candidate divisors tested in that state}.
$$

The exact running time is $O(W+P)$: $W$ covers modulus tests, and $P$ covers copying `t + [n]` into the output. The root contributes at most $O(\sqrt n)$ divisor tests. Every non-root state corresponds to one emitted combination, and a simple coarse bound is $W=O((F+1)\sqrt n)$, though actual remainders rapidly shrink and the observed work is usually much smaller.

The manifest's $O(\sqrt n+\text{output})$ notation is best read as an output-sensitive summary in which traversal needed to discover emitted factorizations is included in “output.” A fully explicit analysis should retain $W$, because recursive states can test nondivisors that do not themselves create output entries.

Ignoring the returned lists, recursion depth is at most $O(\log n)$ because each selected factor is at least two and the remaining quotient shrinks by at least a factor of two. The path list `t` has the same bound. Thus auxiliary working space is $O(\log n)$. Including results, storage is $O(P)$ in addition to that stack.

## Alternatives and edge cases

- **Generate ordered factor sequences:** Trying all factor orders and deduplicating with a set wastes work on permutations. The nondecreasing lower bound prevents duplicates before they are created.
- **Iterative DFS:** Store states containing a factor path, remaining quotient, and minimum factor. It avoids recursion but copies more partial paths and can use substantially more working memory.
- **Prime input:** The root tests candidates through $\sqrt n$ but finds no divisor. Since `t` is empty, `[n]` is not emitted, and the answer is empty.
- **`n = 1`:** No candidate begins below or at its square root, and the top-level one-element form is excluded, so the result is `[]`.
- **Perfect square:** The condition `j * j <= n` includes the square-root divisor. This is necessary for combinations such as `[4, 4]` when `n = 16`.
- **Repeated factors:** Recursing with lower bound `j`, not `j + 1`, allows the same factor again.
- **Remaining quotient as a factor:** Recording `t + [n]` before further splits ensures shorter valid factorizations such as `[2, 6]` are not lost while exploring longer forms.
- **Backtracking restoration:** `t.pop()` must run after every recursive return so a candidate from one branch does not leak into the next branch.
- **Large prime near $10^7$:** There is no output, but the algorithm still performs roughly $\sqrt n$ divisibility tests; this is why the non-output root term matters.
- **Result ordering:** DFS produces a deterministic nondecreasing-factor order, but the outer ordering of combinations need not be sorted because any answer order is accepted.
