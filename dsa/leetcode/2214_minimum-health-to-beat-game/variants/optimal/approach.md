## General

**Reduce the game to total unavoidable damage**

Every level reduces the player's health by a nonnegative amount. Without armor, completing all levels would cause

$$
D = \sum_{i=0}^{n-1} \texttt{damage}[i]
$$

total damage. If the starting health were exactly `D`, health would be zero after the last level, which is forbidden because health must remain strictly greater than zero at all times. Starting with `D + 1` would leave exactly one health after the final hit and would therefore be sufficient without armor.

Armor changes the amount of damage actually received on at most one level. If it is used on a level whose listed damage is `d`, it prevents at most `armor` damage and cannot prevent more damage than that level deals. The amount saved is consequently

$$
\min(d, \texttt{armor}).
$$

Once the best saving is known, the minimum initial health is one more than the remaining total damage. The exact Python solution expresses that whole result in one return statement:

`sum(damage) - min(max(damage), armor) + 1`.

Each part has a separate purpose. `sum(damage)` is the damage before protection. `max(damage)` chooses the largest hit. `min(max(damage), armor)` is the damage the armor actually blocks on that hit. Subtraction gives the damage still received, and `+ 1` enforces the strict positive-health requirement.

**Why the armor belongs on a largest hit**

The armor's saving on damage `d` is `min(d, armor)`. As `d` becomes larger, this quantity never becomes smaller. Before `d` reaches `armor`, every extra point of damage gives one extra point that can be blocked. Once `d` is at least `armor`, the saving reaches its maximum possible value, `armor`, and stays there. Therefore, choosing a maximum element of `damage` maximizes the saving.

Another way to see this is to compare any chosen hit `d` with a largest hit `M`. Since `d \le M`, monotonicity of `min` gives

$$
\min(d, \texttt{armor}) \le \min(M, \texttt{armor}).
$$

Using armor on `M` can thus save at least as much health as using it on `d`. No alternative level can lead to a lower total received damage. If several levels share the maximum value, using the armor on any one of them produces the same saving; the formula does not need to choose an index.

It is also helpful to distinguish two cases. If `armor >= M`, the armor prevents the entire largest hit, so the saving is `M`. It cannot save more by being used elsewhere because no hit is larger than `M`. If `armor < M`, it prevents exactly `armor` points of that hit, which is the largest saving the armor can ever provide. In both cases, the same `min(M, armor)` formula is optimal.

**Why the order of levels does not require a simulation**

At first, “health must be greater than zero at all times” can suggest checking every prefix of the level sequence. Here, all `damage[i]` values are nonnegative. That means cumulative received damage never decreases as levels are completed. The greatest cumulative damage is therefore reached after the last level.

Let `B` be the amount blocked by the armor and let `R = D - B` be the total damage actually received. Starting with `R + 1` leaves one health after all levels. At every earlier point, the player has received no more than `R` damage, so health is also at least one there. Thus, surviving the final cumulative total automatically guarantees survival of every earlier prefix.

This remains true even when the protected level occurs in the middle of the sequence. Before that level, the player has taken only some nonnegative subset of the total unblocked damage. After that level, cumulative damage continues toward `R` but never exceeds the final total. The exact position chosen for armor affects the timing of the saving but not the minimum initial health when every loss is nonnegative and all levels must be completed.

**Why one additional health point is both sufficient and necessary**

After applying armor optimally, every valid play still receives exactly `R = D - \min(M, armor)` total damage. Starting with `R + 1` is sufficient because the ending health is one, and the monotone-prefix argument shows that all earlier health values are also positive.

It is also minimal. Any integer starting health of at most `R` leaves health at most zero after all `R` damage has been received. Since reaching zero is not allowed, no such starting value can beat the game. The computed result is therefore not merely a safe amount; it is the smallest possible amount.

The phrase “at most once” causes no special branch. Using armor cannot increase damage, so there is never a disadvantage to applying it, even if it blocks zero points. When `armor = 0` or every hit is zero, the subtraction is zero and the formula naturally behaves as though the ability were unused. This matches the contract without requiring an explicit decision flag.

**How the exact implementation obtains the result**

The implementation makes two logical passes through `damage` using Python's built-ins. `sum(damage)` accumulates every hit, while `max(damage)` finds the largest one. The constraints guarantee at least one level, so calling `max` is valid. Python evaluates the arithmetic using arbitrary-precision integers, which safely handles a total as large as roughly `10^5 \cdot 10^5`.

No array is modified. No simulation state, prefix array, or armor index is stored. The method returns only the numeric minimum health, so identifying which occurrence of the largest damage would receive the armor is unnecessary.

For example, with `damage = [2, 7, 4, 3]` and `armor = 4`, total damage is `16`, the largest hit is `7`, and the armor saves `min(7, 4) = 4`. The player must absorb `12` damage and therefore needs `13` initial health. Starting with `12` would end at zero; starting with `13` ends at one.

## Complexity detail

Let `n` be the number of levels. Python's `sum(damage)` examines all `n` elements, and `max(damage)` performs another scan of all `n` elements. Two sequential linear scans take `O(n) + O(n) = O(n)` time. The remaining `min` call and arithmetic operations take constant time with respect to the number of levels.

The method stores no collection whose size depends on `n`. Its conceptual working values are the total, maximum, blocked amount, and final arithmetic result, even though the one-line expression does not bind them to local names. Therefore, the auxiliary space complexity is `O(1)`. The input list already belongs to the caller and is not counted as new storage.

In a strict bit-complexity model, operations on arbitrarily large Python integers depend on the integers' digit counts. Standard interview complexity treats bounded input integers and arithmetic as constant-time operations, yielding the declared `O(n)` time and `O(1)` auxiliary space.

## Alternatives and edge cases

- **Simulate health for a guessed starting value:** One could choose where to use armor and walk through every level, but that still leaves the optimization and minimum-start search unresolved. The total-damage formula proves the answer directly and avoids repeated simulations.
- **Binary search the starting health:** A feasibility check could simulate the game for each candidate health, leading to an extra logarithmic factor and still requiring a strategy for armor use. Because all damage is nonnegative and the best saving is known greedily, binary search is unnecessary.
- **Prefix sums:** Prefix sums can report damage accumulated through each level, but the maximum prefix is always the full total here. Storing all prefixes adds `O(n)` space without changing the answer.
- **Try armor on every level:** Computing `D - min(damage[i], armor) + 1` for all indices is correct but redundant. The saving function is monotone, so only a largest hit needs consideration.
- **Armor exceeds every hit:** The armor blocks an entire maximum hit, not `armor` points beyond that hit. The inner `min` prevents subtracting damage that never existed.
- **Zero armor:** The blocked amount is zero, and the result is `sum(damage) + 1`. Using or not using the ability is equivalent.
- **Zero-damage levels:** They do not reduce health. If all levels deal zero damage, both the sum and maximum are zero, and the method returns `1`, the smallest strictly positive starting health.
- **One level:** The formula becomes `damage[0] - min(damage[0], armor) + 1`, exactly the health needed to survive the single protected hit.
- **Repeated largest values:** Any maximum-damage level is equally good. Since the return value does not include the chosen level, no tie-breaking is required.
- **Strictly positive health:** The final `+ 1` must not be omitted. A result equal to net damage would leave exactly zero health after the last level and fail the game.
- **Nonnegative-damage guarantee:** The final-total argument depends on cumulative damage never decreasing. If levels could heal the player through negative damage, the worst prefix might occur before the end and this simple formula would need reconsideration; the stated constraints rule that case out.
- **Large total damage:** The sum can exceed a 32-bit signed integer in other languages. Python handles it automatically; a fixed-width implementation should use a sufficiently wide integer type.
