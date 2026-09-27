# Guided Example: Number of Even and Odd Bits

## 1. The instance and the indexing convention

Take `n = 50`. The contract fixes one convention before any counting begins: bits are numbered **from right to left**, the least significant bit being index $0$. Since $50 = 32 + 16 + 2$, its six-bit representation is `110010`, and the set bits sit at indices 1, 4, and 5.

| Index $i$ (right to left) | 5 | 4 | 3 | 2 | 1 | 0 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Weight $2^i$ | 32 | 16 | 8 | 4 | 2 | 1 |
| Digit of `110010` | 1 | 1 | 0 | 0 | 1 | 0 |
| Index parity | odd | even | odd | even | odd | even |

The two required counters are therefore $\text{even} = 1$ (only index 4) and $\text{odd} = 2$ (indices 1 and 5), giving the pair `[1, 2]`. Only digits equal to 1 are counted, and a digit 0 contributes to neither counter, whatever its index.

## 2. Reading one bit at a time

The low digit of an integer is its parity, and dropping the low digit is a right shift. So a single loop can walk the bits from index 0 upward: read `n & 1`, add it to the counter for the current index parity, shift `n` right by one, and continue until nothing is left.

| Step | Current `n` | Binary of current `n` | Low digit `n & 1` | Index read | Counter touched | `[even, odd]` after |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 50 | `110010` | 0 | 0 | neither | `[0, 0]` |
| 2 | 25 | `11001` | 1 | 1 | odd | `[0, 1]` |
| 3 | 12 | `1100` | 0 | 2 | neither | `[0, 1]` |
| 4 | 6 | `110` | 0 | 3 | neither | `[0, 1]` |
| 5 | 3 | `11` | 1 | 4 | even | `[1, 1]` |
| 6 | 1 | `1` | 1 | 5 | odd | `[1, 2]` |
| 7 | 0 | — | — | loop ends | — | `[1, 2]` |

Each shift halves the value, so the digit examined at step $j$ is the digit of index $j-1$ of the original number, and the loop stops one step after the highest set bit. Nothing beyond the most significant set bit is ever examined, which is why no bit width has to be chosen in advance — leading zeros would add zero to both counters anyway.

## 3. The bookkeeping that must alternate

The only state beyond the two counters is which parity the next digit belongs to. Because consecutive shifts expose consecutive indices, that parity flips on every step.

| Step $j$ | Index read | Index parity | Rule for the next step |
|:---:|:---:|:---:|:---|
| 1 | 0 | even | next index is odd |
| 2 | 1 | odd | next index is even |
| 3 | 2 | even | next index is odd |
| 4 | 3 | odd | next index is even |
| 5 | 4 | even | next index is odd |
| 6 | 5 | odd | no next digit |

Any reliable mechanism works: keep a separate index variable and increment it, keep a flag and negate it, or keep a selector that toggles between the two counter slots. What matters is that the toggle happens exactly once per shifted digit — including for digits equal to 0, because a zero digit still consumes an index. Skipping the toggle on zero digits is the classic way to desynchronize the counters, and on `n = 50` it would move index 4 into the odd counter and report `[0, 3]` instead of `[1, 2]`.

## 4. An equivalent formulation with parity masks

Alternating indices can also be selected arithmetically. The mask with ones in every even index and zeros in every odd index is `0101010101` over ten bits, decimal 341; shifting it left once gives its odd-index twin, decimal 682.

| Mask | Binary (ten bits) | Indices selected | `50 & mask` | Set bits counted |
|:---:|:---:|:---:|:---:|:---:|
| 341 | `0101010101` | 0, 2, 4, 6, 8 | 16 | 1 |
| 682 | `1010101010` | 1, 3, 5, 7, 9 | 34 | 2 |

The intersection with 341 keeps only the even-index digits of 50, namely the digit at index 4, and its popcount is the `even` counter; the intersection with 682 keeps indices 1 and 5, giving 34 whose popcount is 2 for the `odd` counter. Both routes must agree, and here both produce `[1, 2]`. The masking route is only as wide as the mask chosen, so it requires knowing a safe bit width, whereas the shifting route discovers the width as it goes.

## 5. Invariant and correctness of the shift-and-count loop

**Invariant.** After $j$ steps, the working value equals $\lfloor n / 2^{j} \rfloor$, the counters hold the number of set bits at even and odd indices among the original indices $0, \dots, j-1$, and the next index to be read is exactly $j$.

The three parts are preserved by one step. The digit read is `n & 1`, which is precisely bit $j$ of the original number because dividing by $2^{j}$ discards indices below $j$ and leaves bit $j$ as the new low digit. The counter selected by the alternating parity is the counter belonging to index $j$. After the shift the working value is $\lfloor n / 2^{j+1} \rfloor$ and the next index is $j+1$, so the invariant holds for $j+1$.

**Termination and completeness.** Every set bit has a finite index $m \le \lfloor \log_2 n \rfloor$, and the working value becomes 0 after exactly $\lfloor \log_2 n \rfloor + 1$ shifts, which is one step past index $m$. From then on `n & 1` would only ever read zeros, so stopping at zero skips no set bit: every index holding a 1 has been visited exactly once. Since each visited digit is added to exactly one counter according to its own index parity, the final pair is the required `[even, odd]` — for `n = 50`, `[1, 2]`, matching the official expected output.

## 6. Traps and boundary instances

| Tempting rule | Value on `n = 50` | Correct? | Why it fails |
|:---|:---:|:---:|:---|
| Number the bits from the left, most significant first | `[2, 1]` | no | The contract numbers from the right, so a left-to-right scan swaps the two counters |
| Infer the index parity from the weight $2^i$ being even | `[3, 0]` | no | Index parity is not weight parity: index 0 carries the odd weight 1, and weights 2, 8, 32 are even weights sitting at odd indices |
| Read decimal digits by dividing by 10 | meaningless | no | Decimal digits are not binary digits; only division by 2 exposes the bits |
| Stop after a fixed ten digits without checking the value | `[1, 2]` here | risky | Harmless for $n \le 1000$ only because extra leading zeros add nothing, but a wrong width silently truncates larger inputs |

| Instance | Binary | Set-bit indices | `[even, odd]` | What it teaches |
|:---|:---:|:---:|:---:|:---|
| 1 | `1` | 0 | `[1, 0]` | The least significant bit is index 0, an even index |
| 2 | `10` | 1 | `[0, 1]` | A power of two sets exactly one bit, at the index of its exponent |
| 3 | `11` | 0, 1 | `[1, 1]` | Adjacent set bits always land one per parity |
| 10 | `1010` | 1, 3 | `[0, 2]` | Every set bit can be odd-indexed; the `even` counter may be 0 |
| 21 | `10101` | 0, 2, 4 | `[3, 0]` | The `odd` counter may be 0 while the other is large |
| 1000 | `1111101000` | 3, 5, 6, 7, 8, 9 | `[2, 4]` | The largest legal input needs ten digits; index 9 is odd |

A further trap is the meaning of `[even, odd]`: it is an ordered pair, not a sorted pair, so the smaller number does not automatically come first. `n = 10` returns `[0, 2]` and `n = 21` returns `[3, 0]`, which shows both orders occurring.

## 7. Time and auxiliary space complexity

Let $B$ be the number of binary digits of $n$, so $B = \lfloor \log_2 n \rfloor + 1$.

- **Time.** Each step reads one digit and shifts once, so the loop runs $B$ times, giving $O(\log n)$ — at most ten iterations under the constraint $n \le 1000$.
- **Auxiliary space.** The state is two counters plus one index or flag, independent of $n$: $O(1)$. The returned pair is the required output, not auxiliary storage.
- **Mask alternative.** Intersecting with each of the two masks and counting set bits is also $O(\log n)$ if the popcount is computed digit by digit, and $O(1)$ per mask only when the language offers a constant-time population count.

The cost depends only on the bit length of $n$, never on its magnitude in decimal digits.
