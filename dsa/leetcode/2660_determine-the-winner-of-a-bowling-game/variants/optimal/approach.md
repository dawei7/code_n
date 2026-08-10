## General

**Score each player's turns independently**

The rule for one turn depends only on that player's own previous two raw pin counts.

Helper `f(arr)` computes one total. The main function calls it for both arrays, then compares the two scores.

No state is shared between players, and one player's strikes never affect the other's multiplier.

**Check the two eligible prior indices**

At turn $i$, current pin count is $x$.

Its multiplier is two when either:

$$
i\ge1\ \text{ and }\ \texttt{arr[i-1]}=10,
$$

or:

$$
i\ge2\ \text{ and }\ \texttt{arr[i-2]}=10.
$$

Otherwise, multiplier is one.

The exact condition uses:

`(i and arr[i - 1] == 10) or (i > 1 and arr[i - 2] == 10)`.

In Python, zero is falsy and positive indices are truthy, so `i` safely guards the first previous-index access.

**Why raw previous pins are inspected**

The rule says a strike in either previous turn doubles the current turn. It does not depend on the previous turn's already multiplied score.

The source reads `arr[i-1]` and `arr[i-2]` directly. A previous turn that scored 20 only because it was doubled does not count as a strike unless its raw pin value was ten.

This distinction prevents multiplier effects from propagating incorrectly beyond two turns.

**At most one factor of two**

If both previous turns were strikes, the current value is still `2*x`, not `4*x`.

The condition combines the two strike tests with OR and chooses:

`k = 2`

once. It does not add or multiply separate bonuses.

**Boundary turns**

Turn zero has no previous turns, so both guarded conditions are false and its multiplier is one.

Turn one can inspect only turn zero. The `i > 1` guard prevents accessing index negative one as a supposed second prior turn.

From turn two onward, both preceding positions are valid.

**Trace player one in the first example**

For `[5,10,3,2]`:

- turn zero scores five;
- turn one scores ten because prior five is not a strike;
- turn two sees strike ten one turn ago, so scores six;
- turn three sees strike ten two turns ago, so scores four.

Total is:

$$
5+10+6+4=25.
$$

The strike influences exactly the next two turns.

**Trace consecutive strikes**

For a sequence containing `10,10,2`:

- the second ten is doubled if the first ten lies in its prior window;
- the following two is doubled because at least one prior turn is ten;
- it is not quadrupled even though both prior values may be ten.

Later turns stop receiving the effect once both strike positions are more than two indices behind.

**Score accumulation invariant**

Before iteration $i$, `s` equals the total official score for turns zero through $i-1$.

The multiplier condition examines exactly the raw turns that can affect turn $i$, chooses one or two according to the rule, and adds `k*x`.

This establishes the invariant through turn $i$. After the loop, `s` is that player's full score.

Calling the same correct helper on both equal-length arrays produces totals $a$ and $b$.

**Map score comparison to the required code**

The final nested conditional returns:

- one when `a > b`;
- two when `b > a`;
- zero otherwise.

The final case necessarily means equality because integers are totally ordered.

This structure prevents accidentally treating a draw as a win for player two.

**Why one pass is sufficient**

Only two fixed previous positions affect a turn, so no history beyond the input array and current index is needed.

The helper never recomputes scores for prefixes or simulates bowling frames. It makes one constant-time decision per turn.

**A strike can itself receive the multiplier**

Current `x` may also equal ten. If either preceding raw turn was a strike, the current ten contributes twenty to the score. Its raw stored value nevertheless remains ten, so it can trigger doubling for the following two turns as well.

This explains long runs of strikes: each later strike can score double because of earlier strikes, yet every later multiplier check still compares the original array entry with ten. Score multiplication never changes or consumes the triggering event, and one strike may legitimately influence two subsequent turns.

**Input preservation**

Both player arrays are read only. Totals and multipliers are local scalars.

## Complexity detail

For $n$ turns, each helper performs $O(n)$ work. Running it twice is still $O(n)$ total time.

The helper stores only a running score, index, current value, and multiplier. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Track a two-turn bonus countdown:** Maintain how many future turns remain doubled after strikes; correct but raw-array lookback is simpler.
- **Precompute multipliers:** Uses $O(n)$ space unnecessarily.
- **First turn strike:** It scores ten normally but doubles turns one and two.
- **Strike one turn ago:** Current pins are doubled.
- **Strike two turns ago:** Current pins are also doubled.
- **Both prior turns strikes:** Multiplier remains two, not four.
- **No strikes:** Score is ordinary sum of pins.
- **One-turn game:** No bonus can apply to the only turn.
- **Equal totals:** Return zero.
- **Raw versus scored prior value:** Only raw ten triggers the bonus.
