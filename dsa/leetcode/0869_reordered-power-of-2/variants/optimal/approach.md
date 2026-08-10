## General

Reordering digits changes their positions but never changes how many copies of each digit exist. That observation turns the problem from “try every possible ordering” into “compare digit multisets.” Two positive integers can be rearrangements of one another exactly when they contain the same count of `0` digits, the same count of `1` digits, and so on through `9`.

The helper `f(x)` builds this digit signature. It starts with a ten-element list of zeros, where index $v$ records the number of occurrences of decimal digit $v$. Each call to `divmod(x, 10)` returns both the remaining prefix and the final digit. The final digit's counter is incremented, and the process continues until no digits remain. For example, `f(1220)` records two twos, one one, and one zero. The order in which those digits were removed is irrelevant because only their counts are retained.

**Why the signature fully represents every legal reordering.** If some permutation of `n` equals a candidate power of two, both numbers use exactly the same original digits, so their ten counters must match. This proves matching counters are necessary.

They are also sufficient. If the counters match, the decimal digits of the power of two can be paired one for one with the digits of `n`. Arrange `n`'s digits in the exact order used by that power of two and the resulting decimal number is the candidate. A positive power of two never begins with zero, so this ordering automatically obeys the rule forbidding a leading zero. There is no need for a separate leading-zero test.

The solution computes `target = f(n)` once. It then generates powers of two in increasing order. The variable `i` begins at $1=2^0$, and `i <<= 1` doubles it, producing $2^1,2^2,\ldots$. For each candidate no greater than $10^9$, the solution builds its signature and compares that list with `target`. Python list equality compares the corresponding ten counts. A match immediately returns `True`; exhausting the candidates returns `False`.

**Why checking only these powers is complete.** The input satisfies $1 \le n \le 10^9$, so it has at most ten decimal digits, and any number formed by reordering its digits has the same number of digit positions before leading zeros are disallowed. A valid result must itself be a power of two within the relevant numeric range. The loop checks $2^0$ through $2^{29}$ because $2^{29}=536{,}870{,}912$ is at most $10^9$, while $2^{30}=1{,}073{,}741{,}824$ is larger.

One might notice that a ten-digit input such as `1000000000` could theoretically reorder to another ten-digit value above $10^9$. However, it contains nine zeros and one one, and no power of two has that decimal digit multiset. Under the supplied bound, comparing the enumerated powers through $10^9$ is the exact implementation being documented and covers every accepted signature. More generally, a version for a wider range would enumerate powers through the largest value representable with the input's digit count.

**A concrete comparison.** For `n = 128`, the target signature has one `1`, one `2`, and one `8`. The loop eventually reaches `256`, `512`, and then `1024` as it doubles. When it reaches `128` itself, the signatures obviously match, so the result is true. The same signature would also match `821` or `218` as input even though neither is already a power of two, because both can be reordered into `128`.

For `n = 10`, the signature contains one zero and one one. None of the tested powers has exactly those counts, so the loop finishes and returns false. The method does not mistake `01` for `1`: `1` has no zero in its signature, while `10` does. Thus the forbidden act of hiding a zero as a leading digit cannot create a false match.

This avoids factorial growth. With $d$ digits, there can be as many as $d!$ positional permutations, many duplicated when digits repeat. A signature takes a single pass over the digits, and the allowed input range contains only a fixed small number of powers of two.

## Complexity detail

Let $d$ be the number of decimal digits in `n`. Building one signature takes $O(d)$ time. The input constraint fixes the candidate set to the 30 powers from $2^0$ through $2^{29}$. Each has at most ten digits, so the constant-size candidate loop performs $O(d)$ total work under this problem's bounded domain.

- **Time complexity:** $O(d)$. The factor of at most 30 candidate powers is constant for $n \le 10^9$.
- **Space complexity:** $O(1)$. Each signature is a list of exactly ten counters, and the number of scalar variables is fixed. The space does not grow with the value or digit count within the decimal alphabet.

For an unbounded generalized version that checks $p$ powers, the time would be $O(pd)$, but $p$ is fixed by the stated constraint here. The target list remains alive throughout the loop, while each candidate list is temporary.

## Alternatives and edge cases

- **Generate all digit permutations:** Test every ordering, reject leading zero, convert it to an integer, and test whether it is a power of two. This can require factorial time and repeats work when digits are duplicated.
- **Sort decimal strings:** Sorting the digits of `n` and every candidate power provides another canonical signature. It is correct, but sorting costs $O(d\log d)$ per number instead of counting over the fixed ten-digit alphabet.
- **String counter or frequency map:** A language-provided multiset counter expresses the same idea. The ten-slot list is simpler, has fixed memory, and makes equality deterministic.
- **Precomputed signature set:** All eligible power-of-two signatures could be stored in a set and queried. That makes repeated calls convenient, but a single call needs only 30 comparisons and does not require global precomputation.
- **Direct power-of-two test only:** Checking `n & (n - 1) == 0` answers whether `n` itself is a power of two, not whether some digit reordering is one. It misses values such as `821`.
- **Input equal to one:** `1` is $2^0$, the first candidate, so it returns true.
- **Repeated digits:** Counts preserve multiplicity. A number with two copies of a digit cannot match a power containing only one copy.
- **Zeros:** Zeros are counted like every other digit. They cannot be silently discarded as leading zeros because a candidate signature must contain the same number of zeros.
- **Different digit lengths:** Equal signatures imply equal total digit counts, so a shorter power cannot accidentally match a longer input.
- **Upper bound:** The loop includes powers at or below $10^9$ and stops after doubling past it. The stopping rule prevents irrelevant larger candidates while retaining $2^{29}$.
- **Helper and zero:** The helper's loop would return an all-zero signature for `x = 0`, but neither the input nor any candidate is zero under the contract, so that special representation is never used.
