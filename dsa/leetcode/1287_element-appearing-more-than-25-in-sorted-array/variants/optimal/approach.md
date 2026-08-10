## General

**Sorted equal values form contiguous blocks**

Let $n$ be the array length and $q=\lfloor n/4\rfloor$. An element appearing more than 25 percent of the time has an integer frequency greater than $n/4$, which means at least $q+1$ occurrences.

Because the array is sorted, all copies of one value occupy one contiguous block. If a block begins at index $s$ and has at least $q+1$ elements, both `arr[s]` and `arr[s + q]` lie inside it and are equal.

The exact source scans starting positions `i` and checks `arr[i] == arr[i + q]`, where `n >> 2` computes floor division by four for nonnegative $n$.

Right-shifting a nonnegative integer by two bits is equivalent to integer division by $2^2=4$. The shift is therefore only a compact spelling of `n // 4`; it does not change the mathematical threshold or inspect array values as bits.

**Why equality proves the frequency threshold**

If the values at positions $i$ and $i+q$ are equal, sorted order forces every element between them to be equal as well. That block contains at least $q+1$ elements.

Since $q=\lfloor n/4\rfloor$, $q+1>n/4$. Therefore the value occupies more than 25 percent of the array and must be the guaranteed special element.

This implication also prevents returning an ordinary shorter block. Any equality at that spacing is sufficient proof of the required frequency.

**Why the loop returns before its index could go out of range**

The source uses `enumerate(arr)` rather than explicitly stopping at `n - q`. For late indices, `i + q` could exceed the array bounds. Nevertheless, the problem guarantee ensures the function returns first.

Let $s$ be the first index of the guaranteed special block. Its frequency is at least $q+1$, so `s + q <= n - 1`. When the loop reaches `i = s`, the indexed comparison is valid and equal, and the function returns. It never proceeds to a dangerous later index.

Without the guaranteed qualifying element, this exact loop would need a bounded range and a fallback return to be robust.

**Trace the example**

For nine elements, `q = 9 >> 2 = 2`. The loop compares values two positions apart. At index two in `[1,2,2,6,6,6,6,7,10]`, it compares two with six and continues. At index three, it compares `arr[3]` and `arr[5]`, both six, so it returns six.

For `[1,1]`, `q = 0`. The very first comparison is an element with itself, which succeeds. This is correct because any value in an array of length below four that appears at least once exceeds $n/4$, and the guarantee says exactly one qualifies.

**Why uniqueness is consistent with the test**

Any value passing the distance-$q$ comparison occurs at least $q+1$ times and therefore exceeds 25 percent. The statement guarantees exactly one such integer, so the first passing value is unambiguous. Multiple qualifying blocks would contradict the input contract, not create a choice the algorithm must resolve.

The algorithm does not count frequencies explicitly. Sorted adjacency converts the frequency question into a constant-time spacing test at each candidate start.

## Complexity detail

In the worst case, the special block may begin late enough that the loop examines $O(n)$ indices before finding it. Each comparison is constant time, so the exact shipped source takes $O(n)$ time.

It uses only `n` and loop variables, so auxiliary space is $O(1)$.

The manifest's $O(\log n)$ time describes a different strategy that tests a constant number of quartile candidates and uses binary searches for their block boundaries. The exact source shown here is the linear “check $n/4$ ahead” method.

## Alternatives and edge cases

- **Quartile candidates plus binary search:** The special block must cover at least one of the quarter positions. Binary-searching each candidate's first and last occurrence achieves $O(\log n)$ time and $O(1)$ space.
- **Frequency hash map:** Counting all values takes $O(n)$ time and $O(n)$ space but ignores sorted order.
- **Run-length scan:** Count each contiguous block and return the one longer than $n/4$. It is robust and linear but maintains more explicit state.
- **Bound the exact loop:** Iterating only through `range(n - q)` avoids relying on guaranteed early return and is safer general code.
- **Small arrays with `q = 0`:** The first self-comparison succeeds; the uniqueness guarantee determines that this is valid.
- **Special block at the beginning:** The first comparison may return immediately.
- **Special block at the end:** The loop reaches its valid block start and returns before any out-of-range access.
- **Strictly more than 25 percent:** Requiring $q+1$ occurrences correctly handles lengths not divisible by four.
- **Sorted-order requirement:** Without sorting, equal endpoints would not prove that the elements between them match.
- **Missing valid element:** Outside the contract, the exact source could run out of bounds and has no fallback return.
