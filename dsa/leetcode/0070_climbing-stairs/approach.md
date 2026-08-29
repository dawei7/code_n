## General

**Describe a way by its final move**

A climbing way is an ordered sequence of moves of size one or two whose sum is `n`. Order matters: for three steps, `1, 2` and `2, 1` are different ways.

Let $W(i)$ be the number of ways to reach exactly step $i$. Every way reaching step $i$ has exactly one of two mutually exclusive final moves:

- It ends with a one-step move from step $i-1$.
- It ends with a two-step move from step $i-2$.

Removing that last move leaves a valid way to the corresponding earlier step. Conversely, appending the appropriate last move to any way reaching $i-1$ or $i-2$ creates a unique way reaching $i$. No way belongs to both groups because its last move cannot be both one and two. Therefore

$$
W(i)=W(i-1)+W(i-2).
$$

This is the Fibonacci recurrence, but deriving it from the final move is more important than recognizing its name. The derivation explains why addition is correct and why no sequence is missed or counted twice.

**Choose base states that make the recurrence natural**

There is one way to climb zero remaining steps: take no moves. Thus $W(0)=1$. There is also one way to reach step one: one single-step move, so $W(1)=1$.

The code uses the conventional Fibonacci values $F_0=0$ and $F_1=1$ rather than storing $W(0)$ and $W(1)$ directly. Since the climbing sequence is shifted by one position,

$$
W(n)=F_{n+1}.
$$

The variables begin as `a = 0` and `b = 1`, representing $F_0$ and $F_1$. After one update, they represent $F_1$ and $F_2$; after two updates, $F_2$ and $F_3$. Running exactly `n` updates leaves `b` equal to $F_{n+1}=W(n)$.

This shifted viewpoint also handles the smallest allowed input cleanly. When `n == 1`, the loop runs once, changes `(a, b)` from `(0, 1)` to `(1, 1)`, and returns one.

**Use only the two states the next transition needs**

A full dynamic-programming array would store $W(0),W(1),\ldots,W(n)$. Yet the recurrence for the next value consults only the previous two values. Once a transition has been made, older entries can never influence a future answer except through the two accumulated states. They do not need to remain in memory.

The simultaneous assignment

`a, b = b, a + b`

must be read using the old values on the right. Python first evaluates the pair `(b, a + b)`, then assigns its two results to `a` and `b`. Consequently the old `b` becomes the new earlier Fibonacci value, while the sum becomes the new later value. A sequential rewrite such as setting `a = b` before calculating `b = a + b` would incorrectly use the already changed `a` and lose one of the old states.

**A precise loop invariant**

Before iteration $k$, where $k$ iterations have already completed, `a` equals $F_k$ and `b` equals $F_{k+1}$. This is true before the first iteration because the initialization gives $F_0$ and $F_1$.

Assuming it is true for some $k$, the simultaneous update produces

$$
(F_{k+1}, F_k+F_{k+1})=(F_{k+1},F_{k+2}),
$$

so the invariant holds for the next iteration. After `n` iterations, it gives `b = F_{n+1}`. The final-move derivation established that $F_{n+1}=W(n)$, so the returned value is exactly the requested number of climbing sequences.

**Trace a small staircase**

For `n = 4`, the states evolve as follows. Initially `(a, b) = (0, 1)`. After the first step of the loop they are `(1, 1)`, after the second `(1, 2)`, after the third `(2, 3)`, and after the fourth `(3, 5)`. The returned value is five.

Those five ways are `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, and `2+2`. The trace is not enumerating them during execution; it is compressing the counts of all partial ways into two recurrence values.

**Why this is dynamic programming despite having no table**

Dynamic programming means solving overlapping subproblems once and reusing their results. It does not require an array. Here each count is calculated exactly once in increasing step order, and the two values needed by the next subproblem are retained. This is bottom-up dynamic programming with rolling state.

## Complexity detail

The loop performs exactly `n` iterations. Each iteration contains one integer addition and a constant number of assignments, so under the customary arithmetic model the time complexity is $O(n)$, matching the manifest. The constraint `n <= 45` keeps values small, but the structural bound remains linear in `n`.

Only the two recurrence values and the loop counter are stored. Their number does not grow with the staircase length, so auxiliary space is $O(1)$. The approach allocates neither an array nor a recursion stack.

## Alternatives and edge cases

- **Full dynamic-programming table:** Store every $W(i)$ and fill the recurrence from left to right. It is easy to inspect but uses $O(n)$ space even though only two prior values are needed.
- **Memoized recursion:** Express the final-move recurrence directly and cache each step. It runs in $O(n)$ time but uses a cache and an $O(n)$ call stack.
- **Unmemoized recursion:** Branch on taking one or two steps. It mirrors the definition but recalculates the same remaining-step states exponentially many times.
- **Matrix exponentiation:** Raise the Fibonacci transition matrix by repeated squaring for $O(\log n)$ arithmetic operations. It is faster asymptotically but substantially more machinery for this constraint.
- **Closed-form formula:** A formula involving the golden ratio appears constant-sized, but floating-point rounding can return an incorrect integer when values become large.
- **`n == 1`:** One update returns one; no separate branch is needed.
- **`n == 2`:** Two updates return two, representing `1+1` and `2`.
- **Ordered sequences:** `1+2` and `2+1` are distinct; the recurrence counts them through different predecessor states.
- **No zero input in the contract:** The initialization would return one if the loop ran zero times, which is the conventional empty-path count, but the stated domain starts at one.
- **Parallel assignment:** Both right-hand expressions must use the old state. Changing it to careless sequential assignments breaks the recurrence.
- **Maximum input:** At `n == 45`, the loop still uses constant state and performs only 45 transitions.
