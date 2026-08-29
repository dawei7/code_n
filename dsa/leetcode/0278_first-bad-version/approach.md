## General

**Recognize a monotone Boolean sequence**

The versions are ordered from 1 through $n$. Once one version is bad, every later version is also bad. Therefore, the hidden API results have one transition:

```text
false, false, ..., false, true, true, ..., true
                         ^
                   first bad version
```

The task is not to search arbitrary Boolean values. It is to locate the boundary between the good prefix and the bad suffix. This monotonicity is exactly what binary search needs.

The constraints guarantee that a bad version exists somewhere from 1 through $n$, so the desired boundary is always inside the initial search interval.

**Keep an inclusive interval containing the answer**

The source initializes `l = 1` and `r = n`. Both endpoints are included. Throughout the algorithm, the maintained fact is:

> The first bad version lies somewhere in `[l, r]`.

Initially this follows directly from `1 <= bad <= n`. Every update preserves it by removing only versions that have been logically proved unable to be the first bad one.

The loop continues while `l < r`, meaning at least two candidates remain. It chooses

$$
\texttt{mid}
=
\left\lfloor\frac{\texttt{l}+\texttt{r}}{2}\right\rfloor.
$$

The expression `(l + r) >> 1` performs that floor division by two for these non-negative integers.

**When `mid` is good, discard it and everything before it**

If `isBadVersion(mid)` returns false, `mid` is good. Because all versions before the first bad version are good and badness never changes back to goodness, every version at or before `mid` is also too early to be the answer.

The first bad version must be in `[mid + 1, r]`, so the source sets `l = mid + 1`. Adding one is necessary: the API has directly proved that `mid` itself is not bad, so retaining it would waste a candidate and could prevent progress.

**When `mid` is bad, retain it as a possible boundary**

If the API returns true, `mid` is bad, and monotonicity proves every version after it is bad as well. Those later versions cannot be the first bad version because `mid` is already an earlier bad one.

However, `mid` might itself be the first bad version. The algorithm must not discard it. It sets `r = mid`, leaving the new interval `[l, mid]`.

This asymmetry—`mid + 1` for a good result but `mid` for a bad result—is the central boundary-search detail. A bad midpoint is a candidate answer; a good midpoint is not.

**Why the lower midpoint guarantees progress**

When `l < r`, the floor midpoint satisfies `l <= mid < r`. In the good branch, `l` becomes at least `mid + 1`, which is strictly larger than its old value. In the bad branch, `r` becomes `mid`, which is strictly smaller than its old value. Thus every iteration shrinks the inclusive interval.

For the smallest nontrivial interval `[x, x + 1]`, `mid` equals `x`. If `x` is good, the interval becomes `[x + 1, x + 1]`. If `x` is bad, it becomes `[x, x]`. Both API outcomes reduce two candidates to one, confirming that the loop cannot become stuck.

**Why the meeting point is the answer**

The interval invariant says the first bad version is never removed. The strict shrinking argument says the loop eventually ends. It ends only when `l == r`, so the interval contains one version. Since it still contains the first bad version, that sole version must be the answer. Returning `l` is therefore correct; returning `r` would be equivalent at that point.

**Trace `n = 5, bad = 4`**

The API sequence is `false, false, false, true, true`.

| `l` | `r` | `mid` | API result | New interval |
|---:|---:|---:|---|---|
| 1 | 5 | 3 | version 3 is good | `[4,5]` |
| 4 | 5 | 4 | version 4 is bad | `[4,4]` |

The endpoints meet at 4, so the solution returns 4. Notice that querying version 5 is unnecessary for this exact search path; knowing version 4 is bad and version 3 is good already determines the transition.

For `n = 1`, the initial bounds are both 1. The loop makes no API calls and returns 1, which must be bad by the input guarantee.

## Complexity detail

The interval begins with $n$ candidates. Each API call reduces its size to at most roughly half of the previous size. After $t$ iterations, the remaining size is at most about $n/2^t$; reaching one candidate requires $t=O(\log n)$.

More concretely, the algorithm makes at most $\lceil\log_2 n\rceil$ API calls and makes zero calls when $n=1$. Assuming an API call is $O(1)$, total time is $O(\log n)$.

This is asymptotically optimal for an API that supplies one Boolean answer per call. There are $n$ possible boundary locations, and one binary response can distinguish at most two groups of possibilities. Identifying one among $n$ possibilities requires logarithmically many bits of information in the worst case.

The method stores only two bounds and one midpoint, so auxiliary space is $O(1)$. It uses no recursion or collection.

Python integers do not overflow when computing `l + r`. In a fixed-width language, the safer midpoint expression is `l + (r - l) / 2`; this avoids overflow while preserving the same lower-midpoint behavior.

## Alternatives and edge cases

- **Linear scan:** Query versions from 1 upward and return the first bad result. It is correct but makes up to $n$ API calls, far more than binary search for large inputs.
- **Recursive binary search:** The same interval logic can be written recursively, but it uses $O(\log n)$ call-stack space without improving the number of API calls.
- **Discard a bad midpoint:** Setting `r = mid - 1` after a true result is incorrect because `mid` itself may be the first bad version.
- **Retain a good midpoint:** Setting `l = mid` with a lower midpoint can cause an infinite loop on two adjacent candidates and keeps a version already proved good.
- **First version is bad:** Every API result is true. The algorithm repeatedly moves `r` left while retaining the boundary and returns 1.
- **Last version is first bad:** Every queried version before `n` is good, so `l` repeatedly moves right and ultimately reaches `n`.
- **Only one version:** The loop condition is initially false, avoiding an unnecessary API call and returning the guaranteed boundary.
- **Large `n`:** Logarithmic calls remain small even at the signed 32-bit maximum. Python's midpoint arithmetic remains exact.
- **No bad version outside the contract:** If every API result were false, the code would converge to `n` even though `n` was good. Correctness relies on the explicit guarantee that `bad <= n`.
- **Non-monotone API outside the contract:** If a good version appeared after a bad one, neither branch could safely discard half the interval. The algorithm intentionally relies on inherited badness.
