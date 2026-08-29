## General

**Process from the fixed right boundary**

Replacing a number creates smaller positive pieces in the same position relative to the rest of the array. To make the final sequence non-decreasing, every piece created from a value must be no larger than the first piece belonging to the already processed suffix on its right.

This boundary is naturally known when scanning from right to left. The algorithm stores it in `mx`. Initially, the last value needs no replacement and is the first value of the processed suffix, so `mx = nums[-1]`.

At each earlier `nums[i]`, the task is local: split its value into the fewest positive pieces such that every piece is at most `mx`. Then arrange those pieces in non-decreasing order before the processed suffix. The smallest piece becomes the new boundary for the next value on the left.

**Keep a value that already fits**

If `nums[i] <= mx`, no split is necessary. Placing this value before a suffix whose first element is at least `mx` preserves non-decreasing order. The new leftmost suffix value is now `nums[i]`, so the code assigns `mx = nums[i]`.

Splitting such a value would add operations and could only make the new boundary smaller, making life harder for values further left. Keeping it whole is always optimal.

**Find the minimum required number of pieces**

Let the current value be $x$ and the maximum allowed piece size be $m=\texttt{mx}$. If $x>m$ and it is split into $k$ pieces, their total capacity under the boundary is $km$. To sum to $x$, they must satisfy:

$$
km\ge x.
$$

Thus:

$$
k\ge \left\lceil\frac{x}{m}\right\rceil.
$$

The exact code computes this ceiling with integer arithmetic:

```python
k = (nums[i] + mx - 1) // mx
```

Using fewer pieces is impossible because their combined sum could not reach $x$ without some piece exceeding $m$. Using more pieces is legal but costs more operations and creates an equal or smaller boundary for future work. Therefore, the ceiling is the uniquely optimal piece count for this local decision.

**Convert piece count to operation count**

One operation replaces one element by two, increasing the number of elements by exactly one. Starting from one element, producing $k$ pieces requires exactly $k-1$ operations. It is achievable by repeatedly splitting one remaining piece until there are $k$ pieces, so the code adds `k - 1` to `ans`.

This detail prevents the common mistake of adding $k$. Piece count and replacement-operation count differ by one.

**Balance the pieces to preserve the largest future boundary**

For the chosen minimum $k$, the pieces should be as equal as possible. Any $k$ positive integers summing to $x$ have a smallest value no larger than:

$$
\left\lfloor\frac{x}{k}\right\rfloor.
$$

An even split achieves this upper bound: use values of $\lfloor x/k\rfloor$ and $\lceil x/k\rceil$ in non-decreasing order. Because $k=\lceil x/m\rceil$, the largest balanced piece does not exceed $m$. The smallest piece is therefore exactly `x // k`, and the solution updates:

```python
mx = nums[i] // k
```

Maximizing this smallest piece matters because it becomes the maximum allowed value for pieces generated farther left. A larger boundary can never require more future splits; a smaller boundary can.

For `x = 7` and `mx = 3`, the minimum piece count is `ceil(7 / 3) = 3`. The balanced split `[2, 2, 3]` is valid and makes the new boundary `2`. A split such as `[1, 3, 3]` uses the same number of pieces but leaves boundary `1`, unnecessarily restricting the remaining prefix.

**Trace `[3, 9, 3]`**

Start with boundary `3` from the last element. For `9`, `k = ceil(9 / 3) = 3`. Producing three pieces costs two operations, and the balanced split can be `[3, 3, 3]`. The new boundary remains `3`.

The first value `3` already satisfies the boundary and remains whole. Total operations are two, producing a non-decreasing sequence of all threes.

**Why the greedy choices combine globally**

Assume the suffix to the right of index `i` has been made non-decreasing with the minimum operations for the decisions already processed, and `mx` is its first value. Any valid handling of `nums[i]` must use pieces no larger than `mx`. The ceiling formula gives a lower bound on their count and hence on new operations; the balanced construction meets that bound.

Among all minimum-operation constructions for the current value, balancing maximizes the first, smallest piece and thus gives the least restrictive possible boundary to the remaining prefix. It cannot make any future decision worse than another equally cheap split. By applying this argument from right to left, every local choice minimizes current cost without sacrificing future opportunities. The accumulated total is globally minimal.

## Complexity detail

Let $n$ be the length of `nums`. The reverse loop visits each element except the last once. Each iteration performs constant-time comparisons and integer arithmetic, so time complexity is $O(n)$.

The algorithm stores only `ans`, `mx`, `k`, and loop variables. It does not construct the actual pieces or modify `nums`. Auxiliary space is $O(1)$, matching the variant manifest.

The answer can be much larger than $n$, but Python's arbitrary-precision integers store it safely. Constructing the expanded final array would use space proportional to that potentially huge answer and is intentionally avoided.

## Alternatives and edge cases

- **Actually construct every split piece:** This makes the transformation visible but can require enormous time and memory. The boundary calculation contains all information needed for the count.
- **Modify `nums` in place:** Replacing `nums[i]` with the new boundary is a common equivalent implementation. The exact solution keeps a separate `mx` and leaves the input unchanged.
- **Split by repeatedly taking `mx`:** This can leave a very small remainder, such as `[1, 3, 3]` for seven. Balancing preserves a larger boundary for the prefix.
- **Already non-decreasing input:** Every value fits its right boundary, `k` is never computed, and the answer remains zero.
- **One element:** The reverse range is empty, so no replacement is needed.
- **Exact divisibility:** If $x$ is divisible by `mx`, all $k$ pieces may equal `mx` and the boundary remains unchanged.
- **Non-divisible value:** The ceiling adds one piece, and balanced floor/ceiling sizes keep the largest piece within the boundary.
- **Strictly decreasing large values:** Many elements may require splits, but each is still processed in constant time rather than once per generated piece.
- **Positive-value guarantee:** Division boundaries never become zero because $x$ is positive and $k\le x$ when `mx >= 1`.
