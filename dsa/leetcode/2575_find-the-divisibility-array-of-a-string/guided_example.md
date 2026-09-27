# Guided Example: Find the Divisibility Array of a String

## 1. The quantity that has to be tested is too large to build

The divisibility array of a digit string `word` of length $n$ records, for each index $i$, whether the **numeric value** of the prefix `word[0..i]` is divisible by $m$:

$$\text{div}[i] = 1 \iff m \mid V_i, \qquad V_i = \sum_{k=0}^{i} d_k \cdot 10^{\,i-k},$$

where $d_k$ is the digit at position $k$. The constraint $n \le 10^5$ makes the prefix value itself unusable: the full prefix has up to $100000$ decimal digits, roughly $332000$ bits, and constructing every prefix in turn would need quadratic digit work and enormous integers. What the answer needs is not the value of $V_i$ but one bit of information about it, and the constraint $m \le 10^9$ says that bit can be carried by a number smaller than $m$.

## 2. Carrying the remainder instead of the value

The key algebraic fact is that the map $a \mapsto 10a + d$ preserves congruence modulo $m$:

$$a \equiv b \pmod m \implies 10a + d \equiv 10b + d \pmod m .$$

That is exactly the operation that appends a digit in base ten, because

$$V_i = 10\,V_{i-1} + d_i .$$

So if $x_{i-1}$ is the true remainder $V_{i-1} \bmod m$, then $(10 x_{i-1} + d_i) \bmod m$ is the true remainder $V_i \bmod m$, and no exact value is ever needed. The single state variable of the scan is the running remainder, updated by

$$x_i = \left( 10\,x_{i-1} + d_i \right) \bmod m, \qquad x_{-1} = 0 .$$

The invariant maintained after processing the first $i+1$ digits is:

> $x_i$ equals $V_i \bmod m$ exactly, where $V_i$ is the numeric value of the prefix `word[0..i]`.

It holds before the scan because the empty prefix has value $0$ and therefore remainder $0$. If it holds for $i-1$, then appending $d_i$ maps the value by $V_i = 10V_{i-1} + d_i$, and reducing both sides modulo $m$ gives $x_i = (10x_{i-1} + d_i) \bmod m$, which is the update; the invariant is restored. Since divisibility is decided entirely by the remainder,

$$m \mid V_i \iff V_i \bmod m = 0 \iff x_i = 0,$$

each output entry is the single comparison `x == 0`, recorded as $1$ when it holds and $0$ otherwise.

Note that $x_{i-1}$ is always reduced below $m$, so $10x_{i-1} + d_i < 10m \le 10^{10}$: every intermediate value stays small even though the numbers being described have a hundred thousand digits. No modular inverse of $10$ is ever needed, so $m$ does not have to be coprime with $10$ — a detail that matters for divisors such as $m = 10$ in the second official example.

## 3. The worked instance

- Input: `word = "998244353"`, $m = 3$
- Required output: `[1, 1, 0, 0, 0, 1, 1, 0, 0]`

Starting from $x_{-1} = 0$ and processing the digits $9, 9, 8, 2, 4, 4, 3, 5, 3$ one at a time:

| $i$ | Digit $d_i$ | Previous remainder $x_{i-1}$ | $10x_{i-1} + d_i$ | New remainder $x_i$ | `div[i]` |
|---|---|---|---|---|---|
| 0 | 9 | 0 | 9 | 0 | 1 |
| 1 | 9 | 0 | 9 | 0 | 1 |
| 2 | 8 | 0 | 8 | 2 | 0 |
| 3 | 2 | 2 | 22 | 1 | 0 |
| 4 | 4 | 1 | 14 | 2 | 0 |
| 5 | 4 | 2 | 24 | 0 | 1 |
| 6 | 3 | 0 | 3 | 0 | 1 |
| 7 | 5 | 0 | 5 | 2 | 0 |
| 8 | 3 | 2 | 23 | 2 | 0 |

The recorded output is `[1, 1, 0, 0, 0, 1, 1, 0, 0]`, which is the required answer. The four positions where the remainder is $0$ correspond to the prefixes `9`, `99`, `998244`, and `9982443`, matching the fact that exactly four prefixes of this string are multiples of $3$.

Because $m = 3$ has the special property $10 \equiv 1 \pmod 3$, the running remainder here must equal the running digit sum reduced modulo $3$, and that gives an independent check of every step:

| $i$ | Prefix `word[0..i]` | Digit sum | Digit sum mod 3 | Remainder $x_i$ | `div[i]` |
|---|---|---|---|---|---|
| 0 | `9` | 9 | 0 | 0 | 1 |
| 1 | `99` | 18 | 0 | 0 | 1 |
| 2 | `998` | 26 | 2 | 2 | 0 |
| 3 | `9982` | 28 | 1 | 1 | 0 |
| 4 | `99824` | 32 | 2 | 2 | 0 |
| 5 | `998244` | 36 | 0 | 0 | 1 |
| 6 | `9982443` | 39 | 0 | 0 | 1 |
| 7 | `99824435` | 44 | 2 | 2 | 0 |
| 8 | `998244353` | 47 | 2 | 2 | 0 |

The two remainder columns agree at every index, and each agreement follows from $10^k \equiv 1 \pmod 3$: the weighted prefix value collapses to the digit sum modulo $3$. This collapse is a coincidence of $m = 3$ and must not be generalized — for $m = 7$, for instance, the weights $10^k$ cycle through $1, 3, 2, 6, 4, 5$ and the digit sum tells nothing.

## 4. A zero digit is not a divisible prefix

The second official instance, `word = "1010"` with $m = 10$, is the natural trap for this problem, because two of its four digits are `0` while only two of its four prefixes are divisible:

| $i$ | Digit $d_i$ | Previous remainder $x_{i-1}$ | $10x_{i-1} + d_i$ | New remainder $x_i$ | `div[i]` |
|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 10 | 0 | 1 |
| 2 | 1 | 0 | 1 | 1 | 0 |
| 3 | 0 | 1 | 10 | 0 | 1 |

The output is `[0, 1, 0, 1]`. The digit `0` at index `1` and the digit `0` at index `3` are not what makes those prefixes divisible; the prefix `10` has value $10$ and the prefix `1010` has value $1010$, both multiples of $10$, whereas the prefix `1` has value $1$ and the prefix `101` has value $101$, neither of them a multiple. The divisibility comes from the whole prefix, carried in the remainder, never from the newest digit alone. Leading zeros behave the same way for the opposite reason: the prefixes `0` and `00` of the word `0012` have numeric value $0$, and $0$ is divisible by every positive integer, so their entries are $1$ even though the word begins with zeros.

## 5. Boundary analysis

| Input | Expected output | Reading of the reasoning |
|---|---|---|
| `word = "9"`, $m = 3$ | `[1]` | a single digit; $x_0 = 9 \bmod 3 = 0$ |
| `word = "0"`, $m = 10^9$ | `[1]` | the prefix value is $0$, and every positive $m$ divides $0$ |
| `word = "999"`, $m = 3$ | `[1, 1, 1]` | repeated digits keep hitting remainder $0$; nothing about distinctness is required |
| `word = "111111"`, $m = 3$ | `[0, 0, 1, 0, 0, 1]` | the remainder cycles with period $3$, so the hits are periodic |
| `word = "0012"`, $m = 3$ | `[1, 1, 0, 1]` | leading zeros give value $0$; only the last prefix, $12$, is a multiple of $3$ |
| `word = "12345"`, $m = 97$ | `[0, 0, 0, 0, 0]` | no prefix happens to be a multiple; a correct scan may produce no hit at all |
| `word = "90701"`, $m = 1$ | `[1, 1, 1, 1, 1]` | every remainder is $0$ modulo $1$, so every entry is $1$ |
| `word = "1000000000"`, $m = 10^9$ | nine `0` entries then a `1` | the prefixes $1, 10, \dots, 10^8$ are all below $m$, and only $10^9$ reaches remainder $0$ |
| a 30-digit word, $m = 999999937$ | all zeros | a long numeric value is never built; only its remainder is carried |

| Trap | What goes wrong | Correct treatment |
|---|---|---|
| Materializing the prefix value | a prefix of $10^5$ digits costs quadratic work to rebuild and cannot be held as a machine integer | keep only $V_i \bmod m$ and update it with the Horner step |
| Testing the newest digit instead of the prefix | the digit `0` appears in positions that are not divisible prefixes, and a nonzero digit may still complete one | compare the running remainder against $0$ |
| Using 32-bit arithmetic for the intermediate | $10x_{i-1} + d_i$ can reach $10^{10} - 1$, which exceeds the signed 32-bit range $2147483647$ when $m$ approaches $10^9$ | compute the intermediate in 64-bit (or unbounded) arithmetic and reduce immediately |
| Looking for a modular inverse | dividing the remainder by $10$ fails whenever $m$ shares a factor with $10$, for example $m = 10$ or $m = 100$ | the recurrence only multiplies and adds, so no inverse is ever required |
| Generalizing the digit-sum shortcut | $10 \equiv 1 \pmod 3$ holds only for $m = 3$ and $m = 9$ | reduce the accumulated remainder, not the digit sum |

## 6. Time and auxiliary space

- **Time.** The scan touches each of the $n$ digits once and performs a constant number of operations per digit: one multiplication by ten, one addition, one modular reduction, and one comparison. The running time is $\Theta(n)$, which is optimal, since the divisibility array has $n$ entries and any correct method must examine all $n$ digits — the last entry alone depends on every digit of the word.
- **Auxiliary space.** The scan keeps one remainder, one digit, and the output position: $O(1)$ extra space. The returned array of $n$ small integers is the required output and is not counted as auxiliary. Storage never grows with the length of the prefix values, which is the entire point of carrying remainders.
- **Contrast.** Building each prefix explicitly would take $\Theta(n^2)$ digit operations and $\Theta(n)$ space per prefix, and arbitrary-precision arithmetic on numbers with $10^5$ digits would make the per-digit cost grow as well; the modular scan replaces all of that with a single bounded register.
