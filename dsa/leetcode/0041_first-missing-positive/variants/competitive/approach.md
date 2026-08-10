## General

**Turn the array into its own presence table**

For an array of length $n$, the answer cannot exceed $n + 1$. If some value in $1$ through $n$ is absent, the answer is in that interval. If none is absent, those $n$ values fill the entire possible prefix and $n + 1$ is the first missing positive. Values below 1 or above $n$ therefore cannot be the answer and do not need presence slots.

The competitive solution uses index `v - 1` as the designated slot for value `v`. It repeatedly swaps useful values into their designated indices. After this placement phase, index `i` contains `i + 1` exactly when that positive value was available to place there. The first mismatch reveals the answer.

This technique is often called cyclic placement. It resembles cycle sort because a displaced value is immediately examined and moved toward its own destination, but it does not attempt to sort irrelevant values or order duplicate copies.

**Following the nested loop correctly**

The outer `for` visits every index `i`. The inner `while` continues only when the current value satisfies all of these conditions:

- it is at least 1;
- it is at most `len(nums)`;
- the destination at index `nums[i] - 1` does not already contain the same value.

If all hold, the multiple assignment swaps the current value with the value in its home. Python evaluates the right-hand side values before performing the assignments, so neither value is lost.

The same `i` is checked again because the swap delivers a new occupant there. For example, if index 0 contains `3` and index 2 contains `2`, placing `3` at index 2 brings `2` to index 0. That `2` still belongs at index 1, so a `while` can continue the placement chain without waiting for another outer-loop visit.

**Why duplicate values require the destination comparison**

Consider `[1, 1]`. The second `1` points to index 0, which already contains `1`. Swapping equal values would leave the list unchanged, so a loop based only on the numeric range would repeat forever. The condition `nums[nums[i]-1] != nums[i]` detects that a representative of this value is already at home and stops.

The destination test also suppresses pointless self-swaps. If value `i + 1` is already at index `i`, its destination is `i`, so the compared values are equal and the loop ends.

Python evaluates the chained range expression from left to right with short-circuit behavior. The destination expression is reached only after the value is known to be between 1 and $n$. This matters because a negative number would otherwise use negative indexing and an oversized number could access beyond the list.

**A progress argument for linear time and termination**

Whenever a swap is executed, let `v` be the value that started at `nums[i]`. The swap places `v` at index `v - 1`. The guard has already proved that this home did not contain `v`, so a new correct home is created.

The value displaced from index `v - 1` was not correctly homed there. A correctly homed value at that index would necessarily be `v`, contradicting the guard. Therefore, a swap never sacrifices one correct home to create another. The number of correct homes strictly increases, cannot exceed $n$, and proves there can be only $O(n)$ swaps in total even though the code contains nested loops.

**How the generator finds the first mismatch**

After placement, the return expression builds a generator over `enumerate(nums)`. For each `(i, x)`, it yields `i + 1` only if `x != i + 1`. The built-in `next` stops at the first yielded value. Because enumeration is left to right, that value is the smallest index-derived positive whose home is incorrect.

The second argument to `next` is `len(nums) + 1`. It is returned only if the generator yields nothing—that is, when every index `i` contains `i + 1`. In that case, all values from 1 through $n$ are present, so the previously established upper-bound argument proves $n + 1$ is correct.

The generator is lazy. It does not allocate a list of all mismatches; it examines elements only until the first mismatch is found. This preserves constant auxiliary space.

**Why a mismatch really means absence**

Suppose value `v` appears somewhere and lies in $[1,n]$. When the placement scan reaches a copy that is not at home, the loop moves it to index `v - 1`, unless that index already contains another `v`. Either outcome leaves `v` at its designated index. Later swaps cannot remove it: another value only targets its own different index, and a duplicate `v` is blocked rather than swapped with the homed copy.

Thus, if index `v - 1` is incorrect after placement, no copy of `v` existed. Conversely, if it contains `v`, that value necessarily came from the original array because the algorithm creates no values. The generator's first mismatch is exactly the smallest missing positive.

## Complexity detail

The placement pass has $n$ outer iterations. Across all inner loops, each successful swap creates a newly correct home and never destroys one, so there are at most $n$ swaps. The final lazy scan examines at most $n$ entries. Total time is $O(n)$ rather than $O(n^2)$.

Only loop variables and temporary references used by tuple assignment are needed. The generator expression and `enumerate` object maintain constant iterator state; they do not materialize an $n$-element collection. Because the input list provides the presence slots, auxiliary space is $O(1)$. The method does mutate that input list, which is allowed and is the key tradeoff behind the space bound.

## Alternatives and edge cases

- **Explicit second loop:** Returning on the first `nums[i] != i + 1` is equivalent to the `next` expression and may be easier for a beginner to debug. The generator version is concise and remains lazy.
- **Hash set:** Membership tests make the solution simple and expected $O(n)$ time, but the set requires $O(n)$ extra storage.
- **Boolean marker list:** Map value `v` to marker index `v - 1` without rearranging values. It has straightforward logic but violates the required $O(1)$ auxiliary-space bound.
- **In-place sign marking:** Normalize unusable cells and negate indexed positions to record presence. It meets the same bounds but has special cases for value `n` and repeated negations depending on the exact formulation.
- **Comparison sort:** Sorting and scanning works but costs $O(n \log n)$ time, failing the linear-time requirement.
- **Duplicates:** The destination equality guard is essential for termination and means one correctly placed copy is sufficient.
- **No `1`:** The first generator condition succeeds at index 0 and returns 1 immediately.
- **All required values present:** If the list is a permutation of `1` through `n`, placement makes every index correct and the default return is `n + 1`.
- **Irrelevant integers:** Zero, negatives, and values larger than `n` fail the range test and stay wherever swaps leave them. They cannot be the smallest missing positive.
- **Already-correct value:** Its destination is its current index, so the duplicate/destination guard stops without swapping.
- **Mutation visible to callers:** The constant-space strategy rearranges `nums`. Preserving the original array would require a copy and would change the auxiliary-space accounting.
