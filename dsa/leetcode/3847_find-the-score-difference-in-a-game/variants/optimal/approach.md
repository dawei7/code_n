## General

**Represent the active player with a sign**

The requested result is:

$$
\text{first player's score}-\text{second player's score}.
$$

Instead of maintaining two totals, the source uses `k`:

- `k = 1` means the first player is active;
- `k = -1` means the second player is active.

Awarding `x` points changes the score difference by:

- `+x` for the first player;
- `-x` for the second player.

Both cases are expressed by:

`ans += k * x`.

The initial active player is the first, so `k` begins at 1.

**Apply the odd-score swap before awarding points**

For each game value `x`, the first rule says an odd value swaps the players before the game is played.

Multiplying the sign by -1 swaps its meaning:

`k *= -1`.

The source performs this when `x % 2` is nonzero.

Even values leave `k` unchanged.

**Apply the sixth-game swap second**

Game indices are zero-based, so the 6th, 12th, 18th, and later sixth games have indices 5, 11, 17, and so on.

These are exactly indices satisfying:

`i % 6 == 5`.

The source applies another `k *= -1` before scoring such a game.

This is placed after the odd-value condition, matching the stated rule order. Since both operations are the same sign flip, their algebraic effect would commute, but preserving the written order makes the simulation transparent.

**Two simultaneous conditions cancel**

If an odd value appears on a sixth game, both conditions apply:

$$
k\longrightarrow-k\longrightarrow k.
$$

The same player remains active relative to the start of that game's rule processing.

The game is still awarded normally after the two swaps. The source's two independent `if` statements are essential; using `if ... elif` would incorrectly perform only one swap.

**Trace the second example**

For `[2,4,2,1,2,1]`, the first three values are even and occur before a sixth-game index. The first player stays active and gains 8 total, so `ans = 8`.

At index 3, value 1 is odd. `k` changes from 1 to -1, and adding `-1` makes the difference 7.

Index 4 has value 2, no swap, and contributes -2, leaving 5.

Index 5 has odd value 1 and is also the sixth game. The odd rule changes `k` from -1 to 1; the sixth-game rule changes it back to -1. The second player receives the point, and `ans` becomes 4.

This matches first-player total 8 minus second-player total 4.

**Why the signed total always matches two separate scores**

Before each game, `k` identifies the active player. Each satisfied swap condition negates it, exactly exchanging player identities.

After all required swaps, `k * x` is positive precisely when the first player receives `x` and negative precisely when the second player receives it. Adding this signed contribution maintains:

$$
\texttt{ans}=S_1-S_2
$$

after every processed game.

The final value is therefore the requested difference, including negative results when player two leads.

**Each game has four possible swap combinations**

The two conditions form a small transition table:

- even value and not a sixth game: zero swaps, so `k` stays unchanged;
- odd value and not a sixth game: one swap, so `k` is negated;
- even value on a sixth game: one swap, so `k` is negated;
- odd value on a sixth game: two swaps, so `k` returns to its old value.

The source implements this table with two independent sign flips instead of writing four branches. Algebraically, the new sign is:

$$
k_{\text{new}}
=
k_{\text{old}}(-1)^{[\text{x odd}]+[\text{sixth game}]}.
$$

The points are added only after this transition, so `k` also becomes the persisted active state for the following game.

**Why the actual point magnitude does not affect switching beyond parity**

An odd score of 1 and an odd score of 999 both cause exactly one parity swap before positional rules. Their magnitudes matter only when the active player receives the signed contribution.

This separation lets the algorithm use `x % 2` for state and `k * x` for score without mixing the two roles.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The loop processes each game once with constant parity, index, sign, and addition operations. Total time is $O(N)$.

Only `ans`, `k`, `i`, and `x` are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Maintain two score variables:** Track the active player as a Boolean and add to `score1` or `score2`. This is equally correct but uses a final subtraction; the sign directly maintains the requested quantity.
- **Precompute all active players:** Store which player handles every game, then sum scores. This wastes $O(N)$ space for a state that can be updated online.
- **Use if/elif for swaps:** This is wrong when an odd value occurs on a sixth game because both swaps must happen.
- **First game odd:** Player two becomes active before scoring, so the contribution is negative.
- **Odd sixth game:** Two swaps cancel and the previous active player scores.
- **Even sixth game:** Only the positional swap occurs.
- **Several odd games:** Each independently toggles the persistent active state.
- **Negative final difference:** It is valid and returned directly, as in the single odd-value example.
- **One game:** Only its parity rule can apply because index 0 is not a sixth-game index.
- **Game numbering:** The positional rule uses `i % 6 == 5` because the description's sixth games are one-based while the loop index is zero-based.
