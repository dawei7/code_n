## General

**Arrival time is determined only by distance**

Person 1 starts at coordinate `x`, Person 2 starts at coordinate `y`, and the stationary Person 3 is at coordinate `z`. The first two people move toward `z` at the same speed.

For motion at constant positive speed `v`, travel time is:

`time = distance / v`.

Both arrival times have the same positive denominator `v`. Dividing two nonnegative distances by the same positive number preserves their order. Therefore:

- the smaller distance means the earlier arrival;
- equal distances mean equal arrival times.

The actual speed never needs to be known. The problem reduces to computing two number-line distances and comparing them.

**Distance on a number line requires an absolute value**

The distance between coordinates `p` and `q` is `abs(p - q)`. The absolute value matters because a person may begin on either side of `z`:

- if `p < z`, the movement distance is `z - p`;
- if `p > z`, the movement distance is `p - z`;
- if `p = z`, the movement distance is zero.

All three cases are captured by `abs(p - z)` without branching on direction.

The protected source computes:

`a = abs(x - z)`

`b = abs(y - z)`.

Here `a` is Person 1's distance and `b` is Person 2's distance. These short variable names are not positions or times; they are nonnegative travel distances.

**Map the comparison to the required return codes**

The return expression is a nested conditional:

`return 0 if a == b else (1 if a < b else 2)`.

It should be read from left to right:

1. If `a == b`, both travel the same distance at the same speed, so return `0`.
2. Otherwise the distances are unequal. If `a < b`, Person 1 is closer, so return `1`.
3. The only remaining possibility is `a > b`, so Person 2 is closer and the source returns `2`.

These cases are mutually exclusive and exhaustive for two integers. Exactly one required result is returned.

**Why relative side and movement direction do not matter**

Suppose Person 1 is left of `z` and Person 2 is right of `z`. Their routes point in opposite directions, but only route lengths affect arrival time. For example, with `x = 1`, `y = 5`, and `z = 3`, both distances equal two, so both arrive together.

If both people start on the same side, absolute difference still works. With `x = 2`, `y = 5`, and `z = 6`, their distances are four and one. Person 2 arrives first even though both move in the same direction.

If one person already stands at `z`, that person's distance and arrival time are zero, so that person necessarily wins unless the other person is also at `z`. The same comparison covers this without a special rule.

**A direct correctness argument**

Let `d_1 = |x-z|` and `d_2 = |y-z|`. Since both people have the same positive speed `v`, their arrival times are `t_1 = d_1/v` and `t_2 = d_2/v`.

If `d_1 = d_2`, then `t_1 = t_2` and returning zero is correct. If `d_1 < d_2`, division by positive `v` gives `t_1 < t_2`, so Person 1 arrives first and returning one is correct. If neither relation holds, `d_1 > d_2`, which implies `t_1 > t_2`; Person 2 arrives first and returning two is correct.

The source computes exactly `d_1` and `d_2` and implements exactly these three cases, so it always returns the specified result.

**Why no simulation is needed**

One might imagine moving both people one coordinate step per round until someone reaches `z`. That produces the same answer but repeats work proportional to the distances. The coordinates already determine the total route lengths. Comparing those lengths is the mathematical summary of the entire simulation.

This is also why the stationary person's coordinate is not treated differently based on whether it is between `x` and `y`. Every person's route is independent: each travels directly from their own coordinate to `z`.

## Complexity detail

The method performs two subtractions, two absolute-value operations, at most two comparisons, and one return. The number of operations does not depend on the coordinate magnitudes or on any input collection size. Time complexity is `O(1)`.

It stores two integer distances, `a` and `b`, and creates no growing data structure. Auxiliary space is `O(1)`.

The documented coordinates lie from one to one hundred, so subtraction is safe in every ordinary integer type. Python also handles arbitrary-size integers. Even if the coordinate range were much larger, the algorithmic complexity would remain constant under the standard fixed-word model, provided the integer type could represent the difference.

The method is asymptotically optimal: it must inspect the three supplied coordinates to distinguish cases, and it already uses only constant work and storage.

## Alternatives and edge cases

- **Step-by-step movement simulation:** Moving both people toward `z` until one arrives is intuitive but unnecessary. Absolute distance summarizes the number of equal-speed steps immediately.
- **Compare `x - z` with `y - z` without absolute values:** Signed differences encode direction as well as distance and can rank a farther person as “smaller” merely for being left of `z`.
- **Compare x directly with y:** Their closeness to each other says nothing about their separate distances to `z`.
- **Square the distances:** Comparing `(x-z)^2` and `(y-z)^2` would give the same ordering for nonnegative distances, but absolute values are simpler and avoid needless multiplication.
- **Compute explicit arrival times:** Dividing both distances by a shared speed cannot change their order. The speed is not provided because it cancels.
- **People on opposite sides of z:** Direction differs, but `abs` produces comparable route lengths.
- **People on the same side of z:** The nearer coordinate to `z` has the smaller absolute difference, exactly as required.
- **Person 1 already at z:** `a = 0`. The source returns one unless `b` is also zero.
- **Person 2 already at z:** `b = 0`. The source returns two unless `a` is also zero.
- **Both people at z:** Both distances are zero, so the equality branch returns zero.
- **x equals y:** Their distances to every `z` are identical, so the answer is always zero.
- **Symmetric positions around z:** If `x = z-d` and `y = z+d`, both distances are `d` and the result is zero.
- **Nested conditional readability:** Expanding the expression into `if`, `elif`, and `else` branches would be equivalent. The protected one-line return evaluates equality first and then resolves the only two unequal cases.
- **Equal speed assumption:** If speeds differed, distance comparison alone would be insufficient; one would need compare `distance/speed`. The problem explicitly guarantees equal speed.
