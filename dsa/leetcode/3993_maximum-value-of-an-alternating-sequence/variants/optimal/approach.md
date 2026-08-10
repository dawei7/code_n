## General

**Replace the sequence with a sequence of rises and falls.**  The first value is fixed at `s`, so the only freedom is choosing how much each later value rises or falls. Because the sequence must alternate strictly, every adjacent step has a direction:

- an upward step increases the value by at least `1` and at most `m`;
- a downward step decreases the value by at least `1` and at most `m`.

The lower bound of `1` is important. The elements are integers and the inequalities are strict, so a downward step cannot keep the value unchanged. Likewise, an upward step cannot have size zero.

The objective is not to maximize the final element specifically. It is to maximize any element that appears anywhere in the sequence. Therefore, it is natural to look at the high points, or peaks, produced by the alternating steps. To make a peak as large as possible, every rise should use the full allowed increase `m`, while every forced fall before a later rise should lose only `1`. A rise can help the maximum, but a fall is merely the price paid before alternation permits another rise.

**Why the first step should go upward.**  There are two legal alternating patterns:

- `seq[0] < seq[1] > seq[2] < ...`, which rises immediately;
- `seq[0] > seq[1] < seq[2] > ...`, which falls immediately.

Starting upward is never worse for this maximization problem. It gives the sequence a rise of as much as `m` before paying for any fall. Starting downward pays a decrease of at least `1` before receiving its first increase. Since there is no other advantage to starting downward, the greatest attainable element comes from the first pattern.

Now use the best possible steps in that pattern. Beginning at `s`, increase by `m`, decrease by `1`, increase by `m` again, and continue:

`s, s + m, s + m - 1, s + 2m - 1, s + 2m - 2, ...`

Every complete “fall by one, then rise by `m`” pair raises the next peak by `m - 1`. The first peak is slightly special because it has no preceding fall: it is simply `s + m`.

Let

$$
q = \left\lfloor \frac{n}{2} \right\rfloor.
$$

There are exactly `q` upward steps available in the immediately-rising pattern, whether `n` is even or odd. The last and largest peak therefore contains `q` rises of size `m` and only `q - 1` earlier falls of size `1`:

$$
\begin{aligned}
\text{largest peak}
  &= s + qm - (q - 1) \\
  &= s + q(m - 1) + 1.
\end{aligned}
$$

This is exactly the expression used by the solution:

`s + n // 2 * (m - 1) + 1`.

**Why this is both attainable and an upper bound.**  The construction above is a valid sequence: every rise has difference `m`, every fall has difference `1`, and the directions alternate strictly. Thus the formula is not merely a bound; an actual sequence reaches it.

No other immediately-rising sequence can produce a larger peak. Before its `q`-th rise, it can gain at most `m` on each of `q` rises, and it must lose at least `1` on each of the `q - 1` intervening falls. Those limits give the same upper bound `s + qm - (q - 1)`. In the other orientation, every rise has a preceding fall. After the same number of rise/fall pairs, its value is at most `s + q(m - 1)`, one less than the immediately-rising construction. Therefore neither orientation can beat the returned value.

**Even and odd lengths use the same count.**  If `n = 2q`, the sequence ends at its `q`-th peak. If `n = 2q + 1`, the sequence has one extra position after that peak; put a value one smaller there. That final forced fall does not erase the peak that already appeared. This is why integer division `n // 2` works for both parities.

For example, with `n = 4`, `s = 3`, and `m = 5`, `q = 2`. The formula gives

$$
3 + 2(5 - 1) + 1 = 12.
$$

The sequence `[3, 8, 7, 12]` realizes that value. The two rises use the maximum change `5`, and the intervening fall loses only `1`. If `n` were `5` instead, appending `11` would preserve strict alternation, and `12` would still be the maximum.

The separate `n == 1` branch is necessary. A one-element sequence has no rise at all and is alternating by definition, so its only possible maximum is `s`. Substituting `n // 2 = 0` into the general expression would incorrectly add `1`.

## Complexity detail

The method performs a constant number of integer comparisons, divisions, multiplications, additions, and subtractions. It never constructs the sequence because the constraints ask only for its maximum possible element.

- Time complexity is `O(1)`.
- Auxiliary space complexity is `O(1)`.

The input limit `n \le 10^9` makes a direct simulation undesirable, while the formula is unaffected by that large bound. The largest arithmetic result is on the order of `nm`, at most roughly `10^{14}` under the given constraints. Python integers handle that automatically. In a fixed-width language, a 64-bit integer should be used.

## Alternatives and edge cases

- **Dynamic programming over positions and values:** One could track reachable high and low values after every position, but `n` can be as large as `10^9`. The extremal rise/fall argument collapses all of that state into one formula.
- **Building the maximizing sequence:** Repeatedly adding `m` and subtracting `1` makes the construction visible, but it takes `O(n)` time and stores information the return value does not require.
- **Starting with a fall:** This orientation is legal, but every upward move is preceded by a loss of at least `1`. It cannot recover the one-unit advantage of rising first.
- **Length one:** There are no adjacent comparisons, so the only element `s` is the answer. This is why the early return must precede the closed formula.
- **Even length:** The last position can be the largest peak, and there are `n / 2` rises.
- **Odd length:** The largest peak occurs one position before the end; the final fall does not reduce the maximum already attained.
- **The case `m = 1`:** Every legal rise and fall must have magnitude exactly `1`. Later peaks cannot exceed the first peak, and the formula correctly returns `s + 1` for every `n > 1`.
- **Strict inequalities:** Treating a fall as allowed to have size zero would incorrectly change each two-step gain from `m - 1` to `m`. The extra `+1` in the final expression follows directly from paying only `q - 1` falls before the last peak.
- **Values below zero:** The fixed start is positive, but the sequence elements are otherwise integers. The maximizing construction never needs a large downward move, so no lower-bound assumption is used.
- **Overflow outside Python:** The product `(n // 2) * (m - 1)` can exceed a 32-bit signed integer even though each individual input fits. Use 64-bit arithmetic in languages with fixed-width integer types.
