# Guided Example: Number of Distinct Binary Strings After Applying Operations

We may flip every character of any length-$k$ contiguous substring of a binary
string `s`, any number of times, in any order. The question asks how many
*distinct* strings are reachable, reported modulo $10^9 + 7$.

The worked instance is the official one:

- **Input:** `s = "1001"`, $k = 3$
- **Required outcome:** `4`

It is the right sized instance: $n = 4$ is large enough that its two windows
overlap, so the "flips are independent" claim is genuinely at risk, yet small
enough that the entire reachable set can be tabulated by hand and every claim
checked.

---

## 1. Two algebraic facts that shrink the search space

The operation is its own inverse. Flipping the same window twice restores every
character it covers, so applying a chosen window two, four, or any even number of
times is indistinguishable from never applying it. Only the **parity** of how
often each window is used can matter.

The operations also commute. Flipping a bit is addition modulo $2$, and addition
modulo $2$ does not care about order, so the final string depends only on the
*set* of windows that were used an odd number of times — not on the order or the
count of the flips that produced it. A whole (possibly astronomically long)
schedule therefore collapses into a single binary choice vector of length $w$,
where

$$
w = n - k + 1
$$

is the number of distinct length-$k$ substrings, indexed by starting position $0,
1, \dots, w-1$. With $n = 4$ and $k = 3$ this gives $w = 4 - 3 + 1 = 2$, so there
are only $2^2 = 4$ choice vectors to consider.

This collapse gives an immediate **upper bound** of $2^w$ reachable strings.
Reaching the *exact* count $2^w$ requires the other half of the argument: no two
different choice vectors may produce the same string. If some non-empty set of
windows cancelled itself out, the true count would be strictly smaller. Sections
2 and 3 settle that question.

For orientation, the two windows of the instance cover these positions:

| Window (start index) | Covered string positions | Characters it toggles in `1001` |
|---|---|---|
| `0` | $0, 1, 2$ | `1`, `0`, `0` |
| `1` | $1, 2, 3$ | `0`, `0`, `1` |

| Position $p$ | Windows covering $p$ | Position $p$ is toggled by |
|---|---|---|
| $0$ | only window `0` | window `0` alone |
| $1$ | windows `0` and `1` | either window |
| $2$ | windows `0` and `1` | either window |
| $3$ | only window `1` | window `1` alone |

The boundary rows are the crux: position $0$ is covered by exactly one window,
and position $n-1 = 3$ is covered by exactly one window. Those two "private"
positions are what make the windows independent rather than merely numerous.

---

## 2. Complete enumeration on the instance

Enumerating the four choice vectors for `s = "1001"`, $k = 3$ and applying each
selected flip to the original string:

| Choice vector $(c_0, c_1)$ | Windows applied | Resulting string |
|---|---|---|
| $(0, 0)$ | none | `1001` |
| $(1, 0)$ | window `0` | `0111` |
| $(0, 1)$ | window `1` | `1110` |
| $(1, 1)$ | both windows `0` and `1` | `0000` |

All four rows are different strings, so the reachable set
$\{\texttt{1001},\ \texttt{0111},\ \texttt{1110},\ \texttt{0000}\}$ has exactly
four elements and the required output is `4`. The enumeration also makes the next
section's proof visible: the first character of the result is the original first
character toggled exactly when $c_0 = 1$, and the last character is the original
last character toggled exactly when $c_1 = 1$, so the outer positions read the two
choices back independently.

A one-character case with $n = 1$ is a useful contrast, because then the single
window covers the whole string and nothing overlaps:

| Instance | $n$ | $k$ | $w = n-k+1$ | Distinct strings |
|---|---|---|---|---|
| `s = "1001"` | 4 | 3 | 2 | $2^{2} = 4$ |
| `s = "10110"` | 5 | 5 | 1 | $2^{1} = 2$ |
| `s = "0"` | 1 | 1 | 1 | $2^{1} = 2$ |
| `s = "101010"` | 6 | 1 | 6 | $2^{6} = 64$ |

---

## 3. Why the window flips are linearly independent

Suppose, for contradiction, that some non-empty set $S$ of window start indices
had *zero* combined effect: flipping all windows in $S$ would return the original
string unchanged. Even then a contradiction follows from the leftmost member of
$S$.

Let $p = \min S$ be the smallest start index in $S$. Position $p$ is covered by
window $p$ (its first character), so window $p$ toggles it. Which *other* windows
cover position $p$? A window starting at $t$ covers positions $t$ through
$t + k - 1$, so it reaches position $p$ only when $t \le p$. Since $p$ is the
smallest index in $S$, no selected window starts before $p$, and no window
starting after $p$ can reach backwards to $p$. Position $p$ is therefore toggled
by exactly one selected window — namely window $p$ — and hence ends up flipped,
not restored.

That contradicts the assumption that $S$ has zero combined effect. Writing the
window flip patterns as the rows of a matrix over $\mathrm{GF}(2)$, the argument
says each row has a leading $1$ in a column where every earlier row has a $0$;
such rows are linearly independent. So the $w$ windows span a subspace of
dimension $w$, and distinct choice vectors always produce distinct strings.

Combining the two directions gives the exact count:

$$
\text{distinct strings} = 2^{w} = 2^{\,n-k+1}.
$$

Two consequences are worth stating plainly. First, the count **does not depend on
the characters of `s` at all**: the map "choice vector $\mapsto$ final string" is
a bijection onto a coset of the span, and a coset has the same size as the
subspace no matter which string anchors it. Second, $w$ flips always suffice,
since each window is used at most once.

---

## 4. Worked trace of the counting pipeline

The method never enumerates strings; it evaluates the derived expression. Here is
the pipeline for `s = "1001"`, $k = 3$:

| Step | Quantity being computed | Expression | Value | Note |
|---|---|---|---|---|
| 1 | string length | $\lvert s \rvert$ | $4$ | number of characters |
| 2 | window count | $w = \lvert s \rvert - k + 1$ | $4 - 3 + 1 = 2$ | legal start indices $0, 1$ |
| 3 | candidate count | $2^{w}$ | $2^{2} = 4$ | exact, by the independence proof |
| 4 | reported answer | $2^{w} \bmod (10^{9}+7)$ | $4 \bmod (10^{9}+7) = 4$ | below the modulus, so unchanged |

The final reduction matters only for large $w$. Because
$n \le 10^{5}$ we have $w \le 10^{5}$, and $2^{100000}$ has about thirty thousand
decimal digits — far too large to materialise. The arithmetic must therefore be
performed as modular exponentiation: square the base and halve the exponent
repeatedly, reducing after every multiplication, which keeps every intermediate
value below $10^9 + 7$.

| Strategy for forming $2^{w} \bmod (10^9+7)$ | Work | Intermediate size | Verdict |
|---|---|---|---|
| Materialise $2^{w}$, then reduce | builds a $\Theta(w)$-bit integer first | $\Theta(w)$ bits | correct but wasteful; invisible at $w = 2$, fatal at $w = 10^{5}$ |
| Binary (square-and-multiply) modular exponentiation | $\Theta(\log w)$ modular multiplications | $< 10^9 + 7$, fits in one machine word | the sound approach |
| Enumerate all $2^{w}$ reachable strings and count them | exponential in $w$ | exponential | never attempted |

---

## 5. Boundary cases and traps

| Case | Instance shape | Distinct strings | Reasoning |
|---|---|---|---|
| $k = 1$ | `s = "101010"`, windows are single characters | $2^{6} = 64$ | the six windows cover disjoint positions, so every bit is freely flippable |
| $k = n$ | `s = "10110"`, one window covering everything | $2^{1} = 2$ | the only reachable strings are `10110` and its complement `01001` |
| $n = 1$, $k = 1$ | `s = "0"` | $2^{1} = 2$ | the single bit may be left alone or flipped |
| Maximum $k$ for maximum $n$ | $n = 10^{5}$, $k = 10^{5}$ | $2$ | exactly one window, so only the original and its complement |
| Maximum $w$ for maximum $n$ | $n = 10^{5}$, $k = 1$ | $2^{100000} \bmod (10^{9}+7)$ | exponential count, polynomial computation |
| Nearly whole string | $n = 10^{5}$, $k = 10^{5} - 1$ | $2^{2} = 4$ | two overlapping windows; overlap does *not* merge them |
| Any content | `s = "1110010110"`, $k = 7$ | $2^{4} = 16$ | the character mix is irrelevant; only $n$ and $k$ enter |

The trap the instance is built to expose is the belief that **overlapping
windows are dependent**. With $k = 3$ and $n = 4$ the two windows share positions
$1$ and $2$, so a learner may suspect the second flip is partly "already covered"
by the first. The enumeration in section 2 refutes this: $(1,0)$ and $(0,1)$
produce `0111` and `1110`, which differ, and $(1,1)$ produces `0000`, which
differs from both. Sharing positions reduces a window's *effect*, not its
*information*: the leftmost window still owns position $0$ exclusively, and that
private position distinguishes it.

Two smaller traps are worth naming. Applying a window an even number of times
changes nothing, so counting *operations* overcounts. And the answer counts
*strings*, not schedules: many flip sequences produce `0000`, but it is counted
once.

---

## 6. Correctness and complexity derivation

**Invariant.** The map from choice vectors to strings is injective. Equivalently,
the $w$ window flip patterns are linearly independent over
$\mathrm{GF}(2)$. This invariant is what converts the upper bound of $2^{w}$
candidate schedules into an exact count of $2^{w}$ distinct outputs, and it holds
for every binary string and every legal $k$, not just for the traced instance.

**Soundness.** Every string in the reachable set is produced by a legal
schedule: pick the choice vector, then perform one flip per selected window, in
any order. Because flips commute and are self-inverse, that schedule realises the
chosen parity vector.

**Completeness and exactness.** Any legal schedule reduces to a parity vector, so
no reachable string lies outside the $2^{w}$-element family; and the independence
argument shows the family has no collisions. Hence the reachable set has
cardinality exactly $2^{n-k+1}$, and reducing that integer modulo $10^{9}+7$
returns the requested value.

**Cost of the method.** Let $n = \lvert s \rvert$ and let the exponent be
$w = n - k + 1$. Reading the length of `s` and computing $w$ take $O(1)$
arithmetic operations. Evaluating $2^{w} \bmod (10^{9}+7)$ by binary exponentiation
executes $\Theta(\log w)$ modular multiplications, each acting on integers below
$10^{9}+7$, so the total running time is

$$
O(\log w) = O(\log n),
$$

which is at most about seventeen multiplications at the constraint ceiling
$n = 10^{5}$.

**Auxiliary space.** The method stores only a constant number of fixed-width
integers — the exponent, the running base, the accumulated result, and the
modulus — so auxiliary space is $O(1)$. Crucially, the derivation never builds
the reachable set, never stores a window mask, and never materialises $2^{w}$
before reducing; the exponential object is counted symbolically by the
independence theorem rather than constructed. The input string itself is only
measured, so its $O(n)$ storage is part of the input, not auxiliary space.
