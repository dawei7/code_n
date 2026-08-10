## General

**Search the value range without rearranging the array**

The array has length $n+1$, but every value lies from 1 through $n$. The extra array position guarantees a duplicate by the pigeonhole principle: placing $n+1$ entries into only $n$ possible value categories forces at least one category to contain multiple entries.

The exact protected solution does not use the cycle-detection method described by the manifest. It binary-searches the possible duplicate value using a counting predicate. This respects the requirements because it only reads `nums` and keeps no set, copied array, or other size-dependent structure.

For a candidate value $x$, define

$$
C(x)=\#\{v\in\texttt{nums}:v\le x\}.
$$

The helper `f(x)` returns whether `C(x) > x`. The solution finds the smallest $x$ for which this predicate is true.

**Why compare the count with `x`**

There are exactly $x$ possible values in the range `[1, x]`. If more than $x$ array entries fall into that range, at least one of those values must repeat. This is another direct pigeonhole argument: more than $x$ entries are occupying only $x$ value categories.

The special contract that only one distinct number repeats makes the first overloaded prefix identify that repeated value exactly. Before the duplicate value enters the prefix, no value in the prefix can occur more than once. Once the duplicate enters, the prefix contains too many entries for its number of possible values.

**Prove the predicate is false before the duplicate**

Let the one repeated value be $d$. For any $x<d$, the prefix `[1, x]` excludes every occurrence of $d$. Every value it does include occurs at most once, because no other distinct value repeats.

There are only $x$ possible values in that prefix, so at most $x$ array entries can be at most $x$:

$$
C(x)\le x.
$$

Therefore, `f(x)` is false for every $x<d$.

Some values in `[1, x]` may be missing from the array, making the count strictly smaller than $x$; that only strengthens the false result.

**Prove the predicate is true at and after the duplicate**

Suppose $d$ appears $r\ge2$ times. Every other value that appears occurs once. Since the array contains $n+1$ entries, the number of distinct nonduplicate values present is $n+1-r$. Including $d$ itself, the number of distinct present values is $n+2-r$, so exactly

$$
n-(n+2-r)=r-2
$$

values from the full range `[1, n]` are missing.

For any $x\ge d$, begin with the $x$ possible values in `[1, x]`. At worst, all $r-2$ missing values lie inside this prefix, subtracting $r-2$ entries. The repeated value contributes $r-1$ extra occurrences beyond its first. Hence

$$
C(x)
\ge
x-(r-2)+(r-1)
=x+1.
$$

Thus `C(x) > x`, so `f(x)` is true for every $x\ge d$.

This argument covers the less obvious case where the duplicate occurs three or more times and several other allowed values are absent. The predicate still has the exact shape

```text
x:     0  1 ... d-1 | d d+1 ... n
f(x):  F  F ... F   | T  T  ... T
```

The first true position is exactly $d$.

**How the helper computes the prefix count**

The expression `v <= x for v in nums` lazily produces one Boolean per array element. In Python arithmetic, `True` contributes 1 and `False` contributes 0. `sum(...)` therefore equals the number of entries no greater than `x`.

The generator is lazy and does not allocate a Boolean list. Every predicate evaluation scans all array values but uses only a running sum and current element.

**How `bisect_left` searches Boolean keys**

The source calls

```text
bisect_left(range(len(nums)), True, key=f)
```

If `len(nums) = n + 1`, the range contains candidate values `0, 1, ..., n`. It is a lazy range object, not a materialized list.

Python orders `False` before `True`. The key function maps the candidate range to the monotone Boolean sequence proved above. `bisect_left(..., True, key=f)` finds the first position whose key is at least `True`, which is simply the first candidate whose key is true.

The searched range's values equal their zero-based positions: value 0 is at index 0, value 1 at index 1, and so on. Therefore, the insertion index returned by `bisect_left` is numerically the candidate value itself. The method can return that index directly as the duplicate.

The `key` is applied to elements of the searched range, not to the target argument `True`. That distinction is part of Python's `bisect` interface.

**Why include candidates zero and `n`**

Zero cannot be the duplicate because legal values begin at one. Its predicate is safely false: no positive array value is at most zero, so `C(0) = 0`.

Candidate $n$ is always true because all $n+1$ array entries are at most $n$, giving `C(n) = n + 1 > n`. Thus the Boolean sequence definitely contains a true value, and binary search always finds a boundary inside the range.

Including zero makes the searched sequence begin with a known false sentinel. Including $n$ supplies the known true endpoint. Neither requires special-case code.

**Trace the examples**

For `nums = [1,3,4,2,2]`, $n=4$. The prefix counts are:

| `x` | `C(x)` | `C(x) > x` |
|---:|---:|---|
| 0 | 0 | false |
| 1 | 1 | false |
| 2 | 3 | true |
| 3 | 4 | true |
| 4 | 5 | true |

The first true candidate is 2, so binary search returns 2.

For `[3,1,3,4,2]`, candidate 2 has count two and is false, while candidate 3 has count four and is true. The transition occurs at 3.

For `[3,3,3,3,3]`, $n=4$. Values 1 and 2 have count zero; candidate 3 suddenly has count five, which is greater than three. Even though 1, 2, and 4 are absent, the first true candidate remains the repeated value 3.

**Why the input remains unchanged**

The helper compares values but never assigns to `nums`. `range`, the generator, and `bisect_left` operate externally to the list. This satisfies the non-modification constraint, unlike sorting, sign marking, or cyclic placement.

## Complexity detail

Binary search evaluates `f` $O(\log n)$ times. Each evaluation scans all $n+1$ entries to compute `C(x)`, taking $O(n)$ time. The exact total is therefore

$$
O(n\log n).
$$

This differs from the manifest's $O(n)$ time, which belongs to Floyd's cycle-detection algorithm summarized there. The protected source trades linear time for a compact value-domain binary search.

The `range` object is lazy, the counting generator is lazy, and `bisect_left` stores only interval indices. Auxiliary space is $O(1)$. The algorithm does not include recursion and does not modify or copy the array.

Python's `bisect` implementation with a `key` parameter requires a sufficiently recent Python version. Its number of key calls remains logarithmic because random access into a `range` is constant time.

## Alternatives and edge cases

- **Floyd cycle detection:** Interpret each value as the next array index, find a cycle intersection, then find its entrance. It achieves the manifest's $O(n)$ time and $O(1)$ space without mutation, but it is not the exact source.
- **Hash set:** Return the first value seen twice. Expected time is $O(n)$, but the set needs $O(n)$ additional space.
- **Sort then scan:** Adjacent equal values reveal the duplicate in $O(n\log n)$ time, but in-place sorting violates the non-modification requirement and sorting a copy uses $O(n)$ space.
- **Negative marking or cyclic placement:** These can use constant auxiliary space but mutate `nums`, which is explicitly forbidden.
- **Duplicate appears twice:** No allowed value needs to be missing. At $d$, the prefix gains exactly one extra occurrence and becomes overloaded.
- **Duplicate appears many times:** Exactly $r-2$ allowed values are absent when the duplicate occurs $r$ times. The extra occurrences still exceed all possible missing-prefix deficits by one.
- **Duplicate is 1:** `f(0)` is false and `f(1)` is true, so the boundary search returns 1.
- **Duplicate is `n`:** Every smaller candidate is false and the guaranteed true endpoint `n` is returned.
- **Absent candidate values:** Binary search searches the numeric domain, not just values occurring in `nums`. The prefix-count predicate remains meaningful at absent candidates.
- **Only one distinct repeated value:** The proof relies on this guarantee. With several different duplicate values, the first overloaded prefix could identify the smallest repeated region but would not satisfy the stated single-answer contract.
- **Array values outside `[1, n]`:** Zero or larger values would invalidate the sentinel and pigeonhole arguments. The implementation intentionally trusts the range constraint.
- **Read-only behavior:** Repeated full scans may be slower than Floyd's method, but they preserve every input byte and need no auxiliary collection.
