## General

**Count all movement assignments first**

Each of the `n` monkeys independently chooses one of two neighboring directions:

- clockwise;
- anticlockwise.

Therefore, there are:

$$
2^n
$$

total simultaneous movement assignments.

It is easier to subtract the collision-free assignments than to count every possible collision pattern directly.

**Two uniform assignments have no collision**

If every monkey moves clockwise, each leaves its vertex and arrives at the next clockwise vertex. This is a cyclic rotation:

- every destination receives exactly one monkey;
- all monkeys traverse different polygon edges in the same orientation.

No vertices or edge interiors contain two monkeys.

The all-anticlockwise assignment is symmetric and also collision-free.

These give at least two non-collision assignments.

**Why every mixed-direction assignment collides**

Write each monkey's direction around the cyclic vertex order. If both directions occur, the cyclic sequence has a boundary where direction changes.

Among the cyclic boundaries, one has adjacent monkeys moving toward each other along their shared edge: one moves clockwise from one endpoint while the other moves anticlockwise from the other endpoint.

They traverse that same edge in opposite directions and intersect, which the statement defines as a collision.

Equivalently, another kind of direction boundary can send two monkeys toward a common neighboring vertex. In either view, a nonuniform direction pattern cannot be collision-free on the cycle.

Thus the only collision-free assignments are the two uniform rotations.

**Make the cyclic-boundary argument precise**

Encode clockwise as $+$ and anticlockwise as $-$. In a cyclic sequence containing both symbols, there must be at least one transition from $+$ to $-$ while moving clockwise around the labels. Otherwise, after the first $+$ appeared, the sequence could never reach a $-$ before returning to its start.

At adjacent vertices `i` and `i+1`, pattern $+,-$ means monkey `i` moves clockwise toward `i+1` while monkey `i+1` moves anticlockwise toward `i`. They traverse the same edge in opposite directions at the same time and intersect.

This proves one collision exists without needing to analyze the rest of the polygon. A mixed assignment may contain several such transitions, but it is still one counted movement assignment.

**Subtract the complement**

The number with at least one collision is:

$$
2^n-2.
$$

The method computes this modulo $10^9+7$:

`(pow(2,n,mod)-2)%mod`.

The final modulo normalizes a possibly negative intermediate in general, though `n>=3` makes the ordinary value positive.

**Trace the triangle**

For `n=3`, total assignments are $2^3=8$.

Exactly two are uniform and collision-free. The other six mix directions and create at least one edge or vertex collision. The result is $8-2=6$.

**Collisions are counted by assignments, not events**

One movement assignment may create several collisions. It still counts once because the question asks for the number of ways in which at least one collision occurs.

Complement counting naturally avoids overcounting an assignment based on how many collision sites it contains.

**Why the two safe assignments are distinct**

For `n>=3`, all-clockwise and all-anticlockwise choose opposite directions for every monkey, so they are different assignments. Both remain valid even though each destination vertex is occupied again: it is occupied by exactly one arriving monkey, not two.

The original monkey leaving that vertex does not count as residing there after movement.

**Why simultaneity matters**

All monkeys move at the same time. Opposite traversal of one edge causes an intersection even though the monkeys exchange endpoint vertices rather than finish together.

If movements were sequential, this edge-crossing argument would differ. The proof follows the simultaneous rule.

**Fast modular exponentiation**

`n` can be as large as $10^9$, so multiplying two `n` times is too slow.

Python's three-argument `pow(2,n,mod)` uses exponentiation by squaring, repeatedly squaring the base and using the binary representation of `n`. It returns the residue without constructing the enormous integer $2^n$.


Every assignment belongs to exactly one of two categories. Uniform directions yield two collision-free rotations. Any nonuniform cyclic direction sequence contains a conflicting adjacent boundary and hence a collision.

Subtracting those exactly two safe assignments from all $2^n$ assignments gives exactly the requested count, and modular exponentiation returns its required residue.

## Complexity detail

Binary modular exponentiation takes $O(\log n)$ modular multiplication steps. The subtraction and final modulo are constant time.

Only a fixed number of integers is stored, so auxiliary space is $O(1)$ in the iterative exponentiation implementation underlying `pow`.

## Alternatives and edge cases

- **Enumerate assignments:** It costs $O(2^n)$ and is impossible for large `n`.
- **Count collision patterns directly:** Assignments with multiple collisions make inclusion-exclusion unnecessarily difficult.
- **All clockwise:** Collision-free cyclic rotation.
- **All anticlockwise:** Collision-free cyclic rotation.
- **Mixed directions:** A cyclic transition forces a collision.
- **Edge intersection:** It counts even when final vertices differ.
- **Multiple collisions:** The movement assignment is counted only once.
- **`n=3`:** Six of eight assignments collide.
- **Large exponent:** Use modular exponentiation rather than building $2^n$.
- **Modulo subtraction:** Final `%mod` returns the canonical residue.
