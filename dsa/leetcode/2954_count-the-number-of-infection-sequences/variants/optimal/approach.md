## General

**Decompose the healthy positions into gaps.** Initially sick people divide the
line into a left endpoint gap, zero or more internal gaps, and a right endpoint
gap. Within an endpoint gap, infection can advance only from the one sick-side
boundary, so its people have one forced relative order. An internal gap of
size $g$ is attacked from both ends. After choosing the final person reached,
the preceding $g-1$ infections independently choose whether the left or right
front advances, giving $2^{g-1}$ relative orders when $g>0$.

**Interleave the independent gap orders.** Let $H$ be the total number of
initially healthy people and let the gap sizes be $g_1,\ldots,g_m$. Once each
gap's internal order is fixed, the orders from different gaps may be
interleaved arbitrarily without violating adjacency. The number of
interleavings is the multinomial coefficient

$$
\frac{H!}{\prod_{i=1}^{m}g_i!}.
$$

Multiply this coefficient by $2^{g-1}$ for every nonempty internal gap. This
accounts for two independent choices: the legal order within each gap and the
placement of those ordered infections among steps belonging to other gaps.
Every infection sequence has a unique decomposition into these choices, so the
product counts each sequence exactly once.

**Compute under the modulus.** Precompute factorials and inverse factorials up
to $H$. Fermat's theorem supplies the inverse of $H!$, and a backward pass
derives all smaller inverse factorials. Apply every multinomial denominator and
internal-gap power modulo $10^9+7$.

## Complexity detail

Let $N$ be the number of people and $H=N-\lvert\texttt{sick}\rvert$.
Factorial preparation and the gap scan take $O(N)$ time. The two factorial
arrays contain $H+1$ values and use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Simulate every infection order:** Branching over every currently exposed healthy person is exact but grows exponentially.
- **Pascal combination table:** Combining gap orders with a full table remains correct but takes $O(H^2)$ time and space.
- **Endpoint gap:** It has only one spreading direction and contributes no power of two.
- **Internal gap of size one:** Its factor is $2^0=1$ because the only healthy person is already adjacent to both sides.
- **Consecutive sick positions:** Their gap size is zero and contributes a neutral factorial and no power factor.
- **One initially sick person:** Only the two endpoint gaps exist; their forced chains may still be interleaved.
- **Modulo arithmetic:** Division in the multinomial coefficient must use modular inverses, not integer division after reduction.
