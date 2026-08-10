## General

**The deletions always expose symmetric pairs**

The operation repeatedly removes the current first and last elements. In the original array, the pairs are therefore

$$
(0,n-1),(1,n-2),(2,n-3),\ldots
$$

There is no need to physically delete anything. Two pointers `i` and `j` can identify the same elements while moving inward. Initially `i = 0` and `j = len(nums) - 1`. After handling one outer pair, `i` increases and `j` decreases.

Deleting from the front of a Python list would shift all remaining elements and could make a simple-looking simulation quadratic. Pointer movement keeps each array element involved in at most one operation and leaves the input unchanged.

**How the exact solution concatenates a pair**

For current values `nums[i]` and `nums[j]`, the code evaluates

`int(str(nums[i]) + str(nums[j]))`.

Converting both positive integers to strings produces their usual decimal numerals. String addition joins those numerals without arithmetic addition. For example, `str(15) + str(49)` is `"1549"`, and converting that string back to an integer yields $1549$.

Order matters. The first element's digits appear before the last element's digits, exactly as the statement requires. Swapping the conversion order would produce $4915$ and be wrong.

The manifest summary describes arithmetic concatenation, but the checked-in solution actually uses string conversion. Both implement the same mathematical operation under the positive-integer constraints; this document follows the exact code.

**Why the main loop uses `i < j`**

While `i < j`, two distinct elements remain. The solution concatenates them, adds the result to `ans`, and moves both pointers inward. The interval of not-yet-processed elements changes from $[i,j]$ to $[i+1,j-1]$, exactly matching removal of its endpoints.

Eventually there are two possibilities:

- `i > j`, meaning every element belonged to a pair and nothing remains;
- `i == j`, meaning one middle element remains.

The separate condition `if i == j` adds that middle value directly. It must not concatenate the value with itself because the rule for a one-element array says to add the element once.

For an even-length array, the pointers cross after the final pair and the condition is false. For an odd-length array, they meet at the unique middle index and the condition is true.

**Trace the pointer state**

Consider `nums = [5,14,13,8,12]`:

- pointers $(0,4)$ select $5$ and $12$, form $512$, and move to $(1,3)$;
- pointers $(1,3)$ select $14$ and $8$, form $148$, and move to $(2,2)$;
- the loop stops because the pointers are equal, then the middle value $13$ is added.

The result is $512+148+13=673$. At every point, the pointer interval contains exactly the values that would remain after performing the statement's physical removals.

**Why every element contributes exactly once**

Before an iteration, indices below `i` and above `j` have already been processed, while every index from `i` through `j` is unprocessed. The loop uses the two boundary indices once and then excludes both by moving inward. This preserves the same property for the next iteration.

If the pointers cross, the processed pairs cover the entire array. If they meet, only that common index was not used in a pair, and the final branch uses it once. No index is skipped and no index is reused. Because each pair is ordered left value followed by right value, its contribution is also exact. Summing those exact contributions proves the final answer.

**Arithmetic interpretation**

Although the implementation uses strings, concatenating nonnegative integer $a$ before positive integer $b$ can also be written as

$$
a\cdot10^{d(b)}+b,
$$

where $d(b)$ is the number of decimal digits of $b$. Multiplication shifts $a$ left by exactly enough decimal places to make room for $b$. This identity explains why the string conversion produces the intended numeric value and suggests an alternative implementation.

There are no leading zeros in an input numeral because every value is at least $1$. Therefore converting the joined string back to an integer does not discard any meaningful digits.

## Complexity detail

Let $n$ be the array length and let $d$ be the maximum number of digits in an element. There are $\lfloor n/2\rfloor$ pair iterations. Each string conversion, concatenation, and integer parsing uses $O(d)$ character work, so the precise general bound is $O(nd)$ time.

Under the stated constraint `nums[i] <= 10^4`, $d\le5$ is a fixed constant, making the problem-scale bound $O(n)$ as listed in the manifest. Each iteration creates temporary strings of $O(d)$ size. With bounded input digits, auxiliary space is $O(1)$ relative to $n$; more generally it is $O(d)$. The input array is not modified.

## Alternatives and edge cases

- **Arithmetic concatenation:** Compute the power of ten determined by the right value's digit count, then add `left * power + right`. This avoids strings but needs careful digit counting.
- **Physically pop endpoints:** Repeated `pop(0)` shifts the list and can cost $O(n^2)$ overall; it also destroys the input.
- **Deque simulation:** A deque supports removal from both ends in $O(1)$ time, but copying the array into it uses $O(n)$ extra space when two indices suffice.
- **One element:** The loop never runs, the pointers are equal, and the sole value is added once.
- **Two elements:** Exactly one concatenation occurs, then the pointers cross and no middle value is added.
- **Odd length:** The unique middle element contributes as its own value rather than being concatenated with itself.
- **Different digit lengths:** String joining naturally handles cases such as $7$ followed by $52$, producing $752$.
- **Positive-input guarantee:** Since zero and negative values are absent, there are no sign characters or meaningful leading zeros to complicate numeral concatenation.
- **Input preservation:** Pointer movement reads `nums` only; the caller's array retains its original elements and order.
