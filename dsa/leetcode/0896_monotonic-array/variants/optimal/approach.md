## General

An array is monotonic when it satisfies at least one of two complete possibilities:

- every adjacent step is nondecreasing;
- every adjacent step is nonincreasing.

Checking adjacent pairs is sufficient even though the definition quantifies over every $i\le j$. If each neighboring relation is nondecreasing, transitivity gives

$$
\text{nums}[i]\le\text{nums}[i+1]\le\cdots\le\text{nums}[j]
$$

for every earlier $i$ and later $j$. The same transitive chain works with $\ge$ for a nonincreasing array.

The exact solution performs these two checks separately:

```text
asc = all(a <= b for a, b in pairwise(nums))
desc = all(a >= b for a, b in pairwise(nums))
return asc or desc
```

`pairwise(nums)` produces consecutive pairs $(\text{nums}[0],\text{nums}[1])$, $(\text{nums}[1],\text{nums}[2])$, and so on. The first generator asks whether every pair moves upward or stays equal. The second uses a fresh `pairwise` iterator and asks whether every pair moves downward or stays equal.

**Equality is allowed in both directions.** “Monotone increasing” in this problem means nondecreasing, not strictly increasing. Thus `a <= b` accepts an equal adjacent pair. Similarly, `a >= b` accepts equality for nonincreasing order. A constant array satisfies both properties.

**Why the final operation is OR.** The array needs to be monotone in either direction, not both. A rising array makes `asc` true and `desc` false. A falling array does the reverse. A constant or one-element array can make both true. Only a sequence that changes direction makes both false.

For `[1,2,2,3]`, every adjacent pair satisfies `<=`, so `asc` is true. The equal middle pair causes no issue. For `[6,5,4,4]`, every pair satisfies `>=`, so `desc` is true. For `[1,3,2]`, pair $(3,2)$ breaks ascending order and pair $(1,3)$ breaks descending order; both results are false.

**Why a local reversal proves global failure.** If the array contains at least one strict increase and at least one strict decrease, it cannot be globally nondecreasing because the decrease violates one required adjacent inequality, and it cannot be globally nonincreasing because the increase violates the other. Their positions need not be adjacent to each other; the two full scans detect them independently.

Another way to state the same invariant is to classify every adjacent difference `nums[i + 1] - nums[i]`. A nondecreasing array allows positive and zero differences but no negative one. A nonincreasing array allows negative and zero differences but no positive one. The array is nonmonotonic precisely when the scan contains at least one positive and at least one negative difference. The exact code avoids subtraction, which also avoids any overflow concern in fixed-width languages, and checks the equivalent inequalities directly.

The adjacent-to-global implication can also be proved by induction on distance. For positions $i<j$, the base distance one is the adjacent check. Assume the nondecreasing relation holds from $i$ through $j-1$. The final adjacent check gives $\text{nums}[j-1]\le\text{nums}[j]$, and transitivity combines it with $\text{nums}[i]\le\text{nums}[j-1]$ to prove $\text{nums}[i]\le\text{nums}[j]$. Thus checking all adjacent links really does establish every pair required by the formal definition.

Python's `all` short-circuits. The ascending scan stops at its first decrease, and the descending scan stops at its first increase. The second scan still starts from the beginning because `pairwise(nums)` is called again rather than reusing an exhausted iterator.

**Arrays of length one.** `pairwise` produces no pairs. Mathematically, every universal condition over an empty set of comparisons is true, and Python's `all` of an empty iterable returns true. A single value is correctly considered monotonic in both directions.

The method reads values only through adjacent comparisons and never changes the input.

## Complexity detail

Let $n$ be the array length. Each `all` call examines at most $n-1$ adjacent pairs. Two passes are still linear.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space because `pairwise` and the generator expressions are lazy.

Short-circuiting can reduce actual comparisons on a nonmonotonic array, but the worst case completes both scans.

## Alternatives and edge cases

- **One pass with two flags:** Maintain “still nondecreasing” and “still nonincreasing” while scanning once. This avoids the second pass but has the same asymptotic bounds.
- **Infer direction from the first pair:** Equal leading values make direction undecided, so the method needs to skip ties or maintain both possibilities carefully.
- **Sort and compare:** Comparing with sorted and reverse-sorted copies works but costs $O(n\log n)$ time and $O(n)$ extra space.
- **Compare every pair $i<j$:** This follows the definition literally but costs $O(n^2)$; adjacent transitivity makes it unnecessary.
- **One element:** Both `all` checks are vacuously true.
- **All equal:** Every adjacent pair satisfies both inequalities.
- **Strictly increasing:** Ascending succeeds and descending fails at the first increase.
- **Strictly decreasing:** Descending succeeds and ascending fails at the first decrease.
- **Plateaus:** Equal runs are legal in either monotonic direction.
- **One increase and one decrease:** Each direction has a violating adjacent pair, so the result is false.
- **Negative values:** Only ordering matters; sign does not change the logic.
- **Fresh iterators:** Calling `pairwise(nums)` twice is necessary because one generator cannot be replayed after consumption.
- **No input mutation:** The original element order remains unchanged.
