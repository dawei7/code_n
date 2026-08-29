## General

**For a fixed first color, there are no choices.** Row $1$ needs one ball, row $2$ needs two, and in general row $i$ needs exactly $i$ balls. Every row is monochromatic, and neighboring rows have different colors. Once the color of row $1$ is chosen, all later row colors are forced to alternate.

There are exactly two possible color patterns:

- red, blue, red, blue, and so on;
- blue, red, blue, red, and so on.

The source tries both patterns with `for k in range(2)`. It stores the available counts as `c = [red, blue]`. When `k=0`, `j=0` makes row one red; when `k=1`, `j=1` makes row one blue.

**Build consecutive rows until the required color is exhausted.** Variable `i` is the size and number of the next row, beginning at one. Variable `j` identifies its forced color. The condition `while i <= c[j]` asks whether that color has at least `i` balls remaining.

If so, the row can be built. The code subtracts `i` from that color's supply, toggles `j` with `j ^= 1` so the next row uses the other color, records height `i` in `ans`, and increments `i`.

If the required color has fewer than `i` balls, construction for that starting pattern stops. Balls of the other color cannot substitute, because adjacent rows must alternate and each row must contain one color only. Skipping row `i` to build a later row is also impossible: triangle height $h$ requires every row from $1$ through $h$.

The fresh assignment `c = [red, blue]` inside each outer iteration is important. The first simulated pattern consumes its local counts, but the second pattern must start again with the original supplies. Since integers in the new list are independent values, no restoration is needed.

**Why the first failure gives the maximum for one pattern.** For a chosen starting color, the color and size of every row are predetermined. If the simulation successfully builds rows $1$ through $h$, it has explicitly constructed a legal triangle of height $h$. If it cannot build row $h+1$, any triangle of that same starting pattern and greater height would also require row $h+1$ with exactly the same color and number of balls. The available count is insufficient, so no taller triangle exists for that pattern. The simulated height is therefore optimal for that start.

Trying both possible starts covers every legal triangle. `ans = max(ans, i)` after each successful row retains the greatest height reached by either simulation, so the final answer is the global maximum.

**Resource totals explain the simulation.** Suppose a triangle has height $h$. Let

$$
p=\left\lceil\frac h2\right\rceil,\qquad
q=\left\lfloor\frac h2\right\rfloor.
$$

The starting color occupies odd-numbered rows $1,3,\ldots,2p-1$. Their total number of balls is

$$
1+3+\cdots+(2p-1)=p^2.
$$

The other color occupies even-numbered rows $2,4,\ldots,2q$. Their total is

$$
2+4+\cdots+2q=q(q+1).
$$

For red-first, feasibility means $red\ge p^2$ and $blue\ge q(q+1)$. For blue-first, the two resource requirements swap. The loop checks these inequalities incrementally by subtracting one row at a time.

**Trace `red=2, blue=4`.** With red first, row $1$ consumes one red, row $2$ consumes two blue, but row $3$ needs three red and only one remains. This pattern reaches height two. With blue first, row $1$ consumes one blue, row $2$ consumes two red, and row $3$ consumes the remaining three blue. Row $4$ would need four red but none remains. This pattern reaches height three, so the answer is three.

For `red=10, blue=1`, red-first builds row one red but cannot build row two with only one blue. Blue-first builds row one blue and row two red, then cannot build row three blue. The maximum is two. Extra red balls cannot overcome the missing required blue row.

**Unused balls are allowed.** The goal is maximum height, not consumption of every ball. When a pattern stops, there may be many balls of the other color left. They cannot help with the immediately required color, so leaving them unused is unavoidable and correct.

## Complexity detail

Let $S=red+blue$. Building height $h$ consumes

$$
1+2+\cdots+h=\frac{h(h+1)}2
$$

balls, so $h=O(\sqrt S)$. The source simulates at most that many successful rows plus one failed check for each of the two starting colors. Its parameterized time complexity is therefore $O(\sqrt{red+blue})$, and its auxiliary space is $O(1)$.

The manifest claims $O(1)$ time and says the source uses closed forms for odd- and even-row sums. No closed-form computation appears in `solution.py`; it contains a `while` loop and row-by-row subtraction. Because the stated constraints permanently cap both inputs at $100$, the loop executes only a fixed bounded number of times, so one may call it $O(1)$ under a strict bounded-domain convention. As an algorithm over variable ball counts, however, $O(\sqrt{red+blue})$ accurately describes its growth.

Only a two-element list and a few integers are allocated for each of two iterations, so space is genuinely $O(1)$.

## Alternatives and edge cases

- **Closed-form feasibility test:** Use $p^2$ and $q(q+1)$ to test a proposed height for both starting colors. This matches the mathematical resource formulas but still needs a way to find the largest feasible $h$.
- **Binary search on height:** Feasibility is monotone: if height $h$ is possible for a fixed start, every smaller height is possible. Binary search with the closed-form tests runs in $O(\log(red+blue))$ time and $O(1)$ space, which is not better than a direct inverse formula but avoids row simulation.
- **Direct inverse-square formulas:** Candidate bounds can be derived with integer square roots for odd- and even-row totals, yielding true $O(1)$ arithmetic under fixed-width integers. Care is needed with floors and with reconciling the two colors.
- **Try only the more numerous color first:** This is unsafe. Row sizes differ by parity, and the scarcer color may be better suited to the smaller odd or even total for the eventual height. Both starts must be evaluated.
- **Use leftover balls to recolor a row:** Not allowed. A row's color is fixed by alternation, and balls of the other color cannot substitute.
- **Skip an unaffordable row:** Not allowed. Height counts consecutive rows starting at one; row $i+1$ cannot exist without row $i$.
- **Equal color counts:** Both starting patterns are symmetric and reach the same height, though the source still tests each.
- **One color nearly absent:** At least row one can be built because both inputs are at least one. A second row requires two balls of the opposite color.
- **Surplus of one color:** The result may be limited entirely by the other color. Unused surplus does not increase height.
- **Answer update timing:** `ans` is updated only after successfully paying for row `i`. The failed row is never counted.
- **Fresh counts per start:** Reusing the mutated `c` from the first simulation would undercount the second. Creating a new list inside the loop prevents that error.
- **Integer arithmetic:** Every subtraction and comparison is exact. No floating-point square-root rounding enters the simulated source.
- **Manifest mismatch:** The exact implementation is iterative simulation, not a closed-form solution. Its $O(1)$ time claim is defensible only because the input values are capped at $100$, not as a parameterized asymptotic bound.
