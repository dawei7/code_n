## General

Each positive grid cell represents a vertical tower. The solution first counts the exposed surface of every tower as if it were isolated, then subtracts faces hidden where neighboring towers touch.

**Surface of one isolated tower.** A tower of height $v>0$ is a $1\times1\times v$ rectangular column. It has one exposed top face, one exposed bottom face, and four vertical sides of area $v$ each. Its isolated surface area is therefore

$$
2+4v.
$$

This formula already excludes faces between cubes stacked inside the same tower. Thinking of the tower as one column is simpler than beginning with $6v$ cube faces and subtracting its $v-1$ internal horizontal contacts.

An empty cell has no tower and contributes nothing. That is why the code performs the calculation only inside `if v:`.

**Subtract contact with a neighboring tower.** Suppose adjacent towers have heights $v$ and $w$. They touch along one vertical unit face at every height level occupied by both towers. The shared contact area is

$$
\min(v,w).
$$

That contact was counted twice in the isolated surfaces: once as a side of the first tower and once as a side of the second. Neither copy is exposed after gluing, so the total must subtract

$$
2\min(v,w).
$$

**Count every adjacency exactly once.** At cell $(i,j)$, the solution checks only the tower above it when `i > 0` and the tower to its left when `j > 0`. It does not also check below and right. Every horizontal grid adjacency has one endpoint that is lower or farther right, so it is encountered exactly once by these two backward checks.

If all four directions were checked at every cell, each tower pair would be processed twice and the shared area would be subtracted four times instead of twice.

**Why boundaries need no explicit added faces.** The isolated term `2 + 4v` already includes all four side faces. A side remains in the answer unless an actual neighboring tower causes the corresponding contact subtraction. At a grid boundary, there is no neighbor and therefore no subtraction, leaving that entire outer side exposed.

The bottom face also remains included. Gluing occurs between cubes, not between a cube and an omitted ground surface for this area definition, and the problem explicitly says bottoms count.
Every potential exterior unit face belongs to one of three categories:

1. A top or bottom face of a nonempty tower. The isolated formula counts it once, and no horizontal-neighbor subtraction touches it.
2. A vertical face with empty space or the grid exterior on the other side. The isolated formula counts it once, and no positive overlapping neighbor removes it.
3. A vertical face touching a cube in an adjacent tower. The two isolated tower formulas count the same contact twice, and the unique adjacency calculation subtracts both copies.

After all cells are processed, categories 1 and 2 remain counted once and category 3 remains counted zero times. That is exactly total exposed surface area.

For two adjacent towers of heights 3 and 1, their isolated areas are $14$ and $6$. They share one vertical unit face, so subtracting $2\cdot1$ gives 18. Only the lowest level touches; the two higher side units of the height-3 tower remain exposed.

The method works directly with tower heights and never expands individual cubes, so its work depends on grid size rather than total cube count.

## Complexity detail

Let $n$ be the square grid dimension. The nested loops visit all $n^2$ cells. Each positive cell performs a constant number of arithmetic operations and at most two neighbor comparisons.

- **Time complexity:** $O(n^2)$.
- **Space complexity:** $O(1)$ auxiliary space.

The input grid is read without modification. The answer itself is a scalar.

## Alternatives and edge cases

- **Count six faces per cube:** Subtract two faces for every adjacent cube pair, including vertical pairs. This is correct but can take time proportional to the total number of cubes rather than $n^2$.
- **Check all four neighboring cells:** It can work only if each shared contact is divided or carefully deduplicated. The top-and-left rule is simpler.
- **Use `abs(v - w)` for internal boundaries:** Height difference describes exposed side above the shorter tower, but a complete formula must also handle outer boundaries and other sides. Isolated area minus shared contacts is less error-prone.
- **Projection area:** Projection counts shadows, not exposed faces. It is a different problem and cannot replace surface-contact accounting.
- **All zeros:** No tower enters the positive branch, so area is zero.
- **One cube:** The formula gives $2+4=6$, including its bottom.
- **One tall tower:** Area is $2+4v$.
- **Equal adjacent towers:** Their entire common side of height $v$ is hidden, so $2v$ is subtracted.
- **Unequal adjacent towers:** Only the lower shared height is hidden; the taller excess remains exposed.
- **Hole surrounded by towers:** Each side facing the zero cell remains exposed because `min(v,0)=0` causes no subtraction.
- **Grid boundary:** Missing neighbors cause no subtraction, retaining outward faces.
- **Bottom surfaces:** They are always part of each positive tower's initial two horizontal faces, as required.
- **No double-counting:** Each horizontal adjacency is handled by its lower or right endpoint exactly once.
