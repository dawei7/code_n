## General

**Every candidate is one adjacent pair**

A length-two subarray beginning at index `i` contains `nums[i]` and `nums[i+1]`. Therefore, there are exactly $n-1$ candidate sums:

$$
\texttt{nums}[0]+\texttt{nums}[1],\;
\texttt{nums}[1]+\texttt{nums}[2],\;\ldots
$$

The task asks whether any sum occurs for two different starts. It does not require the subarrays to be disjoint. Adjacent candidates may overlap in one element, as in `[4,2]` and `[2,4]`.

**Scan adjacent pairs lazily**

`pairwise(nums)` yields each consecutive value pair `(a, b)` exactly once, in increasing start-index order. The code computes its sum with a walrus assignment:

```python
if (x := a + b) in vis:
```

This both stores the sum in `x` and tests whether an earlier pair produced it.

If the sum is already present, the earlier occurrence necessarily began at a different index because the current pair has not yet been inserted. The method can return true immediately; the question asks only for existence.

If not present, `vis.add(x)` remembers it for all later starts.

**Why a set is sufficient**

The algorithm does not need to remember which earlier index produced a sum. Membership alone proves that at least one different start exists. It also does not need frequencies beyond one: once a second occurrence appears, the answer is already known.

Hash sets support expected constant-time membership and insertion for integer keys, turning a comparison against all earlier sums into one lookup.

**Trace overlapping subarrays**

For `nums = [4, 2, 4]`, `pairwise` first yields `(4, 2)` with sum six. The set is empty, so six is inserted.

The next pair is `(2, 4)`, also sum six. Membership succeeds and the function returns true. These subarrays overlap at the middle value, but begin at indices zero and one, satisfying the problem.

For `[0, 0, 0]`, the first sum zero is stored and the second sum zero repeats it. Equal contents are irrelevant; different start positions make them distinct subarrays.

**Maintain the seen-sums invariant**

Before processing the pair beginning at index `i`, `vis` contains exactly the sums of length-two subarrays beginning at indices smaller than `i`.

The invariant is true before the first pair because there are no earlier starts. If the current sum is new, adding it establishes the invariant for the next iteration. If it is already present, the invariant proves there is an earlier different start with the same sum, so returning true is correct.

If the loop finishes without a match, every candidate sum was new when encountered. All $n-1$ sums are distinct, so no required pair of subarrays exists and false is correct.

**Negative and large values pose no structural issue**

Sums can be negative, zero, or positive. Python set keys handle all integer signs, and equality is the only required operation. Two very different value pairs may share a sum, which is exactly what should be detected.

Python integers also avoid overflow for values up to magnitude $10^9$. In a fixed-width language, the pair sum still fits signed 32-bit under these particular bounds, but using the language's normal safe integer type is prudent.

**Why content equality is not required**

The condition compares sums, not the two elements themselves. Pairs `[1,4]` and `[2,3]` qualify because both sum to five. Storing sums rather than pair tuples captures this correctly.

**Why the index condition is automatic**

`pairwise` generates one tuple for each start index in order. The set contains only sums from previously generated starts. Therefore, a membership hit always compares two distinct positions without explicitly storing indices.

## Complexity detail

Let $n$ be the array length. The iterator produces $n-1$ pairs. Each performs one addition plus expected $O(1)$ hash-set lookup and, unless returning, insertion. Expected total time is $O(n)$.

In the worst case, all pair sums differ, so the set stores $n-1$ integers and uses $O(n)$ space. Early success may use less.

Under a theoretical adversarial hash-collision model, set operations can degrade, but expected linear behavior is the standard analysis for integer hashing.

## Alternatives and edge cases

- **Nested comparison of pair sums:** It uses no set but takes $O(n^2)$ time in the worst case.
- **Sort all pair sums:** Sorting can detect adjacent equal sums in $O(n\log n)$ time and $O(n)$ space, but hashing is faster on average.
- **Fixed frequency array:** Value sums range from $-2\cdot10^9$ to $2\cdot10^9$, making a direct domain array impractical.
- **Exactly two input elements:** There is only one length-two subarray, so the method stores one sum and returns false.
- **Overlapping subarrays:** They are allowed as long as starts differ.
- **Identical pair contents:** Different positions still count as different subarrays.
- **Different contents, equal sum:** The set detects them because only the sum matters.
- **Negative sums:** They are ordinary set keys.
- **Early return:** The first repeated sum is sufficient; later candidates cannot change the Boolean answer.
- **No repetition:** Exhausting the iterator proves every start has a distinct sum.
