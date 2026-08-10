## General

**Fix the number of paid rotations first**

The operation rotates every chocolate type simultaneously and costs `x`. Suppose exactly `j` operations are performed. Their unavoidable cost is `j * x`.

Once `j` is fixed, the remaining question is independent for every target type: among the type configurations seen from time zero through time `j`, what is the cheapest physical chocolate that could be purchased as that type?

The solution precomputes that cheapest collection cost and then compares every possible `j`.

**Which source can represent target type i**

Initially, the chocolate at index `p` has type `p`. After one operation, its type becomes `(p + 1) % n`. After `r` operations, its type is:

$$
(p+r)\bmod n.
$$

For that chocolate to have target type `i` at time `r`, its original index must be:

$$
p=(i-r)\bmod n.
$$

Therefore, if up to `j` rotations have occurred, type `i` could have been bought from original indices:

$$
i,\ i-1,\ i-2,\ldots,i-j\pmod n.
$$

Because chocolates may be collected at different stages, each type can use the cheapest price among all of those opportunities.

**Meaning of the dynamic table**

`f[i][j]` is the minimum purchase cost seen for target type `i` during configurations zero through `j`.

The base case is `f[i][0] = nums[i]`: without rotations, only the chocolate originally at index `i` has type `i`.

For `j>=1`, one new possible source becomes available, `nums[(i - j) % n]`. The recurrence is:

$$
f[i][j]
=
\min\left(f[i][j-1],\ \texttt{nums}[(i-j)\bmod n]\right).
$$

This either retains the best source from earlier configurations or replaces it with the newly exposed cheaper source.

Python's modulo makes a negative index expression wrap into the range zero through $n-1$, exactly matching the circular type rotation.

**Combine independent purchase minima**

After exactly `j` operations are available, the cheapest way to obtain every type is:

$$
jx+\sum_{i=0}^{n-1}f[i][j].
$$

The rotation cost is global and paid once per operation. The purchase choices are independent: buying a chocolate of one type does not prevent using the price opportunity for another type in the abstract collection model. Thus choosing the minimum available cost for each target separately is valid.

The return expression evaluates this total for every `j` from zero through $n-1$ and returns the smallest.

**Why n rotations never need to be considered**

After $n$ rotations, type labels return to their original arrangement. By then, every target type has had access to every original index, so all `f[i][j]` values have reached the global minimum price in `nums` and cannot decrease further.

Any additional full-cycle or partial rotation beyond $n-1$ revisits configurations already seen but adds another positive cost `x`. It cannot improve a purchase minimum, so it cannot lower the total. Enumerating `j=0,1,\ldots,n-1` is complete.

**Trace nums equal to 20, 1, 15**

With zero rotations, the per-type costs are 20, 1, and 15. The total is 36.

After one rotation, each target may use its original source or the preceding circular source:

- type zero uses minimum of 20 and 15, which is 15;
- type one uses minimum of 1 and 20, which is 1;
- type two uses minimum of 15 and 1, which is 1.

The purchase sum is 17, plus one rotation cost five, totaling 22.

After two rotations, every target has seen all three prices and can use one. The purchase sum is three, and two rotations cost ten, totaling 13. The minimum over 36, 22, and 13 is 13.

**Why buying at earlier times is captured**

`f[i][j]` does not claim that every selected price is simultaneously visible after the final rotation. It represents the minimum seen at any time up to `j`. The problem permits collecting chocolates along the way, as the example buys types after different operations. The recurrence deliberately preserves earlier opportunities.

**Exact implementation versus a rolling optimization**

The code allocates the full `n by n` table even though each recurrence uses only the previous column of the same row. This makes every candidate `j` easy to sum afterward and mirrors the mathematical definition directly.

A more memory-efficient implementation could keep one current minimum per type while increasing `j`, but that is not what the exact source does.


For fixed `j`, the recurrence examines exactly the source index that carries target type `i` at every time from zero through `j` and stores their minimum price. Therefore `sum(f[i][j])` is the least possible purchase cost for all types given those configurations, and adding `jx` gives the optimum with `j` rotations. No useful plan needs $n$ or more rotations because configurations repeat and `x>0`. Taking the minimum across zero through $n-1$ therefore returns the global optimum.

## Complexity detail

The nested construction fills $n^2$ table entries in $O(n^2)$ time. The final expression computes $n$ column sums, each over $n$ rows, adding another $O(n^2)$ time. Total time is $O(n^2)$.

The table `f` contains $n^2$ Python integers, so the exact implementation uses $O(n^2)$ auxiliary space. This differs from the manifest's $O(n)$ claim, which describes the rolling-minimum optimization rather than this protected source.

The generator used by `min` does not retain all candidate totals at once, but that does not reduce the already allocated table. Input `nums` is not modified.

## Alternatives and edge cases

- **Rolling minimum array:** Maintain one best price per type as `j` grows, achieving the same $O(n^2)$ time with $O(n)$ auxiliary space.
- **Try every purchase plan:** Exponential and unnecessary because choices become independent once the rotation count is fixed.
- **Perform n or more rotations:** Never beneficial because type configurations repeat while every additional operation has positive cost.
- **Zero rotations optimal:** When rotations are too expensive, candidate `j=0` returns `sum(nums)`.
- **One chocolate:** Only `j=0` is considered, and the answer is its original cost.
- **Very cheap rotation:** More rotations may expose the global cheapest price to every type.
- **Circular wrap:** `(i - j) % n` correctly accesses sources crossing index zero.
- **Repeated prices:** Minima remain correct; source identity is irrelevant.
- **Large costs:** Python integers avoid overflow when summing prices and rotation fees.
- **Manifest mismatch:** The exact table is $O(n^2)$ space even though a straightforward optimization can realize $O(n)$.
