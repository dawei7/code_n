# Guided Example: Smallest Even Multiple

The representative instance for this lesson is `n = 5`, whose required answer is `10`. It is chosen because the first candidate that comes to mind, `n` itself, is rejected by one of the two divisibility requirements, so the solver must decide *which* multiple to take rather than scan a range.

## 1. The Instance and What It Asks For

The contract supplies a positive integer `n` and asks for the smallest positive integer that is a multiple of **both** `2` and `n`. Two divisibility tests therefore have to pass simultaneously:

$$
2 \mid x \quad\text{and}\quad n \mid x .
$$

For `n = 5` the value `5` is a multiple of `5` but not of `2`, because `5 % 2 = 1`. The value `10` is a multiple of both, since `10 = 2 \cdot 5` and `10 = 5 \cdot 2`. Nothing between them qualifies, so `10` is the answer. The interesting question is not *whether* `10` works, but *why no smaller positive integer can*.

## 2. The Candidate Set Is Exactly the Multiples of n

Every common multiple of `2` and `n` is, in particular, a multiple of `n`, so the search space is contained in

$$
M(n) = \{\, m \cdot n : m \in \mathbb{Z}^{+} \,\} = \{\, n,\; 2n,\; 3n,\; \dots \,\}.
$$

This is the first structural fact the lesson relies on: the candidates can be enumerated by a single positive integer *multiplier* $m$, and they appear in strictly increasing order because $n > 0$ makes $m \mapsto m \cdot n$ strictly increasing. Asking for the smallest common multiple is therefore the same as asking for the **least admissible multiplier** $m$, and the answer is that multiplier times `n`.

Writing the first four candidates for `n = 5` and testing both divisibility requirements makes the elimination explicit:

| Multiplier $m$ | Candidate `m * n` | Multiple of `5`? | Multiple of `2`? | Common multiple of both? |
|:---:|:---:|:---:|:---:|:---:|
| 1 | `5` | yes | no (`5 % 2 = 1`) | no |
| 2 | `10` | yes | yes (`10 % 2 = 0`) | **yes — least** |
| 3 | `15` | yes | no | no |
| 4 | `20` | yes | yes | yes, but larger than `10` |

The table shows both halves of the argument at once: `m = 2` is admissible, and every smaller positive multiplier (`m = 1`) is not.

## 3. Why the Decision Collapses to a Parity Test

The second divisibility requirement depends only on the parity of the product $m \cdot n$. Since `2` is prime, $2 \mid m \cdot n$ holds if and only if $2 \mid m$ or $2 \mid n$. That single fact splits the problem into two exhaustive cases:

| Case | Parity of `n` | Is $m = 1$ admissible? | Least admissible multiplier | Answer | Witness for the instance |
|:---|:---|:---|:---:|:---:|:---|
| `n` is even | $2 \mid n$ | yes — `n` is already even | $m = 1$ | `n` | `n = 6` gives `6` |
| `n` is odd | $2 \nmid n$ | no — `n` is odd | $m = 2$ | `2n` | `n = 5` gives `10` |

In the even case, `n` is divisible by itself and by `2`, so `n` is a common multiple of the two inputs, and no positive multiple of `n` is smaller than `n` itself. Doubling an already even number would produce a common multiple that is strictly larger, hence not minimal.

In the odd case, a product of an odd number and an odd number is odd, so $m \cdot n$ is even exactly when $m$ is even. The smallest even positive multiplier is `2`, so `2n` is the first candidate that passes both tests. For `n = 5` the multiplier `1` fails and the multiplier `2` succeeds; `10` is therefore the least common multiple.

## 4. Step-by-Step Trace for `n = 5`

The table records the complete state of the decision at every stage. There is no array, no frontier and no accumulated table: the state is a small set of scalar facts, and each row either adds one derived fact or rejects one candidate.

| Step | Examined quantity | Value at `n = 5` | Rule applied | Decision after the step |
|:---:|:---|:---:|:---|:---|
| 1 | input `n` | `5` | contract guarantees $n \ge 1$, so no degenerate case is reachable | candidate family $M(n)$ is well defined and infinite upward |
| 2 | first candidate `n` | `5` | test $2 \mid n$, i.e. `n % 2 == 0` | fails, so the multiplier `1` is eliminated |
| 3 | required parity of the multiplier | multiplier must be even | product of two odd numbers is odd | multiplier `2` becomes the least survivor |
| 4 | candidate `2 * n` | `10` | re-test both conditions: `10 % 2 == 0`, `10 % 5 == 0` | `10` is confirmed as a common multiple |
| 5 | minimality of `m = 2` | `m = 1` already rejected | the candidates increase strictly in $m$ | no smaller positive common multiple exists; answer is `10` |

The trace finishes in five recorded observations, but the underlying work is one modulo test plus one multiplication. Steps 4 and 5 are *verification* of a candidate that step 3 already produced, not a search.

## 5. Boundary Behaviour Across the Legal Range

The constraint is $1 \le n \le 150$, so the parity rule has to be trusted at the extremes of that interval, not only in the middle. The following boundary analysis checks the rule against every structural special case the range contains.

| Boundary instance | Parity | Rule applied | Answer | Why nothing smaller works |
|:---|:---|:---|:---:|:---|
| `n = 1` | odd | return `2 * 1` | `2` | `1` is odd; `2` is the least positive even number, and it is a multiple of `1` |
| `n = 2` | even | return `n` | `2` | `2` is already a multiple of both inputs; the only smaller positive integer is `1`, which is not a multiple of `2` |
| `n = 3` | odd | return `2 * 3` | `6` | the multiples of `3` are `3, 6, ...`; `3` is odd |
| `n = 5` | odd | return `2 * 5` | `10` | the traced instance; `5` is odd |
| `n = 6` | even | return `n` | `6` | `6` is even and divisible by itself |
| `n = 128` | even | return `n` | `128` | a power of two is even, so the first candidate already passes |
| `n = 149` | odd | return `2 * 149` | `298` | `149` is odd; `298` is exactly one doubling |
| `n = 150` | even | return `n` | `150` | upper end of the range, and still even |

Two entries deserve emphasis. `n = 2` is the case where both branches would agree, which is a useful consistency check rather than a genuine ambiguity: the even branch returns `n = 2`, and the odd branch is simply not taken. `n = 1` is the smallest legal input, and it is *not* degenerate for this rule — the answer `2` is produced by the same odd-parity step used for `n = 149`. No special branch is needed at either end of the range.

## 6. Invariant and Correctness

Let $A$ be the set of positive common multiples of `2` and `n`. The lesson claims a single answer $a^{*}$ with two properties.

**Well-definedness.** *A* is non-empty: the candidate `2 * n` is divisible by `2` by construction, and it is divisible by `n` because it is a multiple of `n`. Since *A* is a non-empty subset of the positive integers, it has a least element. Every positive multiple of `n` is at least `n`, so $M(n)$ is bounded below and contains no infinite descending chain.

**Soundness of the returned value.** In the even case the returned value is `n`; `n` is divisible by `n` trivially and by `2` by hypothesis, so `n ∈ A`. In the odd case the returned value is `2 * n`; it is a multiple of `n` by construction and even because it carries the factor `2`, so `2 * n ∈ A`.

**Minimality of the returned value.** Because $m \mapsto m \cdot n$ is strictly increasing for $n > 0$, minimizing a common multiple is equivalent to minimizing its multiplier $m$. The invariant maintained by the case analysis is:

> at every point in the reasoning, the smallest multiplier that has not yet been eliminated is the one returned.

In the even case, `m = 1` is admissible and `1` is the least positive integer, so no multiplier below it exists to eliminate. In the odd case, step 2 eliminates exactly `m = 1`, and the parity argument shows that every admissible multiplier must be even; the least even positive integer is `2`, so `m = 2` is the smallest surviving multiplier and no admissible multiplier has been skipped. Combining soundness with minimality, the returned value is precisely $\min A$.

The rule also matches the general least-common-multiple identity, which is a useful independent check of the case split:

$$
\operatorname{lcm}(2, n) = \frac{2n}{\gcd(2, n)} =
\begin{cases}
n, & n \text{ even},\\[2pt]
2n, & n \text{ odd},
\end{cases}
$$

because $\gcd(2, n) = 2$ for even `n` and $\gcd(2, n) = 1$ for odd `n`. Substituting `n = 5` gives $\operatorname{lcm}(2,5) = 10$ and substituting `n = 6` gives $\operatorname{lcm}(2,6) = 6$, matching the traced outcomes.

## 7. Alternative Methods and Their Trade-offs

The instance also shows why the parity test is preferred over the general machinery. Each alternative below is genuinely correct; each is eliminated on cost or on clarity, not on wrongness.

| Alternative | Work performed | Correctness | Trade-off against the parity rule |
|:---|:---|:---|:---|
| Enumerate multiples `n, 2n, 3n, ...` until one is even | at most two candidates | sound | terminates after at most two trials, yet it presents a search where a parity proof suffices |
| Count upward from `n` until both divisibility tests pass | up to `n` candidate tests in the worst case | sound | makes the cost depend on the magnitude of `n` instead of being constant |
| General `gcd`-based formula $2n / \gcd(2,n)$ | one gcd plus one division | sound and fully general | correct at any modulus, but the extra arithmetic obscures the fact that only parity matters here |
| Parity rule with a conditional selection | one modulo test plus at most one multiplication | sound | chosen: constant work, and the proof is the code path |

There is one tempting simplification that is *wrong*: returning `2 * n` unconditionally. It fails immediately on `n = 6`, where it would return `12` while `6` is already a common multiple; the even branch is not optional.

## 8. Complexity Derivation

**Time.** The method performs one parity test `n % 2 == 0` and then at most one multiplication (`2 * n`). Both are single-word arithmetic operations that do not depend on the magnitude of `n`, so the running time is $O(1)$. This is the strongest possible bound for a problem whose input is a single scalar: no loop over the range $1 \le n \le 150$ is required, and the answer is produced by a fixed number of operations for every legal input.

**Auxiliary space.** The only extra storage is the handful of scalar temporaries used to hold the parity result and the computed candidate. No array, set, or table is allocated, and nothing is allocated that grows with `n`, so the auxiliary-space cost is $O(1)$.

## 9. Takeaway

The lesson of this instance is that "smallest integer satisfying two divisibility conditions" reduces to one binary observation about a prime factor. Because `2` is prime, the condition $2 \mid m \cdot n$ is decided by the parity of `n` alone, which collapses an unbounded search over multiples into a two-branch decision. The multiplier formulation generalizes: for a modulus `k` the same reasoning asks for the least `m` such that $k \mid m \cdot n$, which yields $m = k / \gcd(k, n)$.
