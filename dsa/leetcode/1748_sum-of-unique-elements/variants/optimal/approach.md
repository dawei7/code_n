## General

**“Unique” means frequency one, not merely distinct**

The central distinction is between a value that appears in the array and a value that appears exactly once. A set can identify distinct values, but it discards how many times each value occurred. This problem needs the complete frequency of each number before deciding whether that number contributes to the sum.

The exact solution uses `Counter(nums)`. A Python `Counter` is a dictionary-like mapping from each distinct value to its occurrence count. If a number occurs once, its stored count is one. If it occurs two or more times, it must contribute nothing, regardless of how large or small it is.

For `nums = [1,2,3,2]`, the counter conceptually contains one mapped to one, two mapped to two, and three mapped to one. Values one and three satisfy the exact-frequency test, so their sum is four.

**Count first because future elements can change eligibility**

It is tempting to add a value the first time it appears. That is not enough by itself because a later duplicate can make the earlier contribution invalid. For instance, after reading the first two in `[2,3,2]`, two appears unique so far, but it is not unique in the complete array.

Building all counts first separates two concerns cleanly:

- The counting pass discovers the final frequency of every distinct value.
- The aggregation pass includes only keys whose final frequency equals one.

This makes the correctness condition visible in the code rather than requiring compensating updates when second or later occurrences arrive.

**Read the generator expression from left to right**

The return statement is:

`sum(x for x, v in cnt.items() if v == 1)`.

`cnt.items()` produces each distinct number and its count as a pair `(x, v)`. The filter `if v == 1` retains exactly those pairs whose number occurred once. The generator yields only `x`, not its count. Finally, `sum` adds the yielded values.

The generator is lazy. It does not allocate a separate list of unique values before summing. At any moment, it only needs the current mapping entry and the running total maintained by `sum`.

The order in which the counter entries are visited does not matter because integer addition is independent of order. The task asks for one total, not for the unique values in their original positions.

**Why repeated values contribute zero rather than once**

A value with frequency two is not “one of the distinct values to sum once.” It fails the problem's definition entirely. Therefore the correct contribution rule for a value $x$ with frequency $c_x$ is:

$$
\operatorname{contribution}(x)
=
\begin{cases}
x, & c_x=1,\\
0, & c_x\ne 1.
\end{cases}
$$

The generator's condition implements precisely this piecewise rule. It does not multiply `x` by `v`, and it does not include one copy of every counter key.

In the all-repeated example `[1,1,1,1,1]`, the only mapping entry has count five. The filter yields no values. Python's `sum` of an empty generator is zero, producing the required result without a special case.

**Why the fixed value range matters for space**

The constraints limit each element to the integers from one through one hundred. Consequently, the counter can have at most one hundred keys no matter whether the input contains one element or one hundred elements.

The exact implementation still uses a hash-based `Counter` rather than a 101-position array. That choice is concise and directly names the frequency operation. Under the fixed domain, both structures have constant bounded size in asymptotic analysis.

If the value range were unrestricted and the input length could grow, a counter could hold up to $n$ distinct keys. In that generalized setting its auxiliary space would be $O(n)$ rather than $O(1)$. The manifest's constant-space claim relies on the stated bounded domain.

**Trace the all-unique example**

For `[1,2,3,4,5]`, every counter value is one. The generator yields one, two, three, four, and five. `sum` accumulates them to fifteen.

No element is added more than once because `cnt.items()` has one entry per distinct key. That is exactly right: a qualifying value occurs once in the array, so adding the key once equals adding its only occurrence.

**Why the returned sum is correct**

For every distinct number in `nums`, `Counter` records its exact occurrence count. The generator includes the number if and only if that count equals one, which is exactly the definition of a unique element in this problem. It excludes every other number.

Thus the generated collection contains every unique array value once and contains no non-unique value. Applying `sum` to that collection returns exactly the requested sum.

## Complexity detail

Let $n$ be the length of `nums` and $U$ the number of distinct values. Constructing `Counter(nums)` processes all $n$ elements and takes expected $O(n)$ time using hash-table operations. Iterating through `cnt.items()` takes $O(U)$ time. Since $U \le n$, total expected time is $O(n)$.

The counter uses $O(U)$ entries in the exact Python implementation. Because the problem restricts values to a domain of only 100 integers, $U \le 100$ and this is $O(1)$ auxiliary space under the official constraints, matching the manifest. Without that fixed-domain guarantee, the appropriate generalized bound would be $O(U)$ or $O(n)$.

The generator expression itself uses $O(1)$ additional space because it yields values one at a time. The returned integer is also constant-sized in the problem's bounded numeric model.

## Alternatives and edge cases

- **Fixed frequency array:** Use 101 counters indexed by value. It provides deterministic constant-time updates and makes the bounded-domain space explicit, but is less flexible than `Counter`.
- **Set only:** A plain set loses occurrence counts and would incorrectly include values that repeat.
- **Nested counting:** Calling `nums.count(x)` for every element is simple but can take $O(n^2)$ time.
- **One-pass adjusted sum:** Add a value on its first occurrence and subtract it on its second. This can work with frequency tracking, but later occurrences add state-transition complexity.
- **All values unique:** Every counter entry passes, so the answer is the ordinary array sum.
- **No unique values:** The generator is empty and `sum` returns zero.
- **One-element array:** Its only frequency is one, so that element is returned.
- **A value appearing twice:** It is fully excluded, not counted once.
- **A value appearing many times:** Count magnitude beyond one does not matter to the filter.
- **Same numeric total from different sets:** Only the sum is returned; the solution need not preserve which unique values formed it.
- **Positive-value constraint:** There is no cancellation between positive and negative unique values, although the counter method would still work if negatives were allowed.
- **Bounded domain:** At most 100 counter entries justify the stated $O(1)$ space.
- **Input preservation:** `Counter` reads `nums` and does not reorder or modify it.
- **Hash behavior:** The $O(n)$ time is the standard expected bound for Python dictionary-based counting.
