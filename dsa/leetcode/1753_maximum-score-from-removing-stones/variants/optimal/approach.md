## General

**Choose stones from the two largest piles**

Every move consumes one stone from each of two different non-empty piles. The exact solution repeatedly sorts the three current sizes and removes one stone from the two largest piles.

After `s = sorted([a, b, c])`, the invariant is:

$$
\texttt{s[0]}\le\texttt{s[1]}\le\texttt{s[2]}.
$$

The second element `s[1]` tells whether at least two piles are non-empty. If it is zero, then `s[0]` is also zero, so fewer than two non-empty piles remain and no legal move exists. While `s[1]` is positive, both `s[1]` and `s[2]` are non-empty and can supply the next move.

The loop increments `ans`, subtracts one from each of those two piles, and sorts the three sizes again to restore their order.

**Why balancing the large piles is safe**

The only way to lose future scoring opportunities is to leave stones stranded in one pile after the other two become empty. Taking from two largest piles avoids exhausting a scarce small pile while two much larger piles can be paired with each other.

For example, with sizes `[1,8,8]`, repeatedly using the two large piles earns eight moves. Spending the one-stone pile immediately is not necessarily fatal, but it provides no advantage; the large piles already balance each other perfectly.

With `[2,4,6]`, taking from piles four and six reduces the imbalance. Re-sorting after every move adapts when their relative order changes. Eventually the stones can be paired for six moves with none stranded.

An exchange argument supports the greedy choice. Consider any state sorted as $x\le y\le z$ with $y>0$. If an optimal plan's next move uses $x$ and one larger pile instead of $y$ and $z$, swap that move to use $y$ and $z$. The total number of stones falls by the same two, and the smallest pile is preserved as an additional future partner. This cannot reduce the number of later legal pairings. Repeating the exchange yields an optimal plan that makes the greedy move first.

**Two upper bounds reveal the achievable score**

Let $T=a+b+c$ be the total number of stones and $M=\max(a,b,c)$ the largest pile.

Every move removes two stones, so no strategy can score more than:

$$
\left\lfloor\frac{T}{2}\right\rfloor.
$$

Also, every move must use at least one stone outside the initially largest pile. There are $T-M$ such stones, so no strategy can score more than $T-M$ if the largest pile dominates all others.

The maximum possible score is consequently bounded by:

$$
\min\left(\left\lfloor\frac{T}{2}\right\rfloor,\ T-M\right).
$$

The two-largest greedy process achieves this bound. When no pile dominates, it keeps the piles balanced until at most one total stone remains, reaching $\lfloor T/2\rfloor$. When the largest pile is larger than the other two combined, every smaller-pile stone can be paired with it, reaching $T-M$, after which only the largest pile remains.

The exact source does not calculate this formula; it realizes the same optimum one move at a time.

**Why sorting after subtraction matters**

Suppose `s[1]` and `s[2]` are decremented. Either may become smaller than `s[0]`, so the previous indices no longer necessarily identify the two largest piles.

Calling `s.sort()` reestablishes the order before the next condition check. Since the list always has exactly three items, the sort has constant cost per iteration. Omitting it could repeatedly choose a now-empty or no-longer-largest slot and break the greedy invariant.

The piles have no identities relevant to the answer. Reordering their sizes loses no information because a move depends only on choosing two different non-empty piles, not on their original labels.

**Trace the balanced example**

Starting from `[4,4,6]`, the loop always reduces two largest current values. The total is fourteen, and no pile exceeds the other two combined. The total-stone upper bound is seven.

After seven iterations, all fourteen stones have been removed in pairs, `s[1]` becomes zero, and `ans` is seven. The greedy simulation therefore reaches the upper bound and is optimal.

**Why termination and the answer are correct**

At the top of each iteration, sorted `s` has at least two positive entries, so the chosen move is legal. Each iteration represents exactly one game move and increments the score exactly once. Total stones decrease, so the loop must terminate.

When it stops, `s[1] == 0` implies at most one pile remains non-empty, exactly the game's stopping condition. The greedy exchange reasoning and bound argument show that the sequence does not stop earlier than an optimal strategy would. Therefore `ans` is the maximum score.

## Complexity detail

Let $P$ be the returned score. The while loop executes exactly $P$ times. Sorting exactly three integers is $O(1)$ per iteration, as are the subtraction and counter update. The exact implementation therefore takes $O(P)$ time. Since $P \le \lfloor(a+b+c)/2\rfloor$, this is also $O(a+b+c)$.

This does not match the manifest's stated $O(1)$ time. A direct return of `min((a + b + c) // 2, a + b + c - max(a, b, c))` would achieve constant time, but that formula is not what the current `solution.py` executes. The approach documents the exact source honestly.

The list always contains three integers, and all other state is scalar. Auxiliary space is $O(1)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Closed-form bound:** Return $\min(\lfloor T/2\rfloor,T-M)$ in $O(1)$ time and space. It is asymptotically faster than the exact simulation.
- **Max heap:** Repeatedly pop the two largest piles and push decremented sizes. It generalizes to more piles but adds machinery for exactly three.
- **Choose arbitrary non-empty piles:** It can exhaust small partners too soon and strand avoidable stones in a large pile.
- **Two equal largest piles:** Pairing them is immediately safe and keeps their sizes balanced.
- **One dominant pile:** Every stone from the other two can score once; leftover dominant stones cannot be paired.
- **No dominant pile:** Stones can be paired until at most one total stone remains.
- **All piles equal:** Re-sorting rotates which physical piles are largest, but labels do not matter.
- **Positive inputs:** The initial loop always has a legal move because all three piles begin non-empty.
- **Stopping condition:** In sorted order, `s[1] == 0` exactly means fewer than two non-empty piles.
- **Sort of three values:** It is constant per move, but the number of moves grows with input magnitudes.
- **Score counter:** One increment corresponds to one legal removal from two distinct indices.
- **Large pile sizes:** The simulation can perform up to roughly 150000 iterations under the constraints, unlike the constant-time formula.
- **Input values:** They are copied into `s`, so the integer arguments themselves are not mutated.
- **Pile identity:** Sorting is valid because the objective and legal move depend only on current sizes.
