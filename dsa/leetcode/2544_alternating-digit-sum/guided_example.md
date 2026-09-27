# Guided Example: Alternating Digit Sum

A positive integer is written in decimal and its digits are added with alternating signs. The most significant digit is positive, each following digit takes the opposite sign of the digit before it, and the signed digits are summed. The representative instance is $n = 886996$, whose signed digits cancel exactly to $0$, and the instance that exposes the most common mistake is $n = 10$.

## 1. The Sign Rule and the Instance

The rule assigns signs by position, not by digit value. Number the digits from the left starting at $0$, and let $d_i$ be the digit in position $i$ of a number with $L$ digits. Then $d_0$ is the most significant digit and $d_{L-1}$ is the least significant.

| Position $i$ from the left | Digit $d_i$ | Sign | Contribution |
|---|---|---|---|
| $0$ | $8$ | positive | $+8$ |
| $1$ | $8$ | negative | $-8$ |
| $2$ | $6$ | positive | $+6$ |
| $3$ | $9$ | negative | $-9$ |
| $4$ | $9$ | positive | $+9$ |
| $5$ | $6$ | negative | $-6$ |

The rule "each digit takes the opposite sign of its neighbours" together with "the most significant digit is positive" leaves no freedom: the sign of position $i$ is $(-1)^{i}$, positive on even positions from the left and negative on odd ones. That is the whole specification, and it is the only thing the computation needs.

## 2. Tracing $n = 886996$ Digit by Digit

Walking the digits from the left with a running total, alternating the sign at every step:

| Step | Digit read | Sign applied | Contribution | Running total |
|---|---|---|---|---|
| start | none | none | none | $0$ |
| 1 | $8$ | positive | $+8$ | $8$ |
| 2 | $8$ | negative | $-8$ | $0$ |
| 3 | $6$ | positive | $+6$ | $6$ |
| 4 | $9$ | negative | $-9$ | $-3$ |
| 5 | $9$ | positive | $+9$ | $6$ |
| 6 | $6$ | negative | $-6$ | $0$ |

The total ends at $0$. Note that the running total passes through negative values even though the final answer here is $0$: a partial total has no meaning of its own, and nothing about the method requires it to stay positive.

## 3. Pairing Consecutive Digits

Because the signs alternate, consecutive digits form pairs whose contribution is a difference. With an even number of digits every digit is paired and the sum is the sum of those differences.

| Pair | Digits | Contribution | Running total |
|---|---|---|---|
| first pair | $(8,\ 8)$ | $8 - 8 = 0$ | $0$ |
| second pair | $(6,\ 9)$ | $6 - 9 = -3$ | $-3$ |
| third pair | $(9,\ 6)$ | $9 - 6 = +3$ | $0$ |

For an even digit count $L$ this gives the closed form

$$
A = \sum_{k=0}^{L/2 - 1} \left( d_{2k} - d_{2k+1} \right),
$$

and for an odd count the first digit stands alone while the remaining $L - 1$ digits pair up in the same way. The pairing view explains the exact cancellation in $886996$: the second and third pairs produce $-3$ and $+3$ from different digits, so the total vanishes without any digit matching its partner.

## 4. Why the Sign Must Be Anchored at the Left

It is tempting to run the same alternation from the other end, starting the last digit positive, because a single loop over the digits from the right is just as easy to write. The two readings do not agree in general.

| Instance | Digits | Reading from the left | Reading from the right | Same result |
|---|---|---|---|---|
| $521$ | $3$ | $+5-2+1 = 4$ | $+1-2+5 = 4$ | yes |
| $111$ | $3$ | $+1-1+1 = 1$ | $+1-1+1 = 1$ | yes |
| $10$ | $2$ | $+1-0 = 1$ | $+0-1 = -1$ | no |
| $12$ | $2$ | $+1-2 = -1$ | $+2-1 = 1$ | no |
| $886996$ | $6$ | $0$ | $0$ | yes |
| $1000000000$ | $10$ | $1$ | $-1$ | no |

The pattern is exact rather than accidental. Reversing the alternation multiplies the sum by $(-1)^{L-1}$, so the right-anchored reading equals the required answer when $L$ is odd and equals its negation when $L$ is even. Two consequences follow. The mistake is invisible on every odd-length instance, and it is also invisible on the even-length sample $886996$, because the answer there is $0$ and zero is its own negation. The instances that actually catch it are $10$ and $1000000000$, both of which expect $1$ and would receive $-1$.

| Instance | Digits in the number | Expected | Left-anchored | Right-anchored | Catches the anchoring mistake |
|---|---|---|---|---|---|
| $521$ | $3$ | $4$ | $4$ | $4$ | no, odd count |
| $111$ | $3$ | $1$ | $1$ | $1$ | no, odd count |
| $886996$ | $6$ | $0$ | $0$ | $0$ | no, the answer is its own negation |
| $7$ | $1$ | $7$ | $7$ | $7$ | no |
| $10$ | $2$ | $1$ | $1$ | $-1$ | yes |
| $987654321$ | $9$ | $5$ | $5$ | $5$ | no, odd count |
| $909090909$ | $9$ | $45$ | $45$ | $45$ | no, odd count |
| $1000000000$ | $10$ | $1$ | $1$ | $-1$ | yes |

Four of the eight authored cases have an odd digit count and a fifth has answer $0$, so only two of them can distinguish the two readings. A method that anchors the sign at the right would pass six of the eight cases and fail the other two, which is exactly the kind of defect that a happy-path test suite hides.

## 5. Algorithmic Correctness of the Alternating Sum

The decision the method makes at each step is which sign to apply, and the invariant pins that down.

**Invariant.** After the first $k$ digits have been read from the left, the running total is $\sum_{i=0}^{k-1} (-1)^{i} d_i$.

**Base case.** With $k = 0$ no digit has been read and the total is $0$, the empty sum.

**Inductive step.** The invariant holds for $k$, so the total is $\sum_{i<k} (-1)^{i} d_i$. Reading digit $d_k$ and applying the sign $(-1)^{k}$ contributes exactly the next term, leaving $\sum_{i<k+1} (-1)^{i} d_i$, which is the invariant for $k + 1$.

**Termination.** After all $L$ digits are read the total is $\sum_{i=0}^{L-1} (-1)^{i} d_i$. The problem states that the most significant digit is positive and that each digit is opposite to its neighbours; the only sign assignment satisfying both is $(-1)^{i}$, which the invariant uses, so the final total is the required answer.

The following identity certifies the parity relationship between the answer and the digit sum. Split the digits into the positive positions with total $P$ and the negative positions with total $N$. Then the answer is $A = P - N$ while the digit sum is $S = P + N$, so $A - S = -2N$ and therefore $A \equiv S \pmod 2$ and $\lvert A \rvert \le S$. Both are useful as cheap sanity checks: an answer of the wrong parity, or larger in magnitude than the digit sum, cannot be right.

## 6. Boundary Instances and Material Traps

| Instance | Digits | Answer | What the instance establishes |
|---|---|---|---|
| $1$ | $1$ | $1$ | the smallest legal value; a single digit is positive by rule |
| $7$ | $1$ | $7$ | with one digit there is nothing to negate |
| $10$ | $2$ | $1$ | a trailing zero still consumes a negative position |
| $12$ | $2$ | $-1$ | the answer can be negative, and the smallest even-length instance separates the two anchorings |
| $19$ | $2$ | $-8$ | the answer is not a digit sum, which would be $10$ here |
| $886996$ | $6$ | $0$ | exact cancellation with no pairing rule |
| $909090909$ | $9$ | $45$ | zero digits occupy positions that matter |
| $999999999$ | $9$ | $9$ | five positive nines against four negative nines |
| $1000000000$ | $10$ | $1$ | the largest legal value, and the only ten-digit one |

| Guess that looks plausible | Verdict | The instance that settles it |
|---|---|---|
| the answer is the digit sum | false | $19$ answers $-8$ while its digit sum is $10$ |
| the answer is never negative | false | $12$ answers $-1$ |
| starting the sign at the last digit is equivalent | false for even digit counts | $10$ expects $1$ and the right-anchored reading gives $-1$ |
| an even digit count cancels to zero | false | $12$ has two digits and answers $-1$; only $886996$ happens to cancel |
| zero digits can be skipped | false | dropping the zeros of $909090909$ answers $9$ instead of $45$, because each skipped zero shifts every later sign |
| the answer has the same parity as the digit sum | true | $A - S = -2N$, so the two differ by an even number |
| a one-digit number is its own answer | true | there is no second digit to negate |

```mermaid
flowchart LR
  accTitle: Reading the digits from the most significant end
  accDescr: The digits are read from the most significant end, the first contributing with a positive sign and every following digit contributing with the opposite sign of the digit before it, until the total is complete.
  A["most significant digit, positive sign"] --> B["next digit, opposite sign"]
  B --> C["and so on through the last digit"]
```

## 7. Cost of the Method

- **Time Complexity:** $O(L)$, where $L$ is the number of decimal digits, because each digit is read exactly once and contributes one addition. Since $L$ is the number of digits of $n$, this is $O(\log n)$, and under the constraint $n \le 10^{9}$ it never exceeds ten iterations.
- **Auxiliary Space Complexity:** $O(1)$ beyond the decimal representation that must be read; the method holds one running total, one position counter and one digit at a time. Materializing the digits as a sequence of length $L$ would cost $O(L)$, which is bounded by the same ten positions.

An alternative worth knowing is to read the digits from the right after first counting them, applying the sign $(-1)^{L-1-j}$ to the digit $j$ positions from the end. It computes the same answer, and the equivalence above shows exactly why it agrees with the left-anchored reading precisely when $L$ is odd, so it needs the digit count to be known before the first addition rather than discovered on the way. The single left-to-right pass avoids that dependency altogether.
