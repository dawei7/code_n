## General

**Use query equality to compare hidden bits**

The API reveals only whether a four-index sample contains four equal bits, a three-to-one split, or a two-to-two split. It does not reveal which bit is zero or one.

However, compare two queries that share three indices and differ only in the fourth. Their results are equal exactly when the two substituted hidden bits are equal. If the substituted bits match, the four-bit multisets are identical. If they differ, replacing a zero with a one or vice versa changes the balance category, so the returned value changes.

The solution uses this observation to classify every position relative to index three. It never needs to know whether `nums[3]` itself is zero or one.

**Establish the reference query**

`x = reader.query(0, 1, 2, 3)` records the distribution of the first four positions.

Counters `a` and `b` mean “same as index three” and “different from index three.” The initialization `a = 1` counts index three itself, while `b = 0` starts the opposite class empty.

Variable `k` stores an index known to be in the different class. It is updated whenever such an index is discovered. Its initial value does not matter if no different element exists, because it is returned only when the different class is larger.

**Classify indices four and beyond**

For every `i` from four through `n-1`, the source compares `query(0, 1, 2, i)` with `x`. These queries share indices zero, one, and two; they substitute `i` for index three.

Equal results mean `nums[i] == nums[3]`, so `a` increases. Different results mean the bits differ, so `b` increases and `k = i` records a representative.

This loop includes index four. Later, the code calls the same query `query(0, 1, 2, 4)` again and stores it as `y`. That duplicate call is part of the exact implementation.

**Classify indices zero, one, and two**

Now `y` describes indices zero, one, two, and four.

`query(1, 2, 3, 4)` shares indices one, two, and four with `y`. Its substituted pair is index three versus index zero. Equality therefore means `nums[3] == nums[0]`. The solution increments `a` when equal; otherwise it increments `b` and records zero.

Similarly, `query(0, 2, 3, 4)` compared with `y` substitutes index three for index one, classifying `nums[1]`.

Finally, `query(0, 1, 3, 4)` compared with `y` substitutes index three for index two, classifying `nums[2]`.

After these three checks, the counters cover every array position exactly once: index three from initialization, indices four onward from the loop, and indices zero through two from the final comparisons.

**Turn relative classes into a majority answer**

Because every value is binary, positions different from `nums[3]` all contain the other bit. Thus `a` and `b` are exactly the frequencies of the two hidden values, even though the solution never labels them zero and one.

If `a == b`, the frequencies tie and the required result is negative one.

If `a > b`, index three belongs to the majority class, so the source returns three.

If `b > a`, any recorded different index is a valid majority index. At least one such position must exist when `b` is positive and larger, so returning `k` is safe.

**Why the classification rule is sound**

Fix the three shared bits in a pair of queries, and let their number of ones be $s$. Adding a fourth zero yields $s$ ones; adding a fourth one yields $s+1$. For $s$ from zero through three, those adjacent counts always correspond to different return categories under the API's symmetry between zeros and ones.

Therefore equal query results imply equal substituted bits, and different results imply different substituted bits. Applying that equivalence to each constructed pair proves every counter update is correct.

Once every position is classified, comparing class sizes plainly identifies the more frequent bit or a tie. The returned index belongs to the selected class, completing the correctness argument.

**Respecting the query budget**

The source makes one call for `x`, $N-4$ calls in the loop, one additional call for `y`, and three final classification calls. The total is $N+1$.

For every legal $N \ge 5$, $N+1 \le 2N$, so the explicit budget is respected. Caching the loop's query for index four could remove the duplicate and reduce the count by one, but it is not required for correctness or the limit.

## Complexity detail

Let $N$ be the hidden array length. The loop performs $N-4$ iterations, and the remaining work uses a fixed number of API calls. With each query guaranteed $O(1)$, total time is $O(N)$.

The exact query count is $N+1$, which is linear and within the allowed $2N$ calls.

Only counters, saved query results, indices, and the array length are stored. Auxiliary space is $O(1)$, matching the manifest. The hidden array is neither copied nor accessed directly.

## Alternatives and edge cases

- **Cache the index-four query:** Reusing the loop result as `y` saves one call and gives $N$ total queries without changing the reasoning.
- **Try to decode actual bit values:** It is unnecessary; majority depends only on the sizes of the two equivalence classes.
- **Compare arbitrary queries:** Equality is informative for individual bits only when the queries share three indices and differ in exactly one.
- **Equal frequencies:** The code returns negative one before choosing either representative.
- **Reference class majority:** Index three is always a valid returned index when `a > b`.
- **Opposite class majority:** `k` has been assigned to a proven different position before it can be returned.
- **All bits equal:** Every classification joins `a`, and index three is returned.
- **Minimum length five:** All indices used by the fixed queries exist, and the query count is six, below the budget of ten.
- **Binary-domain requirement:** With more than two possible values, “different from index three” would not necessarily be one uniform class.
- **Valid query ordering:** Every call passes four distinct indices in strictly increasing order.
- **Symmetric query result:** The API does not distinguish zero-majority from one-majority, which is why relative comparison is the appropriate tool.
- **Interactive boundary:** The platform supplies `ArrayReader`; the solution must not implement or inspect it.
- **Follow-up minimum calls:** The exact source is budget-compliant but intentionally does not prove the theoretical minimum.
