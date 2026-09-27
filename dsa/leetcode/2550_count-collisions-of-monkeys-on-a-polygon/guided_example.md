# Guided Example: Count Collisions of Monkeys on a Polygon

## 1. The instance, and why counting collisions directly is the wrong direction

Take the first official sample: a polygon with `n = 3` vertices, one monkey on each vertex, and a required output of `6`. Every monkey moves simultaneously to one of the two neighbouring vertices. A collision occurs when two monkeys end on the same vertex **or** when two monkeys intersect while travelling along an edge. We must count the direction assignments that produce at least one collision, modulo $10^9 + 7$.

The instance is small enough to enumerate by hand, and doing so exposes the structure of the whole problem. Each monkey has exactly two choices, so there are $2^3 = 8$ assignments, and each can be inspected individually. The pedagogical point of this lesson is that the eight cases split $2$ to $6$, and that the split is not an accident of the triangle: for every $n$ there are exactly **two** collision-free assignments.

## 2. An assignment is a binary string

Label the vertices $0, 1, \dots, n-1$ clockwise. Monkey $i$ occupies vertex $i$ and chooses between two moves:

- **clockwise**, written `C`, sending monkey $i$ from vertex $i$ to vertex $i + 1$ modulo $n$;
- **anticlockwise**, written `A`, sending monkey $i$ from vertex $i$ to vertex $i - 1$ modulo $n$.

Because the monkeys sit on distinct vertices and choose independently, the direction assignments are in bijection with the $2^n$ binary strings of length $n$ indexed by vertex. That bijection is the *input space*. The *output space* is the number of those strings containing a collision, which the statement asks for modulo $10^9 + 7$ because $n$ can reach $10^9$.

| Assignment | Landing vertices | Witness of collision | Collides |
|---|---|---|---|
| `C C C` | 1, 2, 0 | rotation by one step; every vertex receives exactly one monkey | no |
| `A A A` | 2, 0, 1 | the other rotation; again every vertex receives exactly one monkey | no |
| `C C A` | 1, 2, 1 | monkeys 0 and 2 both land on vertex 1 | yes |
| `C A C` | 1, 0, 0 | monkeys 1 and 2 share vertex 0, and monkeys 0 and 1 cross edge $(0,1)$ | yes |
| `C A A` | 1, 0, 1 | monkeys 0 and 2 both land on vertex 1 | yes |
| `A C C` | 2, 2, 0 | monkeys 0 and 1 both land on vertex 2 | yes |
| `A C A` | 2, 2, 1 | monkeys 0 and 1 both land on vertex 2 | yes |
| `A A C` | 2, 0, 0 | monkeys 1 and 2 both land on vertex 0 | yes |

Six of the eight assignments collide, and the two that do not are exactly the two uniform strings `C C C` and `A A A`. Note that the witness can be a shared vertex, as in most rows, or a crossing, as in the fourth row, where the landing vertices are all distinct yet the monkeys still meet. A count based only on shared landing vertices would be wrong, and the next section explains why the crossing case cannot be ignored.

## 3. Why every mixed assignment collides

Write the assignment as a cyclic sequence of $n$ labels, each `C` or `A`. Call it **uniform** when all $n$ labels agree, and **mixed** otherwise. The correctness argument has two halves.

- **Uniform assignments are safe.** If every monkey moves clockwise, the whole configuration rotates by one vertex: monkey $i$ goes to $i+1$, so the landing vertices are $0 \mapsto 1, 1 \mapsto 2, \dots, n-1 \mapsto 0$, a permutation of the vertices with exactly one monkey per vertex. Distinct landing vertices rule out a shared-vertex collision, and the travelled edges are the $n$ distinct polygon edges, each used once, so no two paths intersect. The all-anticlockwise assignment is the same rotation in the opposite direction. That is $2$ collision-free assignments.
- **Mixed assignments always collide.** Since both labels occur in the cyclic sequence, there is an adjacent pair with `C` at vertex $i$ and `A` at vertex $i+1$: start at any position labelled `C` and walk clockwise; because some position is labelled `A`, the walk reaches an `A`, and the position immediately before that first `A` is labelled `C`. For that pair, monkey $i$ travels from vertex $i$ to vertex $i+1$ while monkey $i+1$ travels from vertex $i+1$ to vertex $i$. Both paths use the same polygon edge in opposite directions and therefore intersect in its interior.

```text
vertex i  ------ edge (i, i+1) ------  vertex i+1
 monkey i   ---------------------->    (moves clockwise)
 monkey i+1 <----------------------    (moves anticlockwise)
            the two paths meet inside the shared edge
```

The mixed case is where the simultaneity trap lives. An assignment can place every monkey on a distinct vertex and still collide, precisely because two monkeys may swap vertices across the edge joining them. In the `n = 3` row `C A C` the landing vertices are $1, 0, 0$ and a shared vertex already witnesses the collision; for a cleaner example, take `n = 4` with `C A C A`, whose landing vertices $1, 0, 3, 2$ are all distinct, yet monkeys 0 and 1 traverse edge $(0,1)$ in opposite directions and intersect there.

## 4. The count, and what it looks like at the boundaries

Since exactly two of the $2^n$ assignments are collision-free, the number that produce at least one collision is

$$
2^n - 2 .
$$

For the traced instance $2^3 - 2 = 6$, matching the required output; the second official sample gives $2^4 - 2 = 14$. The formula never needs the geometry of a specific $n$; it only needs the two structural facts established above.

| $n$ | $2^n$ | $2^n - 2$ | Reported value | Source |
|---|---|---|---|---|
| 3 | 8 | 6 | `6` | first official sample |
| 4 | 16 | 14 | `14` | second official sample |
| 5 | 32 | 30 | `30` | trial case |
| 10 | 1024 | 1022 | `1022` | trial case |
| 100 | $2^{100} = 1267650600228229401496703205376$ | reduced below | `976371283` | trial case |
| 1000 | far beyond machine integers | reduced below | `688423208` | trial case |
| 1 | 2 | 0 | `0` | trial case, outside the stated domain |

The $n = 1$ row is worth naming explicitly. The statement constrains $3 \le n \le 10^9$, so a one-vertex "polygon" is degenerate and the geometric argument above does not apply to it; the closed form nevertheless evaluates to $2^1 - 2 = 0$, which is the value the package's trial case records. It is a consistency check on the arithmetic, not evidence that the geometry extends to $n = 1$.

## 5. Evaluating $2^n - 2$ modulo $10^9 + 7$

With $n$ up to $10^9$, the power $2^n$ has about $3 \times 10^8$ decimal digits: it cannot be formed and then reduced. The answer is computed by **binary exponentiation**, which reads the exponent in binary and maintains a running power with one squaring per bit and one extra multiplication by the base for each bit equal to $1$. The trace below evaluates $2^{10}$; the exponent $10$ is `1010` in binary, so four bits drive four steps.

| Bit of `1010` | Operation on the running power $r$ | New $r$ | Power of two represented |
|---|---|---|---|
| 1 | $r = 1^2 \cdot 2$ | 2 | $2^1$ |
| 0 | $r = 2^2$ | 4 | $2^2$ |
| 1 | $r = 4^2 \cdot 2 = 16 \cdot 2$ | 32 | $2^5$ |
| 0 | $r = 32^2$ | 1024 | $2^{10}$ |

The running value after the last bit is $1024$, so the answer is $1024 - 2 = 1022$, matching the trial case for $n = 10$. Two details of the modular form matter. First, every squaring and every multiplication must be reduced modulo $10^9 + 7$ immediately, because intermediate values such as $r^2$ grow past $10^{18}$ for large $n$. Second, the subtraction of $2$ can in principle produce a negative residue, so the result is taken modulo $10^9 + 7$ once more; for $n \ge 3$ the residue is at least $4$ and the guard is inert, but it keeps the expression total. For $n = 100$, the residue of $2^{100}$ modulo $10^9 + 7$ is $976371285$, and subtracting $2$ gives the reported `976371283`; for $n = 1000$, the residue is such that the reported value is `688423208`. Neither number is guessable from the small cases, which is the point of asking for the reduced form.

## 6. Traps this instance exposes

| Situation | Naive expectation | Actual behaviour | Where it bites |
|---|---|---|---|
| Direct counting | enumerate assignments and test them | $2^n$ assignments exist for $n$ up to $10^9$ | only the complement count is tractable |
| Shared vertices | a collision means two monkeys on one vertex | intersecting paths along an edge also collide | `C A C A` for `n = 4` has distinct landings and still collides |
| Safe assignments | many mixed patterns look safe | exactly the two uniform assignments are safe | the count is $2^n - 2$, never $2^n - m$ for larger $m$ |
| The cyclic boundary | the `C`-then-`A` pair might not exist | a mixed cyclic sequence always contains one | skipping this step leaves the "always collides" claim unproved |
| Uniform assignments | $n$ rotations should be safe | there are only two uniform strings, not $n$ | a rotation by $k$ steps is not a legal single move |
| Modular arithmetic | take the modulus at the end | reduce after every squaring and multiplication | unreduced intermediate powers are astronomically large |
| Negative residues | $2^n - 2$ is always positive | it is $0$ at $n = 1$, outside the stated domain | an unsigned type would wrap; the trial case expects `0` |
| Degenerate polygons | the geometry extends to every $n$ | $n = 1$ and $n = 2$ are degenerate; the domain starts at $3$ | reasoning about "two neighbours" fails when neighbours coincide |

The most damaging of these is the second: a solver who equates "collision" with "shared vertex" will over-count the safe assignments, and the mistake is invisible on the triangle, where every mixed assignment also shares a vertex. Stating the crossing rule separately from the shared-vertex rule is what makes the uniform-only classification airtight.

## 7. Time and auxiliary space

The running time is $O(\log n)$ modular multiplications, one squaring and at most one extra multiplication per bit of the exponent, so the count of operations is at most $2 \lceil \log_2 n \rceil$ — about $60$ multiplications at the maximum $n = 10^9$. The subtraction and final reduction are constant work. Auxiliary space is $O(1)$: the running power, the base, the modulus, and the exponent are each a single machine-sized integer, and no enumeration of assignments or landing-vertex table is ever materialized.

For contrast, judging assignments one by one would need $\Theta(2^n)$ time and at least $O(n)$ space per assignment, and even a clever sweep over the $n$ cyclic boundaries would still be $\Theta(n)$ time — infeasible at $n = 10^9$. The complement argument removes the geometry entirely and leaves only the two uniform strings to exclude, which is why a problem that looks like simulation reduces to one modular power.