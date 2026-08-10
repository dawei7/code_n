## General

The split depends on each element's index, not on whether the element itself is prime. Index 2 is prime regardless of the value stored at `nums[2]`, while indices 0 and 1 are never prime.

The exact source precomputes primality for every possible index once at module load, then evaluates the requested difference with one signed sum.

**Global primality table**

`m = 10**5 + 10` is slightly larger than the maximum array length. `primes[i]` is intended to be true exactly when index `i` is prime.

The list begins as all true, after which indices 0 and 1 are explicitly marked false. For each integer `i >= 2` still marked prime, the nested loop marks:

`2i, 3i, 4i, ...`

as composite. Every marked number has divisor `i` and is therefore not prime.

Conversely, a composite number has a prime divisor smaller than itself. When that divisor is processed, the number is marked false. Thus every table entry is correct after preprocessing.

The loop starts at `i+i` rather than the more optimized `i*i`. This repeats some markings—for example, 6 is marked when processing both 2 and 3—but does not change correctness.

**Representing the two sums without constructing arrays**

Let:

- `A` contain values at prime indices;
- `B` contain values at every other index.

The requested quantity is:

$$
\left|\sum A-\sum B\right|.
$$

The generator expression contributes `x` when `primes[i]` is true and `-x` otherwise:

`x if primes[i] else -x`.

Summing these signed contributions gives exactly `sum(A) - sum(B)`. Applying `abs` produces the required nonnegative difference.

The source therefore never allocates arrays `A` and `B` and never needs to compute their sums separately.

**Why negative values still work**

The sign in the generator represents which side of the subtraction an element belongs to; it is independent of the element's own sign.

If a non-prime-index value is `-5`, its contribution is `-(-5)=+5`. This is correct because subtracting `sum(B)` subtracts every B value, including negative ones.

Similarly, a negative value at a prime index contributes negatively to `sum(A)` exactly as ordinary summation requires.

**Following the first example**

For `nums=[2,3,4]`:

- index 0 is not prime, contributing `-2`;
- index 1 is not prime, contributing `-3`;
- index 2 is prime, contributing `+4`.

The signed total is `-1`, equal to `4-(2+3)`. Its absolute value is 1.

**Following the second example**

Indices 2 and 3 are prime. The contributions for `[-1,5,7,0]` are:

- index 0: `-(-1)=+1`;
- index 1: `-5`;
- index 2: `+7`;
- index 3: `+0`.

Their total is 3, matching `sum(A)-sum(B)=7-4`.

**Why the one-pass method is complete**

`enumerate(nums)` visits every index-value pair exactly once. The global table classifies the index into exactly one of the two groups. The conditional contribution then adds that value with the algebraic sign belonging to its group.

By distributivity, the total of all positive-side contributions minus all negative-side contributions is precisely the difference of the two group sums. No element is omitted or counted twice.

**Difference from the manifest**

The manifest says the source sums prime positions and derives the complementary sum from the total array sum. That is a valid alternative, but it is not what the exact source does. The source directly forms the signed difference in one generator.

The manifest also states `O(n\log\log n)` time as though a size-`n` sieve were built for each call. The exact table has fixed size and is created once when the module loads. Per method call, only the `O(n)` signed scan occurs.

**Environment dependency**

The method annotation uses `List[int]`, but the shown file does not import `List`. It requires the surrounding execution environment to provide that name or a standalone module to import it from `typing`. The primality algorithm itself is otherwise fully defined in the file.

## Complexity detail

Let `N = len(nums)` and let `M = 100010` be the fixed global sieve size.

Module initialization marks multiples in `O(M\log\log M)` time by the usual harmonic sum over primes, despite beginning at `2i` rather than `i^2`. The Boolean table uses `O(M)` persistent space. This cost is paid once per module load, even if a call uses a short array.

`splitArray` itself visits `N` values, performs constant-time table lookup and arithmetic per value, and uses Python's streaming `sum`. Its per-call time is `O(N)` and its auxiliary space is `O(1)` beyond the already-existing global table.

If preprocessing is charged to one isolated invocation, total time is `O(M\log\log M+N)` and space is `O(M)`. Since `M` is tied to the maximum allowed `N`, this is commonly summarized as `O(N\log\log N)` preprocessing and `O(N)` space, but that summary hides the source's fixed eager table.

## Alternatives and edge cases

- **Sieve only through `len(nums)-1`:** It avoids precomputing unused indices for short calls but repeats setup for every invocation.
- **Prime sum plus total sum:** Compute `prime_sum` and `total`, then use `abs(2*prime_sum-total)`. This matches the manifest summary and is algebraically equivalent.
- **Test every index individually:** Trial division per index uses less persistent memory but can cost roughly `O(n\sqrt n)` time.
- **Construct `A` and `B`:** It is straightforward but wastes `O(n)` extra storage when only their sums matter.
- **Index 0:** It is not prime and always belongs to B.
- **Index 1:** It is also not prime.
- **Index 2:** It is the first prime index and belongs to A.
- **One-element input:** A is empty, B contains `nums[0]`, and the result is `abs(nums[0])`.
- **All prime-index values absent:** This occurs only for very short arrays; the signed formula still treats A's sum as zero.
- **Negative elements:** Group membership is unchanged, and the conditional sign correctly preserves subtraction algebra.
- **Zero elements:** They contribute zero regardless of group.
- **Equal group sums:** The signed total is zero and `abs` returns zero.
- **Repeated calls:** They reuse the same global primality table without mutation.
- **Input preservation:** The method streams over `nums` and never changes its values or order.
- **Missing `List` import:** Standalone execution must provide the annotation name.
