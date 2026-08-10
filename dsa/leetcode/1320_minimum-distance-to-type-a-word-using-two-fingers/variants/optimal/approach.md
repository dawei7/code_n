## General

Typing one letter tells us where the finger that pressed it ends, but the other finger may be at any keyboard letter. That second position affects future cost, so a greedy choice such as “always move the nearer finger” is not automatically safe. A move that is cheapest now can leave both fingers poorly placed for later letters.

The exact Optimal solution keeps both finger positions in a dynamic-programming state:

`f[i][l][r]` is the minimum total movement cost after typing `word[i]`, with one finger at letter index `l` and the other at letter index `r`.

The code labels the fingers by their two table coordinates, but the physical fingers are interchangeable. It keeps both orientations so every transition is direct.

**Mapping letters to keyboard coordinates**

Uppercase letters are numbered from zero through 25:

`ord(letter) - ord("A")`.

The keyboard has six columns. For letter index `a`, `divmod(a, 6)` returns row `a // 6` and column `a % 6`. For example, `A` has index zero and coordinate $(0,0)$, while `P` has index 15 and coordinate $(2,3)$.

`dist(a, b)` computes Manhattan distance:

$$
\left\lvert x_a-x_b\right\rvert+
\left\lvert y_a-y_b\right\rvert.
$$

Only finger movement costs distance. Pressing a letter once a finger is there costs nothing.

**Why at least one finger is at the latest letter**

Immediately after typing `word[i]`, whichever finger pressed that character must be located there. Therefore, every reachable state has either `l == word[i]` or `r == word[i]`.

This fact greatly restricts useful transitions even though the exact table allocates all $26 \times 26$ position pairs for every word index. States that violate the fact remain positive infinity.

**Free initial finger placement**

Before the first character, both finger positions are free. The solution represents this by initializing every state in which either finger is on the first letter:

`f[0][first][j] = 0` and `f[0][j][first] = 0` for every `j`.

This does not mean the other finger physically had to press some arbitrary key. It means we may choose its initial position anywhere at zero cost. The finger on `first` types the first character, also at zero cost.

Allowing all 26 possibilities is necessary. The best initial location of the unused finger may depend on a much later character, and the problem explicitly says starting positions are free.

**Continuing with the same finger**

For position `i > 0`, let `a` be the previous character and `b` the current one. Their direct movement cost is `d = dist(a, b)`.

Suppose the first finger typed `a` and the other finger is at `j`. Moving the first finger from `a` to `b` produces:

`f[i][b][j] = min(f[i][b][j], f[i - 1][a][j] + d)`.

The symmetric line handles the second finger:

`f[i][j][b] = min(f[i][j][b], f[i - 1][j][a] + d)`.

The stationary finger remains at `j`. These two updates cover every way of using the same finger for consecutive characters.

**Switching to the other finger**

The other possibility is that the finger which did not type `a` now types `b`. Immediately before this switch, one finger is at `a` and the other is at some position `k`. The `k` finger moves to `b`, while the former typing finger stays at `a`.

In the target state, the stationary position must therefore be `a`. That is why the expensive-looking inner loop runs only when `j == a`.

For every possible earlier position `k`, the source considers both finger orientations:

- from `f[i - 1][k][a]`, move the first finger from `k` to `b` and reach `f[i][b][a]`;
- from `f[i - 1][a][k]`, move the second finger from `k` to `b` and reach `f[i][a][b]`.

The added cost is `dist(k, b)`. Enumerating all `k` preserves the best location of the previously idle finger.

Together, “same finger” and “switch fingers” exhaust all possibilities for typing the next character. Exactly one of the two fingers must press it.

**Why the recurrence is correct**

The initialized states describe every legal free placement after the first letter. Assume the preceding layer stores the minimum cost for every reachable pair of finger positions.

Any legal next action either moves the finger currently at `a` or moves the other finger. The first two updates cover the former; the `k` loop covers the latter. Each transition adds exactly the Manhattan distance traveled and changes only the finger that presses `b`. Taking `min` retains the cheapest path to each resulting state.

Conversely, every transition represents a legal finger movement and types exactly the next required character. By induction, the final layer contains all and only valid typing histories with their minimum costs.

After the last character, one finger must be at `last`. The source takes the minimum across states where the first table coordinate equals `last` and states where the second equals `last`. The smaller value is the global minimum.

**Repeated letters**

If `a == b`, `dist(a, b)` is zero, so the same finger can type the repeated character without moving. Switching is also considered, but cannot create a negative cost. The minimum remains correct.

## Complexity detail

Let $n$ be the word length and let $\Sigma=26$ be the alphabet size.

The exact table contains $n\Sigma^2$ entries. Creating and filling it with infinity costs $O(n\Sigma^2)$ time and space. The initialization costs $O(\Sigma)$.

For each later character, the outer `j` loop has $\Sigma$ iterations. Constant transitions run every time, and the `k` loop of $\Sigma$ iterations runs only for the single value `j == a`. Transition work is therefore $O(n\Sigma)$, but table allocation still makes exact total initialization time $O(n\Sigma^2)$.

With the fixed English alphabet, both expressions simplify to $O(n)$ time and $O(n)$ space because $26^2$ is a constant. The manifest's $O(1)$ space does not describe this exact source: it retains a separate $26 \times 26$ layer for every one of the $n$ characters.

A rolling or symmetry-reduced DP can use only $O(\Sigma)$ or $O(\Sigma^2)$ storage, which becomes $O(1)$ with a fixed alphabet. That is a different implementation.

## Alternatives and edge cases

- **Symmetry-reduced state:** Track only the position of the non-typing finger because one finger must be on the latest character. This gives $O(n\Sigma)$ time and $O(\Sigma)$ rolling space.
- **Two rolling full layers:** If retaining labeled finger positions, only layers `i - 1` and `i` are needed. This removes the factor of $n$ from storage.
- **Greedy nearest finger:** It can make a locally cheap move that leaves bad positions for later letters, so it lacks the global optimality guarantee of DP.
- **Free initial positions:** Charging distance to the first letter or fixing both fingers at `A` would violate the contract.
- **Both fingers on one letter:** Such a state is legal and appears naturally in the initialization or transitions.
- **Consecutive equal letters:** Their same-finger movement cost is zero.
- **Last keyboard row:** `divmod(index, 6)` correctly maps `Y` and `Z` into the partial fifth row; nonexistent positions are never used.
- **Finger identity:** Swapping physical finger names does not change cost, but the exact table stores both orientations and takes the minimum over both at the end.
- **Positive infinity states:** Unreachable position pairs remain `inf` and cannot beat a finite transition.
- **Exact-space qualification:** The allocated three-dimensional table is linear in word length, not constant space.
