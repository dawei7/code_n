## General

On a number line, the travel distance between positions $a$ and $b$ is $\lvert a-b\rvert$. Because Person 1 and Person 2 move at the same speed, their arrival-time ordering is exactly their distance ordering; neither their direction of travel nor which side of `z` they start on changes the comparison.

Compute $d_1=\lvert x-z\rvert$ and $d_2=\lvert y-z\rvert$. Equal distances mean equal arrival times and require `0`. If $d_1<d_2$, Person 1 arrives first and the answer is `1`. The only remaining relation is $d_2<d_1$, which returns `2`. These three mutually exclusive comparisons cover every input.

## Complexity detail

The contract always supplies exactly three integer positions. Two subtractions, two absolute values, and a constant number of comparisons take $O(1)$ time and $O(1)$ auxiliary space.

The complete legal domain contains $100^3=1{,}000{,}000$ triples. A bounded-domain certificate replaces runtime scaling because there is no variable-size input to scale; exhaustive verification checks every legal combination against an independent squared-distance comparison.

## Alternatives and edge cases

- **Simulate movement:** Advancing both people one step at a time eventually gives the same result but performs unnecessary work proportional to their bounded distances.
- **Compare signed differences:** Positions on opposite sides of `z` can have differences with different signs, so travel requires absolute values.
- **Equal distances:** A tie returns `0`; it must not be broken by person number or starting side.
- **Person 1 starts at `z`:** Its distance is zero, so it wins unless Person 2 also starts there.
- **Person 2 starts at `z`:** The symmetric rule returns `2` unless both distances are zero.
- **All positions equal:** Both people have zero travel time, so the answer is `0`.
- **Same starting position:** If `x == y`, their distances and arrival times are necessarily equal.
- **Boundary positions:** Coordinates `1` and `100` use the same absolute-distance calculation without special handling.
