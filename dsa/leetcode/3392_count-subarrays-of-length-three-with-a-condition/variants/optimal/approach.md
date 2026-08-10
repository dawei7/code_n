## General

**Every length-three subarray has one middle index.** A window ending around center `i` is

`[nums[i-1], nums[i], nums[i+1]]`.

Valid centers range from one through `len(nums)-2`. This visits every contiguous length-three subarray exactly once: its middle position uniquely identifies it.

**Rewrite the half condition using integers.** The statement requires

$$
\texttt{nums}[i-1]+\texttt{nums}[i+1]
=\frac{\texttt{nums}[i]}2.
$$

Multiplying both sides by two gives

$$
2\bigl(\texttt{nums}[i-1]+\texttt{nums}[i+1]\bigr)
=\texttt{nums}[i].
$$

The source tests this equivalent relation directly:

`(nums[i - 1] + nums[i + 1]) * 2 == nums[i]`.

This avoids floating-point division and handles negative and odd middle values exactly.

**Why odd middle values cannot qualify.** The left side is always an even integer. If the middle value is odd, equality is impossible, matching the fact that half the middle is not an integer while the endpoint sum is.

**Use Boolean summation as a count.** The generator produces `True` for a valid window and `False` otherwise. In Python, these act as integers one and zero in `sum`. The result is the number of valid centers.

**Trace the first example.** Centers one, two, and three represent windows `[1,2,1]`, `[2,1,4]`, and `[1,4,1]`. Only the last satisfies $2(1+1)=4$, so the sum of Booleans is one.

**Trace negative values.** For window `[-1,-4,-1]`, endpoint sum is negative two and twice it is negative four, equal to the middle. The integer equation correctly counts it. No special sign handling is required.

**Why windows do not interact.** The task only counts; it does not select disjoint subarrays or modify values. Overlapping length-three windows are independent candidates and may both count.

**Use the middle as the loop variable, not the window start.** A start-index formulation would inspect `nums[start]`, `nums[start+1]`, and `nums[start+2]`. Setting `i=start+1` gives the exact source's three indices. Both enumerate $n-2$ windows, but the center formulation makes the algebra read naturally because `nums[i]` is the value being halved.

**Trace an odd center carefully.** For `[0,1,0]`, endpoint sum is zero. Integer floor division would say `1 // 2 = 0` and incorrectly accept it. The exact doubled test compares zero with one and rejects it. This example demonstrates why avoiding `//` is a correctness requirement, not merely a style preference.

**Trace cancellation at a zero center.** Window `[-3,0,3]` qualifies because the endpoints sum to zero, which is exactly half of zero. Endpoint values need not be equal; only their sum matters.

**Boolean expressions have integer values in Python.** `sum` starts at numeric zero. Each generated `True` adds one and each `False` adds zero. The method returns an integer count even though the generator elements are Boolean objects.

**The input bounds prevent arithmetic concerns.** Each endpoint sum lies between -200 and 200, and doubling lies between -400 and 400. Python would be safe for much larger values as well, but the stated domain makes overflow impossible even in ordinary fixed-width integer languages.

**Why the range bounds are exact.** Center zero would access index negative one as a wraparound Python element rather than a real left neighbor. Center `n-1` has no right neighbor. `range(1,n-1)` excludes both invalid cases and includes all others.

**Why the one-line method is complete.** Every candidate window maps to exactly one generated center. The Boolean condition is algebraically equivalent to the problem statement. Summing true outcomes therefore gives neither omissions nor duplicates.

**No division means no rounding ambiguity.** Writing `nums[i] // 2` would be wrong for odd values because floor division changes “exactly half” into a rounded integer. Writing `nums[i] / 2` uses floating point unnecessarily. Cross-multiplication preserves exact mathematical equality.

## Complexity detail

For array length $n$, the generator evaluates $n-2$ centers. Each does constant arithmetic and indexing, so time is $O(n)$.

The generator is consumed lazily by `sum` and stores no list of results. Auxiliary space is $O(1)$. The input array is read only.

## Alternatives and edge cases

- **Explicit loop and counter:** It is equivalent and may be easier for beginners to debug.
- **Sliding window object:** Maintaining a queue is unnecessary because direct indexing already exposes all three values.
- **Floating-point half:** It is avoidable and less exact than multiplication.
- **Floor division:** It would incorrectly accept some odd-middle cases.
- **Odd-center counterexample:** `[0,1,0]` exposes the floor-division bug.
- **Minimum length three:** Exactly one center is examined.
- **Odd middle:** It can never satisfy the doubled integer equation.
- **Even middle:** It qualifies only when endpoints sum to its exact half.
- **Negative middle:** Cross-multiplication handles it normally.
- **Zero middle:** Endpoints must sum to zero.
- **Different cancelling endpoints:** Values such as -3 and 3 can qualify around zero.
- **Overlapping valid windows:** Each is counted independently.
- **Repeated values:** They have no special behavior.
- **Boolean arithmetic:** `True` contributes one and `False` contributes zero.
- **Return type:** Summing Booleans produces an integer.
- **Index safety:** Center range guarantees both neighbors exist.
- **Input preservation:** No element is changed.
- **Annotation import:** `List` must be available.
