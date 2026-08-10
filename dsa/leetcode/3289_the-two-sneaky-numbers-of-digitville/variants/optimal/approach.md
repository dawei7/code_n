## General

**Use the unusually strong frequency guarantee.** The input is built from every integer in the range $[0,n-1]$ appearing once, after which exactly two of those values are added one extra time. Therefore exactly two values have frequency two, and every other value has frequency one. The task is not to reconstruct an unknown complicated distribution; it is simply to identify the two frequency-two entries.

The exact source expresses that observation with `Counter(nums)`. A `Counter` is a mapping from each distinct value to the number of times it occurs. Constructing it performs one pass over `nums`. For a simple example, if `nums = [0, 1, 1, 0]`, the mapping is logically `{0: 2, 1: 2}`. For a larger example such as `[0, 1, 2, 3, 2, 1]`, the counts of $1$ and $2$ are two while the counts of $0$ and $3$ are one.

The list comprehension `[x for x, v in cnt.items() if v == 2]` then visits every distinct key-count pair. It includes the key `x` exactly when its count `v` equals two. By the construction guarantee, this condition holds for precisely the two sneaky numbers, so the returned list has exactly the required two values.

**Why checking equality with two is correct.** In a more general duplicate-finding problem, a value might appear three or more times, and checking `v == 2` could miss it. That concern does not apply here. The original range contributes one copy of every value, and each of the two selected sneaky values receives one additional copy. The two sneaky values are distinct because the statement says that two elements each appear twice. Hence no count can exceed two. The code deliberately relies on this contract rather than defending against malformed inputs outside it.

**The output order is intentionally unspecified.** The problem permits the two values in any order. Modern Python dictionaries, and therefore `Counter`, preserve the order in which distinct keys are first encountered. As a result, this exact implementation normally returns the two duplicated values in the order of their first occurrences in `nums`. That behavior is harmless but is not part of the correctness argument. A judge must accept either ordering, and callers should not infer that the result is numerically sorted.

**A direct proof from the counts.** Consider any returned value $x$. The comprehension returned it only because `cnt[x] == 2`, and under the input construction only a sneaky number occurs twice; therefore every returned value is valid. In the other direction, consider either sneaky number $y$. Its original copy and its one added copy make `cnt[y] == 2`, so the comprehension necessarily returns it. These two directions show that the result contains no false values and omits no required value.

The source is shorter than the reasoning because `Counter` encapsulates the counting loop. An equivalent manual implementation would initialize an empty dictionary, increment `count[x]` for each number, and finally select keys with value two. Using the library abstraction does not change the algorithm.

**Source and manifest must not be confused.** The Optimal manifest summary describes a set distinguishing first occurrences from repeated occurrences, but the protected Optimal source shown here does not use a set. It constructs a complete `Counter` and filters the frequency table. Both ideas have the same $O(n)$ asymptotic time and space under ordinary hash-table assumptions, yet learners should understand the actual frequency-counting data flow because that is what this file documents.

The snippet also assumes `Counter` is already available in the execution environment, normally through `from collections import Counter`. If the surrounding harness does not provide that import, it must be added for the standalone Python file to run. That import detail is separate from the algorithm's correctness.

## Complexity detail

Let $N$ denote `len(nums)`. Because the array contains the $n$ base values plus two extra values, $N=n+2$, so using either symbol gives the same asymptotic result. Building the counter reads all $N$ elements once and takes expected $O(N)$ time with Python's hash table. Iterating through `cnt.items()` visits exactly $n$ distinct keys, which is also $O(N)$. The total expected time is $O(N)$.

The counter stores one entry for every distinct number, namely $n=N-2$ entries, so the auxiliary space is $O(N)$. The returned list always contains exactly two integers and therefore occupies $O(1)$ result space, but that does not remove the linear counter storage. Hash operations on Python integers are constant time here. In adversarial models that do not grant expected constant-time hashing, dictionary bounds require qualification, but ordinary Python complexity analysis uses the expected bound.

## Alternatives and edge cases

- **Seen set plus duplicate list:** On the first occurrence, insert the value into a set; on the second, append it to the result. This avoids storing explicit counts but still takes expected $O(N)$ time and $O(N)$ auxiliary space. It also matches the manifest summary more closely than the exact source does.
- **Boolean or integer array:** Since every value lies in $[0,n-1]$, an array indexed by value can record whether each number has appeared. This gives deterministic $O(N)$ time and $O(n)$ space without hashing.
- **In-place sign marking:** Many duplicate problems mark an index by negating an array entry. Here zero needs special handling, input mutation may be undesirable, and the clean range guarantee makes counting easier to explain and safer to use.
- **Algebra with sums and squares:** The excess sum gives the sum of the two sneaky numbers, while an excess square-sum can derive their product and then the two roots. Python avoids overflow, but fixed-width languages need careful integer sizing, and the method is less robust and less transparent than counting.
- **XOR partitioning:** XORing the full input with $0$ through $n-1$ leaves the XOR of the two duplicates. A distinguishing set bit can partition both collections and recover each duplicate in $O(N)$ time and $O(1)$ auxiliary space. It is more space-efficient but considerably less beginner-friendly.
- **Sorting:** After sorting, equal adjacent values reveal the two duplicates. This costs $O(N\log N)$ time and either mutates the input or uses $O(N)$ space for a copy, so it gives up the linear-time advantage.
- **Smallest legal input:** When $n=2$, the input length is four and both values $0$ and $1$ are duplicated. The counter returns both; there is no special boundary case.
- **Duplicates next to each other or far apart:** Position and separation do not matter. Counting aggregates occurrences regardless of where they appear.
- **Zero as a sneaky value:** Zero is an ordinary dictionary key and needs no special treatment, unlike some arithmetic or sign-marking techniques.
- **Unsorted return order:** The problem accepts any order. If an external caller demands increasing order, it could sort the two-element result in constant asymptotic time, but that behavior is not required by this contract.
- **Malformed frequency greater than two:** The exact `v == 2` filter would exclude a value occurring three times. This is acceptable only because the stated input construction rules that case out; changing the contract would require changing the predicate.
