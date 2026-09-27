# Guided Example: Closest Fair Integer

The representative instance is `n = 403`, whose required answer is `1001`. It is chosen because `403` has three digits and *no* fair integer can have three digits at all, so the lesson must derive why a whole length class is impossible and how to build the smallest fair integer of the next admissible length. A second worked case, `n = 100000`, exposes the other half of the method: the ascending repair walk that an even-length input requires.

## 1. The Rule and the Traced Instance

An integer $k$ is **fair** when the number of even digits in its decimal representation equals the number of odd digits. Parity is decided per digit, and `0` counts as an **even** digit, so `10` is fair with one odd and one even digit. Leading zeros never occur, because $k$ is written in ordinary decimal notation.

Writing $d$ for the digit count of $k$, and $a$, $b$ for its odd-digit and even-digit counts,

$$
d = a + b,
\qquad
k \text{ is fair} \iff a = b .
$$

The task is the smallest fair $k$ with $k \ge n$, where $1 \le n \le 10^{9}$. For `n = 403` the counts are $a = 1$ (the digit `3`) and $b = 2$ (the digits `4` and `0`), so `403` is not fair:

| Position (most significant first) | Digit | Digit parity | Running $a$ | Running $b$ | Fair so far? |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `4` | even | 0 | 1 | no — one even digit is unopposed |
| 2 | `0` | even | 0 | 2 | no — two even digits are unopposed |
| 3 | `3` | odd | 1 | 2 | no — $a = 1 \ne 2 = b$ |

The table shows something no amount of incrementing can change: with $d = 3$ the two counts must add to `3`, an odd number, so they can never be equal.

## 2. Odd Lengths Admit No Fair Integer

Because $a = b$, the digit count is twice the odd-digit count:

$$
d = a + b = 2a .
$$

This is the pivotal fact of the problem, stated as a lemma.

> **Lemma (length parity).** If $k$ is fair, then $k$ has an even number of digits.

Its contrapositive is what the instance uses: a three-digit integer has $d = 3$, and $2a$ is never `3`, so no three-digit integer is fair. The feasibility census makes the pattern unmistakable, and its last three columns are computed by enumerating each length:

| Digit count $d$ | Parity of $d$ | Fair $d$-digit integer exists? | Smallest | Largest | Count |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | odd | no | — | — | 0 |
| 2 | even | yes | `10` | `98` | 45 |
| 3 | odd | no | — | — | 0 |
| 4 | even | yes | `1001` | `9988` | 3375 |
| 5 | odd | no | — | — | 0 |

For `n = 403` the answer cannot have three digits, and it cannot have one or two digits either, since those are smaller than `403`. The smallest admissible length is exactly four, so the search collapses to "the smallest fair four-digit integer".

## 3. Building the Smallest Fair Integer of the Next Even Length

With $d = 3$, the next length of even parity is $d + 1 = 4$, so the target counts are $a = b = (d+1)/2 = 2$. The smallest four-digit numeral with those counts is built greedily from the most significant position, because equal-length numerals compare lexicographically.

| Position | Quotas still owed | Digit placed | Reason |
|:---:|:---|:---:|:---|
| 1 | 2 odd, 2 even; no leading zero | `1` | `1` is the smallest legal leading digit and it is odd, spending one odd slot |
| 2 | 1 odd, 2 even | `0` | `0` is the smallest digit and it is even; two positions remain, enough for the one odd digit still owed |
| 3 | 1 odd, 1 even | `0` | placing the second even digit here leaves exactly one position for the final odd digit |
| 4 | 1 odd, 0 even | `1` | the odd quota must be filled, and `1` is the smallest odd digit |

The greedy sequence is `1, 0, 0, 1`, giving $k = 1001$ with $a = 2$ and $b = 2$; the census confirms it is the smallest four-digit fair integer. The construction has a closed form: for odd $d$, the answer is

$$
10^{d} + \underbrace{11\cdots1}_{(d-1)/2 \text{ ones}} = 10^{d} + \frac{10^{(d-1)/2} - 1}{9},
$$

that is, the numeral `1`, then $(d+1)/2$ zeros, then $(d-1)/2$ ones. Substituting $d = 3$ gives $10^{3} + 1 = 1001$; $d = 1$ gives $10 + 0 = 10$; $d = 9$ gives $10^{9} + 1111 = 1000001111$. The leading `1` is *forced* to be odd — it is the smallest legal leading digit — which is exactly why the even digits (zeros) come before the odd ones (ones). And the formula answers a narrower question than the original: it builds the smallest fair integer of length $d+1$, which is automatically smaller than every fair integer with more digits, so no longer candidate can undercut it.

## 4. The Repair Walk for an Even-Length Input

The complementary case is an even-length input that is not fair. For `n = 100000` the digit count is $d = 6$ and the counts are $a = 1$, $b = 5$, so `100000` is unfair. No length jump is available, because the current length is already admissible; the answer must be the first fair integer at or above `100000`, found by examining consecutive integers upward.

| Round | Value examined | Odd $a$ | Even $b$ | Fair? | Action |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `100000` | 1 | 5 | no | advance |
| 1 | `100001` | 2 | 4 | no | advance |
| 2–8 | `100002` … `100008` | alternates 1/5 and 2/4 | alternates 5/1 | no | advance (see explanation below) |
| 9 | `100009` | 2 | 4 | no | advance |
| 10 | `100010` | 2 | 4 | no | advance |
| 11 | `100011` | 3 | 3 | **yes** | return `100011` |

The oscillation is not random. Every value from `100000` to `100009` shares the four-digit prefix `1000`, whose own counts are one odd and three even — a deficit of two odd digits. The final position contributes at most one odd digit, so no value in that block can close the gap, and the odd count flips between `1` and `2` as the last digit alternates parity. Rounds `2`–`8` therefore add nothing structural: they repeat the flips already recorded at rounds `1` and `9`. Only when the tens position changes does the trailing pair become `11`, giving `100011` with the required three-and-three split.

This is the structure the method exploits: **increment by one and re-count**, never skipping, because fair integers of a given length are not equally spaced. The block `100000`–`100009` contains none of them, while a block starting at a length boundary contains one immediately.

## 5. Boundary Behaviour

| Instance $n$ | $d$ | Parity of $d$ | $(a, b)$ | Branch applied | Answer | Why it is correct |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| `1` | 1 | odd | $(1, 0)$ | length jump | `10` | no one-digit integer is fair; `10` is the smallest fair integer of all |
| `2` | 1 | odd | $(0, 1)$ | length jump | `10` | the official example; `10` has one digit of each parity |
| `11` | 2 | even | $(2, 0)$ | walk, 1 round | `12` | `12` has one digit of each parity |
| `98` | 2 | even | $(1, 1)$ | already fair | `98` | the input itself satisfies $a = b$, so nothing larger is minimal |
| `99` | 2 | even | $(2, 0)$ | walk, 1 round | `1001` | `100` has three digits, so the walk crosses into the length jump, which returns `1000 + 1` |
| `403` | 3 | odd | $(1, 2)$ | length jump | `1001` | the traced instance |
| `100000` | 6 | even | $(1, 5)$ | walk, 11 rounds | `100011` | traced in Section 4 |
| `123456789` | 9 | odd | $(5, 4)$ | length jump | `1000001111` | $10^{9} + 1111$ by the closed form |
| `1000000000` | 10 | even | $(1, 9)$ | walk, 1111 rounds | `1000001111` | the walk reaches a ten-digit value with five digits of each parity |

The `n = 99` row is the most instructive: the walk does **not** stop at the end of the two-digit range, it crosses into `100`, and that crossed value has an odd digit count, so the length jump ends the process in one step. Without that branch the walk would have had to test values up to the next fair integer of an even length, which is far above.

## 6. Invariant, Termination, and Correctness

Both branches must be shown **sound** (the returned value is fair and at least $n$) and **minimal** (no smaller fair value is at least $n$).

**Length jump (odd $d$).** By the lemma, no fair integer has $d$ digits, and any number with fewer than $d$ digits is below $n$. Every fair $k \ge n$ therefore has at least $d + 1$ digits, and since $d$ is odd the smallest even length that is at least $d$ is exactly $d + 1$. Integers with more digits exceed every $(d+1)$-digit integer, so it suffices to minimize over numerals of length $d+1$. The greedy table picks the smallest digit at each position that keeps the remaining parity quotas satisfiable — precisely lexicographic minimization — so the constructed numeral is the smallest fair integer of length $d+1$, and hence the smallest fair integer $\ge n$. Soundness holds because the construction places exactly $(d+1)/2$ digits of each parity.

**Repair walk (even $d$).** The walk classifies $n, n+1, n+2, \dots$ in increasing order, returning a value only after its counts match, so the result is fair and at least $n$. It is minimal because the tested values are consecutive and none is skipped; the maintained invariant is:

> after each round, every integer in $[n, v]$ has been classified and none is fair, where $v$ is the value just tested.

The first round establishes it for $v = n$, and each round extends the classified interval by exactly one value. When a value is classified fair, it is the minimum of $\{k \ge n : k \text{ is fair}\}$.

**Termination.** Each length class contains finitely many values, and once the walk passes $10^{d}$ the current value has $d + 1$ digits; since $d$ is even here, $d + 1$ is odd, so the length jump returns a closed-form value immediately. The walk therefore either finds a fair integer of the current length or crosses the boundary, which is settled in one step. Neither branch can loop, and the two branches are exhaustive because every digit count is either odd or even.

## 7. How Long the Repair Walk Can Be

The walk is the only non-constant cost, so its length deserves an answer. Inputs whose leading digits read `1999…` are the worst: such a prefix holds a surplus of odd digits that the low-order positions cannot cancel, so the walk must carry the prefix up to `2000…` before the trailing positions can be filled with ones.

| Even digit count $d$ | Longest unfair window | Instance | Answer reached | Evidence |
|:---:|:---:|:---:|:---:|:---|
| 2 | 2 rounds | `19` | `21` | exhaustive over all two-digit inputs |
| 4 | 22 rounds | `1989` | `2011` | exhaustive over all four-digit inputs |
| 6 | 222 rounds | `199889` | `200111` | exhaustive over all six-digit inputs |
| 8 | 2222 rounds | `19998889` | `20001111` | verified at the pattern instance |
| 10 | 22222 rounds | `1999988889` | `2000011111` | verified at the pattern instance |

The sequence $2, 22, 222, 2222, 22222$ equals $2 \cdot (10^{d/2} - 1)/9$, so the longest walk for a $d$-digit input grows like $10^{d/2}$ — far smaller than the $10^{d}$ values in the length class, but not constant. For the contract's range the worst walk observed is `22222` rounds; by contrast `1000000000`, the largest legal input, needs only `1111`, and every odd-length input needs none.

## 8. Alternative Formulations

| Alternative | Work performed | Cost | Trade-off against the two-branch method |
|:---|:---|:---|:---|
| Increment by one and re-count, with no length shortcut | test every integer upward until fair | for odd $n$ up to $10^{d}$ integers away | sound and simple, but gives up the closed form that makes odd lengths immediate |
| Enumerate all fair integers of each length in order | generate candidates length by length | up to $O(10^{d})$ candidates per length | never better than the walk, and it also considers candidates below $n$ |
| Digit dynamic programming over positions and the odd-digit count | choose digits position by position under a parity budget | $O(d^{2})$ states | the fully general construction, and the right answer for a "smallest number with a digit-count condition" variant, but a whole DP overkill here |
| Length-jump closed form plus ascending walk | classify once, then build `1 0…0 1…1` or walk | $O(d)$ for odd lengths, $O(T \cdot d)$ for even lengths | chosen: each branch is exact and the costly branch is provably short |

Two tempting errors are worth naming. First, **returning `n` whenever the digit count is even** is wrong — `100000` in Section 4 is a counterexample. Second, treating `0` as neither even nor odd breaks the definition: `0` is even, and misclassifying it would make `10` unfair and shift every answer upward.

## 9. Complexity Derivation

Let $d$ be the digit count of $n$ (so $d \le 10$ because $n \le 10^{9}$) and let $T$ be the number of repair rounds in the even-length branch.

**Classification.** Counting odd and even digits is one pass over $d$ digits with two counters: $O(d)$ time and $O(1)$ auxiliary state, repeated once per value examined.

**Odd-length branch.** The closed form $10^{d} + (10^{(d-1)/2}-1)/9$ is built with no search once the classification is done, so the branch costs $O(d)$ overall.

**Even-length branch.** Each round classifies one $d$-digit value in $O(d)$ time over consecutive integers, so the branch costs $O(T \cdot d)$. The window size $T$ is bounded by the integers between $n$ and $10^{d}$, and the empirical maxima of Section 7 follow $2 \cdot (10^{d/2}-1)/9$. For the contract's range, $T \le 22222$, so the worst-case work is about $22222 \times 10 = 2.2 \times 10^{5}$ digit inspections — small, and far below the $10^{10}$ values in the ten-digit class.

**Total time.** $O(d)$ when $d$ is odd or when $a = b$, and $O(T \cdot d)$ otherwise. The asymmetry is the point: the length shortcut turns the worst structural case into constant work, leaving only the even-length repair proportional to a window size.

**Auxiliary space.** The counters $a$, $b$ and the digit count occupy a fixed number of scalars, so the auxiliary space is $O(1)$ beyond the input. One nuance: expressing the walk by recursive descent adds $O(T)$ call frames for a long window (`22222` in the worst legal case), whereas an iterative walk stays at $O(1)$.

**Summary.** Classify the digits once; if the digit count is odd, answer with the closed-form numeral; if it is even and the counts already match, answer with the input itself; otherwise walk upward one value at a time until the counts match or the length boundary is crossed.