## General

Deleting elements never changes the relative order of retained elements. It only shifts an original index left by the number of earlier deletions.

For an element with original index $i$ and value $v=\texttt{nums}[i]$ to become a fixed point, it must end at index $v$. Therefore exactly

$$
d=i-v
$$

earlier elements must be deleted.

The source turns every individually possible fixed point into a pair $(d,v)$, sorts those pairs, and finds a longest strictly increasing subsequence of the values. That subsequence is exactly the largest compatible collection of fixed points.

**Filtering individually impossible elements**

Deletions can only shift an element left. Its new index can range from 0 through its original index $i$.

If $v>i$, the element would need to move right to reach index $v$, which deletion cannot do. Such an element can never become fixed and is excluded.

If $v\le i$, deleting $d=i-v\ge0$ earlier positions can place it at index $v$ when considered alone. The source records:

```text
(index - value, value)
```

for exactly these candidates.

**Compatibility between two chosen fixed points**

Suppose two retained fixed points come from original indices $i_1<i_2$, with values $v_1$ and $v_2$ and required earlier-deletion counts

$$
d_1=i_1-v_1,
\qquad
d_2=i_2-v_2.
$$

Two conditions are necessary.

First, the number of deletions seen while moving right through the original array cannot decrease:

$$
d_1\le d_2.
$$

Second, retained elements keep their order and occupy distinct final indices. Since each final index equals its value:

$$
v_1<v_2.
$$

These two inequalities are also sufficient. Before the first chosen element, delete exactly $d_1$ positions. Between consecutive chosen elements, delete the additional $d_2-d_1$ positions required.

There are enough positions available. Because $i=d+v$:

$$
i_2-i_1
=(d_2-d_1)+(v_2-v_1).
$$

With $v_2-v_1\ge1$, the interval between chosen indices contains enough non-chosen positions to realize the required increase in deletions while retaining the chosen endpoints.

**Why sorting the points removes one dimension**

The source sorts candidate tuples lexicographically:

1. increasing required deletions $d$;
2. increasing value $v$ when $d$ ties.

After sorting, any subsequence automatically has non-decreasing $d$. It remains only to enforce strictly increasing $v$.

The original indices also end up increasing for a compatible sequence because

$$
i=d+v.
$$

If $d$ is non-decreasing and $v$ is strictly increasing, their sum strictly increases. Thus the sorted-point subsequence respects original array order even though the sort key does not mention $i$ directly.

**Why equal deletion counts may be selected together**

For equal $d$, increasing values correspond to increasing original indices:

$$
i_2-i_1=v_2-v_1.
$$

No extra deletion is needed between them. All intervening original positions can remain, allowing both chosen elements to land at their respective fixed indices.

That is why sorting equal-$d$ points by increasing value is correct. A common LIS trick sorts ties in descending order when only one point per equal first coordinate is allowed; that restriction does not apply here.

**Longest increasing subsequence of values**

After sorting, the problem is to select the most values in strictly increasing order. The source uses the standard patience-sorting `tails` array.

After processing some values, `tails[t]` is the smallest possible ending value of any strictly increasing subsequence of length $t+1$ found so far.

For current value $v$:

```text
position = bisect_left(tails, v)
```

- If `position == len(tails)`, $v$ exceeds every tail and extends the longest subsequence.
- Otherwise, replacing `tails[position]` with $v$ preserves the same subsequence length but gives it a smaller or equal endpoint, which is at least as flexible for future values.

`bisect_left` is what makes the subsequence strict. An equal value replaces an existing tail rather than extending it. Two fixed points cannot have the same final index, so equal values must not both be selected.

The length of `tails` is the maximum number of compatible fixed points.

**Example**

For `nums = [1,0,1,2]`, candidates are:

- index 1, value 0: $(d,v)=(1,0)$;
- index 2, value 1: $(1,1)$;
- index 3, value 2: $(1,2)$.

Index 0 with value 1 is impossible because $1>0$.

The three candidate pairs already have equal deletion requirement and increasing values. Their LIS length is three. Deleting original index 0 supplies the shared one deletion, leaving `[0,1,2]` with three fixed points.

For `[0,2,1]`, compatible candidates allow values 0 and 1, corresponding to deleting the middle value 2 and obtaining `[0,1]`.

**Why the LIS length is exact**

Every realizable set of fixed points produces non-decreasing deletion counts and strictly increasing values, so after sorting it appears as an increasing-value subsequence. Its size cannot exceed the LIS.

Conversely, every increasing-value subsequence in sorted point order has non-decreasing required deletions and increasing original indices. The gap argument constructs a deletion pattern meeting each chosen $d$, so all its values become their final indices simultaneously. The LIS size is attainable.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Building candidates costs $O(N)$ time and up to $O(N)$ space.

Sorting them costs

$$
O(N\log N)
$$

time. Each candidate performs one `bisect_left` on `tails`, also totaling $O(N\log N)$ time.

Overall time is

$$
O(N\log N).
$$

The candidate list and `tails` each hold at most $N$ entries, so auxiliary space is

$$
O(N).
$$

The input array is not modified.

## Alternatives and edge cases

- **Quadratic compatibility DP:** Sort the points and compare every predecessor, giving $O(N^2)$ time; patience sorting reduces the second phase to $O(N\log N)$.
- **Longest chain in two dimensions:** This is the underlying formulation, with non-decreasing deletion count and strictly increasing value.
- **Value greater than original index:** The element cannot shift right and is excluded immediately.
- **Value equal to original index:** It requires zero earlier deletions and is an ordinary candidate.
- **Equal candidate values:** They target the same final index and cannot both count; `bisect_left` prevents an LIS extension.
- **Equal deletion counts:** Multiple candidates may coexist when values rise, because no additional deletion is needed between them.
- **Delete every element:** This produces zero fixed points and is allowed, so an empty candidate list correctly returns zero.
- **Already fixed points:** They have $d=0$ and can be selected when their values form the naturally increasing index order.
- **Large values:** Values above all feasible final positions are filtered by `value <= index`.
- **Stable original order:** Compatibility implies increasing original index through $i=d+v$, so sorting points does not invent an impossible reordering.
- **Input preservation:** Only derived tuples and LIS tails are changed.
