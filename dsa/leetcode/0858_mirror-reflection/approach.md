## General

**Unfold reflections into a straight ray**

Tracking every mirror bounce inside one square is awkward. Instead, imagine reflecting the room itself across a wall whenever the laser would bounce.

In this unfolded tiling of square rooms, the laser travels in one straight line. A receptor is reached when the line arrives at a corner of one reflected square.

Each time the ray crosses one room width `p` horizontally, its unfolded vertical rise is `q`. After `m` room widths, its coordinates relative to the original scale are:

$$
(mp,mq).
$$

It reaches a corner when the vertical coordinate is also a multiple of `p`:

$$
mq=np
$$

for some integer `n`.

**Find the first common alignment**

Let `g=\gcd(p,q)`. Dividing by `g` gives coprime values:

$$
p'=\frac p g,\qquad q'=\frac q g.
$$

The smallest positive solution to:

$$
mq=np
$$

is:

$$
m=p',\qquad n=q'.
$$

So the first receptor depends only on whether `p'` and `q'` are odd or even.

The code calculates exactly these reduced parities:

`p = (p // g) % 2` and `q = (q // g) % 2`.

After these assignments, local `p` and `q` no longer store wall length and rise; each is only a parity bit.

**Interpret horizontal parity**

Each unfolded room-width crossing alternates between the original room's east and west walls when folded back:

- odd `m=p'` means the receptor is on the east wall;
- even `m` means it is on the west wall.

**Interpret vertical parity**

Each vertical room height also alternates top and bottom:

- odd `n=q'` means the receptor is at the top;
- even `n` means it is at the bottom.

Combining parities identifies the corner.

The alternation can be visualized directly. Crossing one vertical room boundary changes east to west in the folded original; crossing another changes west back to east. Hence only whether the count is odd matters. The same alternating fold occurs vertically between bottom and top. The exact number of copied rooms is irrelevant after the first common corner is found; horizontal and vertical parity retain all information needed to identify its physical receptor.

**Map parity pairs to receptor numbers**

The three possible reduced parity cases are:

- `p'` odd and `q'` odd: east-top corner, receptor 1;
- `p'` odd and `q'` even: east-bottom corner, receptor 0;
- `p'` even and `q'` odd: west-top corner, receptor 2.

Both reduced values cannot be even because dividing by their gcd made them coprime. Therefore, there is no fourth both-even case.

The exact code implements:

- if both parity bits are 1, return 1;
- otherwise, if reduced `p` is odd, return 0;
- otherwise, return 2.

**Trace `p=2,q=1`**

The gcd is one, so reduced values are `p'=2` and `q'=1`: even horizontal count and odd vertical count.

The unfolded ray reaches a corner after two room widths and one room height. Folding back places it on the west-top corner, receptor 2.

**Trace `p=3,q=1`**

Reduced values are 3 and 1, both odd. The first corner is east-top, receptor 1.

**Why gcd reduction finds the first receptor**

Any receptor hit requires positive integers `m,n` satisfying `mq=np`. With reduced coprime `p',q'`, the equation becomes:

$$
mq'=np'.
$$

Coprimality forces `p'` to divide `m` and `q'` to divide `n`. The smallest positive pair is therefore exactly `m=p',n=q'`. No earlier bounce can reach a corner.

The parity mapping then follows from alternating reflected-room orientation, so the returned receptor is the first one hit.

Notice that reducing before taking parity is essential. For example, unreduced counts may both be even merely because they describe reaching the same receptor after repeating the entire path. Dividing by the gcd removes that repeated cycle and exposes the parity of the earliest corner encounter.

## Complexity detail

Euclid's algorithm computes `gcd(p,q)` in:

$$
O(\log \min(p,q))
$$

time. All divisions, parity operations, and comparisons afterward take constant time.

Only a fixed number of integer variables is stored, so auxiliary space is `O(1)`.

The method performs no bounce-by-bounce simulation, so its running time does not grow with the number of reflections except through the logarithmic gcd calculation.

## Alternatives and edge cases

- **Simulate reflections geometrically:** It can work but needs repeated position/direction updates and potentially many bounces before a corner is reached.

- **Use least common multiple explicitly:** The first common height is `lcm(p,q)`. Dividing it by `p` and `q` yields the same parity counts, but gcd reduction avoids constructing more values.

- **`q=p`:** Gcd is `p`, reduced values are both one, and the ray reaches east-top receptor 1 immediately.

- **Reduced odd/odd:** Return receptor 1.

- **Reduced odd/even:** Return receptor 0.

- **Reduced even/odd:** Return receptor 2.

- **Reduced even/even:** Impossible because the reduced pair is coprime.

- **Smallest room `p=q=1`:** The ray goes directly to receptor 1.

- **Many common factors:** Gcd removal is essential; unreduced parities can both be even and would describe a later repeated corner rather than the first hit.

- **Integer arithmetic:** The solution uses exact gcd, division, and parity with no floating-point slope error.

- **Input mutation:** Integers are immutable; local parameter names are rebound to parity bits without affecting caller values.
