# Guided Example: Convert the Temperature

## 1. Two affine maps, not two formulas to memorize

The whole problem fits in one sentence: a single degree-Celsius reading must be
re-expressed in two other temperature scales. What makes it worth a lesson is
recognising that both targets are **affine functions** of the Celsius value, and
that each constant in the problem statement is doing a separate job.

Write a scale change in rectified form as $y = a \cdot c + b$, where $c$ is the
Celsius input, $a$ is the **unit ratio** between the two scales, and $b$ is the
**zero-point offset** that compensates for the two scales placing their zero in
different physical places.

$$
\text{Kelvin}(c) = 1 \cdot c + 273.15, \qquad
\text{Fahrenheit}(c) = 1.8 \cdot c + 32
$$

The Kelvin map has $a = 1$: a Kelvin degree and a Celsius degree are the same
size, so converting Celsius to Kelvin is pure translation. The Fahrenheit map
has $a = 1.8 = \tfrac{9}{5}$: a Fahrenheit degree is smaller, so a Celsius
interval stretches by that factor before the offset is applied.

| Target scale | Unit ratio $a$ | Zero-point offset $b$ | Rectified map | Effect on an interval of width $\Delta c$ |
|---|---|---|---|---|
| Kelvin | $1$ | $273.15$ | $\text{K} = c + 273.15$ | $\Delta \text{K} = \Delta c$ (width preserved) |
| Fahrenheit | $1.8$ | $32$ | $\text{F} = 1.8c + 32$ | $\Delta \text{F} = 1.8\,\Delta c$ (width stretched) |
| Celsius (identity) | $1$ | $0$ | $\text{C} = c$ | reference for both comparisons |

## 2. Reading the contract precisely

Three contract details decide whether an implementation is correct:

1. **Domain.** The input satisfies $0 \le c \le 1000$ and is *rounded to two
   decimal places*. The domain is therefore a finite grid of
   $\frac{1000 - 0}{0.01} + 1 = 100{,}001$ admissible values, with $0.01$ the
   smallest positive step. Nothing about the answer depends on which grid point
   is chosen, but the grid explains why a precomputed table is a real (if
   wasteful) alternative.
2. **Output shape.** The answer is the ordered pair $ans = [\text{kelvin},
   \text{fahrenheit}]$. Order is part of the answer: swapping the two entries is
   wrong even though both numbers are individually correct.
3. **Tolerance.** The returned pair must agree with the exact real-arithmetic
   answer within $10^{-5}$. This is generous by roughly seven orders of
   magnitude, which is why the standard double-precision evaluation is safe and
   no exotic precision strategy is needed.

Because $a > 0$ in both maps, both outputs are strictly increasing functions of
$c$. That monotonicity is the core invariant the answer relies on: a hotter
Celsius reading can never produce a lower Kelvin or Fahrenheit reading.

## 3. Worked trace on the official instance `celsius = 122.11`

Trace the second published example because it exercises a fractional input whose
Fahrenheit result carries three decimals — a useful test of where the decimal
digits come from.

$$
\text{Kelvin} = 122.11 + 273.15 = 395.26, \qquad
\text{Fahrenheit} = 1.8 \times 122.11 + 32 = 219.798 + 32 = 251.798
$$

| Step | Sub-expression | Exact decimal arithmetic | Register receiving the value |
|---|---|---|---|
| K1 | $c + 273.15$ | $122.11 + 273.15 = 395.26$ | kelvin entry of the pair |
| F1 | $1.8 \times c$ | $1.8 \times 122.11 = 219.798$ | unscaled product, not yet the answer |
| F2 | $219.798 + 32$ | $219.798 + 32 = 251.798$ | fahrenheit entry of the pair |
| R | assemble $[K, F]$ | $[395.26,\ 251.798]$ | returned pair |

The three-decimal tail appears in F1 and survives F2: multiplying by $1.8 =
\tfrac{9}{5}$ can turn a two-decimal input into a three-decimal product, while
adding the integer offset $32$ adds no new fractional digits. Kelvin, by
contrast, keeps exactly two decimals because adding $273.15$ cannot change the
number of decimal places of a two-decimal value.

## 4. Per-step state of the computation

There is no loop and no collection to grow; the entire mutable state is the
input register plus the two output slots. Making that state explicit is still
worth it, because it shows that each slot is written exactly once from the
untouched input — neither output is derived from the other.

| Step | Operation applied | `celsius` | kelvin slot | fahrenheit slot | Why the transition is valid |
|---|---|---|---|---|---|
| 0 | admit the input | `122.11` | empty | empty | $122.11$ is a two-decimal value inside $[0, 1000]$ |
| 1 | Kelvin slot $\leftarrow c + 273.15$ | `122.11` | `395.26` | empty | Kelvin uses Celsius-sized degrees, so only the $273.15$ zero shift applies |
| 2 | product $\leftarrow 1.8 \times c$ | `122.11` | `395.26` | intermediate `219.798` | the Celsius interval must be stretched by $1.8$ before any offset |
| 3 | Fahrenheit slot $\leftarrow$ product $+ 32$ | `122.11` | `395.26` | `251.798` | the offset moves the stretched value onto the Fahrenheit zero |
| 4 | emit $[\text{kelvin}, \text{fahrenheit}]$ | `122.11` | `395.26` | `251.798` | both slots are final and in the contract's order |

A subtle consequence of reading the input but never rewriting it: the two
conversions are independent, so their order of evaluation is irrelevant, and
neither conversion can contaminate the other's operands.

## 5. Boundary analysis over the admitted domain

The interesting boundaries are the ends of the domain and the single point where
the two output scales cross. Setting $\text{K} = \text{F}$ gives
$c + 273.15 = 1.8c + 32$, hence $c^{*} = \frac{241.15}{0.8} = 301.4375$. That
crossover value is *not* on the hundredth grid, so no admissible input produces
exactly equal Kelvin and Fahrenheit readings; the two neighbouring grid points
straddle it.

| `celsius` $c$ | Kelvin $c + 273.15$ | Fahrenheit $1.8c + 32$ | $\text{F} - \text{K}$ | What this row demonstrates |
|---|---|---|---|---|
| `0.00` | `273.15` | `32.00` | $-241.15$ | domain minimum; Fahrenheit reaches its smallest admissible value $32$ |
| `0.01` | `273.16` | `32.018` | $-241.142$ | smallest positive grid step still moves both outputs |
| `36.50` | `309.65` | `97.70` | $-211.95$ | first published example; both results end in two decimals |
| `100.00` | `373.15` | `212.00` | $-161.15$ | integer input; Fahrenheit stays an integer here by luck of the $0.01$ grid |
| `301.43` | `574.58` | `574.574` | $-0.006$ | last grid point below the crossover; Kelvin still leads |
| `301.44` | `574.59` | `574.592` | $+0.002$ | first grid point above the crossover; Fahrenheit overtakes |
| `1000.00` | `1273.15` | `1832.00` | $+558.85$ | domain maximum; largest magnitudes, so the worst rounding exposure |

Two further boundary facts follow from the affine structure:

- Since $\text{F} - \text{C} = 0.8c + 32 \ge 32 > 0$ on this domain, the
  Fahrenheit reading always exceeds the Celsius reading. The scales only meet at
  $c = -40$, which the constraint $c \ge 0$ excludes.
- Since $\text{K} - \text{C} = 273.15$ is constant, the Kelvin reading always
  exceeds the Celsius reading by the same amount; no input can make the gap
  smaller.

## 6. Why the reasoning is correct

**Invariant.** After step 1 the Kelvin slot holds $c + 273.15$ and after step 3
the Fahrenheit slot holds $1.8c + 32$, with $c$ still equal to the admitted
input. The invariant is established by reading the input once and is never
disturbed, because no later step writes the input register.

**Soundness.** Kelvin as a scale shares the Celsius degree size and differs only
by the zero point at absolute zero, which lies $273.15$ Celsius degrees below
the Celsius zero; adding that offset therefore relocates the reading without
rescaling it. Fahrenheit differs in *both* respects: its degree is $\tfrac{5}{9}$
of a Celsius degree, so the reading must be multiplied by the reciprocal
$1.8$, and its zero lies $32$ Fahrenheit degrees below the Celsius zero, so
$32$ is added after the scaling. Applying the offset before the scaling would
be wrong precisely because the offset is expressed in the target scale.

**Completeness.** The requested output is exactly the ordered pair of these two
values, and the method computes both; there is no candidate set to search and
nothing is skipped. Monotonicity ($a = 1 > 0$ and $a = 1.8 > 0$) guarantees the
two outputs agree in direction with the input, so no admissible input is mapped
to a contradictory pair.

**Tolerance margin.** Each literal ($1.8$, $273.15$, $32$) has relative
representation error at most $2^{-53} \approx 1.11 \times 10^{-16}$, and the
evaluated expressions introduce a few more rounding steps. At the worst
magnitude on this domain, ulp$(1832) = 2^{-52} \cdot 2^{10} \approx
2.27 \times 10^{-13}$, so the accumulated absolute error is on the order of
$10^{-12}$ — about seven orders of magnitude inside the allowed $10^{-5}$.

## 7. Alternative formulations and what they cost

| Formulation of the Fahrenheit entry | Value at $c = 122.11$ | Behaviour over the whole grid | Verdict |
|---|---|---|---|
| $1.8c + 32$ (single multiply, then add) | `251.798` | one multiply and one add; error within a few ulps | direct and adequate |
| $(9c)/5 + 32$ | `251.798` | replaces the inexact literal $1.8$ with the exact integer $9$, at the price of a division | marginally tighter, no practical gain |
| $(c + 40) \cdot 1.8 - 40$ | `251.798` | uses the $-40$ fixed point of the two scales; adds a subtraction that reintroduces rounding | elegant but not more accurate here |
| derive Fahrenheit from Kelvin, $1.8\,\text{K} - 459.67$ | `251.798` | makes one output depend on the other and uses the larger literal $459.67$ | needless coupling; rejected |
| precomputed lookup on the $100{,}001$-point grid | `251.798` | replaces arithmetic with memory: one entry per admissible input | correct but stores $10^5$ entries to avoid four operations |

The four arithmetic variants agree to the last printed decimal at every grid
point, which is the practical evidence that the tolerance makes their
differences unobservable. The lookup alternative is the informative contrast: it
does not buy accuracy, and it converts a constant-space computation into one
that stores an entry for each of the $100{,}001$ possible inputs.

## 8. Verification against the authored cases

Recomputing every authored case from the two affine maps confirms the lesson's
arithmetic independently of the implementation.

| Case | `celsius` | Kelvin, computed | Fahrenheit, computed | Matches authored expectation |
|---|---|---|---|---|
| `sample-1` | `36.5` | `309.65` | `97.7` | yes |
| `sample-2` | `122.11` | `395.26` | `251.798` | yes |
| `trial-zero` | `0.0` | `273.15` | `32.0` | yes |
| `trial-boiling-water` | `100.0` | `373.15` | `212.0` | yes |
| `trial-smallest-hundredth` | `0.01` | `273.16` | `32.018` | yes |
| `trial-upper-bound` | `1000.0` | `1273.15` | `1832.0` | yes |
| `trial-two-decimal-value` | `17.23` | `290.38` | `63.014` | yes |

## 9. Derived time and auxiliary-space complexity

Let $c$ denote the Celsius input. The work performed is a fixed collection of
scalar operations — one addition for Kelvin, one multiplication and one addition
for Fahrenheit — regardless of how large $c$ is or where it sits on the grid:

$$
T(c) = \Theta(1), \qquad S_{\text{aux}}(c) = \Theta(1)
$$

**Time.** No step inspects the magnitude of $c$ or iterates over the grid; the
operation count is bounded by a constant independent of the input, so the
running time is $\Theta(1)$.

**Auxiliary space.** The method allocates exactly one two-element result
container and holds no intermediate growth structure. The two-element output is
mandated by the contract and does not scale with $c$, so auxiliary space beyond
the returned pair is $\Theta(1)$. The three scalar constants of the problem
($273.15$, $1.8$, $32$) are fixed parts of the specification, not storage that
depends on the input.
