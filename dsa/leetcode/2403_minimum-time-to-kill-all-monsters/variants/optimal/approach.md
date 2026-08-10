## General

**The only decision is monster order**

After each kill, mana resets to zero and `gain` increases by one. If exactly $c$ monsters have already been killed, the current gain is always:

$$
c+1.
$$

It does not depend on which monsters were killed, only how many. Therefore, a state can be represented by the subset of monsters still alive. The transition chooses which remaining monster to kill next.

**Meaning of the bitmask state**

Bit `i` in `mask` is one when monster `i` remains. `dfs(mask)` returns the minimum additional days needed to kill exactly those remaining monsters, given that all other monsters have already been killed.

The full-mask call begins with every monster alive. State zero has no remaining work and returns zero.

The number already killed is:

```python
n - mask.bit_count()
```

so the current gain is one plus that count.

**Compute days needed for the next monster**

Mana begins at zero after the previous kill. Each day adds `gain`. To reach monster power `x`, the minimum number of days is:

$$
\left\lceil\frac{x}{\textit{gain}}\right\rceil.
$$

The source computes the ceiling with integer arithmetic:

```python
(x + gain - 1) // gain
```

Killing immediately on the first day mana is sufficient is always optimal. Waiting longer does not increase gain—the gain changes only after a kill—and excess mana is discarded when the monster is defeated.

**Try every possible next monster**

For each set bit `i`, the recurrence removes it with:

```python
mask ^ (1 << i)
```

Because the bit is known to be one, XOR clears it. The candidate total is the days to accumulate enough mana for monster `i` now, plus the optimal days for the smaller remaining subset.

Taking the minimum examines every possible first choice and therefore every possible monster ordering.

**Why subset identity still matters**

Two states with the same number of remaining monsters have the same gain but may contain different power values. Their optimal future time can differ. The full subset mask—not only its bit count—is needed to identify which choices remain.

`@cache` ensures each subset is solved once even though many kill orders can reach it.

**Trace the first example**

For powers `[3,1,4]`, choosing power one first costs one day at gain one. One monster is then dead, so gain becomes two.

Choosing power four next costs `ceil(4/2) = 2` days. Gain becomes three, and power three costs one day. Total is four.

Choosing power three first would cost three days before gain can increase, which leads to a worse order. The recurrence evaluates both and retains the minimum.

**Why the recurrence is correct**

Consider an optimal strategy for state `mask`. It must kill some remaining monster `i` first. Before that first kill, gain is fixed by the number already dead, so at least `ceil(power[i]/gain)` days are necessary, and killing at that time is achievable.

After the kill, mana resets, gain increases, and the remaining problem is exactly `dfs(mask without i)`. By optimal substructure, replacing the suffix strategy with the cached optimum cannot worsen the total.

The recurrence considers the first monster used by every possible strategy and takes the best resulting cost. Induction on `mask.bit_count()` proves every state value is minimal, including the full starting mask.

**Duplicate powers are separate choices**

Monsters with equal powers have different bit indices. Different orders involving them may lead to identical numeric costs, but treating them as distinct state elements is harmless and matches the array's monster identities. Caching still merges states only when the same indices remain.

**Why no mana amount belongs in the state**

The algorithm assumes each transition kills immediately upon reaching enough mana. At that moment mana resets to zero. Thus, every recursive boundary begins with zero mana, and no leftover value needs to be remembered. This reset is what keeps the state to one subset mask.

## Complexity detail

There are $2^n$ possible masks. For each nonzero state, the loop scans all $n$ monster indices and performs constant work for set bits. Time complexity is $O(n2^n)$.

The cache stores one integer per reached mask, using $O(2^n)$ space. Recursive depth is at most $n$, which is dominated by cache storage. With $n\le17$, roughly 131,072 masks are manageable.

## Alternatives and edge cases

- **Bottom-up subset DP:** Initialize `dp[0] = 0` and add monsters in killed-set order. It has the same $O(n2^n)$ time and avoids recursion.
- **Greedy weakest first:** It often raises gain quickly but is not generally proven optimal; subset DP safely evaluates all orders.
- **Greedy strongest first:** It can waste many low-gain days on a powerful monster.
- **One monster:** The answer is `ceil(power[0] / 1)`.
- **Power divisible by gain:** Ceiling division returns the exact quotient without an extra day.
- **Power below gain:** One day is still required because mana starts at zero and increases only once per day.
- **Equal powers:** They remain separate bits but give symmetric transitions.
- **Mana reset:** No excess carries into the recursive state.
- **Gain progression:** It is determined solely by the number of cleared bits, not elapsed days.
