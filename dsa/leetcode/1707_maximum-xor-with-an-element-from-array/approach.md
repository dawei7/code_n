## General

**Separate the threshold condition from XOR maximization**

For query `[x, m]`, only numbers no greater than `m` are eligible. Among those numbers, the task is to maximize `x XOR value`.

Trying every eligible number for every query could take $O(NQ)$. The source handles the two requirements with complementary techniques:

- Sort numbers and queries by the eligibility threshold so each number is activated once.
- Store active numbers in a binary trie so the best XOR partner is found one bit at a time.

Here $N$ is the length of `nums` and $Q$ is the number of queries.

**Process queries offline in increasing limit order**

`nums.sort()` arranges candidate values from smallest to largest and mutates the input list. Pointer `j` marks the first number not yet inserted.

The expression `sorted(zip(range(n), queries), key=lambda x: x[1][1])` pairs each query with its original index and sorts those pairs by the query's second value `m`. In this function, the local variable `n` is `len(queries)`, not the number of input numbers.

Before answering a sorted query, the while loop inserts every remaining `nums[j] <= m`. Because later queries have limits at least as large, inserted values never need to be removed. Just before each search, the trie therefore contains exactly all array occurrences eligible under the current limit.

The preserved query index `i` is used to write `ans[i]`, restoring original order even though evaluation uses sorted-limit order.

**Represent every integer as a 31-bit path**

Each `Trie` node has two child slots: child zero and child one. `__slots__ = ["children"]` prevents a per-instance attribute dictionary, reducing node overhead without changing the algorithm.

`insert(x)` visits bit positions 30 down through zero. At position `i`,

`v = x >> i & 1`

extracts that bit. A missing child `v` is created, then traversal moves to it. After 31 steps, one complete root-to-leaf path represents `x`.

The constraints cap values at $10^9$, which fits within these 31 nonnegative bit positions. Leading zero bits are included so every inserted path has the same depth.

Duplicate numbers follow an already existing path and create no new nodes. That is safe because numbers are never deleted and multiplicity cannot change the maximum XOR value.

**Greedily maximize the most significant XOR bit**

At each bit of query value `x`, let `v` be its bit. XOR produces one at that position only if the chosen number has the opposite bit `v ^ 1`.

The search first checks `node.children[v ^ 1]`. If it exists, it takes that branch and sets the answer bit with `ans |= 1 << i`. If the opposite branch does not exist, it follows the same-bit child, which contributes zero at this position.

This greedy choice is optimal because higher bits dominate every combination of lower bits. Gaining $2^i$ at bit `i` is worth more than the maximum possible sum $2^i-1$ of all positions below it. Therefore, whenever an opposite-bit branch contains any eligible number, no same-bit branch can produce a larger final XOR.

Once a branch is chosen, the same reasoning repeats inside that prefix for the next bit. The traversal ultimately selects one inserted number and `ans` is exactly its XOR value with `x`.

**Return negative one when no number is eligible**

The trie begins empty. If a query's limit is smaller than every number, neither root child exists. In `search`, the opposite-bit check and same-bit check both fail, so the function returns `-1`.

After at least one complete value has been inserted, every visited node on the chosen route has a child for the next level until all 31 bits are processed. The generic fallback remains useful for detecting the initially empty trie.

The result array is prefilled with negative ones, but every query position is then assigned the value returned by `search`. Prefilling supplies the correct type and size; it is not relied upon to skip any queries.

**Why the offline invariant proves eligibility**

Before a query with limit $m$, all sorted values at indices below `j` satisfy `nums[index] <= m` and have been inserted. The while loop stops only when `j` reaches the end or the next sorted value exceeds $m$. Thus no eligible value is absent and no ineligible value is present.

Trie search maximizes XOR over exactly that inserted set. Writing the result at the original index therefore gives the required answer for this query. Since every query is processed once, the returned array is correct in its original ordering.

For `nums = [0,1,2,3,4]` and query `[3,1]`, only zero and one have been inserted. The trie search prefers the bits of zero where they oppose three and returns `3 XOR 0 = 3`, which exceeds `3 XOR 1 = 2`.

## Complexity detail

Let $B=31$, $N$ be the number of values, and $Q$ the number of queries. Sorting `nums` costs $O(N\log N)$. Building and sorting the indexed query sequence costs $O(Q\log Q)$.

Every array occurrence is inserted once in $O(B)$ time, and every query performs one $O(B)$ search. Total time is

$$
O(N\log N+Q\log Q+(N+Q)B),
$$

equivalent to the manifest's combined sorting form.

A distinct inserted path can create up to $B$ nodes, so the trie uses $O(NB)$ space in the worst case. The sorted indexed-query list and answer use $O(Q)$ space. Python sorting may also use linear temporary storage. Total space is $O(NB+Q)$, matching the manifest.

With $B=31$ fixed by the value bound, trie insertion and search are constant with respect to numeric magnitude, though retaining $B$ makes the bit dependence explicit.

## Alternatives and edge cases

- **Brute force per query:** Test every `nums` value no greater than `m` and keep the best XOR. It is simple but costs $O(NQ)$.
- **Persistent trie:** Build versions by sorted value and choose the version for each limit. It supports other query orders but uses more complex versioned storage.
- **Balanced ordered set alone:** Numeric closeness does not determine XOR maximum, so ordinary predecessor or successor queries are insufficient.
- **All numbers exceed `m`:** The trie is empty for that query and `search` returns `-1`.
- **Limit equals a number:** The insertion comparison is `<=`, so that value is correctly eligible.
- **Repeated limits:** No removal or duplicate reinsertion is needed; queries reuse the same activated prefix.
- **Repeated numbers:** They traverse the same trie path. Multiplicity does not affect a maximum with no deletions.
- **Zero values:** Their all-zero path is represented normally and may be the only eligible choice.
- **`x = 0`:** Maximizing XOR is equivalent to choosing the numerically largest eligible value; the bitwise greedy search does exactly that.
- **High leading bits:** Iteration from bit 30 ensures the most significant difference is prioritized.
- **Original query order:** Stored indices are essential because sorting by `m` changes evaluation order.
- **Input mutation:** `nums.sort()` permanently reorders the provided number list; `queries` itself is not mutated.
- **Fixed bit width:** The loop is correct for the stated nonnegative values up to $10^9$; larger values would require increasing the highest bit.
- **Empty internal branch:** Search falls back to the same-bit child, accepting a zero XOR bit when a one is impossible.
