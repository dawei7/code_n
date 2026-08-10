## General

**Choose the smallest legal positive integer at every step.** The array elements must be distinct, positive, and contain no two different selected values summing to `k`. The exact solution builds the set in increasing order. Variable `i` is the next positive candidate, `s` is the running sum, and `vis` stores values that are forbidden because of earlier choices.

For every selected value $a$, its only conflicting partner is $k-a$. The statement `vis.add(k - i)` records exactly that partner. Before selecting a future candidate, the loop skips it while `i in vis`.

**Why selected values themselves do not need a set.** `i` only increases and is selected at most once, so distinctness is automatic. The set is not a set of chosen numbers; it is a set of complements that future candidates may not use.

For example, with `k = 4`, selecting one records three as forbidden. Selecting two records two, but two has already been selected and the scan never returns to it. This is valid because the prohibited pair requires two distinct array elements, and distinctness prevents selecting another two. Candidate three is later skipped, then four, five, and six are allowed.

**Advance past every forbidden candidate.** At the start of each of the `n` selections, the inner while loop may advance `i` through one or more recorded complements. The first value not in `vis` is the smallest positive integer that can be added without conflicting with any earlier selection.

The code adds its complement to `vis`, adds the value to `s`, and increments `i` so the next iteration begins with a larger candidate.

**Why the greedy choices are globally minimal.** Positive integers below `k` form independent complementary pairs `{a, k-a}`. From a pair with two different positive members, at most one may be selected. Choosing the smaller member is never worse for total sum than choosing the larger. The increasing scan encounters that smaller member first, selects it, and records the larger as forbidden.

When `k` is even, `k/2` is its own complement. The restriction concerns two distinct elements, and the array itself must have distinct values, so selecting `k/2` once is safe. The implementation checks it before adding its self-complement, so it selects it exactly once and never revisits it.

At values at least `k`, the complement `k-i` is nonpositive. Since future candidates remain positive and increasing, such complements can never block anything. All sufficiently large integers are therefore selected consecutively.

This structure shows that the greedy sequence is the lexicographically smallest feasible increasing sequence. If another feasible array first differed at some position by using a larger value, the greedy smaller candidate was not forbidden by earlier greedy choices. Complement pairs are independent, so replacing the larger first-difference value with the greedy one cannot introduce a conflict with the common earlier prefix. The replacement lowers the sum. Therefore, no alternative has a smaller total.

**A concrete trace.** For `n = 5` and `k = 4`:

- Select one, forbid three.
- Select two, record two after it has already been used.
- Skip forbidden three.
- Select four; its complement zero is irrelevant.
- Select five and six.

The chosen values are one, two, four, five, and six, summing to eighteen.

**The set can contain irrelevant values.** Choosing a value greater than `k` inserts a negative complement. Choosing `k` inserts zero. These entries consume some set space but can never match the future positive `i`. The source does not filter them because doing so is unnecessary for correctness.

**The exact algorithm differs from the manifest.** The manifest describes computing two arithmetic blocks in constant time. This source performs `n` greedy selections and maintains a set of forbidden complements. With `n,k\le50` it is easily fast enough, but its real time and space are linear in `n`, not constant.

## Complexity detail

The outer loop performs exactly $n$ selections. How many times can the inner while loop advance? Each skipped positive candidate must be present in `vis` and is passed only once because `i` never decreases. Before the scan reaches `k`, there are at most $O(k)$ possible positive candidates, and under the stated $n,k\le50$ this is small.

A precise general bound is $O(n+k)$ expected time: $n$ selections plus at most $k-1$ positive candidates that can be skipped before all complements become nonpositive. Since the constraints tie both quantities to at most fifty, and common analysis treats the generated sequence length as the main variable, this is often summarized as $O(n+k)$ rather than the manifest's $O(1)$.

The set receives one entry per selected value, so it contains at most $n$ values and uses $O(n)$ space. Scalar variables use constant space. Hash lookup and insertion are expected $O(1)$.

An arithmetic closed form can compute the same sequence sum in $O(1)$ time and space, which is the optimization described by the manifest and used in the larger-constraint version of this problem.

## Alternatives and edge cases

- **Arithmetic two-block formula:** Select one through $\lfloor k/2\rfloor$, then continue from `k` upward for any remaining slots. Sum both arithmetic progressions directly in $O(1)$ time and space.
- **Chosen-value set:** Instead of storing forbidden complements, test whether `k - i` has already been chosen. This is equally correct and may be more intuitive, with the same expected bounds.
- **Brute-force combinations:** Enumerating candidate arrays is unnecessary because every value conflicts with at most one complement.
- **Even `k`:** Value `k/2` is safe once because a second equal value is disallowed by distinctness; the greedy code selects it.
- **`k = 1`:** Every complement of a positive selection is nonpositive, so the method simply chooses one through `n`.
- **Complement zero or negative:** It is stored but can never block a future positive candidate.
- **Forbidden consecutive values:** The while loop continues until it finds the first allowed candidate rather than skipping only once.
- **Distinctness:** Monotonic `i` ensures no chosen value repeats without needing to store chosen values.
- **Minimum sum versus arbitrary validity:** Choosing the smallest allowed candidate is what proves optimality; many larger valid arrays exist.
- **Hash-set assumptions:** Expected constant operations give the stated time; adversarial hashing is not material for small Python integers.
- **Manifest mismatch:** The closed-form constant bound belongs to the alternative, while the exact source explicitly loops and allocates `vis`.
