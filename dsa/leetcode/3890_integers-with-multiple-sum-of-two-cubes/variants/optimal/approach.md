## General

A number is good when the same value can be formed by at least two distinct pairs $(a,b)$ of positive integers satisfying $a\le b$. The checked-in source handles the entire allowed input range once, when the Python module is loaded, and then answers each call by taking a prefix of the precomputed good values.

This organization matters. `findGoodIntegers(n)` itself does not enumerate cube pairs for the supplied `n`. The expensive work occurs in the global statements above the `Solution` class and always uses the fixed bound `LIMIT = 10**9`.

**Why canonical pairs prevent false duplicates**

Addition is symmetric:

$$
a^3+b^3=b^3+a^3.
$$

If both ordered pairs $(a,b)$ and $(b,a)$ were counted, almost every sum with $a\ne b$ would incorrectly appear to have two representations. The requirement $a\le b$ provides one canonical orientation. The nested loops enforce it by starting `b` at `a`.

Pairs with $a=b$ are allowed and are visited once. They count as one representation, not two. A sum enters the answer only when the count of distinct canonical pairs is greater than one.

**Why bases through 1000 cover the fixed limit**

Both bases are positive. If either base were at least 1000, then even the smallest possible other cube would make

$$
1000^3+1^3=1{,}000{,}000{,}001>10^9.
$$

Therefore no valid sum at most `LIMIT` needs a base greater than 999. The source builds

```text
cubes[i] = i³
```

for indices 0 through 1000. Including 1000 is harmless and lets the loop discover the boundary by its ordinary stopping condition.

For every `a` from 1 through 1000, `b` increases from `a` through 1000. The value

$$
x=a^3+b^3
$$

strictly increases as `b` increases. As soon as `x > LIMIT`, every later `b` for the same `a` would also be too large, so `break` safely ends that inner loop. Every legal canonical pair is visited exactly once before a break, and no illegal over-limit value is inserted into the counter.

**What the counter represents**

The global dictionary `cnt` maps a cube sum to the number of canonical pairs that produce it. Each visited pair performs `cnt[x] += 1`.

After enumeration, the comprehension keeps precisely those keys whose count is greater than one:

$$
\texttt{GOOD}
=
\operatorname{sorted}\{x:\texttt{cnt}[x]>1\}.
$$

The “greater than one” test matches “at least two distinct pairs.” It also naturally handles numbers with three or more representations: they appear once in `GOOD`, because `GOOD` contains sum values rather than representation pairs.

Sorting is performed once. The resulting global list is strictly increasing because dictionary keys are unique.

**Answering one input with a right-boundary search**

For a call with upper bound `n`, all required results form a prefix of `GOOD`. The source uses `bisect_right(GOOD, n)` to find the insertion position immediately after the last value less than or equal to `n`.

If that index is `idx`, then:

- positions before `idx` contain exactly the good values satisfying $x\le n$;
- positions from `idx` onward contain values greater than $n$; and
- using a right-biased search includes `n` itself when `n` is good.

Returning `GOOD[:idx]` copies that prefix into a new list. Because `GOOD` is already sorted, no per-call sorting is needed.

For example, the pair enumeration finds

$$
1729=1^3+12^3=9^3+10^3
$$

and

$$
4104=2^3+16^3=9^3+15^3.
$$

Both counts exceed one, so both values are in `GOOD`. A query at 4104 places `idx` after both of them and returns them in ascending order. A query at 578 ends before the first good value and returns an empty prefix.

**Why no qualifying value is missing or duplicated**

Suppose $x\le10^9$ is good. Each of its qualifying representations has positive bases and can be placed in the unique orientation $a\le b$. The base bound shows both bases lie inside the enumerated range, so every distinct representation increments `cnt[x]` once. At least two increments make `cnt[x] > 1`, placing $x$ in `GOOD`.

Conversely, if $x$ enters `GOOD`, the counter received increments from at least two different loop iterations. Different iterations correspond to different canonical pairs, every pair has positive bases with $a\le b$, and the loop inserts it only when its sum is at most `LIMIT`. Thus $x$ satisfies the definition. The binary search then includes exactly those verified values that do not exceed the particular query bound.

## Complexity detail

The source has two phases, so their costs should be stated separately.

Let $B$ be the cube-base limit used by the global precomputation; here $B=1000$. Let $S$ be the number of distinct sums stored in `cnt`, let $G$ be the number of good sums in `GOOD`, and let $R$ be the number returned for a particular query.

Building `cubes` costs $O(B)$ time and space. The triangular pair enumeration considers at most

$$
\frac{B(B+1)}{2}
$$

pairs, with early breaks removing some of them. Its worst-case time is $O(B^2)$. The dictionary can contain at most one key per visited pair, so it uses $O(B^2)$ space in the worst case.

Filtering the dictionary costs $O(S)$, and sorting the $G$ qualifying keys costs $O(G\log G)$. The one-time module initialization therefore costs

$$
O(B^2+G\log G)
$$

time and $O(B^2)$ auxiliary/global storage. This agrees with the broad manifest bound when $B$ means the fixed precomputation base limit.

One call to `findGoodIntegers` performs a binary search in $O(\log G)$ time and copies $R$ list elements in $O(R)$ time. Its per-call time is

$$
O(\log G+R),
$$

and the returned list occupies $O(R)$ space.

There is an important qualification: the local Function Contract defines $B$ from the individual input `n`, but this source does not scale its precomputation down for smaller `n`. It always prepares every good value through $10^9$. Consequently, describing the actual source as doing $O(B(n)^2)$ work for each query would be inaccurate. The global cost is tied to `LIMIT`; only the binary search and prefix copy depend on the requested `n`.

In the usual judge process, module initialization happens once and one `Solution` call follows. If multiple calls reuse the same loaded module, they share the precomputed table and pay only their respective query costs after the first initialization.

## Alternatives and edge cases

- **Per-query enumeration:** Enumerating only pairs whose sums are at most the supplied `n` can do less work for a small one-off input, but it repeats the expensive stage across calls and differs from the fixed global strategy in the source.
- **Store only repeated sums:** A set-based transition from “seen once” to “seen multiple times” can reduce stored counts, although all first occurrences still need tracking to detect the second representation.
- **Pair-sum sorting:** Generating every cube sum into a list, sorting it, and detecting adjacent duplicates also works, but stores duplicate sum entries and pays to sort the full pair list.
- **Positive bases only:** Zero is not a legal base. The loops correctly begin at 1, so representations such as $0^3+b^3$ never count.
- **Equal bases:** A pair $(a,a)$ is legal and is enumerated once. It cannot alone make a number good; another distinct canonical pair is still required.
- **Boundary value inclusion:** `bisect_right` is necessary because the answer includes values equal to `n`. A left-biased search would wrongly exclude a good value exactly at the query boundary.
- **Small upper bounds:** When no precomputed good value is at most `n`, `idx` is zero and slicing returns `[]`.
- **Values with more than two representations:** The counter may exceed two, but `GOOD` still contains the integer only once.
- **Fixed constraint ceiling:** The precomputation is valid because the contract caps `n` at $10^9$. Raising that ceiling without also raising `LIMIT` and the base range would silently omit answers.
- **Module-level work:** Importing the file performs the full enumeration before `findGoodIntegers` is called. This can be advantageous for repeated queries but should not be mistaken for a constant-cost method call in a fresh process.
- **Required library names:** Standalone execution needs `defaultdict` and `bisect_right` supplied from the Python standard library; the checked-in file assumes the harness exposes them.
