## General

The order of the moves determines the route taken, but the question asks only for the distance after every move has finished. For the final position, only the net displacement matters. All fixed moves can therefore be summarized by two signed coordinates, and every underscore contributes one additional unit move that may be chosen later.

The source uses these variables:

- `x` for the net displacement produced by `U` and `D`;
- `y` for the net displacement produced by `L` and `R`;
- `z` for the number of underscores.

Its sign convention is

```python
U: x -= 1
D: x += 1
L: y -= 1
R: y += 1
```

This rotates or reflects the usual coordinate naming, where horizontal displacement is often called `x` and upward movement is positive. That difference has no effect on Manhattan distance because only `abs(x) + abs(y)` is used. A coordinate axis can be named either way, and reversing both signs preserves absolute values.

After scanning the fixed commands, the current Manhattan distance is

$$
\lvert x\rvert+\lvert y\rvert.
$$

The source returns this value plus `z`.

**Why one wildcard can improve the distance by at most one**

One underscore becomes one unit move. If it changes one coordinate from `a` to `a+1` or `a-1`, the absolute value of that coordinate changes by at most one:

$$
\bigl\lvert\,\lvert a\pm1\rvert-\lvert a\rvert\,\bigr\rvert\le1.
$$

The other coordinate does not change. Therefore one wildcard can increase the final Manhattan distance by no more than one. With `z` wildcards, no assignment can improve the fixed displacement by more than `z`:

$$
\text{maximum distance}
\le
\lvert x\rvert+\lvert y\rvert+z.
$$

This is also an application of the triangle inequality. Every wildcard step has Manhattan length one, so adding all wildcard displacement vectors can increase the norm by at most the sum of their lengths.

**Why the upper bound is always attainable**

At least one direction can be chosen so that each wildcard extends the displacement rather than canceling it.

- If `x>0`, assign every wildcard to the move that increases `x`.
- If `x<0`, assign every wildcard to the move that makes `x` more negative.
- If `x=0` but `y\ne0`, extend `y` in its existing sign.
- If both coordinates are zero, choose any one direction for every wildcard.

In each case, every underscore increases one coordinate's absolute value by exactly one and never decreases the other. After all `z` assignments, the distance is exactly

$$
\lvert x\rvert+\lvert y\rvert+z.
$$

Because this construction reaches the previously established upper bound, it is optimal.

The wildcards do not have to use different directions. The contract says they may be replaced independently, which permits assigning all of them to the same direction. Independence gives freedom; it does not impose variety.

**Why the route order does not create an extra opportunity**

Manhattan distance is measured only after all commands. Vector addition is commutative, so the final displacement from a collection of moves is independent of the order in which their vectors are added. A route might temporarily travel farther from the origin and later return, but temporary distances are irrelevant to the requested final value.

For example, fixed moves `U` and `D` cancel regardless of where underscores appear between them. Once all fixed commands are summarized as `x=0` on that axis, assigning all wildcards in one direction yields their full contribution.

**How the scan maps to the formula**

The loop examines each character exactly once. The four explicit branches update the fixed displacement. The final `else` increments `z`; under the input contract, the only remaining possible character is underscore.

No wildcard direction is stored because the function returns only the maximum value, not an actual replacement string. The exact final line,

```python
return abs(x) + abs(y) + z
```

is the attainable upper bound derived above. The reasoning supplies a valid assignment whenever one is needed.

Consider `moves = "L_D_"`. The fixed moves give one unit left and one unit down, so `\lvert x\rvert+\lvert y\rvert=2` under the source's coordinate convention. There are two wildcards. Extending the negative directions uses both units productively, reaching distance four. The source calculates `2+2` directly.

If fixed commands cancel completely, such as `"UD__"`, the fixed distance is zero and there are two wildcards. Sending both in one direction reaches distance two, exactly the returned result.

## Complexity detail

Let `n` be the length of `moves`. The loop reads all `n` characters and performs constant work for each one, so time complexity is `O(n)`.

The method stores only three integer counters and the current character. It creates no array, replacement string, or route history. Auxiliary space complexity is `O(1)`.

Reading every character is necessary in the worst case because changing one unexamined command can change either the fixed displacement or wildcard count. The linear running time is therefore asymptotically optimal for the explicit input string.

The magnitude of each counter is at most `n`, and Python integers represent these values exactly. The input string is not modified.

## Alternatives and edge cases

- **Try all wildcard assignments:** With `z` underscores there are `4^z` possible replacements. The triangle-inequality upper bound and matching construction collapse that exponential search to one count.

- **Dynamic programming over reachable coordinates:** Tracking all positions after each command can require quadratic or larger state. Only the most distant final position is needed, and every wildcard can be made to contribute one to the fixed Manhattan norm.

- **Greedily choose while following the route:** One may assign each underscore to increase the current distance at that moment, but temporary position is unnecessary. Summarizing fixed displacement first gives a simpler global argument.

- **Split wildcards between axes:** This can also be optimal in some cases, but it is never necessary. Extending one existing nonzero coordinate, or choosing any axis from the origin, already gains one per wildcard.

- **No underscores:** Then `z=0` and the result is simply the Manhattan distance of the fixed endpoint.

- **Only underscores:** The fixed endpoint is the origin. Assigning all moves to one direction gives distance equal to the string length.

- **All fixed moves cancel:** Cancellation makes the fixed distance zero but does not reduce wildcard potential; every underscore can still extend a newly chosen direction.

- **One command:** A fixed command or an underscore always permits final distance one.

- **Axis naming and signs:** The source makes `U` negative on `x` and uses `y` horizontally. Manhattan distance is invariant under this convention, so it remains correct.

- **Unexpected characters:** The `else` branch would count any unrecognized character as a wildcard. The contract guarantees that only underscore reaches it; the source does not independently validate input.

- **Final distance rather than maximum during the walk:** The formula would not answer a question about the farthest intermediate position under sequential replacement decisions. It is correct because the requested measurement occurs after all moves.

- **Return value only:** The implementation does not reconstruct wildcard choices. The problem requests the maximum distance, and the constructive reasoning proves that this numerical value is achievable.
