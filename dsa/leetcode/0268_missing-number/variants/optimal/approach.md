## General

**Turn “one missing value” into pair cancellation**

The array has length $n$, while the complete allowed range `[0, n]` contains $n+1$ values. The uniqueness guarantee and the statement that exactly one value is missing mean that `nums` is precisely the complete range with one member removed. This is stronger than merely saying that every array value lies inside the range: it allows the algorithm to compare the complete collection with the observed collection and cancel every value that occurs in both.

The exact protected solution performs that cancellation with bitwise XOR. It does not use the arithmetic-sum method described by the variant summary. Both ideas have linear time and constant auxiliary space, but understanding this source requires following its XOR expression exactly.

XOR has three properties that matter here:

$$
x \oplus x = 0,
\qquad
x \oplus 0 = x,
$$

and XOR is both associative and commutative. Associativity allows parentheses to be regrouped, while commutativity allows terms to be reordered. Therefore, if the same number appears twice anywhere in a long XOR expression, its two copies can be brought together and reduced to zero. Zeros then disappear from the expression.

Suppose the missing value is $m$. XORing every expected value with every observed value gives

$$
(0 \oplus 1 \oplus \cdots \oplus n)
\oplus
\left(\bigoplus_{v \in \texttt{nums}} v\right).
$$

Every value other than $m$ appears once in the complete range and once in `nums`, so those two copies cancel. The missing value appears only in the complete range, so it is the only term left. The result is exactly $m$.

**Why the source enumerates from one instead of zero**

The code uses `enumerate(nums, 1)`. For an array of length $n$, this produces pairs whose indices are `1, 2, ..., n`, not the usual `0, 1, ..., n - 1`. The generator contributes `i ^ v` for each pair, so all of its generated terms together are

$$
(1 \oplus \texttt{nums}[0])
\oplus
(2 \oplus \texttt{nums}[1])
\oplus \cdots \oplus
(n \oplus \texttt{nums}[n-1]).
$$

After regrouping, this is the XOR of all expected numbers `1` through `n` and all observed values. The expected range technically begins at zero, but zero does not need to be generated because $x \oplus 0 = x$. Thus `1` through `n` represents the entire expected range for XOR purposes.

Starting enumeration at one is a compact way to include the endpoint $n$. A more familiar implementation might initialize an accumulator to `n` and enumerate the array from zero. That would combine `n`, indices `0` through `n - 1`, and all values. The exact source instead shifts the enumerated indices to `1` through `n`; the two formulations contain the same meaningful expected terms because the omitted zero has no effect.

**How the lazy reduction evaluates the expression**

For each pair `(i, v)`, the generator computes `i ^ v`. `reduce(xor, generator)` then XORs all generated values into one result. Because XOR is associative, it makes no mathematical difference that each expected index is first XORed with its corresponding array value. The terms can still be conceptually flattened and regrouped into “all expected values” and “all observed values.”

The generator is lazy. It does not first create a list containing all $n$ pairwise XOR results. `reduce` requests one result, incorporates it into its accumulator, then requests the next. At every moment, only the enumeration state, the current pair, the current generated integer, and the reduction accumulator are needed.

The call to `reduce` has no explicit initializer. That is safe for every legal input because the constraints say $n \ge 1$, so `nums` contains at least one value and the generator is nonempty. `reduce` uses the first generated value as its initial accumulator and combines the rest into it. This detail matters: an empty generator without an initializer would raise an exception, but an empty array is outside the stated contract.

**Trace `nums = [3, 0, 1]`**

Here $n=3$, so `enumerate(nums, 1)` supplies the following pairs:

| Expected term `i` | Observed term `v` | Generated `i ^ v` |
|---:|---:|---:|
| 1 | 3 | 2 |
| 2 | 0 | 2 |
| 3 | 1 | 2 |

The reduction computes `2 ^ 2 ^ 2`, which is `2`. The cancellation is clearer when the terms are expanded and reordered:

$$
(1 \oplus 3) \oplus (2 \oplus 0) \oplus (3 \oplus 1)
= (1 \oplus 1) \oplus (3 \oplus 3) \oplus 0 \oplus 2
= 2.
$$

The numbers `1` and `3` occur in both collections and cancel; `0` is neutral; `2` occurs only among the expected terms and remains.

For `nums = [0, 1]`, the expected enumeration terms are `1` and `2`. Expanding the expression gives `1 ^ 0 ^ 2 ^ 1`. The two `1` terms cancel, zero changes nothing, and `2` remains. This shows that the endpoint $n$ is handled naturally even though it is not a valid ordinary zero-based array index.

For `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`, the expected side supplies every number from `1` through `9`. The observed side supplies every number from `0` through `9` except `8`. Regardless of the array's order, matching values cancel and `8` remains. No sorting is necessary because XOR itself is order-independent.

**Why this identifies the answer uniquely**

The cancellation proof depends on the contract's exact guarantees. Each nonmissing value appears exactly once in `nums`, so it appears exactly twice across the expected and observed collections. The missing value appears exactly once across them. That leaves one uncancelled term and proves the returned value is the required missing number. If duplicates were allowed or more than one value were absent, several terms could survive and their XOR would not in general identify any one missing value. The method is correct because the input rules create precisely the pairing structure XOR needs.

## Complexity detail

Let $n$ be `len(nums)`. `enumerate` visits every array element once, the generator performs one pairwise XOR per element, and `reduce` combines the $n$ generated values using $n-1$ more XOR operations. Under the standard word-RAM model, each operation is constant time, so the total time complexity is $O(n)$.

This is asymptotically optimal. An algorithm must account for every array element in the worst case: if it ignored some position, changing only that unseen value could change which number is missing while leaving everything the algorithm inspected unchanged. Therefore, the linear scan is not avoidable in the general case.

The extra-space complexity is $O(1)$. `enumerate` and the generator expression are lazy iterators rather than length-$n$ containers. The reduction maintains one integer accumulator, and the loop machinery holds only a constant number of current values. The algorithm does not allocate a set, copy the input, or sort it. It also leaves `nums` unchanged.

Python integers do not overflow, while fixed-width languages can also safely use XOR as long as every legal value fits the chosen integer type. More formally, bitwise work on arbitrarily large integers depends on their bit length; with values at most $n$, one XOR costs $O(\log n)$ bit operations. Conventional interview complexity treats an input-sized integer as one machine word, yielding the stated $O(n)$ time and $O(1)$ word-space bounds.

## Alternatives and edge cases

- **Arithmetic-sum difference:** Compute $n(n+1)/2$ and subtract `sum(nums)`. This also achieves $O(n)$ time and $O(1)$ extra space and is the method named by the manifest summary, but it is not the exact protected source. In fixed-width languages, the intermediate product or sum may overflow unless a sufficiently wide type or careful multiplication order is used.
- **Sort and find the first mismatch:** After sorting, compare each value with its expected position. This is intuitive but costs $O(n \log n)$ time and either mutates the input or requires a copy.
- **Hash set:** Store every observed value and scan `[0, n]` for the absent one. Expected time is $O(n)$, but the set requires $O(n)$ additional space, so it misses the follow-up's constant-space target.
- **Mark values in the input:** Some problems permit sign marking or cyclic placement. Here zero and $n$ complicate ordinary sign marking, and modifying the caller's array is unnecessary when XOR solves the problem without mutation.
- **Missing zero:** Zero is absent from `nums`, while every value `1` through `n` appears on both sides and cancels. The result becomes zero even though the source never explicitly contributes an expected zero term, because zero is XOR's identity.
- **Missing `n`:** The shifted enumeration explicitly contributes $n$, and no array value cancels it. This is why using `enumerate(nums, 1)` rather than ordinary zero-based enumeration is essential in the one-line formulation.
- **Array order:** The values may be arbitrarily arranged. Associativity and commutativity make the cancellation independent of positions, so no sortedness assumption is hidden in the method.
- **One-element input:** If `nums = [0]`, the only generated value is `1 ^ 0 = 1`, so the answer is `1`. If `nums = [1]`, the result is `1 ^ 1 = 0`, so the answer is `0`.
- **Empty input outside the contract:** Mathematically, an empty array would correspond to $n=0$ and missing value zero. The exact `reduce` call has no initializer, however, so it would raise an exception on an empty generator. This does not affect correctness for the legal constraint $n \ge 1$.
- **Duplicates or multiple missing values:** These violate the contract. XOR would still produce an integer, but it would represent the XOR of all unmatched terms rather than necessarily being a missing value, so the result would have no promised interpretation.
- **No overflow concern:** Unlike summation, XOR never produces carries and cannot require more bits than its operands. This makes the technique especially useful in fixed-width environments while preserving the same linear-time, constant-space bounds.
