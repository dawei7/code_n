## General

An allowed operation chooses two positions `a` and `b` such that the current value at `a` is divisible by the current value at `b`. It then replaces `nums[a]` with `nums[b]`. Since all values are positive, replacing a value by a proper divisor makes that position smaller; replacing it by an equal value changes nothing.

At first, the operations may appear globally dependent. Changing one position can alter which value it can donate later, and a newly copied value might participate in another operation. The key simplification is to characterize exactly which final values can ever reach one original position.

**Every value is copied from the original array**

An operation never performs arithmetic to invent a new integer. It copies a value that already exists at another position. Trace any current value backward through the operations that copied it: eventually that chain ends at an occurrence of the same value in the original input. Therefore every value that appears at any time belongs to the set of distinct initial values.

This is why the source creates `present`. It is a byte array indexed by integer value, and `present[x] == 1` means that `x` occurs somewhere in the original array. Duplicate occurrences do not need separate flags because they offer the same possible donor value.

**What can replace one original value**

Consider a position whose original value is $x$. If an operation changes its current value $y$ to a donor value $d$, the rule requires $d\mid y$. If more replacements follow, each next value divides the previous one. Divisibility is transitive, so the final value must divide the original $x$.

Combining this fact with the copying observation gives a lower bound: the final value at an original $x$ must be an initially present value that divides $x$. It cannot be smaller than the smallest initially present divisor of $x$.

That lower bound is also reachable directly. If an initially present value $d$ divides $x$, a position initially holding $d$ can be used as the donor to replace the position holding $x$. No intermediate chain is required. Thus the best possible value for each occurrence of $x$ is exactly

$$
\min\{d : d \text{ occurs initially and } d\mid x\}.
$$

The set is never empty because $x$ occurs initially and $x\mid x$. This turns the problem from a search over sequences of operations into a divisor lookup for every original value.

**Why the per-position minima can coexist**

It is not enough merely to find a lower bound for each position; those best values must be achievable in one common operation sequence. A concern is that a position serving as the only donor of value $d$ might itself later be replaced by a smaller divisor.

One valid scheduling idea is to process donor values from larger to smaller. Before changing an original occurrence of $d$, use it to perform every replacement whose chosen final value is $d$. If that donor should ultimately become a smaller value $e$, the original occurrence of $e$ has not needed to be destroyed first; its work can be performed later. Equal-value copies require no operation. In this way, every needed initial value remains available until all positions that need it have received it.

Equivalently, imagine a preparation phase in which each original donor creates all necessary copies of itself before donors are minimized. Copying does not consume the donor. These schedules show that the individual minima are simultaneously attainable, so summing them gives the global minimum rather than merely a collection of incompatible wishes.

**A sieve over multiples**

The source must find the smallest present divisor for every distinct input value. Testing every pair of array entries would repeat work, especially when many values are equal. Instead, it uses a sieve organized by possible divisor.

First, `limit = max(nums)` determines the largest value that needs to be represented. `present` has indices from zero through `limit`, and the input loop marks every value that occurs.

The array `smallest_divisor` initially contains zeros, meaning “not assigned yet.” The outer loop visits candidate divisors in increasing order from $1$ through `limit`. If a candidate is absent from the original array, it is skipped because only an initially present value can be copied.

For a present divisor $d$, the inner loop visits

$$
d,2d,3d,\ldots
$$

through `limit`. These are exactly the values divisible by $d$. The code only acts when the multiple itself is present and its answer is still zero. It then records $d$ as that value's `smallest_divisor`.

Because candidate divisors are processed in increasing order, the first present divisor that reaches a present multiple $x$ is necessarily the smallest initially present divisor of $x$. The zero check prevents any later, larger divisor from overwriting it. Every input value is guaranteed to be assigned at least to itself: when the outer loop reaches $x$, `present[x]` is true and $x$ is one of its own multiples.

Finally, the source evaluates `smallest_divisor[value]` for every occurrence in `nums` and sums those minima. Repeated occurrences are deliberately included repeatedly because each array position contributes separately to the final array sum, even though the sieve computed their shared best value only once.

**An example of why the global minimum alone is insufficient**

Suppose the initially present values include $6$ and $10$ but do not include $1$ or $2$. Neither value divides the other, so neither can replace the other. Simply filling the array with its globally smallest value, $6$, would be illegal for a position holding $10$. The sieve instead asks which present values divide each particular number. It assigns $6$ to occurrences of $6$ and $10$ to occurrences of $10$, unless some other smaller present divisor applies. This preserves the operation's divisibility condition.

## Complexity detail

Let $n$ be the array length and let

$$
V=\max(\texttt{nums}).
$$

Marking present values takes $O(n)$ time. Initializing and scanning the two value-indexed arrays costs $O(V)$ time and $O(V)$ space.

If every possible divisor were present, the number of inner-loop visits would be

$$
\sum_{d=1}^{V}\left\lfloor\frac{V}{d}\right\rfloor
=O(V\log V).
$$

Skipping absent divisors can only reduce that work. The final sum takes another $O(n)$ time. The complete time complexity is therefore $O(n+V\log V)$, and the additional space complexity is $O(V)$.

The manifest expresses time as $O(N\log N)$ and space as $O(N)$ for $N=\max(n,V)$. Since both $n$ and $V$ are at most $N$, that is a valid compact form of the more descriptive bounds above.

The byte array makes `present` more memory-efficient than a Python list of Boolean objects, while `smallest_divisor` stores one integer per possible value. The algorithm's dependence on $V$ is appropriate under the stated upper bound of $10^5$.

## Alternatives and edge cases

- **Try every donor for every array position:** Checking whether each input value divides every other input value can take $O(n^2)$ time and repeats identical questions for duplicate values. The value-domain sieve shares the work.
- **Simulate operation sequences:** The state graph can be enormous, and the order of copies obscures the simple reachability fact. Tracing copied values back to initially present divisors removes the need for state search.
- **Replace everything by the global minimum:** This is valid only when that minimum divides every original value. Numeric order alone does not satisfy the divisibility precondition.
- **Use the greatest common divisor of the whole array:** A gcd need not occur in the array, and operations can copy only existing values. A mathematically valid divisor that is absent cannot be introduced.
- **Enumerate divisors separately for every distinct value:** Factoring each value up to its square root and checking presence can also work, but the sieve is direct and has a clean harmonic-series bound over the permitted value range.
- **Sort the distinct values and scan possible donors:** This can still require many divisibility tests between unrelated values. Iterating multiples visits only divisor-multiple relationships.
- **Value `1` is present:** Since $1$ divides every positive integer, the sieve assigns $1$ to every present value, and the minimum sum is exactly the number of array positions.
- **All values are equal:** Each value's smallest present divisor is itself unless a smaller divisor also appears, which it does not in an all-equal array. No useful operation exists and the sum stays unchanged.
- **Duplicate values:** `present` stores the distinct donor fact once, while the final generator expression counts the computed minimum once per occurrence.
- **A value has smaller mathematical divisors that are absent:** Those divisors are irrelevant because no operation can create them. The outer loop deliberately skips every absent divisor.
- **A donor is later replaced:** Operations can first copy that donor value to all positions that need it. Copying is non-destructive, so changing the original donor afterward does not invalidate completed replacements.
- **The maximum value indexes the arrays:** Both arrays have length `limit + 1`, making index `limit` valid. Index zero is unused because all input values are positive.
- **Nonempty positive input:** `max(nums)` relies on the contract's nonempty array guarantee, and value-indexed storage relies on positive bounded integers.
- **Overflow of the sum:** Python integers grow as needed, so summing many values does not overflow a fixed-width integer type.
