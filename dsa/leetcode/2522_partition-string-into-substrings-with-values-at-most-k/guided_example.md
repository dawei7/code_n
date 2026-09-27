# Guided Example: Partition String Into Substrings With Values at Most K

## 1. The Instance and the Requirement

We are given a string of decimal digits, each of them from `1` to `9`, together with a threshold $k$. A partition cuts the string into contiguous substrings so that every digit belongs to exactly one piece, and a partition is *good* when the integer value of every piece is at most $k$. We must return the **minimum** number of pieces in a good partition, or `-1` when no good partition exists.

We work the first official instance:

- `s` = `"165462"`
- `k` = `60`

The required output is `4`. This instance is chosen because it contains a local decision that punishes the wrong instinct: at the very start the prefix `"165"` has value $165 > 60$ and is forbidden, so the first piece can be at most `"16"`. Later, after the piece `"54"`, the greedy boundary appears again when the two digits `"62"` exceed the threshold and must be split into `"6"` and `"2"`. A method that always splits as early as possible also produces a *good* partition — into six single digits — but that partition uses six pieces and is not minimal. The whole lesson is about why taking the **longest** legal piece at each step is safe.

## 2. Substring Values and the Prefix Family

The value of a piece is its decimal interpretation. For a piece covering positions $i$ through $j-1$, define

$$V(i, j) = \sum_{t=i}^{j-1} s[t] \cdot 10^{\,j-1-t},$$

where each character is interpreted as a digit. Extending a piece by one character on the right is Horner's rule:

$$V(i, j+1) = 10 \cdot V(i, j) + \mathrm{digit}(s[j]),$$

so the running value of a piece can be maintained with one multiplication and one addition per appended character, without ever re-reading the earlier characters.

Two structural facts follow from the guarantee that **no digit is `0`**, and both are essential:

1. **Strict monotonicity.** Extending a piece multiplies its value by ten and adds at least $1$, so $V(i, j+1) > V(i, j)$ for every extension. The values of the prefixes of the remaining string therefore form a strictly increasing sequence, and each fixed start position has a unique longest feasible prefix — no ties, no plateaus, no ambiguity about where to stop.
2. **Suffix dominance.** Removing the leading digit of a $d$-digit number with no zero digits strictly decreases its value: the remaining at most $d-1$ digits form a number below $10^{\,d-1}$, while the original is at least $10^{\,d-1}$. Consequently, any *suffix* of a feasible piece is itself feasible.

The second fact is not a curiosity; it is the engine of the optimality proof in section 6. With zeros allowed it would fail (`"10"` has value $10$ but its suffix `"0"` has value $0$, and worse, `"05"` and `"5"` would collide), which is why the constraint that digits run from `1` to `9` is doing real work.

## 3. Feasibility: Exactly When `-1` Is Forced

A single digit is the finest possible piece, so if every digit is at most $k$ then splitting into single characters is already a good partition, using exactly $n$ pieces where $n = \texttt{s.length}$. Conversely, if some digit $d > k$, every piece containing that character covers a contiguous block whose value is at least $d$ — because appending digits to a nonzero leading digit only grows the value — so no good partition exists. Hence:

$$\text{a good partition exists} \iff \max_i \mathrm{digit}(s[i]) \le k.$$

| String | $k$ | Largest digit | Feasible? | Reason |
|:---|:---:|:---:|:---|:---|
| `"165462"` | 60 | 6 | yes | Even the six-digit single-split needs values at most $6 \le 60$. |
| `"238182"` | 5 | 8 | no | Digit `8` alone exceeds $k = 5$; every piece containing it is worse, so the answer is `-1`. |
| `"999"` | 9 | 9 | yes | Equality is allowed, so the three single digits are each legal. |
| `"123456"` | 1000 | 6 | yes | Feasible, and the longest legal prefixes are three digits long. |
| `"999999999"` | 1000000000 | 9 | yes | The entire string has value $999999999 \le 10^{9}$, so one piece suffices. |

The check $\max_i \mathrm{digit}(s[i]) \le k$ is worth stating separately for two reasons: it proves that the greedy method can never get stuck (every step has at least the single digit available), and it explains the only source of the `-1` answer. A greedy scan that discovers infeasibility mid-way would be harder to reason about than a one-line pre-condition.

## 4. The Greedy Extension Trace

The method fixes the start of the current piece and extends it as far as the threshold permits, maintaining the running value by Horner's rule. When the next digit would push the value above $k$, the piece is closed at the previous position and a new piece begins at that digit. No backtracking is performed, and the decision to stop is forced: once $V(i, j) > k$, every longer piece from the same start is even larger, so the whole extension family is eliminated at once.

Tracing `"165462"` with $k = 60$, start positions are $0$-indexed:

| Piece # | Start index | Value after 1 digit | Value after 2 digits | Value after 3 digits | Extension verdict | Piece chosen | Its value |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | 0 | 1 | 16 | 165 | third digit exceeds $k$ | `"16"` | 16 |
| 2 | 2 | 5 | 54 | 546 | third digit exceeds $k$ | `"54"` | 54 |
| 3 | 4 | 6 | 62 | — | second digit exceeds $k$ | `"6"` | 6 |
| 4 | 5 | 2 | — | — | end of string reached | `"2"` | 2 |

Reading the table row by row:

- **Piece 1.** `"1"` and `"16"` are legal; `"165"` is not. The greedy choice is the longest legal prefix, namely `"16"`. Note that `"16"` is not required — the piece could legally be `"1"` — and the next section shows why taking the longer one never costs anything.
- **Piece 2.** Starting at index $2$, the values are $5$, then $54$ (legal, since $54 \le 60$), then $546$ (illegal). The piece is `"54"`. This is the interesting step: the digit `6` that follows could have been appended to make `"546"` only if the threshold were larger, and it cannot.
- **Piece 3.** Starting at index $4$, the very second digit already breaks the budget: `62 > 60`. The piece must be the single digit `"6"`. This is the step where an implementation that assumed "pieces are always as long as possible, so let us grab two digits" would produce an illegal piece.
- **Piece 4.** Only the final character remains, and a single digit is always legal under the feasibility condition, so the last piece is `"2"`.

A subtle point about the failing appends: the digit that breaks a piece is not consumed. It becomes the first digit of the next piece, and the running value is reset to it. In the trace, the `6` at index $4$ fails as the third digit of piece 2 and immediately opens piece 3 with value $6$; nothing is lost and no digit is skipped.

## 5. The Resulting Partition and Its Cost

The four pieces and the threshold check:

| Piece | Index range | Value | $\le k = 60$? | Characters consumed so far | Pieces so far |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"16"` | 0 to 1 | 16 | yes | 2 | 1 |
| `"54"` | 2 to 3 | 54 | yes | 4 | 2 |
| `"6"` | 4 to 4 | 6 | yes | 5 | 3 |
| `"2"` | 5 to 5 | 2 | yes | 6 | 4 |

Every digit is in exactly one piece, every value is at most $60$, and the count is $4$, matching the required output. Comparing against the alternatives that a learner might reach for:

| Candidate partition | Pieces | Values | Good? | Comment |
|:---|:---:|:---|:---:|:---|
| `"1","6","5","4","6","2"` | 6 | all single digits | yes | The finest partition: always legal, never minimal. |
| `"1","6","54","6","2"` | 5 | $1, 6, 54, 6, 2$ | yes | Splits the first piece too early; one piece wasted. |
| `"16","5","4","6","2"` | 5 | $16, 5, 4, 6, 2$ | yes | Splits the second piece too early; one piece wasted. |
| `"16","54","6","2"` | 4 | $16, 54, 6, 2$ | yes | The greedy result, and the optimum. |
| `"165","462"` | 2 | $165, 462$ | no | Two pieces, but both exceed $60$; a coarse partition is not automatically disqualified only by its length — it must be legal. |

The last row is the mirror-image mistake: counting pieces is only meaningful among *good* partitions, and `"165"` is not a legal piece at all. The row above it is the greedy answer, and the two rows above that are the same answer with a piece needlessly subdivided. Every deviation from greedy that stays legal costs at least one extra piece.

## 6. Correctness: The Exchange Argument and the Greedy Invariant

**Greedy invariant.** Before each step, the pieces already emitted form a good partition of a prefix of $s$, and the current piece starts at the first unpartitioned character.

The invariant is maintained trivially: a piece is emitted only after its running value has been checked against $k$, and the next piece always starts at the character that failed to extend it, so the emitted pieces cover a prefix exactly and use only legal values.

**Optimality by exchange.** Let the greedy piece at some step be $P$, covering positions $i$ through $j-1$ with $V(i,j) \le k$, and suppose it is maximal, meaning $V(i, j+1) > k$ or $j = n$. Consider any good partition of the remaining suffix $s[i..n-1]$; its first piece $Q$ is a prefix of that suffix with $V(i, \ell) \le k$ for some $\ell \le j$. Replace $Q$ with $P$ and keep every later piece. The pieces after $Q$ now cover $s[\ell..n-1]$, and because $\ell \le j$, what they cover inside the longer first piece is the *tail* of $P$, a suffix of a feasible piece. By the suffix dominance property of section 2, that tail is feasible on its own. Truncating the later pieces in this way leaves a good partition of $s[j..n-1]$ that uses **no more** pieces than the original partition of $s[i..n-1]$ did.

Applying the exchange at every step shows by induction that the greedy partition uses at most as many pieces as any good partition of the whole string. Since the greedy partition is itself good, it is optimal — and this is why the choice of the *longest* legal piece is never a mistake, while a shorter legal piece is never better.

**Termination and feasibility.** Each piece consumes at least one character, so the procedure terminates after at most $n$ steps. Because the feasibility condition of section 3 guarantees that every single digit is legal, the extension loop always advances by at least one character and the method never stalls; when the condition fails, the answer `-1` is reported before any greedy work begins. The returned count is therefore the minimum number of pieces in a good partition, or `-1` when none exists.

## 7. Traps and Boundary Behaviour

| Scenario | Instance | What the method does | Result | Why the rule still holds |
|:---|:---|:---|:---:|:---|
| one feasible digit | `s = "1"`, `k = 1` | single piece, value $1 \le 1$ | 1 | The minimum is at least one piece for a nonempty string, and one piece achieves it. |
| every digit at the limit | `s = "999"`, `k = 9` | `"99" = 99 > 9`, so each digit stands alone | 3 | Equality at the threshold is legal for a single digit but two digits already exceed it. |
| two maximal pieces | `s = "123456"`, `k = 1000` | `"123"` has value 123, `"1234"` has 1234, so the piece closes at three digits; then `"456"` | 2 | Pieces are limited by the digit count of $k$, not by a fixed length; here each piece is three digits. |
| a short remainder | `s = "11111"`, `k = 11` | `"11"` has value 11 and `"111"` has 111, so two digits per piece, twice, then the leftover `"1"` | 3 | A short final piece can be forced, which is why the count cannot be computed as a division. |
| whole string fits | `s = "999999999"`, `k = 1000000000` | the entire value $999999999 \le 10^{9}$ | 1 | One piece is the global minimum for any nonempty string. |
| an impossible digit | `s = "238182"`, `k = 5` | digit `8` exceeds $k$ | -1 | No piece containing `8` can be feasible, so the pre-condition fails immediately. |
| a `0` digit (outside the constraints) | `s = "105"`, `k = 1` | `"10"` has value ten, and suffix `"0"` has value zero | — | The suffix dominance property collapses without the no-zero guarantee; the greedy argument would need restating. |
| threshold just one below a prefix | `s = "165462"`, `k = 60` | `"165" = 165 > 60`, so the piece stops at `"16"` | — | Feasibility is a value comparison, not a length comparison; a first digit of `1` does not license a long piece. |
| values exceed the machine word | `s` of length $10^{5}$, $k = 10^{9}$ | the running value is abandoned as soon as it exceeds $k$ | — | Because the extension stops at the first violation, the running value never exceeds $10k$, so no overflow-prone large integer is ever built. |

Two traps are worth stating plainly. First, **never assume a fixed piece length**: the legal length depends on the leading digits as well as on $k$, so the number of pieces is not $\lceil n / L \rceil$ for any fixed $L$. Second, **do not stop at the first piece that is legal**: the shortest legal piece is always legal, so any stopping rule that ignores the threshold produces a good but non-minimal answer. Greedy pushes each piece to its maximal legal length for exactly that reason.

## 8. Complexity: Time and Auxiliary Space

**Time.** Each appended character costs one multiplication, one addition and one comparison. A piece grows only while its running value stays at most $k$, and because every digit is at least `1`, a piece with $L$ digits has value at least $10^{\,L-1}$; so $10^{\,L-1} \le k$, giving

$$L \le \lfloor \log_{10} k \rfloor + 1 \le 10 \quad \text{under } k \le 10^{9}.$$

The digits failing an extension are not wasted: the failing digit opens the next piece, so the total number of extension attempts is at most $L$ per piece and the pieces partition the string. Hence

$$T(n) = \mathrm{O}(n \cdot L) = \mathrm{O}(n),$$

since $L$ is bounded by the constant $10$ for the stated ceiling on $k$. In particular the method is a single left-to-right pass: no suffix is ever revisited, and no table of subproblem answers is filled.

**Auxiliary space.** The scan keeps only the current running value, the index marking the start of the current piece, and the piece counter — all integers whose size depends on $k$, not on $n$. So

$$S_{\text{aux}}(n, k) = \mathrm{O}(1).$$

This is the sharpest advantage of the greedy formulation over a memoized search over split points, which stores one entry per position and therefore uses $\mathrm{O}(n)$ extra memory, and over a recursive formulation, whose call depth also grows with $n$ and can exhaust the stack for a string of length $10^{5}$.

## 9. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Greedy longest feasible piece | Extend the current piece until the threshold is about to break, then start a new piece. | $\mathrm{O}(n)$ time, $\mathrm{O}(1)$ space | The preferred method: one pass, no auxiliary table, and optimal by the exchange argument of section 6. |
| Split into single digits | Emit every character as its own piece. | $\mathrm{O}(n)$ time, $\mathrm{O}(1)$ space | Always legal when a solution exists, but gives the maximum number of pieces and is therefore never minimal unless every two-digit prefix exceeds $k$. |
| Memoized search over split points | Let $f(i)$ be the minimum pieces for the suffix starting at $i$, and try every feasible first piece. | $\mathrm{O}(n \cdot L)$ time, $\mathrm{O}(n)$ space | Correct and a useful way to *verify* the greedy result, but it stores a table for the whole suffix space and needs a recursion or an explicit stack. |
| Full dynamic programming over all splits | Consider every pair of cut points and minimize. | $\mathrm{O}(n^{2})$ time | Correct but quadratic; it also has to represent piece values, which grow beyond machine words for long pieces. |
| Split as early as possible | Take the shortest legal piece at each step. | $\mathrm{O}(n)$ time | Produces a good partition with too many pieces; the instance above needs six pieces instead of four. |
| Any nonzero `0` handling based on leading zeros | Treat `"05"` and `"5"` as one value class. | — | The constraint removes `0` from the input precisely so that values are monotone under extension and truncation; a variant allowing `0` needs a different argument. |

The transferable idea is the shape of the exchange: when a feasible choice is a prefix and *every suffix of a feasible prefix is also feasible*, extending the prefix can only shrink the remaining problem, so the longest feasible prefix is safe. That condition — monotonicity of value under extension together with inheritance under truncation — is exactly what the no-zero digit guarantee buys here.