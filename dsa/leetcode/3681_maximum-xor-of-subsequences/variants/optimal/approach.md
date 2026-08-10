## General

At first, selecting two subsequences seems to create two independent combinatorial choices. The permission for those subsequences to overlap is the key simplification. After examining what one array occurrence contributes to `X XOR Y`, the problem becomes the standard maximum subset-XOR problem.

**Combining the two subsequences into one selection**

For an occurrence with value `v`, there are four possible membership choices:

- it belongs to neither subsequence, so it contributes nothing;
- it belongs only to the first subsequence, so it contributes `v` through `X`;
- it belongs only to the second subsequence, so it contributes `v` through `Y`; or
- it belongs to both subsequences, so its two contributions cancel because `v XOR v = 0`.

Therefore, an occurrence affects `X XOR Y` exactly when it is selected in **one** of the two subsequences, but not both. If $A$ and $B$ denote the sets of selected indices, the relevant indices are their symmetric difference $A \mathbin{\triangle} B$.

Because XOR is associative and commutative,

$$
X \mathbin{\mathrm{XOR}} Y
=
\mathop{\mathrm{XOR}}_{i \in A \mathbin{\triangle} B} \texttt{nums}[i].
$$

Any subset of array indices can be written in increasing order and is therefore a valid subsequence. Conversely, every subset XOR can be realized in the original problem by choosing those indices for the first subsequence and choosing the second subsequence to be empty. The empty subsequence is explicitly allowed and has XOR zero.

Thus, the set of achievable values of `X XOR Y` is exactly the set of XORs of arbitrary subsets of `nums`. The task is to find the largest value in that set.

**Viewing integers as binary vectors**

XOR behaves like addition over the two-element field: each bit is added modulo two, with no carry between positions. An integer can therefore be viewed as a vector of bits, and the XOR of a subset is a linear combination of the corresponding vectors with coefficients zero or one.

A linear basis stores only independent vectors while preserving every XOR value obtainable from all processed numbers. The source allocates

`basis = [0] * 31`

where `basis[bit]` is either zero or a vector whose highest set bit is `bit`. The input is nonnegative and at most $10^9$, so 31 slots indexed from $0$ through $30$ safely cover every possible set bit. In fact, $10^9 < 2^{30}$, making the top slot harmless extra capacity.

**Inserting one number by eliminating leading bits**

For each input `value`, `current` begins as that value. Bits are considered from $30$ down to $0$.

If `current` does not have the current bit set, there is nothing to eliminate at that position, so the loop continues downward.

If the bit is set and `basis[bit]` already contains a vector, XORing that basis vector into `current` clears the bit. This works because both values have that bit set, and $1 \mathbin{\mathrm{XOR}} 1 = 0$. The stored vector has no bit above `bit`, so this operation cannot reintroduce any higher bit that was already eliminated.

If the bit is set and the slot is empty, `current` has a leading bit that no existing basis vector has. It is independent of the stored vectors, so the source saves it in `basis[bit]` and stops processing this input.

Sometimes repeated elimination reduces `current` to zero. That means the original value is an XOR combination of existing basis vectors. It adds no new achievable result and does not need to be stored.

As a small example, suppose the basis first receives $5=101_2$ and then $3=011_2$. Five is stored with leading bit $2$, and three is stored with leading bit $1$. If $6=110_2$ arrives later, its leading bit $2$ is cleared with five, producing $011_2$; that is then cleared with three, producing zero. Indeed, $6=5 \mathbin{\mathrm{XOR}} 3$, so the third vector was dependent.

After every insertion, two properties hold:

- every stored basis vector is an XOR of processed input values, so the basis cannot manufacture an unreachable value; and
- every processed input value is either stored independently or was reduced using stored vectors, so it remains expressible as an XOR of the basis.

It follows that the basis and the full processed prefix generate exactly the same set of subset-XOR values.

**Constructing the numerically largest reachable XOR**

Once the basis is complete, the source starts with

`answer = 0`

and visits basis vectors from the highest slot to the lowest using `reversed(basis)`. For each vector, it compares the current answer with `answer ^ vector` and keeps the larger value.

This greedy comparison is valid because a vector stored at position `bit` has no set bit above `bit`. When it is considered, choices about higher bits have already been finalized. XORing the vector cannot change any of those higher bits.

At its own leading bit, the vector toggles the answer. If that bit is currently zero, toggling it to one makes the result larger regardless of all lower-bit changes. If it is currently one, toggling it to zero makes the result smaller regardless of lower bits. The `max` expression makes exactly the favorable choice. Later vectors have lower leading bits and can never undo a decision at a higher bit.

This is equivalent to maximizing a binary number lexicographically from its most significant bit downward. After the final vector, no reachable XOR can have a better highest differing bit than `answer`, so `answer` is the maximum subset XOR and therefore the maximum possible `X XOR Y` for the original two-subsequence problem.

For `nums = [5, 2]`, the vectors have different leading bits and remain independent. Starting from zero, the maximization phase uses both to produce $5 \mathbin{\mathrm{XOR}} 2 = 7$. For `[1,2,3]`, the value $3$ is dependent because $3=1 \mathbin{\mathrm{XOR}} 2$, but the basis still generates $3$, which is the desired maximum.

## Complexity detail

Let $n$ be the array length and let $B=31$ be the number of represented bit positions.

Inserting one number examines at most $B$ bits and performs at most one constant-time XOR operation per bit. Processing all numbers therefore takes $O(nB)$ time. The maximization pass examines the $B$ basis slots once, taking $O(B)$ additional time. Altogether, the running time is $O(nB)$, which is effectively $O(n)$ under the fixed $10^9$ value bound.

The basis contains exactly $B$ integer slots, so its auxiliary space usage is $O(B)$. No collection grows with the number of input elements. Under the fixed constraints, this is constant auxiliary space, while the manifest keeps the more informative bit-width notation `O(B)`.

The rank of the basis can never exceed $B$, even when $n$ is $10^5$. This is the source of the improvement over enumerating subsequences: exponentially many index selections collapse into combinations of at most 31 independent directions.

## Alternatives and edge cases

- **Enumerate subsequences:** There are $2^n$ index subsets, so evaluating every subset XOR is infeasible for $n$ up to $10^5$.
- **Maintain every reachable XOR:** Repeatedly add `old_xor ^ value` to a set of reachable values. The set can grow to $2^B$ distinct values, which is far larger than the 31-vector basis.
- **Use a bitwise trie for array elements:** A trie can maximize the XOR of two stored elements, but the optimum here may require XORing many elements. It does not directly represent the span of all subset XORs.
- **Treat the subsequences as disjoint:** The statement explicitly allows overlap. More importantly, the symmetric-difference reduction already accounts for overlap: occurrences chosen twice cancel, and every remaining subset is achievable.
- **Order of selected indices:** XOR does not depend on order, and every selected index set has a unique increasing order, so the subsequence requirement imposes no extra restriction.
- **Both subsequences empty:** This produces zero. The basis maximization starts from zero, so the empty choice is always available if no positive value can be formed.
- **Zero values:** Zero reduces immediately and never enters the basis. Including or excluding it cannot change any XOR.
- **Duplicate or dependent values:** A value that reduces to zero adds no new combination. Discarding it from the basis does not discard any achievable XOR.
- **All values zero:** Every basis slot remains zero, every maximization step leaves `answer` unchanged, and the method correctly returns zero.
- **Highest bit handling:** The loop includes bit $30$, while values up to $10^9$ need only bits $0$ through $29$. The extra zero slot is safe and keeps the implementation within a conventional 31-bit nonnegative range.
