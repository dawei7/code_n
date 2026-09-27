# Guided Example: Distinct Prime Factors of Product of Array

## 1. The Instance and the Quantity Requested

We are given an array of integers, each at least $2$, and must report how many **distinct** primes appear in the complete prime factorization of the product of all the elements. Exponents do not matter: what matters is the *support* of the factorization, the set of primes that occur at least once.

We work the first official instance:

- `nums` = `[2, 4, 3, 7, 10, 6]`

The required output is `4`. The instance is worth tracing because it exercises three ideas at once: a prime factor that many elements share (`2` appears in four of the six elements), a composite that *introduces* a new prime mid-array (`10` is the only source of `5`), and an element that is itself prime (`7`). It also has enough elements that forming the product and factoring it would actually work — and that is precisely the trap, because the input bound of up to $10^{4}$ elements makes the product astronomically large and impossible to represent in fixed-width arithmetic.

## 2. Why the Product Is Never Formed

The fundamental theorem of arithmetic says every integer $x \ge 2$ has a unique expression

$$x = \prod_{p \in \mathbb{P}} p^{e_p(x)}, \qquad e_p(x) \ge 0,$$

where only finitely many exponents are nonzero; the support $\mathrm{supp}(x) = \{\, p : e_p(x) > 0 \,\}$ is the set of distinct primes dividing $x$. For a product of array elements the exponents add, because multiplication concatenates the prime multisets:

$$e_p\Big(\prod_{i} \texttt{nums[i]}\Big) = \sum_{i} e_p(\texttt{nums[i]}).$$

An exponent is positive exactly when at least one summand is positive, which gives the identity the whole solution rests on:

$$\mathrm{supp}\Big(\prod_{i} \texttt{nums[i]}\Big) = \bigcup_{i} \mathrm{supp}(\texttt{nums[i]}).$$

The union on the right is taken over at most $10^{4}$ sets, each of which has at most four elements under the bound $\texttt{nums[i]} \le 1000$ (since $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 = 2310 > 1000$). Nothing in that identity requires knowing the product, and no intermediate value ever exceeds $1000$. Forming the product instead would build an integer with more than thirty thousand decimal digits for a full-length input and would risk silent overflow in a fixed-width language — a failure mode that produces a plausible but wrong count rather than an error.

$$\mathrm{supp}\Big(\prod_{i} \texttt{nums[i]}\Big) = \{\, p \text{ prime} : p \text{ divides at least one } \texttt{nums[i]} \,\}.$$

## 3. Factorizing One Element by Trial Division

Factorizing a single value $x$ uses trial division with a bound that makes it complete. The loop walks candidate divisors $p = 2, 3, 4, \dots$ while $p \le \lfloor x/p \rfloor$, i.e. while $p^{2} \le x$. When $p$ divides the current cofactor, $p$ is recorded and *all* copies of it are removed before the loop continues. Whatever survives the loop is either $1$ or a single prime larger than $\sqrt{x}$.

The reason the bound is complete is the standard sieve argument: if the residual cofactor $r > 1$ were composite after the loop, it would have a prime factor $q \le \sqrt{r}$, and that $q$ would have been tested and removed. Hence a leftover greater than $1$ must be prime, and it belongs in the support.

Tracing the loop on the composite `1000` shows both mechanisms — exponent stripping and the residual prime:

| Candidate $p$ | Loop guard $p^{2} \le x$ | Cofactor $x$ | Test `x % p` | Action | $x$ after |
|:---:|:---:|:---:|:---:|:---|:---:|
| 2 | $4 \le 1000$ true | 1000 | 0 | record 2, divide out every copy | 125 |
| 3 | $9 \le 125$ true | 125 | 2 | no divisor, advance | 125 |
| 4 | $16 \le 125$ true | 125 | 1 | no divisor, advance | 125 |
| 5 | $25 \le 125$ true | 125 | 0 | record 5, divide out every copy | 5 |
| 6 | $36 \le 5$ false | 5 | — | loop ends on the guard | 5 |
| residual | — | 5 | — | $5 > 1$, record 5 | 1 |

The support of `1000` is $\{2, 5\}$, since $1000 = 2^{3} \cdot 5^{3}$. Two details in the table carry the correctness of the whole method. First, **candidate 4 is harmless**: after every copy of `2` has been removed, no even cofactor remains, so no composite candidate can ever divide the cofactor. Second, **the residual test is mandatory**: stopping at the loop guard alone would silently drop `5`, and with it an entire prime from the answer.

The loop also shrinks its own work: dividing out $2$ reduced the cofactor from $1000$ to $125$, so the later guard $p^{2} \le x$ fails much earlier than $p^{2} \le 1000$ would allow. Exponent stripping is therefore both a correctness requirement and the main speedup.

## 4. Factorizing Every Element of the Instance

Applying that procedure to each element independently, with no element influencing another:

| Index $i$ | `nums[i]` | Factorization | Support $\mathrm{supp}(\texttt{nums[i]})$ | Trial divisors actually tested |
|:---:|:---:|:---|:---|:---|
| 0 | 2 | $2^{1}$ | $\{2\}$ | guard fails immediately; residual 2 recorded |
| 1 | 4 | $2^{2}$ | $\{2\}$ | 2 divides; cofactor drops to 1; residual 1 ignored |
| 2 | 3 | $3^{1}$ | $\{3\}$ | guard $4 \le 3$ fails at once; residual 3 recorded |
| 3 | 7 | $7^{1}$ | $\{7\}$ | 2 tested (guard $4 \le 7$); residual 7 recorded |
| 4 | 10 | $2^{1} \cdot 5^{1}$ | $\{2, 5\}$ | 2 divides, cofactor 5; guard $9 \le 5$ fails; residual 5 |
| 5 | 6 | $2^{1} \cdot 3^{1}$ | $\{2, 3\}$ | 2 divides, cofactor 3; guard $4 \le 3$ fails; residual 3 |

Each support is independent of the others; the factorization of `4` does not know or care that `2` was already seen. The union step is the only place where elements interact.

## 5. Growing the Union of Distinct Primes

Processing the elements left to right while accumulating a set of primes gives a trace of the answer in the making. A set is the right container because it enforces "distinct" structurally: adding a prime that is already present changes nothing, so no explicit deduplication logic is needed anywhere.

| Step | Element processed | Support of that element | Primes newly added | Set after the step | Size |
|:---:|:---:|:---|:---|:---|:---:|
| 1 | 2 | $\{2\}$ | 2 | $\{2\}$ | 1 |
| 2 | 4 | $\{2\}$ | none | $\{2\}$ | 1 |
| 3 | 3 | $\{3\}$ | 3 | $\{2, 3\}$ | 2 |
| 4 | 7 | $\{7\}$ | 7 | $\{2, 3, 7\}$ | 3 |
| 5 | 10 | $\{2, 5\}$ | 5 | $\{2, 3, 5, 7\}$ | 4 |
| 6 | 6 | $\{2, 3\}$ | none | $\{2, 3, 5, 7\}$ | 4 |

The set reaches its final size at step 5 and step 6 leaves it untouched — the last element contributes two primes, but both were already known. That is the whole algorithm: factor, union, repeat, then read the cardinality. The reported value is $\lvert\{2, 3, 5, 7\}\rvert = 4$, matching the required output.

Note that the *order* of the elements cannot affect the result, because set union is commutative and associative; the left-to-right trace is a presentation choice, not a dependency.

## 6. Exponents Collapse, the Support Does Not

It is instructive to expand the same instance the way the problem statement does, because it shows exactly what information the set discards. The full product is

$$2 \cdot 4 \cdot 3 \cdot 7 \cdot 10 \cdot 6 = 10080 = 2^{5} \cdot 3^{2} \cdot 5^{1} \cdot 7^{1}.$$

Contributions per element, where a blank means that element does not contain the prime:

| Element | Exponent of 2 | Exponent of 3 | Exponent of 5 | Exponent of 7 |
|:---:|:---:|:---:|:---:|:---:|
| 2 | 1 | 0 | 0 | 0 |
| 4 | 2 | 0 | 0 | 0 |
| 3 | 0 | 1 | 0 | 0 |
| 7 | 0 | 0 | 0 | 1 |
| 10 | 1 | 0 | 1 | 0 |
| 6 | 1 | 1 | 0 | 0 |
| **total (product)** | **5** | **2** | **1** | **1** |

The answer is the number of columns whose total is positive — four — and not any particular total. Summing the exponents of `2` to `5` and of `3` to `2` would be wasted effort for this question, and it is precisely that effort which becomes intractable when the array has $10^{4}$ elements. The table also demonstrates the union identity concretely: a column is nonzero exactly when at least one row contributes to it.

## 7. Correctness and the Support Invariant

**Per-element invariant.** When the trial-division loop for an element $x$ ends, the recorded primes together with the residual value (when it exceeds $1$) form exactly $\mathrm{supp}(x)$, and the working cofactor equals $1$.

*Initialization.* No prime has been recorded and the cofactor equals the original $x$, which trivially satisfies $x = \big(\prod \text{recorded } p^{e_p}\big) \cdot \text{cofactor}$ with the empty product equal to $1$.

*Preservation.* The loop tests a candidate $p$ only while $p^{2} \le x$, so the remaining cofactor $x$ has no divisor in $[2, p-1]$ left; if `x % p == 0` then $p$ is prime, because any smaller prime factor would already have been stripped. Recording $p$ once and dividing out every copy preserves the product identity, so the invariant survives each iteration, and the guard's failure at the top of the loop means the residual cofactor has no divisor $q$ with $q^{2} \le x$ other than the ones already removed.

*Termination.* The cofactor strictly decreases whenever a divisor is found, and the candidate $p$ strictly increases otherwise, so the loop ends. At that moment the cofactor is $1$ or a prime greater than $\sqrt{x_{\text{original}}}$, which is recorded as the final factor. Hence the recorded set is exactly $\mathrm{supp}(x)$.

**Global invariant.** After processing $i$ elements, the accumulated set equals $\bigcup_{j < i} \mathrm{supp}(\texttt{nums[j]})$.

The base case is the empty union for $i = 0$. The inductive step adds $\mathrm{supp}(\texttt{nums[i]})$ to a set already equal to the union over the first $i$ elements; set insertion is idempotent, so the accumulated value becomes the union over the first $i+1$ elements regardless of how many primes were already present. After the last element the set equals $\bigcup_{i} \mathrm{supp}(\texttt{nums[i]})$, which the exponent identity of section 2 equates with $\mathrm{supp}\big(\prod_i \texttt{nums[i]}\big)$. Since the cardinality of a set counts each distinct prime exactly once, the returned size is exactly the number of distinct prime factors of the product — and no product was ever constructed to obtain it.

## 8. Traps and Boundary Behaviour

| Scenario | Instance | Behaviour of the method | Result | Why the rule still holds |
|:---|:---|:---|:---:|:---|
| every element is a power of one prime | `[2, 4, 8, 16]` | supports are $\{2\}$ four times | 1 | The set is idempotent, so repeated factors never inflate the count; the exponent total of $2$ would be $10$. |
| composites share both primes | `[12, 18]` | $12 = 2^{2}\cdot3$, $18 = 2\cdot3^{2}$ | 2 | Distinctness is decided by the union, not by the number of factor occurrences. |
| each element is a new prime | `[3, 7, 11]` | three singleton supports, all disjoint | 3 | Disjoint supports make the union size the sum of the sizes. |
| a repeated large prime | `[997, 997]` | trial division tests every $p$ with $p^{2} \le 997$, i.e. $p \le 31$; none divides | 1 | The residual $997 > 1$ is prime and is recorded once; the second copy adds nothing. |
| primes that are perfect squares of a larger prime | `[49, 77, 121]` | $49 = 7^{2}$, $77 = 7 \cdot 11$, $121 = 11^{2}$ | 2 | Exponent stripping reduces $49$ to $1$ and $121$ to $1$; the union is $\{7, 11\}$. |
| large composites leaving a big leftover | `[1000, 999, 998]` | $\{2,5\} \cup \{3,37\} \cup \{2,499\}$ | 5 | `999` reduces to $37$ and `998` to $499$; dropping the residual would lose two primes. |
| a prime element above $\sqrt{1000}$ | `[997]` | the loop body never executes a successful division | 1 | The guard $p^{2} \le x$ correctly refuses to test further once $p > \sqrt{x}$; a divisor above $\sqrt{x}$ would need a partner below it. |
| the product is never needed | any full-length array | only cofactors up to $1000$ are ever held | — | Representing the product would need integer widths far beyond machine words; the union identity removes the need. |

Two semantic traps deserve naming. First, **testing only up to $\sqrt{\texttt{nums[i]}}$ without the residual step** is the single most common defect: it silently returns $\{2, 5\}$ for `1000`, which happens to be complete, but loses `37` for `999` and `499` for `998`. Second, **confusing "factor" with "prime factor"**: the problem counts primes, not all divisors. For `1000` the divisors include `4`, `8`, `25`, `40` and many others, none of which belong in the answer; the exponent-stripping loop is what keeps composites out of the recorded set.

## 9. Complexity: Time and Auxiliary Space

**Time.** Factorizing one element $x$ tests candidate divisors while $p^{2} \le x$, with each candidate costing one modular reduction; when a divisor is found, all of its copies are removed in additional divisions whose total number is the exponent. The worst case is an element that is prime, where every candidate up to $\lfloor\sqrt{x}\rfloor$ is tested and rejected, so the per-element cost is $\mathrm{O}(\sqrt{x})$. Over an array of $N$ elements it is

$$T(N) = \mathrm{O}\Big(\sum_{i=0}^{N-1} \sqrt{\texttt{nums[i]}}\Big) = \mathrm{O}(N\sqrt{M}), \qquad M = \max_i \texttt{nums[i]},$$

where the equality uses $\sqrt{\texttt{nums[i]}} \le \sqrt{M}$. With the stated bounds $N \le 10^{4}$ and $M \le 1000$, the inner loop never exceeds $31$ iterations, so the total is at most a few hundred thousand cheap integer operations. Exponent stripping only ever reduces this cost, since it lowers the cofactor and therefore ends the loop earlier.

**Auxiliary space.** The only growing structure is the set of distinct primes, whose size is bounded by the number of primes not exceeding $M$:

$$S_{\text{aux}}(N, M) = \mathrm{O}\big(\pi(M)\big), \qquad \pi(1000) = 168.$$

Per-element working storage is a single cofactor and a loop counter, so it does not grow with $N$. Because the set never exceeds $168$ entries here, the memory cost is effectively constant — but the bound is stated in terms of $\pi(M)$ so it remains honest if the numeric ceiling is raised. Building the set of all primes up to $M$ with a sieve first would use the same asymptotic order of memory while replacing the per-element loop with a shorter candidate list, at the cost of a preprocessing pass.

## 10. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Factor the product directly | Multiply all elements, then trial-divide the product. | $\mathrm{O}(\text{product size})$ time and space | The product is astronomically large for a full-length array; even with arbitrary-precision integers, dividing it repeatedly is far more expensive than factoring small elements. |
| Sieve all primes up to 1000, then test each | Build the prime list once with a sieve and divide each element by those primes. | $\mathrm{O}(M \log\log M + N \cdot \pi(M))$ time | A legitimate and often faster variant; it trades a preprocessing pass and an explicit prime table for a shorter candidate list, but it does not change the result and costs more code than a direct trial division. |
| Smallest-prime-factor table | Precompute for every value up to 1000 its smallest prime factor, then factor by repeated lookup. | $\mathrm{O}(M \log\log M + N \log M)$ time, $\mathrm{O}(M)$ space | The fastest option for this numeric ceiling and the right choice if the value bound grows, but the extra table is unnecessary work at $M = 1000$. |
| Count factors with multiplicity | Tally every prime occurrence with its exponent instead of a set. | Same time, larger container | Answers a different question: `[2, 4, 8, 16]` would report the exponent total $10$ rather than the $1$ distinct prime asked for. |
| Test divisibility by every integer up to the element | Trial-divide without the $\sqrt{x}$ guard. | $\mathrm{O}(N \cdot M)$ time | Correct but needlessly slow, and it makes the residual-prime step harder to see: the guard is what guarantees a leftover above $1$ is prime without further testing. |

The generalizable idea is that multiplicative structure distributes over a product as a *union of supports*. Whenever a question asks about the prime factors of a product, the answer lives in the union of the elements' supports, and the product itself is usually a quantity that should never be built.
