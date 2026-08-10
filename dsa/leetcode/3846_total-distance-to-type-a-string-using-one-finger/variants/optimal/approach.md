## General

**Precompute one coordinate for every letter**

The keyboard rows are stored as:

- `"qwertyuiop"` at row 0;
- `"asdfghjkl"` at row 1;
- `"zxcvbnm"` at row 2.

The nested module-level loops use `enumerate` to assign each character:

`pos[key] = (row_index, column_index)`.

The shorter second and third strings naturally omit the blank table cells. Every lowercase English letter appears exactly once, so `pos` ends with 26 unambiguous coordinates.

This precomputation keeps the typing loop simple and avoids searching the keyboard rows for every character.

**The finger position is completely determined**

Only one finger is used, and characters must be typed in string order. There is no choice about which key to visit next.

Before the first character, the finger is on `'a'`, so the source initializes:

`pre = 'a'`.

For each current character `cur`, `pos[pre]` is the starting coordinate and `pos[cur]` is the destination.

After paying the distance, `pre = cur` records that the finger remains on the newly typed key. This becomes the starting position for the next character.

**Compute one Manhattan distance**

If the previous key is at $(x_1,y_1)$ and the current key at $(x_2,y_2)$, the required movement is:

$$
\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert.
$$

The source calculates exactly this and adds it to `ans`.

Manhattan distance corresponds to moving vertically and horizontally through the grid. No diagonal shortcut is allowed.

The layout rows need not have equal numbers of real keys for this formula. Every actual letter still has the coordinate assigned by its table cell.

**Trace hello**

The initial key `a` is at $(1,0)$.

`h` is at $(1,5)$, so the first movement costs:

$$
\lvert1-1\rvert+\lvert0-5\rvert=5.
$$

The finger now starts from `h`. Moving to `e` at $(0,2)$ costs 4. Moving from `e` to `l` at $(1,8)$ costs 7.

The next character is also `l`. Both coordinates are identical, so that movement costs zero. Finally `l` to `o` at $(0,8)$ costs 1.

The source accumulates $5+4+7+0+1=17$.

**Why no pathfinding is necessary**

For two grid coordinates under Manhattan distance, every route using exactly the needed vertical and horizontal displacements has the same minimum length. Obstacles or unavailable blank cells are not part of the distance definition.

The problem supplies the distance formula directly, so breadth-first search over keyboard cells would add work without changing the result.

**Row offsets are exactly those shown in the table**

Real keyboards sometimes stagger letter rows horizontally. This problem does not introduce fractional offsets or diagonal geometry. The table places `q`, `a`, and `z` at column 0 of rows 0, 1, and 2.

Using the character's index inside its row string therefore gives the exact required column. For example, `h` is the sixth character of `"asdfghjkl"` and receives column 5, while `n` is the sixth character of `"zxcvbnm"` and also receives column 5.

The omitted cells after `l` and `m` are simply blank positions with no key. They do not shift any earlier coordinate.

**Typing has no optimization choice**

The word “total distance” can suggest finding a minimum route. With one finger and a fixed character order, every destination is forced. Manhattan distance already gives the required cost between consecutive destinations.

The algorithm is therefore a deterministic simulation, not dynamic programming: after typing a prefix, the only relevant state is its last character.

**Why the accumulated sum is exact**

Before each iteration, `pre` is the key holding the finger after typing the preceding character, or `a` before the first character. The calculated term is therefore exactly the movement required for the current character.

Updating `pre` preserves this invariant. Summing one exact movement for every character produces the total typing distance and neither skips nor double-counts a transition.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Building `pos` processes 26 fixed letters once at module load, which is $O(1)$ with respect to $N$.

The method visits each of the $N$ characters once and performs constant-time dictionary lookups and arithmetic. Total per-call time is $O(N)$.

`pos` has exactly 26 entries, and the method stores only `pre`, `cur`, coordinates, `dist`, and `ans`. Auxiliary space is $O(1)$ under the fixed alphabet.

## Alternatives and edge cases

- **Search row strings per character:** Find each letter's row and column on demand. It remains bounded by 26 but repeats avoidable work; the coordinate map is clearer.
- **Hard-code 26 coordinates:** This removes initialization loops but is more error-prone and harder to compare with the shown keyboard.
- **Breadth-first search:** It is unnecessary because the statement defines distance directly as Manhattan distance.
- **First character a:** The finger already starts there, so the first contribution is zero.
- **Repeated consecutive letter:** The two coordinates match and movement costs zero.
- **One-character string:** The answer is simply the distance from `a` to that key.
- **Letters on different rows:** Both vertical and horizontal differences contribute.
- **Blank table cells:** They are not included in the row strings and never appear in valid input.
- **Finger persistence:** Every transition starts from the previously typed character, not from `a` again.
- **All lowercase letters covered:** The coordinate dictionary contains every permitted input character.
