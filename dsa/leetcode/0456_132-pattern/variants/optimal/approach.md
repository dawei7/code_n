## General

A 132 pattern needs indices $i<j<k$ whose values satisfy

$$
\texttt{nums}[i] < \texttt{nums}[k] < \texttt{nums}[j].
$$

The middle index `j` supplies the largest value—the “3”—and the rightmost index `k` supplies the middle value—the “2.” The remaining task is to find an earlier, smaller “1.”

The exact solution scans from right to left. This direction is useful because, when a value is considered as the possible “1,” every possible `j` and `k` lies in the suffix that has already been processed. A monotonic stack discovers valid `(3, 2)` pairs in that suffix, and `vk` remembers the best certified “2.”

**Meaning of the stack and `vk`**

`stk` contains unresolved suffix values that may serve as the “3” of a future pattern. From bottom to top it is monotonically nonincreasing: larger values are below, and smaller or equal values are above.

`vk` starts at negative infinity. Once a stack value is popped by a larger value `x`, that popped value is certified as a possible “2”: `x` occurs to its left in the original array and is strictly larger, so together they satisfy

$$
\text{popped value} < x.
$$

Here `x` can play the “3” and the popped value can play the “2.” `vk` stores the strongest such “2” established so far. If a still-earlier value is smaller than `vk`, the three values and their scan order form the required 132 pattern.

**Why the check happens before stack updates**

For each reverse-scanned value `x`, the first operation is `if x < vk`. At that moment, `vk` came from a `(3, 2)` pair located entirely to the right of `x` in the original array. Therefore using `x` as the “1” automatically gives the correct index order $i<j<k$. The strict inequality supplies the remaining value relation.

Only after this check does the code let `x` act as a possible “3.” Checking afterward could incorrectly try to use the same array position as two roles.

**Why popping smaller values finds a `(3, 2)` pair**

While the stack top is strictly smaller than `x`, the code pops it and assigns it to `vk`. The current `x` appears earlier in the original array than every stack element because of the reverse scan. Thus each pop proves a pair with `x` as `nums[j]` and the popped value as `nums[k]`, satisfying both $j<k$ and `nums[k] < nums[j]`.

Because the stack is decreasing from bottom to top, popped values come off in nondecreasing order. The last popped value is the largest one below `x`, making it the easiest certified “2” for an earlier number to fall below. The stack structure also prevents a previously stronger certified value from being lost: either a later `x` cannot cross the larger barrier that certified it, or it crosses that barrier and establishes an even larger candidate.

After all smaller tops are removed, `x` is appended. The remaining top, if any, is greater than or equal to `x`, so appending preserves the monotonic order. Equal values are not popped because the pattern requires a strict `nums[k] < nums[j]` relation.

**Trace `[3,1,4,2]`**

The reverse order is `2, 4, 1, 3`.

1. Read `2`. It is not below negative infinity. Nothing is popped, so push `2`.
2. Read `4`. It is not below `vk`. Since `2 < 4`, pop `2` and set `vk = 2`; this certifies `(4, 2)` as the “3, 2” portion. Push `4`.
3. Read `1`. Now `1 < vk`, or $1<2$. The stored pair gives $1<2<4$, and reverse processing guarantees original indices `1 < 2 < 3`. Return `True`.

**Why a returned result is always valid**

`vk` is assigned only from a stack pop. Every such pop has a current larger value to its original left, giving real indices `j < k` with `nums[k] = vk < nums[j]`. A later reverse iteration examines an original index `i < j`. If its value is below `vk`, all three strict inequalities and index inequalities hold. Therefore the method never returns a false positive.

**Why an existing pattern is found**

Suppose a valid pattern exists. When its “3” value is scanned, its smaller “2” is in the processed suffix. The monotonic-stack process either pops that value, certifying it or a still larger valid “2,” or retains a barrier that will be popped by an appropriate larger candidate. By the time the pattern's “1” is scanned, `vk` is at least a certified middle value greater than that “1.” The initial comparison therefore succeeds. The stack compresses many possible pairs without discarding the existence of the useful one.

## Complexity detail

Let $n$ be the array length. Each value is pushed onto `stk` once. A value can be popped at most once, so all executions of the inner `while` loop across the entire scan total at most $n$. The monotonic-stack work is therefore $O(n)$ time.

The expression `nums[::-1]` creates a reversed list copy in $O(n)$ time and $O(n)$ space. The stack can also contain up to $n$ values. Total auxiliary space is $O(n)$ and total time remains $O(n)$.

Using `reversed(nums)` instead would avoid the explicit reversed copy, but the stack still requires $O(n)$ worst-case space. The input list itself is not modified.

## Alternatives and edge cases

- **Check every triple:** It directly follows the definition but takes $O(n^3)$ time.
- **Prefix minimum plus suffix scan:** Fix the “3,” use the minimum value to its left, and scan its right side for a middle value. This improves to $O(n^2)$ but repeats suffix work.
- **Prefix minima plus a monotonic stack:** Another linear method explicitly stores the best “1” for every position and searches right-side “2” candidates. It uses $O(n)$ space but more state than the exact reverse-stack solution.
- **Balanced search structure:** Scanning possible middle indices while querying a suffix set can take $O(n\log n)$ time.
- **Fewer than three values:** No triple exists. The loop performs harmless stack operations and returns `False`.
- **Strict inequalities:** Equal values never form either `<` relation. The stack pops only with `<`, and detection also uses `<`.
- **Strictly increasing input:** Reverse scanning keeps popping, but no earlier value is smaller than the certified middle in the needed index arrangement, so no pattern is reported.
- **Strictly decreasing input:** Nothing is popped because reverse-scanned values keep getting smaller; `vk` remains negative infinity.
- **Negative values:** Starting `vk` at `-inf` works below every legal integer, and comparisons are otherwise unchanged.
- **Reversed-copy cost:** The exact syntax duplicates the array. An iterator can remove that copy if constant factors matter.
