## General

**Focus on the exact moment person `k` finishes**

A direct simulation would repeatedly move through the queue, subtract one ticket from the person at the front, and move that person to the back if more tickets remain. That matches the story, but it performs one operation for every ticket bought. The total number of tickets can be much larger than the number of people.

The optimal solution instead asks a sharper question: by the moment person `k` buys their final ticket, how many tickets can each person possibly have bought?

Let

$$
T=\texttt{tickets[k]}.
$$

Person `k` needs exactly $T$ turns. The queue proceeds from lower indices to higher indices in each pass. This ordering splits everyone into two groups:

- a person at index `i <= k` is reached before or at `k` during the final pass, so that person can receive as many as $T$ buying opportunities;
- a person at index `i > k` would be reached only after `k` during that final pass, but the process stops immediately when `k` finishes, so that person can receive at most $T-1$ opportunities.

This single distinction lets the code compute the complete elapsed time in one traversal.

**Cap opportunities by the tickets a person actually needs**

Being offered $T$ turns does not mean a person necessarily uses all $T$. If someone needs only two tickets, they leave after their second purchase. Their contribution to the elapsed time is two seconds, even if the queue could otherwise have reached their position many more times.

For a person at or before `k`, the contribution is therefore

$$
\min(\texttt{tickets[i]},T).
$$

For a person after `k`, it is

$$
\min(\texttt{tickets[i]},T-1).
$$

The implementation encodes both formulas in one expression:

`min(x, tickets[k] if i <= k else tickets[k] - 1)`,

where `x` is `tickets[i]`. Each actual ticket purchase consumes exactly one second, so adding these per-person contributions gives the required total time.

Consider `tickets = [2, 3, 2]` and `k = 2`. Here $T=2$, and every index is at or before `k`. The contributions are $\min(2,2)=2$, $\min(3,2)=2$, and $\min(2,2)=2$, for a total of 6. The middle person still needs one more ticket after that, but that future purchase never occurs because person `k` has already finished.

Now consider `tickets = [5, 1, 1, 1]` and `k = 1`. Here $T=1$. Indices 0 and 1 can be served once, giving contributions 1 and 1. Indices 2 and 3 come after `k` and can be served at most $T-1=0$ times before the stopping moment, so each contributes 0. The answer is 2 seconds.

**Why the position boundary includes `k`**

The condition is `i <= k`, not merely `i < k`. Person `k` must contribute all $T$ of their own purchases, including the final purchase that ends the process. Using the later-position formula for `k` would cap their contribution at $T-1$ and make the answer one second too small.

For an earlier person, the $T$th opportunity occurs earlier in the same pass as `k`'s $T$th opportunity. For a later person, that opportunity would occur afterward and is never reached. This is why array position affects the cap by exactly one.

**Why summing the contributions is correct**

Every second before termination corresponds to exactly one person buying exactly one ticket. No second is shared between people, and there is no idle time. Thus the total elapsed seconds equal the sum of all purchases made before and including `k`'s final purchase.

For `i <= k`, the queue reaches `i` in each of the first $T$ passes unless that person has already left. Consequently, person `i` buys exactly the smaller of their need and $T$. For `i > k`, the queue reaches them during only the first $T-1$ complete passes before stopping at `k` in pass $T$. They therefore buy exactly the smaller of their need and $T-1$.

The loop adds precisely those exact purchase counts for every person. Since the people partition into the two position groups and all purchases up to the stopping moment are counted once, `ans` equals the elapsed time.

The input guarantees positive ticket counts. In particular, $T\ge 1$, so the later-person limit $T-1$ is never negative. The method reads `tickets` but does not change it; no simulation state is needed.

## Complexity detail

Let $n$ be the number of people, which is the length of `tickets`.

The loop visits each array element once. Each visit performs an index comparison, chooses one of two constant-time caps, computes a minimum, and adds it to `ans`. The total time complexity is $O(n)$.

Only `ans`, the loop index `i`, and the current ticket count `x` are maintained. The value `tickets[k]` is read directly from the input. No queue, copied array, or per-person state is allocated, so the auxiliary space complexity is $O(1)$.

The numeric value of the answer may be much larger than $n$, but it does not increase the number of loop iterations. This is the key advantage over simulation, whose running time is proportional to the number of purchases made.

## Alternatives and edge cases

- **Literal queue simulation:** Repeatedly decrementing the front person's tickets is easy to visualize and can be correct, but it takes one step per elapsed second. The contribution formula compresses all full and partial queue passes into $O(n)$ work.
- **Using a queue data structure:** A queue models the rotations but stores indices or remaining counts and still processes every purchase. It adds space without improving the purchase-proportional running time.
- **Counting full rounds globally:** It is possible to reason about complete rounds and then a partial round, but people leave at different times, which complicates the bookkeeping. The per-person minimum expresses the same effect locally and directly.
- **Person `k` at index zero:** No one appears before `k`. Later people receive at most $T-1$ turns, and when $T=1$ they contribute zero because the process stops after the very first purchase.
- **Person `k` at the last index:** Every person satisfies `i <= k`, so everyone may participate in the final pass before `k` finishes. Their contributions are all capped by $T$.
- **Target needs one ticket:** With $T=1$, people through index `k` contribute at most one purchase, while every later person contributes zero. The positivity guarantee makes this case safe and meaningful.
- **Another person needs fewer tickets than the cap:** The `min` is essential. Once that person buys all needed tickets, they leave and cannot contribute on later passes.
- **Another person needs many more tickets:** Their contribution is limited by the number of times their position is reached before `k` finishes. Tickets they would buy afterward do not belong in the answer.
- **The `i <= k` boundary:** Changing it to `i < k` undercounts person `k` by one. Changing it to apply $T$ to every index overcounts later people who are not reached in the final partial pass.
- **Input preservation:** The exact solution never decrements `tickets`. This is useful when the caller expects the input array to remain unchanged and reinforces that the computation is analytical rather than simulated.
