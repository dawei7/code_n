## General

**Reduce survival to total unavoidable damage**

Every damage value is nonnegative and the levels have a fixed order. Consequently, cumulative damage never decreases, so the lowest health occurs after the final level. If the total unavoidable damage is $D$, starting with $D+1$ health is both sufficient and necessary: the final health is one, while starting with only $D$ would end at zero.

**Spend the armor where it saves the most**

Using the armor on damage $x$ prevents $\min(x,\texttt{armor})$. This saving is non-decreasing as $x$ grows, so no choice can save more than using it on the maximum element. Scan the list once while accumulating its sum and largest value. Subtract the smaller of that maximum and `armor`, then add one for the strict-positive requirement.

An exchange argument confirms the greedy choice. If a plan uses armor on a value smaller than the maximum damage, moving it to a maximum-damage level cannot reduce the prevented amount. Thus an optimal plan always has the saving used by the formula, and the returned health is minimal.

## Complexity detail

Let $n$ be the number of levels. Computing the sum and maximum takes $O(n)$ time.

Apart from scalar totals, the method uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try every armor placement:** Computing the resulting total for every level can take $O(n^2)$ time if the damage sum is recomputed each time.
- **Prefix simulation:** Tracking health after choosing an armor position is unnecessary because all damage is nonnegative and the final cumulative loss is always the largest.
- **Armor exceeds every hit:** The armor prevents only the full damage of one level, never more than that level deals.
- **Zero armor:** No damage is prevented, so the answer is the total damage plus one.
- **Zero-damage levels:** They do not change the cumulative loss or invalidate the maximum-based choice.
- **Strict positivity:** The final `+1` is required even when all damage is zero.
