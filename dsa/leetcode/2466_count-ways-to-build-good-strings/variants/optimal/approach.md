## General

Let $H=\texttt{high}$ and define `ways[length]` as the number of different strings of exactly that length. The empty string is the unique construction of length zero, so `ways[0] = 1`.

Every non-empty constructible string has a unique final operation. If its last operation appended `zero` zeros, removing that suffix leaves a string counted by `ways[length - zero]`. If its last operation appended `one` ones, removing that suffix leaves a string counted by `ways[length - one]`. The two groups are disjoint because their final characters differ, even when `zero == one`. Therefore

$$
\texttt{ways[length]}=
\begin{cases}
\texttt{ways[length-zero]} & \text{if }\texttt{length}\ge\texttt{zero},\\
0 & \text{otherwise}
\end{cases}
+
\begin{cases}
\texttt{ways[length-one]} & \text{if }\texttt{length}\ge\texttt{one},\\
0 & \text{otherwise.}
\end{cases}
$$

Process lengths from one through `high`, applying the modulus after each recurrence. Add `ways[length]` to the answer exactly when `length >= low`. Since both operations strictly increase length, every predecessor is already finalized and no cycle is possible.

## Complexity detail

Each of the $H$ lengths performs at most two constant-time transitions, so time is $O(H)$.

The DP array stores one value for every length from zero through $H$, giving $O(H)$ auxiliary space.

## Alternatives and edge cases

- **Top-down memoization:** Recursing on the current length with caching has the same $O(H)$ state count, but iterative DP avoids recursion-depth limits.
- **Combinatorial enumeration:** Enumerating counts of zero and one blocks and summing binomial coefficients is correct, but doing so for every target length can take $O(H^2)$ time.
- **Generate actual strings:** Materializing every construction is exponential in `high` and is unnecessary because the final operation determines the recurrence.
- **Equal block lengths:** When `zero == one`, both transitions must still be added because appending zeros and appending ones produce different strings.
- **Unreachable lengths:** A DP entry remains zero when neither block length can reach it.
- **Inclusive range:** Lengths equal to `low` and `high` both contribute to the answer.
- **Modulo arithmetic:** Reduce both state counts and the running total so large construction counts remain bounded.
