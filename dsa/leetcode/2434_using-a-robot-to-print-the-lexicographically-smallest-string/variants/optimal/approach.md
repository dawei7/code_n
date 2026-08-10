## General

**Model the robot's temporary string as a stack**

Characters leave `s` only from its front and are appended to the end of `t`. Characters leave `t` only from its end to reach the paper. Therefore `t` behaves exactly like a last-in, first-out stack. The list `stk` stores that stack, and `ans` stores characters already written on paper.

The important decision after pushing a character is whether to pop the stack now or keep reading from `s` in hope of printing a smaller future character first.

**Know the smallest unread character**

The counter `cnt` initially records how many occurrences of every character remain in all of `s`. The variable `mi` starts at `'a'` and moves only upward. It represents the smallest character still unread after the current input character has been removed.

For each `c`, the code first decrements `cnt[c]` because that occurrence is no longer in unread `s`. It then advances `mi` while the count at the current letter is zero. Counter lookups for absent letters return zero, so `mi` skips every exhausted letter.

The loop stops at the first letter that still occurs, or at `'z'`. When no unread characters remain, `'z'` serves as a harmless upper sentinel: every lowercase stack character is at most `'z'`, so the stack will be completely emptied.

**When it is safe to print the stack top**

After appending `c` to `stk`, the code repeatedly pops while

`stk[-1] <= mi`.

If the top character is no greater than the smallest unread character, continuing to read cannot reveal a character smaller than that top. The top also blocks every older character beneath it, because stack order requires it to be removed first. Printing it now therefore gives the smallest possible next output character among all choices that can become available without first printing that same top.

If the top is greater than `mi`, some unread occurrence of `mi` can eventually be pushed. By waiting, that smaller character can sit above the current top and be printed first. Popping the larger top immediately would make the paper lexicographically worse at the earliest differing position, so the algorithm correctly keeps it in the stack.

The inner loop repeats because removing one safe top may expose another top that is also no greater than the unread minimum.

**Trace the choices**

For `s = "bac"`, the unread minimum after moving `b` is `a`. Since stack top `b > a`, the robot waits. After moving `a`, the unread minimum becomes `c`. The top `a <= c` is printed, exposing `b`; `b <= c` is also printed. Finally `c` is moved, no unread characters remain, and it is printed. The result is `"abc"`.

For `s = "zza"`, the unread minimum remains `a` while both z characters are pushed, so neither is printed. Once `a` is pushed and the input becomes empty, the sentinel condition allows pops in stack order: a, z, z. The result is `"azz"`.

**Why the greedy decision is correct**

At any moment, the only character immediately writable is the stack top. The alternative is to transfer more unread characters to the stack. If the top is at most the smallest unread character, no future transfer can place a smaller character above it. Any strategy that waits must eventually print some character no smaller than the current top before it can remove the current top, so printing the top now is lexicographically optimal.

If the top is larger than the smallest unread character, there exists a strategy that keeps transferring until an occurrence of that smaller character is pushed, then prints it before the larger top. Printing the top now would commit a larger next character and cannot be optimal.

These two cases cover every state. Each pop fixes the smallest possible next output character, so applying the rule repeatedly constructs the lexicographically smallest complete paper string.

**Every character is handled exactly once**

The outer loop pushes each source character once. A pushed character remains until one inner loop pops it, and no character can be popped twice. After the final input character, `mi` reaches the effective upper bound and the loop empties the stack. Thus both `s` and `t` are empty at completion, and `ans` contains all $n$ characters.

The counter may retain keys with zero values, but that does not affect minimum tracking. Only positive counts prevent `mi` from advancing.

## Complexity detail

Let $n$ be the string length. Building `Counter(s)` takes $O(n)$ time. The outer loop performs $n$ iterations. Although the inner loop is nested, every character is pushed once and popped once, so all inner iterations across the entire run total $n$. The pointer `mi` advances at most 25 times through the fixed alphabet. Total time is $O(n)$.

The counter uses at most 26 entries. The stack and answer lists can each hold $O(n)$ characters, so auxiliary space is $O(n)$. The final `join` creates the returned length-$n$ string. If output space is excluded, the stack can still grow to $n$, preserving the $O(n)$ bound.

The algorithm never removes characters from the front of a Python string, which would require repeated copying. Iterating over `s` models those removals without mutating the source.

## Alternatives and edge cases

- **Suffix-minimum array:** Precompute the smallest character in every suffix, then pop while the stack top is at most the next suffix minimum. This is equally $O(n)$ but uses another $O(n)$ array instead of a fixed alphabet counter.
- **Priority queue of unread characters:** A heap can reveal the minimum, but deletions of the current streamed occurrence and duplicate handling add overhead. Counts plus a monotone 26-letter pointer are simpler.
- **Explore operation sequences:** Each state can choose a transfer or pop, producing exponentially many possibilities. The greedy comparison eliminates that branching.
- **Already increasing string:** Each pushed character is no greater than the unread minimum and is printed quickly, preserving the string.
- **Strictly decreasing string:** Characters tend to accumulate until smaller ones arrive, then leave in stack order as allowed.
- **All characters equal:** Every top is safe immediately, so the output equals the input.
- **Repeated minimum letters:** `mi` remains at that letter until its last unread occurrence is consumed; stack tops equal to it may be printed safely.
- **No unread characters:** `mi` stops at `'z'`, and every lowercase stack top satisfies the pop condition, ensuring the temporary string empties.
- **Equality in the pop test:** A top equal to the unread minimum is safe to print. Requiring strict inequality would delay equal characters unnecessarily but would not improve the prefix.
- **LIFO restriction:** A smaller character buried below a larger stack top cannot be printed first. The proof always reasons about the accessible top and future characters that can be pushed above it.
