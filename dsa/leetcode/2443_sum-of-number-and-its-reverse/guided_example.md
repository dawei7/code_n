# Guided Example: Sum of Number and Its Reverse

## 1. The decision that has to be made for `num = 443`

The problem hands us one non-negative integer and asks a pure existence
question: is there a non-negative integer $k$ with

$$
k + \operatorname{rev}(k) = \texttt{num},
$$

where $\operatorname{rev}$ reverses the decimal digits and then reads the result
back as an ordinary integer? The representative input for this lesson is

- **Input:** `num = 443`
- **Required outcome:** `true`

Two witnesses are visible immediately once one is written down: $172 + 271 = 443$
and, symmetrically, $271 + 172 = 443$. The lesson below does not merely exhibit
them; it derives the *complete* witness list for `443` from the column structure
of three-digit addition and shows why the ascending scan is correct in both
directions — it never claims a witness that does not exist, and it never misses
one that does. Because the result is a Boolean, the search may stop the instant
a witness appears, which is why the worked trace can be truncated at one
decisive row.

---

## 2. Bounding the search: a witness can never exceed the target

Both addends are non-negative by the statement of the problem, so
$\operatorname{rev}(k) \ge 0$ for every candidate $k$. Therefore

$$
k \le k + \operatorname{rev}(k) = \texttt{num}.
$$

This one inequality collapses an infinite search space to the finite interval
$0 \le k \le \texttt{num}$, and it is *tight*: every integer in that interval
must be regarded as a candidate, because a reversal can be far smaller or far
larger than the number it came from. Two facts make this concrete for `443`:

1. `443` is odd and every one-digit candidate contributes $2k$, an even number,
   so no one-digit witness exists.
2. Every two-digit candidate contributes $11(a+b)$ for digits $a$ and $b$, and
   `443` is not a multiple of $11$ (`443 = 11 \cdot 40 + 3`), so no two-digit
   witness exists either.

The interval bound together with those two parity/divisibility facts means the
only witnesses for `443` must be three-digit candidates. A heuristic that
searched "near half the target" would look around `221`, and that region
contains no witness at all.

---

## 3. What reversal actually does to digits, including trailing zeros

Reversal is a digit permutation, not a string operation with padding. Writing a
three-digit candidate as $k = 100a + 10b + c$ with $a \ge 1$, the reversed
digits $cba$ read as a number are $100c + 10b + a$ — except when $c = 0$, where
the leading zero of the reversed string is dropped and the value is $10b + a$.
Both cases are covered at once by

$$
k + \operatorname{rev}(k) = 101(a+c) + 20b .
$$

The table below shows the operation on values that matter later in the lesson.

| Candidate $k$ | Reversed digit string | $\operatorname{rev}(k)$ | $k + \operatorname{rev}(k)$ | Note |
|---|---|---|---|---|
| `0` | `"0"` | 0 | 0 | unique witness for `num = 0` |
| `5` | `"5"` | 5 | 10 | unique witness for `num = 10`; addends equal |
| `99` | `"99"` | 99 | 198 | two-digit, palindrome |
| `140` | `"041"` | 41 | 181 | leading zero dropped, so the triple is not symmetric |
| `171` | `"171"` | 171 | 342 | palindrome, still below `443` |
| `172` | `"271"` | 271 | 443 | first witness reached by an ascending scan |
| `271` | `"172"` | 172 | 443 | same unordered pair, distinct candidate |
| `370` | `"073"` | 73 | 443 | trailing zero becomes a leading zero |

Row five is the trap row. A learner who pads the reversed string instead of
parsing it would turn `"041"` into something other than 41 and would wrongly
declare `181` unreachable, even though the problem's own third example is
exactly $140 + 41 = 181$.

---

## 4. The ascending scan over the candidate interval

The method walks the candidates in increasing order, maintaining one piece of
state: the boundary of the certified prefix.

> **Search invariant.** Immediately before candidate $k$ is tested, every
> integer in $[0, k-1]$ has been tested and rejected, so no witness smaller
> than $k$ exists.

The invariant starts true at $k = 0$ (the prefix is empty) and is preserved by
the test itself: if $k$ is rejected, the certified prefix extends to include
it. The scan stops the first time the equality holds, which is an immediate
certificate that the answer is `true`.

| Stage of the scan | Candidate $k$ | $\operatorname{rev}(k)$ | Sum | Comparison with `443` | Action taken |
|---|---|---|---|---|---|
| Smallest candidate | `0` | 0 | 0 | $0 < 443$ | reject, extend prefix |
| End of the one-digit band | `9` | 9 | 18 | $18 < 443$ | reject, extend prefix |
| First two-digit candidate | `10` | 1 | 11 | $11 < 443$ | reject, extend prefix |
| Last two-digit candidate | `99` | 99 | 198 | $198 < 443$ | reject, extend prefix |
| First three-digit candidate | `100` | 1 | 101 | $101 < 443$ | reject, extend prefix |
| Trailing-zero candidate | `140` | 41 | 181 | $181 < 443$ | reject; this value witnesses `181`, not `443` |
| Final rejected candidate | `171` | 171 | 342 | $342 < 443$ | reject, extend prefix |
| **Decisive candidate** | `172` | 271 | 443 | $443 = 443$ | equality certified, return `true` |
| Unexamined remainder | `173` … `443` | — | — | never evaluated | skipped by short-circuiting |

The scan performs 173 candidate tests for this input and stops. Since `172` lies
*below* half of `443` while its partners `271` and `370` lie above it, neither
"search the low half" nor "search the high half" is sound on its own; the
certified prefix is what makes early termination safe. A `false` answer has no
such shortcut: for `num = 63` every candidate in $[0, 63]$ is tested, and only
after the interval is exhausted may the method report `false`.

---

## 5. Deriving every witness of `443` from the column structure

Because candidates above `443` are impossible, three-digit candidates are the
only ones left, and for those the sum is exactly $101(a+c) + 20b$. Solving

$$
101(a+c) + 20b = 443
$$

modulo $101$ gives $20b \equiv 443 \equiv 39 \pmod{101}$. Since
$20 \cdot 5 = 100 \equiv -1$, the inverse of $20$ is $-5 \equiv 96$, so
$b \equiv 39 \cdot 96 = 3744 \equiv 7 \pmod{101}$, and because $0 \le b \le 9$
the middle digit is forced: $b = 7$. Substituting back gives
$101(a+c) = 443 - 140 = 303$, hence $a + c = 3$.

| Constraint | Forced value | Consequence |
|---|---|---|
| $20b \equiv 39 \pmod{101}$ | $b = 7$ | the tens digit of every witness is 7 |
| $a + c = 3$, $a \ge 1$ | $(a,c) \in \{(1,2),(2,1),(3,0)\}$ | exactly three digit patterns |
| $\operatorname{rev}(370) = 73$, not 730 | $k = 370$ | a trailing zero still produces a valid witness |

The three patterns are the complete witness set $\{172, 271, 370\}$: the first
hit of the ascending scan, its reversal, and the pattern whose units digit is
zero. This is why the official explanation can name $172 + 271 = 443$ without
enumerating anything — the modular equation forces the answer.

---

## 6. Boundary behaviour across the whole input range

| Target `num` | Witness set | Outcome | Why |
|---|---|---|---|
| `0` | $\{0\}$ | `true` | the candidate `0` is admissible and $\operatorname{rev}(0) = 0$ |
| `1` | $\emptyset$ | `false` | candidates `0` and `1` give 0 and 2; the interval is exhausted |
| `10` | $\{5\}$ | `true` | $5 + 5 = 10$; no two-digit candidate divides as $11 \nmid 10$ |
| `63` | $\emptyset$ | `false` | odd target rules out one-digit candidates, and $11 \nmid 63$ |
| `181` | $\{140\}$ | `true` | the reversed form `"041"` parses back to 41 |
| `200` | $\emptyset$ | `false` | no $b$ makes $200 - 20b$ a multiple of 101, and $11 \nmid 200$ |
| `443` | $\{172, 271, 370\}$ | `true` | $b = 7$, $a + c = 3$ from the column equation |
| `666` | $\{135, 234, 333, 432, 531, 630\}$ | `true` | $b = 3$, $a + c = 6$ gives six palindromic-partner patterns |
| `100000` | $\emptyset$ | `false` | worst case: all 100 001 candidates are tested before failing |

The last row is the cost ceiling of the method: the largest legal target forces
a complete failed sweep, which is still fast because each candidate costs one
digit reversal.

---

## 7. Why the enumeration is correct

**Soundness (no false positives).** The equality test is evaluated exactly on
the number the reversal function defines, so a `true` result always names a
genuine non-negative $k$ whose sum with its own reversal equals the target. The
certified prefix is discarded at that moment, but the witness itself is the
proof.

**Completeness (no false negatives).** Suppose some non-negative $w$ satisfies
$w + \operatorname{rev}(w) = \texttt{num}$. Since $\operatorname{rev}(w) \ge 0$
we get $w \le \texttt{num}$, so $w$ sits inside the scanned interval. The scan
either reaches $w$ and returns `true`, or it has already returned `true` at some
smaller candidate. A `false` report is therefore only possible after every
integer in $[0, \texttt{num}]$ has been rejected, and the interval bound shows
nothing outside it could have succeeded.

The invariant and the terminating condition together prove that a report of
`false` means the witness set is empty, and that a report of `true` is witnessed
by the very candidate that triggered it.

---

## 8. Alternative methods and their trade-offs

| Method | How it decides | Time | Auxiliary space | Verdict |
|---|---|---|---|---|
| Ascending scan with string reversal | test each $k \le \texttt{num}$ against one reversal | $O(\texttt{num} \cdot D)$ | $O(D)$ for one digit buffer | the exact method used; simplest correct bound |
| Ascending scan with arithmetic reversal | peel digits with `% 10` and integer division | $O(\texttt{num} \cdot D)$ | $O(1)$ | same asymptotics, no temporary string |
| Column and carry analysis | solve $101(a+c) + 20b = \texttt{num}$ and its two-digit analogue | $O(D)$ | $O(1)$ | far faster, but each digit-length case must be derived separately |
| Precomputed reachable set | build every value $k + \operatorname{rev}(k)$ once, then answer in $O(1)$ | $O(\texttt{num} \cdot D)$ to build | $O(\texttt{num})$ stored values | only pays off across many queries, not one |

The string-reversal scan is chosen because $\texttt{num} \le 10^{5}$ makes
$10^{5}$ digit reversals trivial, whereas the column analysis of Section 5 needs
a fresh case distinction for every digit length.

---

## 9. Complexity derivation: time and auxiliary space

Let $N = \texttt{num}$ and let $D = \lfloor \log_{10}(N+1) \rfloor + 1$ be the
number of decimal digits of the target.

**Time.** The candidate interval contains at most $N + 1$ integers. Reversing the
decimal digits of one candidate touches each of its digits a constant number of
times, at most $D$, and the equality test is a constant-time integer comparison.
The worst case — a target with no witness, such as `100000` — tests all $N+1$
candidates and never short-circuits, giving

$$
O\big((N+1) \cdot D\big) = O(N \log N).
$$

Short-circuiting only improves the constant: for `443` the scan stops at
candidate `172` after 173 tests, and for `181` it stops at 140.

**Auxiliary space.** The scan keeps the current candidate, its reversed digit
buffer, and one comparison result; no accumulator array or memo table is built.
Peak auxiliary memory is one $D$-digit buffer, that is

$$
O(D) = O(\log N),
$$

which is $O(1)$ in the machine-integer model when $N$ is bounded by $10^{5}$ but
correctly scales with the digit count when the target is treated as an
arbitrary-precision integer.

---

## 10. Traps this instance exposes

- **Padding the reversed string:** treating `"041"` as a fixed-width string
  instead of the integer 41 would reject `181` and hide the witness `140`.
- **Assuming the witness sits near $\texttt{num}/2$:** for `443` the first
  witness is `172`, below half, while `271` and `370` are above it.
- **Assuming the two addends must be equal:** only palindromic candidates such
  as `55` give a doubled value; `172 + 271` is the ordinary case.
- **Stopping a `false` verdict early:** `1` and `63` are decided only after the
  whole interval is exhausted.
- **Forgetting the zero candidate:** `0` is a legal non-negative integer and is
  the unique witness for `num = 0`.
- **Treating $k$ and $\operatorname{rev}(k)$ as one candidate:** they are two
  distinct integers in the interval, which is why `443` has three witnesses
  rather than two.
- **Confusing the input space with the output space:** the target is a single
  integer, while the search space is the whole interval $[0, \texttt{num}]$.
