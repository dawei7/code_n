# Guided Example: Count the Digits That Divide a Number

## 1. The Instance and the Question It Asks

We are given a positive integer whose decimal representation contains no `0` digit, and we must count how many of its digits divide that same integer exactly. A digit $d$ qualifies when the remainder of the division of the number by $d$ is zero; a digit that appears several times is counted once per occurrence, and the number itself is never counted as its own digit.

We work the second official instance:

- `num` = `121`

Its decimal representation is $1, 2, 1$, and the required output is `2`. Two structural facts make this instance more informative than the trivial one-digit case:

- the digit `1` occurs **twice**, so the answer is not the number of distinct qualifying digits but the number of qualifying digit *occurrences*;
- the digit `2` does **not** divide $121$, so a census that assumes every digit of a number divides it — a surprisingly common misreading, since `1248` does divide by all four of its digits — is immediately refuted.

The method is deliberately elementary: peel the digits off the number from the least significant end and test each one against the original value. What matters pedagogically is why the peeled remainder *is* the digit, and why using the original number as the dividend at every test is the correct choice rather than reusing the shrinking quotient.

## 2. What a Digit Is Here: Value, Not Position

A decimal digit is a coefficient, not a location. Writing $x$ in base $10$,

$$x = \sum_{j \ge 0} d_j \cdot 10^{j}, \qquad d_j \in \{0, 1, \dots, 9\},$$

assigns to each power of ten a coefficient $d_j$; that coefficient is the digit. For $121$ the expansion is

$$121 = 1 \cdot 10^{2} + 2 \cdot 10^{1} + 1 \cdot 10^{0},$$

so the digit sequence read from the most significant end is $(1, 2, 1)$, while the digit *values* available to test are the multiset $\{1, 1, 2\}$.

This distinction drives the whole answer. The divisibility test is a property of the digit's **value**: `num % d == 0`. It has nothing to do with the digit's place, and two positions may carry the same value and therefore produce two separate successes. For `121` the multiset contains two copies of $1$, and both are counted, which is exactly why the sample answer is $2$ rather than $1$.

| Position (power of ten) | Coefficient $d_j$ | Place value $d_j \cdot 10^{j}$ | Counts toward the answer? |
|:---:|:---:|:---:|:---|
| units, $10^{0}$ | 1 | 1 | yes, $1 \mid 121$ |
| tens, $10^{1}$ | 2 | 20 | no, $2 \nmid 121$ |
| hundreds, $10^{2}$ | 1 | 100 | yes, second occurrence of $1$ |

The place-value column is there to be ignored: $121$ is divisible by $1$ and not by $2$, but the *place values* $1$, $20$ and $100$ play no role in the test at all.

## 3. Peeling Digits with Integer Division and Remainder

Repeated integer division by ten exposes the coefficients from the least significant end. For any positive $x$,

$$\mathrm{divmod}(x, 10) = \big(\lfloor x / 10 \rfloor,\; x \bmod 10\big),$$

and the remainder $x \bmod 10$ is precisely the digit $d_0$ of $x$. Dividing by ten shifts the whole representation one place to the right, because it removes the term $d_0 \cdot 10^{0}$ and divides every remaining term by ten:

$$\lfloor x/10 \rfloor = \sum_{j \ge 1} d_j \cdot 10^{\,j-1}.$$

Iterating this until the quotient becomes $0$ yields every coefficient, one per iteration. The number of iterations equals the number of decimal digits, which for $121$ is three — this instance is exemplary because that count is larger than the number of *distinct* digit values, so the loop cannot be replaced by a set-based shortcut without losing the multiplicity.

| Step | Value of $x$ before | Quotient $\lfloor x/10 \rfloor$ | Digit $d = x \bmod 10$ | $x$ after | Digits still unexamined |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 121 | 12 | 1 | 12 | 2, 1 |
| 2 | 12 | 1 | 2 | 1 | 1 |
| 3 | 1 | 0 | 1 | 0 | none |
| — | 0 | — | — | — | loop terminates: $x = 0$ is falsy |

The loop terminates exactly when the last quotient reaches $0$, which happens after the most significant digit has itself been extracted. There is no fourth iteration and no leading zero is ever produced, because a positive integer's decimal expansion has no leading zeros. That is also why the "no `0` digit" guarantee matters: the loop's stopping condition $x = 0$ is never confused with a genuine digit value, and no test needs to guard against a zero divisor.

## 4. The Divisibility Census for 121

Each extracted digit is tested against the **original** value, not against the shrinking quotient. Keeping the original dividend fixed is essential: $121$ is the number whose divisors we are counting, and after two iterations the working value is $1$, which would divide by everything and turn every later digit into a false success. Pinning the dividend to a saved copy removes that error entirely.

| Extracted digit $d$ | Test computed | Remainder | Verdict | Running count |
|:---:|:---|:---:|:---|:---:|
| 1 | `121 % 1` | 0 | divides | 1 |
| 2 | `121 % 2` | 1 | does not divide | 1 |
| 1 | `121 % 1` | 0 | divides | 2 |

The final count is $2$, matching the required output. Notice how the two rows for digit $1$ are independent: the same test is performed twice and contributes twice. A census that deduplicated digits before testing would report $1$ here and would also misreport `999999999`, where nine identical digits divide and the answer is $9$.

## 5. Correctness and the Digit-Extraction Invariant

**Invariant.** At the top of every loop iteration, the digits already extracted are exactly the coefficients $d_0, d_1, \dots, d_{k-1}$ of the original number — that is, the digits removed by the preceding $k$ divisions by ten — and the working value $x$ equals $\sum_{j \ge k} d_j \cdot 10^{\,j-k}$, the original number with those $k$ digits deleted. The counter equals the number of extracted digits that divide the original number.

*Initialization.* Before the first iteration no digit has been extracted, the working value equals the original number, and the counter is $0$, so the invariant holds vacuously with $k = 0$.

*Preservation.* The division-and-remainder step splits $x$ as $x = 10 \cdot \lfloor x/10 \rfloor + (x \bmod 10)$; the remainder is therefore the coefficient of $10^{0}$ in the current representation, which by the invariant is the next original coefficient $d_k$, and the new working value is the representation of the remaining coefficients with their exponents reduced by one. The counter is incremented exactly when the extracted digit divides the fixed original value, which is the criterion the problem states.

*Termination and completeness.* Each iteration strictly decreases the positive working value, so the loop terminates; it stops at $x = 0$ only after the most significant coefficient has been extracted, because a leading coefficient is nonzero. Every digit of the representation is therefore visited exactly once, and no digit outside it is ever produced. Since each visit contributes at most one to the counter and precisely when the divisibility test succeeds, the final counter equals the number of digit occurrences dividing the number — the required answer.

The argument also isolates the two failure modes worth naming. Using the shrinking working value as the dividend breaks the invariant's link to the problem statement: divisibility must be judged against the original integer throughout. And terminating the loop one iteration too early — for example by stopping when the quotient is a single digit — would drop the most significant digit, which here is one of the two counting digits.

## 6. Traps and Boundary Behaviour

| Scenario | Instance | Digit walk | Result | Why the rule still holds |
|:---|:---|:---|:---:|:---|
| single-digit number | `num` = `7` | extracts 7; `7 % 7` = 0 | 1 | The number divides itself, and the loop runs exactly once. |
| all digits divide | `num` = `1248` | 8, 4, 2, 1 all succeed | 4 | Nothing about the method special-cases this; it is simply the case where every test passes. |
| no digit divides | `num` = `37` | `37 % 7` = 2, `37 % 3` = 1 | 0 | A count of zero is a legitimate answer; the accumulator must start at `0`, not at `1`. |
| repeated divisor | `num` = `212` | digits 2, 1, 2 — all succeed | 3 | Occurrences are counted separately; three digits, three successes. |
| mixed repeats | `num` = `121` | 1 succeeds, 2 fails, 1 succeeds | 2 | Multiplicity and divisibility are independent axes and must both be respected. |
| nine identical digits | `num` = `999999999` | nine extractions, all `9` | 9 | The loop is driven by digit count, not by distinct values, so nine identical tests still run. |
| many distinct digits | `num` = `123456789` | only 1, 3 and 9 succeed among the nine | 3 | Divisibility is far from automatic: 2, 4, 5, 6, 7 and 8 all fail against this odd, non-multiple dividend. |
| counting distinct values instead | `num` = `121` | distinct set is $\{1, 2\}$ | 2 would be wrong for `999999999` | Distinct-value counting happens to agree here but returns 1 for `999999999` and 3 for `212`; the problem counts digit occurrences. |
| dividing by the shrinking value | `num` = `121` | after two steps the working value is 1 | inflated count | Every later digit would "divide" the value 1; the dividend must remain the original number. |

The guarantee that `0` never appears as a digit is doing real work in the boundary column: an extracted zero would make the divisibility test undefined, since division by zero has no remainder, and any implementation would have to skip it explicitly. Under the stated constraints the problem removes that branch entirely, so the method never needs a zero guard — but a different input domain would require one, and that is exactly the difference between a correct solution and a lucky one.

## 7. Complexity: Time and Auxiliary Space

**Time.** Each iteration of the extraction loop performs one integer division, one remainder, and one divisibility test — a constant amount of work. For an input value $x$, the number of iterations is the number of decimal digits,

$$D(x) = \lfloor \log_{10} x \rfloor + 1,$$

so the running time is

$$T(x) = \mathrm{O}(D(x)) = \mathrm{O}(\log_{10} x).$$

Under the stated bound $x \le 10^{9}$ the loop runs at most ten times, so the algorithm is effectively constant-time in this domain; the logarithmic description is what remains true if the bound is ever raised. Extracting the digits as characters and then converting each back to a value would also cost linear time in the digit count, but it allocates a representation the arithmetic path never needs.

**Auxiliary space.** The method stores the working value, a saved copy of the original number, and the counter — three integers, independent of the magnitude of the input:

$$S_{\text{aux}}(x) = \mathrm{O}(1).$$

No array of digits, no stack, and no string buffer is created. This is the practical reason to prefer arithmetic extraction over a string conversion: the two approaches share the same asymptotic time, but only this one keeps the extra memory truly constant.

## 8. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Arithmetic extraction by division | Repeatedly divide by ten, test the remainder against the original value. | $\mathrm{O}(\log_{10} x)$ time, $\mathrm{O}(1)$ space | The preferred method: no allocation, no parsing, and it works identically in any language with integer division. |
| Convert to a decimal string | Read the decimal representation and iterate over its characters, converting each back to a digit. | $\mathrm{O}(\log_{10} x)$ time, $\mathrm{O}(\log_{10} x)$ space | Same time class with extra memory and an extra conversion step; the character form is convenient for display but not for arithmetic. |
| Count distinct digits with a small set | Collect the distinct digit values, test each once, and multiply by nothing. | $\mathrm{O}(\log_{10} x)$ time | Answers a different question. Multiplicity is part of this problem: `999999999` has one distinct digit and nine counting occurrences. |
| Precompute divisibility by table | Hard-code the divisibility rules for the ten possible digits. | $\mathrm{O}(\log_{10} x)$ time | Adds a teardown of special cases (rules for 3, 6, 7, 9 are not single arithmetic tests) where a single remainder handles every digit uniformly. |
| Test every integer from 1 to `num` | Count divisors of the number in general. | $\mathrm{O}(x)$ time | Answers a strictly harder question than the one asked; the digits are a tiny, cheaply extracted subset of the candidate divisors. |

The generalizable idea is to keep the *object being divided* fixed while decomposing it. Digit extraction is a mechanical way to enumerate the coefficients of a positional representation, and every test against those coefficients is performed against the original value, not against an intermediate that has been mutilated by the decomposition itself.