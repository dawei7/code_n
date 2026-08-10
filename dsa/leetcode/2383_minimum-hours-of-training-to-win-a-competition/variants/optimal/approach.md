## General

**Energy and experience create independent deficits**

Before each opponent, both current energy and current experience must be *strictly* greater than that opponent's values. Training one hour can increase either initial energy or initial experience, never both. Therefore, the minimum total hours is the sum of the independently necessary energy-training and experience-training increments.

The exact solution processes opponents in order and repairs each quantity only when the current value would fail. Although the problem says training occurs before the competition, adding a deficit during the loop is accounting shorthand: every added unit represents one extra unit that could have been trained initially. Additive state evolution makes the timing of this accounting equivalent.

**Repair energy just enough**

Let current energy be `x` and the opponent require strict superiority over `dx`. If `x > dx`, no energy training is needed for this fight. If `x <= dx`, the smallest winning value is `dx + 1`, so the exact deficit is:

```python
dx + 1 - x
```

The algorithm adds that many hours to `ans` and sets `x = dx + 1`. After winning, it subtracts `dx`, leaving energy one.

Training beyond `dx + 1` at that moment could help later opponents, but doing it early or lazily later costs the same number of hours. Adding only the currently forced deficit never increases the final total and avoids speculative overtraining.

**Repair experience just enough**

Current experience `y` must likewise satisfy `y > dy`. If it does not, the smallest legal value is `dy + 1`. The code adds `dy + 1 - y` training hours and raises `y` to that boundary.

After victory, experience increases by `dy` rather than decreasing. This makes later experience checks progressively easier, but a large upcoming opponent may still require an additional initial-training deficit in the accounting.

**Update state after both checks**

Both comparisons must use the values immediately before the current fight. Only after ensuring both are strictly greater does the algorithm execute:

```python
x -= dx
y += dy
```

Energy loss and experience gain then establish the state before the next opponent.

Using `<` rather than `<=` in a failure check would be wrong. Equality is not sufficient to win, so exactly matching an opponent requires one more training hour.

**Why lazy training still represents pre-competition training**

Suppose the loop discovers three missing experience points before a later opponent. Imagine adding those three points to the initial experience instead. Every earlier experience state would also be three larger, so earlier victories remain valid, and the later state becomes exactly the repaired value.

The same argument holds for energy. Extra initial energy simply carries through all earlier subtractions. A deficit detected later can be shifted back to the start without changing its one-hour-per-unit cost or invalidating any earlier fight.

Thus, the loop is not proposing illegal between-fight training. It incrementally calculates how much initial training was necessary.

**Trace the first example**

Initial energy `5` is enough for opponent energy `1`, then falls to `4`. Before the second opponent with energy `4`, equality fails. The algorithm adds one hour, raises energy to `5`, then spends four and leaves one. Later deficits are repaired similarly. Across the full sequence, the energy repairs total six, equivalent to starting with energy eleven.

Initial experience `3` beats the first opponent's `2` and becomes five. The next opponent has experience six, so the algorithm needs `6 + 1 - 5 = 2` hours, then winning raises experience further. No more experience training is needed. Total training is `6 + 2 = 8`.

**Why each repair is necessary**

At any encounter where current `x <= dx`, every successful plan must have contributed at least `dx + 1 - x` more initial energy than the training accounted so far. Nothing during competition increases energy, so no other mechanism can close that deficit.

Likewise, if `y <= dy`, every successful plan needs at least `dy + 1 - y` additional initial experience relative to the current accounting. Earlier opponent gains are already included in `y`, so they cannot supply more than recorded.

The algorithm adds exactly these unavoidable deficits and never adds training when current values already win. Every fight is therefore feasible, and the accumulated training contains no unnecessary unit. This proves minimality.

**Connection to a direct energy formula**

Since all energy costs are positive and no fight restores energy, starting energy must exceed the sum of every opponent's energy. The energy portion can be computed directly as:

$$
\max\left(0,\sum_i\texttt{energy}[i]+1-\textit{initialEnergy}\right).
$$

The exact code reaches the same total through lazy per-fight repairs. Experience cannot be summarized by just the total because each prefix has its own strict threshold, so sequential checks remain natural.

## Complexity detail

Let $n$ be the number of opponents. `zip(energy, experience)` produces each pair once. Every iteration performs constant-time comparisons and arithmetic, so total time is $O(n)$.

The method stores only `ans`, current energy `x`, current experience `y`, and the current opponent pair. It uses $O(1)$ auxiliary space and does not modify the input arrays.

Python integers prevent overflow in accumulated totals; fixed-width languages should choose types wide enough for sums.

## Alternatives and edge cases

- **Direct energy deficit plus experience scan:** Compute the energy formula once and simulate only experience. It is equally optimal and aligns with the manifest summary.
- **Train to a very large value immediately:** It ensures victory but can add unnecessary hours; exact deficits provide the minimum.
- **Simulate every training hour:** Incrementing one unit at a time is correct but obscures the direct deficit calculation.
- **Equality with an opponent:** Strict superiority means equality requires exactly one additional unit.
- **No training needed:** If both quantities exceed every current requirement as states evolve, `ans` remains zero.
- **One opponent:** Independently add the energy and experience deficits needed to exceed that opponent by one.
- **Energy always decreases:** Later checks include every earlier energy cost, which is why lazy repairs accumulate correctly.
- **Experience always increases after wins:** Earlier gains are automatically available to reduce later training needs.
- **Large early experience gain:** It may eliminate all later experience deficits even when initial experience was small.
- **Training accounting timing:** Every lazily added unit can be moved to the initial state, so the constructed count respects the before-competition-only rule.
