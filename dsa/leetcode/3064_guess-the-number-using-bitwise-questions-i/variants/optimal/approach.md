## General

**A one-bit query isolates one bit of the secret.** Query the API with

$$
\texttt{num}=2^i.
$$

This number has exactly one set bit, at position $i$. Therefore `n & num` is either zero when secret bit $i$ is zero, or $2^i$ when that bit is one. `commonSetBits(num)` consequently returns either 0 or 1 for a legal single-bit query.

The source includes `1 << i` in the answer whenever the API result is truthy:

`sum(1 << i for i in range(32) if commonSetBits(1 << i))`.

Adding distinct powers of two reconstructs the integer whose set-bit positions were detected.

**Why summation works like bitwise OR.** Every queried power has a different bit position. No two included terms overlap, so addition causes no carries and equals their bitwise OR. The binary representation of the sum is exactly the union of detected set bits.

**A trace for 33.** Decimal 33 is binary `100001`, with bits 0 and 5 set. Queries 1 and 32 return one common set bit. All other legal one-bit queries return zero. The sum is $1+32=33$.

**The intended legal range has only 30 positions.** The constraint says

$$
0\le\texttt{num}\le2^{30}-1
$$

and $n$ obeys the same upper bound. Legal bit positions are 0 through 29. Querying those 30 powers is sufficient because bits 30 and above of $n$ must be zero.

**Exact-source contract defect.** The protected implementation uses `range(32)`, so it additionally calls:

`commonSetBits(1 << 30)` and `commonSetBits(1 << 31)`.

Both query numbers exceed $2^{30}-1$. The reference explicitly warns that API output is unreliable for out-of-range queries. If either invalid call returns a truthy value, the source adds a bit that cannot belong to legal $n$ and returns an incorrect number.

The local manifest says the algorithm queries each legal bit position independently, but the actual loop includes two illegal positions. The correct bound for this contract is `range(30)`. This is a genuine source defect even if a particular judge implementation happens to return zero for those calls.
Restricting the argument to positions 0 through 29, every secret bit is independently identified by a query that contains only that bit. Set positions are added and unset positions are omitted, so the reconstructed binary number equals $n$ exactly. No adaptivity is needed; each query answer is independent.

**Query count.** The source makes 32 API calls unconditionally. The legally correct version needs 30. The number of calls is fixed rather than dependent on the secret value.

## Complexity detail

Under the fixed 30-bit domain, the intended algorithm performs a constant number of API queries and arithmetic operations: $O(1)$ time and $O(1)$ auxiliary space.

If generalized to a $B$-bit allowed range, it would take $O(B)$ queries and time, still using $O(1)$ local storage beyond the output accumulator/generator state.

The exact source makes 32 rather than 30 calls, which remains constant complexity but violates the API range. Asymptotic bounds do not establish semantic correctness.

## Alternatives and edge cases

- **Query all legal bits with `range(30)`:** This is the direct correction and deterministically reconstructs every allowed secret.
- **Group-testing queries:** Asking about several bits at once returns only their count, not identities, so decoding requires a more elaborate scheme and provides no benefit in this first version.
- **Binary search:** The API does not compare magnitudes, so ordinary higher/lower binary search is unavailable.
- **Secret is a power of two:** Exactly one legal single-bit query is truthy, and the sum returns that power.
- **All 30 bits set:** Every legal query succeeds and their sum is $2^{30}-1$.
- **Secret minimum one:** Bit zero or another single bit is detected normally; the contract excludes secret zero.
- **Truthiness:** Legal one-bit queries return 0 or 1, so using the result as a condition is safe.
- **Illegal bits 30 and 31:** The exact source queries them despite the explicit reliability warning, so its result is not guaranteed.
- **Addition versus OR:** Distinct powers make them equivalent; duplicate bit queries would break that simple reasoning but none are duplicated.
- **Manifest mismatch:** “Legal bit positions” describes 30 queries, not the actual 32-query loop.
- **No ambiguity from the returned count:** With a one-hot query there is at most one common bit, so the count reveals that bit exactly. Multi-bit queries would return a total without identifying positions.
- **Highest legal bit:** Position 29 corresponds to $2^{29}$ and is included in `range(30)`. Position 30 corresponds to $2^{30}$ and already exceeds the maximum legal query.
- **Unreliable does not mean guaranteed zero:** The API warning forbids assuming benign behavior outside range. Correctness must hold for every behavior permitted by the contract, which the 32-query source cannot guarantee.
- **Fixed query strategy:** Results from earlier calls do not influence later queries. This makes the reasoning simple and allows each bit to be verified independently.
