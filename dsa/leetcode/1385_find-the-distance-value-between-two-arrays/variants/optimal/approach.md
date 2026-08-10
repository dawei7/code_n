## General

**Turn an absolute-difference test into an interval search**

For a fixed value `x` from `arr1`, an `arr2` value `y` violates the distance condition when

$$
\lvert x-y\rvert\le d.
$$

This is equivalent to

$$
x-d\le y\le x+d.
$$

So `x` should be counted only when `arr2` contains no value in the closed interval `[x-d,x+d]`.

The exact solution sorts `arr2` in place. Sorting lets one binary-search for the first possible value in that forbidden interval instead of comparing `x` against every `arr2` element.

**Why search for `x - d`**

`bisect_left(arr2, x - d)` returns the smallest index `i` whose value is greater than or equal to the lower boundary `x-d`. All entries before `i` are strictly smaller than `x-d` and therefore safely farther than $d$ below `x`.

There are now only two ways for the forbidden interval to be empty:

1. `i == len(arr2)`. No value reaches the lower boundary; every `arr2` value is below `x-d`.
2. `arr2[i] > x + d`. The first value at or above the lower boundary is already beyond the upper boundary.

If neither is true, `arr2[i]` lies between both inclusive boundaries and is a witness with absolute difference at most $d$. No other element needs inspection.

This explains the compact update:

`ans += i == len(arr2) or arr2[i] > x + d`.

Python treats the Boolean result as one for true and zero for false, so `ans` increases exactly for valid `arr1` elements.

**Why checking one candidate is sufficient**

Because `arr2` is sorted, `arr2[i]` is the smallest element that could possibly enter the forbidden interval. If it exceeds `x+d`, every later element is at least as large and also exceeds the interval. If it does not exceed `x+d`, it itself is a violation. Earlier elements are all below `x-d` by the definition of `bisect_left`. These three regions exhaust the array.

For `x=4` and $d=2$, the forbidden interval is `[2,6]`. Sorting the first example's second array gives `[1,8,9,10]`. The first value at least two is eight, which exceeds six, so four is counted.

For `x=8`, the interval is `[6,10]`. The first value at least six is eight, which lies inside the interval, so eight is not counted.

**Closed boundaries matter**

The original condition rejects a pair with difference equal to $d$, not only one with smaller difference. That is why the lower-bound search includes `x-d` and the validity check requires strictly greater than `x+d`. If the candidate equals either boundary, it is a violation.

When $d=0$, the forbidden interval contains only `x`. The algorithm counts `x` exactly when no equal value exists in `arr2`, which is the correct interpretation.

**Input order and mutation**

The loop reads `arr1` in any order because answers are only counted, not returned per position. The code calls `arr2.sort()`, so it permanently rearranges the caller's second list. This is acceptable to the usual judge but is a material side effect. Using `sorted(arr2)` would preserve the input at the cost of an explicit copy.

**Why the algorithm is correct**

For each `x`, binary search partitions sorted `arr2` into values below $x-d$ and values at or above it. If no second region exists, every value is safely outside. Otherwise its first value is the only boundary candidate needed: if it is above $x+d$, all later values are also outside; if it is at most $x+d$, it proves a prohibited pair. Thus the Boolean added to `ans` is true exactly when no prohibited `arr2` value exists. Summing that exact decision across all `arr1` elements returns the distance value.

## Complexity detail

Let $n$ be `len(arr1)` and $m$ be `len(arr2)`. Sorting `arr2` costs $O(m\log m)$. Each of the $n$ values performs one $O(\log m)$ binary search, so total time is

$$
O(m\log m+n\log m).
$$

This matches the manifest. Python's in-place sort can use $O(m)$ temporary memory in the worst case, while the loop itself uses constant scalar state. The manifest therefore lists $O(m)$ space. In-place mutation avoids a separate persistent sorted copy but does not imply that the sorting implementation uses constant workspace.

## Alternatives and edge cases

- **Brute-force nested loops:** Check every pair directly in $O(nm)$ time. It is easy to derive and may be acceptable for tiny inputs, but binary search scales better.
- **Two nearest neighbors:** Search for the insertion position of `x` and inspect the immediate predecessor and successor. It is also correct because the closest sorted value must be one of them.
- **Two-pointer sweep:** Sort both arrays and advance pointers to test ranges in near-linear scan time after sorting. It can be efficient but must preserve multiplicity of `arr1` answers carefully.
- **Value-frequency array:** The bounded values from $-1000$ to $1000$ permit prefix counts over a fixed universe. It can answer interval emptiness in constant time after preprocessing.
- **`d = 0`:** Only exact equality disqualifies `x`.
- **Value on a boundary:** Difference exactly $d$ is disqualifying, so `arr2[i] > x+d` must be strict.
- **All values below the interval:** Binary search returns the array length and `x` is counted.
- **First candidate above the interval:** Sorted order proves every later candidate is also too large.
- **Negative numbers:** Interval arithmetic and binary search work without modification.
- **Duplicate `arr1` values:** Each occurrence is a separate element and is counted separately, as required.
- **Duplicate `arr2` values:** One violating occurrence is enough; `bisect_left` finds the first relevant one.
- **Input mutation:** `arr2.sort()` changes the supplied list order. Use a sorted copy when callers require immutability.
- **Required import:** `bisect_left` must be available, normally from `bisect`.
