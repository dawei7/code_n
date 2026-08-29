## General

**There is only one possible coin combination per turn.** Let a turn use $a$ coins worth $75$ and $b$ coins worth $10$. It must satisfy

$$
75a+10b=115.
$$

Dividing by five gives $15a+2b=23$. The right side is odd, so $a$ must be odd. If $a\ge3$, the value already exceeds $115$. Therefore $a=1$, and then $b=4$.

Every legal turn consumes exactly one 75-value coin and four 10-value coins. There are no strategic choices, despite the game wording.

The total number of playable turns is

$$
T=\min\left(x,\left\lfloor\frac y4\right\rfloor\right).
$$

Alice plays turns $1,3,5,\ldots$, while Bob plays turns $2,4,6,\ldots$. The player who makes the final possible move wins because the other player then cannot move. Alice wins when $T$ is odd; Bob wins when $T$ is even.

**Understand the source's paired-turn shortcut.** Instead of computing $T$ directly, the code calculates

`k = min(x // 2, y // 8)`.

One pair of turns consumes two 75-value coins and eight 10-value coins. Thus `k` is the number of complete two-turn blocks that can be removed. Each block contains one Alice move and one Bob move and returns the turn to Alice, so removing any number of complete blocks does not change the winner.

The assignments

`x -= k * 2` and `y -= k * 8`

leave only the residual resources after all complete pairs.

**Check whether one Alice turn remains.** After maximal paired removal, fewer than two additional turns can be played. Alice can make one residual turn exactly when at least one 75-value coin and four 10-value coins remain.

The return condition is

`"Alice" if x and y >= 4 else "Bob"`.

In Python, positive integer `x` is truthy and zero is false. Because subtraction cannot make it negative here, bare `x` is equivalent to `x >= 1`. The other comparison explicitly checks `y >= 4`.

If both requirements hold, Alice makes the one remaining move and Bob loses. Otherwise, Alice cannot move after an even number of completed turns, so Bob is the winner.

**Why at most one turn remains.** If residual resources supported two turns, they would include at least two 75-coins and eight 10-coins. Then `k` was not maximal, contradicting its definition through integer division and minimum. Therefore a Boolean residual check completely determines parity.

**Trace $x=2,y=7$.** No full two-turn block exists because `y // 8 = 0`, so `k=0`. Residual `x` is nonzero and `y>=4`, meaning Alice can take one turn. She wins.

For $x=4,y=11$, one complete pair is removed: residual values are $x=2,y=3$. Alice cannot form another turn because fewer than four 10-coins remain. Exactly two turns occurred, so Bob made the last move and wins.

**Optimal play is automatic.** A player who can move must pick the unique combination. Refusing is not an allowed winning action, and no choice can preserve different coins for later. The result depends only on resource-limited turn count.

**Interface metadata discrepancy.** The checked-in method is named `losingPlayer`, which is the callable actually defined by `solution.py`. Its `submission.json` records native entrypoint `Solution.winningPlayer`. Those names disagree. This approach explains the source's behavior; integration must use the platform's real template contract rather than trusting the stale metadata field.

## Complexity detail

The method performs a fixed number of integer divisions, multiplications, subtractions, comparisons, and one conditional return. Time is $O(1)$ and auxiliary space is $O(1)$.

The constraints cap both counts at $100$, but the same constant-operation analysis applies to arbitrary machine-sized counts. Python's arbitrary-precision arithmetic would technically depend on integer bit length for enormous inputs, outside the problem model.

## Alternatives and edge cases

- **Direct turn parity:** Compute `turns = min(x, y // 4)` and return Alice if `turns % 2 == 1`. This is clearer and has the same constant bounds.
- **Turn-by-turn simulation:** Subtract one and four while possible, toggling the player. It is correct but takes $O(T)$ time and hides the closed form.
- **Search other coin combinations:** Unnecessary; the Diophantine equation has only $(1,4)$ in nonnegative integers.
- **Exactly one turn:** Alice makes it and wins.
- **Exactly two turns:** Bob makes the last move and wins.
- **Too few 75-coins:** `x` limits the total turns.
- **Too few 10-coins:** `y // 4` limits them.
- **Residual `x=0`:** The truthiness test fails even if many 10-coins remain.
- **Residual `y<4`:** No turn exists even if many 75-coins remain.
- **Positive-input guarantee:** Initial counts are at least one, but residual counts may become zero.
- **No strategic branching:** Every move consumes the same resources, so “optimal” players cannot change game length.
- **Method-name mismatch:** The implementation defines `losingPlayer` while submission metadata names `winningPlayer`; this should be reconciled outside the documentation campaign if runtime wiring relies on metadata.
- **Relation to the direct turn count:** `min(x // 2, y // 8)` equals the number of complete pairs inside `min(x, y // 4)` playable turns. Removing those pairs leaves precisely the total-turn parity as a one-move feasibility test.
