# Guided Example: Minimum Operations to Reduce an Integer to 0

## 1. Each operation is a signed power of two

One operation adds $+2^e$ or $-2^e$ to the current value, for a freely chosen exponent $e \ge 0$. A sequence of $k$ operations therefore has the net effect

$$\sum_{j=1}^{k} \varepsilon_j\,2^{e_j}, \qquad \varepsilon_j \in \{+1,-1\},$$

and the order in which the operations are performed is irrelevant because addition and subtraction commute. Reaching $0$ from $n$ means exactly that $n$ is representable as such a signed sum:

$$n \;=\; \sum_{j=1}^{k} \varepsilon_j 2^{e_j}.$$

So the question "how few operations?" becomes "how few signed powers of two add up to $n$?" Intermediate values are unconstrained — they may overshoot, as the official instance for $39$ does when it first grows to $40$ — because only the total matters.

Let $w(n)$ denote that minimum. Two legal decompositions of $39$ illustrate the gap between a careless and a careful answer:

| Decomposition of 39 | Terms | Operations | Why it is of interest |
|---|---|---|---|
| $32 + 4 + 2 + 1$ | 4 | subtract 32, 4, 2, 1 | one operation per set bit, the obvious reading |
| $32 + 8 - 1$ | 3 | add 1, subtract 8, subtract 32 | one operation crossed a bit boundary and saved a term |

The second row is optimal, and the reason is structural rather than lucky: a block of consecutive set bits can be replaced by a difference of two powers.

## 2. Normalization: no exponent needs to appear twice

**Lemma (no repeated exponents).** In a decomposition with the minimum number of terms, every exponent occurs at most once.

*Proof.* Suppose $2^e$ appears twice. If the two signs are opposite, the two terms cancel and deleting them lowers the count, contradicting minimality. If the signs are equal, they combine into the single term $\varepsilon 2^{e+1}$, again lowering the count. So neither situation can occur in a minimum. $\square$

Two consequences matter for the rest of the argument. First, an optimal decomposition has at most one term of exponent $0$, namely $\pm 1$. Second, since a decomposition of an $L$-bit number can only use exponents below $L$ plus one more, $w(n)$ is bounded by the bit length plus one — the search space is tiny even though exponents are unbounded.

## 3. Halving: the parity recursion

**Even values halve for free.** If $n$ is even, no optimal decomposition contains a $\pm 1$ term: all other terms are multiples of $2$, so a $\pm 1$ term would make the sum odd. Every exponent is then at least $1$, and dividing the whole decomposition by $2$ shows $w(n) = w(n/2)$.

**Odd values spend exactly one operation.** If $n$ is odd, the sum is odd, so an odd number of exponents equal $0$ occur; the normalization lemma caps that at one, hence exactly one. Removing it and halving the rest gives

$$w(n) \;=\; 1 + \min\Bigl(w\!\left(\tfrac{n-1}{2}\right),\; w\!\left(\tfrac{n+1}{2}\right)\Bigr), \qquad n \text{ odd},$$

where the two candidates correspond to the unit term being $-1$ or $+1$.

Combining the two cases, the exact recurrence is

$$w(n) = \begin{cases} w(n/2), & n \text{ even},\\[2pt] 1 + \min\bigl(w((n-1)/2),\, w((n+1)/2)\bigr), & n \text{ odd},\end{cases} \qquad w(0) = 0 .$$

This is already an algorithm: repeatedly strip the parity of $n$. What remains is to decide the $\min$ without exploring both branches.

## 4. The even successor always wins

For odd $n$ the two candidates $(n-1)/2$ and $(n+1)/2$ are consecutive integers, one even and one odd. The even one is never worse.

**Dominance lemma.** For every $m \ge 1$, $\;w(2m) \le w(2m+1) - 1$ and $w(2m) \le w(2m-1) - 1$.

*Proof.* Take an optimal decomposition of $2m+1$. Its sum is odd, so by the parity argument it contains exactly one unit term, and the parity of an odd sum forces that term to be $+1$. Deleting it leaves a decomposition of $2m$ using one term fewer, so $w(2m) \le w(2m+1) - 1$. The same argument applies to $2m-1$. $\square$

Now apply the recurrence. If $n \equiv 1 \pmod 4$, the candidates are the even number $(n-1)/2 = 2j$ and the odd number $(n+1)/2 = 2j+1$ with $j \ge 1$, and the lemma gives $w(2j) < w(2j+1)$: the even candidate wins outright. If $n \equiv 3 \pmod 4$, the candidates are $(n-1)/2 = 2j+1$ and the even $(n+1)/2 = 2j+2$; here $w(2j+1) \ge 1 + w(j+1) - 1 = w(j+1) = w(2j+2)$, using $\lvert w(j) - w(j+1)\rvert \le 1$ (any decomposition of one of two consecutive integers extends to the other by appending $\pm 1$) together with the even-value halving rule. The even candidate is again at least as good.

The winning choice is therefore always the sign that makes the *successor* even:

- $n \equiv 1 \pmod 4$: subtract $2^0 = 1$, then halve.
- $n \equiv 3 \pmod 4$: add $2^0 = 1$, then halve.

In binary terms, this is the classic rule "round toward the even neighbour", and it is exactly what turns a run of low-order ones into a single carry into the next zero bit.

## 5. Tracing the official instance, $n = 39$

Since $39 = 100111_2$, the set bits are at positions $0, 1, 2$ and $5$. Applying the recursion bit by bit, least significant first:

| Step | Current $n$ | Parity | Term $\varepsilon\,2^{e}$ of the decomposition | New value $(n-\varepsilon)/2$ | Digit recorded at position $e$ |
|---|---|---|---|---|---|
| 1 | 39 | odd, $39 \equiv 3 \pmod 4$ | $-2^0$ | 20 | $-1$ at $2^0$ |
| 2 | 20 | even | none | 10 | 0 at $2^1$ |
| 3 | 10 | even | none | 5 | 0 at $2^2$ |
| 4 | 5 | odd, $5 \equiv 1 \pmod 4$ | $+2^0$ | 2 | $+1$ at $2^3$ |
| 5 | 2 | even | none | 1 | 0 at $2^4$ |
| 6 | 1 | odd, $1 \equiv 1 \pmod 4$ | $+2^0$ | 0 | $+1$ at $2^5$ |

Reading the recorded digits back with their positions gives $39 = -2^0 + 2^3 + 2^5 = 32 + 8 - 1$, three nonzero digits and therefore three operations. The operation applied at each odd step is the *negation* of the recorded term, since the term is a part of $n$ that has to be removed: the sequence is $+1$, then $-2^3 = -8$, then $-2^5 = -32$. The actual values therefore run $39 \to 40 \to 32 \to 0$ — add $1$, subtract $8$, subtract $32$ — which is precisely the published explanation of the sample and matches the authored answer $3$.

Note how step 1 replaced the entire block of three low ones $2^0+2^1+2^2 = 7$ by the difference $2^3 - 2^0$: one subtraction at the bottom of the block and one carry at the top. Step 4 then consumed that carry together with the isolated bit at position $5$, because $32 + 8 = 40$ needs exactly two subtractions.

## 6. The run-and-carry reading

The recursion has a purely combinatorial description. A maximal run of consecutive set bits occupying positions $[s, t]$ sums to

$$2^s + 2^{s+1} + \dots + 2^t \;=\; 2^{t+1} - 2^s,$$

so a run of length $L = t - s + 1 \ge 2$ can be replaced by the two-term difference $2^{t+1} - 2^s$: **two** operations instead of $L$, one at the bottom of the run and one at the bit just above it. A run of length $1$ is already a single power, so it costs **one** operation and produces no carry. The carry is why runs cannot be priced independently: it can land on a zero bit and fuse two blocks into one larger chain, as $27 = 11011_2$ shows, where the carry out of $[0,1]$ meets the block $[3,4]$ and the total stays at three operations rather than four.

| $n$ | Binary | Maximal runs of 1-bits | Optimal decomposition | Operations |
|---|---|---|---|---|
| 1 | `1` | `[0,0]` | $2^0$ | 1 |
| 3 | `11` | `[0,1]` | $2^2 - 2^0$ | 2 |
| 8 | `1000` | `[3,3]` | $2^3$ | 1 |
| 10 | `1010` | `[1,1]`, `[3,3]` | $2^3 + 2^1$ | 2 |
| 27 | `11011` | `[0,1]`, `[3,4]` | $2^5 - 2^2 - 2^0$ | 3 |
| 28 | `11100` | `[2,4]` | $2^5 - 2^2$ | 2 |
| 39 | `100111` | `[0,2]`, `[5,5]` | $2^5 + 2^3 - 2^0$ | 3 |
| 54 | `110110` | `[1,2]`, `[4,5]` | $2^6 - 2^3 - 2^1$ | 3 |
| 100000 | `11000011010100000` | `[5,5]`, `[7,7]`, `[9,10]`, `[15,16]` | $2^{17} - 2^{15} + 2^{11} - 2^9 + 2^7 + 2^5$ | 6 |

Row $28$ is the trap the case file flags: clearing set bits one at a time costs $16 + 8 + 4$, three operations, while recognizing the run $[2,4]$ as $2^5 - 2^2$ costs two. Row $100000$ shows the same mechanism at the maximum legal input, where the two long runs each collapse and the answer drops to six operations.

## 7. Why the reasoning is correct

- **Faithfulness.** Every operation is a signed power of two and vice versa, so the operation count equals the number of terms in a signed decomposition, and the recursion of Section 3 computes the minimum number of terms exactly.
- **Halving is exact, not a heuristic.** The even case is an equality, because the absence of a unit term is forced by parity and the normalization lemma.
- **The greedy sign is optimal.** The dominance lemma rules out the odd candidate in both residue classes, so choosing the sign that makes the successor even attains the minimum at every step of the recursion.
- **The run view is the same process.** A run $[s,t]$ becomes $-2^s$ plus a carry at $t+1$, which is the digit pair the recursion records at those two positions; a length-one run records a single digit. The carry state is precisely the recursion's pending odd value.
- **Termination and bounds.** Each step halves the value, so the recursion runs for at most $\lceil \log_2 n \rceil + 1$ steps, and $w(n)$ never exceeds the number of steps.

## 8. Traps this instance exposes

| Tempting reasoning | Where it breaks | Correct view |
|---|---|---|
| "Subtract one power per set bit of $n$." | $39$ would cost $4$ and $28$ would cost $3$. | A run of length $L \ge 2$ costs two operations, not $L$. |
| "Adding is never useful, only subtracting." | $39$ needs the addition of $1$ before subtracting $8$ and $32$. | Both signs are legal; the optimal choice is the one that makes the successor even. |
| "Process the largest bit first." | the recursion's decisions are forced by parity and depend on the low bits | the data flow runs least significant bit upward, carrying into higher positions |
| "Price each run independently and add up." | $27$ would be priced as $2+2=4$, but the answer is $3$. | a carry can fuse neighbouring blocks, so the carry state must be tracked between runs |
| "The intermediate value may not exceed $n$ or go negative." | the sample passes through $40 > 39$. | no monotonicity constraint exists; only the final value $0$ matters |
| "Greedy on the largest power below $n$ is optimal." | for $28$ the largest power $16$ leads to $12 \to 8 \to 4$, three operations | the correct greedy is on the low-order parity, not on the magnitude |

## 9. Time and auxiliary space

Let $L = \lceil \log_2(n+1) \rceil$ be the bit length of the input; for the constraint $n \le 10^{5}$ this is at most $17$.

- **Time** $O(L)$: each recursive step tests the parity and the value modulo $4$, performs one addition or subtraction, and halves. There are at most $L + 1$ steps, and no step examines more than the two low bits.
- **Auxiliary space** $O(1)$: only the current value, a running count of operations, and the carry state between adjacent bit positions are stored. The method never builds the binary string or a table indexed by value, so it does not allocate anything proportional to $n$.

Both bounds are logarithmic in the value and constant in the number of representable numbers, which is what makes the signed-decomposition view so much stronger than any search over operation sequences.