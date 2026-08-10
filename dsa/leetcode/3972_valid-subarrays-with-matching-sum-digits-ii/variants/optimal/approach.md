## General

The smaller version can enumerate every subarray, but `n\le10^5` makes `O(n^2)` pairs impossible here. The Optimal source counts many left endpoints together by combining three ideas:

1. express every subarray sum as a difference of prefix sums;
2. express “leading digit is `x`” as membership in decimal magnitude intervals;
3. express “last digit is `x`” as a modulo-ten condition.

Because every array value is positive, the prefix sums are strictly increasing. This lets two pointers maintain the eligible left prefixes for each right prefix in linear time per decimal magnitude.

**Prefix differences represent subarrays**

The source builds:

```python
prefix = [0]
for number in nums:
    prefix.append(prefix[-1] + number)
```

Thus `prefix[j]` is the sum of the first `j` elements. For a nonempty subarray `nums[i..j-1]`, its sum is

$$
\texttt{prefix}[j]-\texttt{prefix}[i],
\qquad 0\le i<j\le n.
$$

During the main loop, the variable named `right` is a right prefix-sum value, not an array index. The algorithm considers `prefix[1]` through `prefix[n]` as possible right endpoints and counts earlier prefix values that can serve as the left endpoint.

**All numbers with leading digit `x`**

For a decimal place value `p` equal to `1,10,100,\ldots`, the positive integers having leading digit `x` and exactly that magnitude lie in the inclusive interval

$$
[xp,(x+1)p-1].
$$

For example, when `x=3`:

- `p=1` gives `[3,3]`;
- `p=10` gives `[30,39]`;
- `p=100` gives `[300,399]`.

The source names these endpoints `lower` and `upper`. It starts with `power=1` and multiplies by ten after every pass.

These intervals are disjoint, and their union contains every positive integer whose first digit is `x`. Therefore each qualifying subarray sum belongs to exactly one pass; it cannot be counted twice.

The loop continues while `x\cdot power` is at most the total array sum `prefix[-1]`. Once even the smallest number in the next interval exceeds the largest possible subarray sum, no later magnitude can contribute.

**Converting the leading-digit interval into a prefix window**

Fix one interval `[lower,upper]` and one right prefix value `R`. A left prefix value `L` produces a sum in this interval exactly when

$$
\texttt{lower}\le R-L\le\texttt{upper}.
$$

Rearranging both inequalities gives

$$
R-\texttt{upper}
\le L\le
R-\texttt{lower}.
$$

So, for this `R`, the eligible left prefix sums occupy one numerical window.

The source maintains two indices:

- `add` is the first prefix not yet inserted into the active window;
- `remove` is the first inserted prefix not yet removed from its left side.

It adds while

```python
prefix[add] <= right - lower
```

because `R-lower` is the inclusive upper bound for `L`.

It removes while

```python
prefix[remove] < right - upper
```

because values strictly below `R-upper` are too small. Equality remains eligible, matching the inclusive sum bound.

After both loops, the active prefixes are exactly those satisfying

$$
R-\texttt{upper}\le L\le R-\texttt{lower}.
$$

**Why numerical eligibility also guarantees the left endpoint is earlier**

A prefix difference must use `i<j`. The pointer loops do not explicitly compare prefix indices with the current right index, but positivity makes that unnecessary.

Every leading-digit interval has `lower\ge1`. Therefore an added left value satisfies

$$
L\le R-\texttt{lower}<R.
$$

Since positive elements make `prefix` strictly increasing, any prefix value smaller than `R=prefix[j]` must occur at an earlier index. A current or future prefix cannot enter the window accidentally.

This is one reason the positivity guarantee is structurally important rather than incidental.

**Encoding the last digit as a residue**

The subarray sum must also end in digit `x`. In modular form:

$$
(R-L)\bmod10=x.
$$

Rearranging gives

$$
L\bmod10=(R-x)\bmod10.
$$

The source maintains `residue_counts[d]` for `d=0,\ldots,9`, storing how many currently active left prefix sums have remainder `d` modulo ten.

When a prefix enters the numerical window, its residue bucket is incremented. When it leaves, the same bucket is decremented. After the window has been adjusted for `R`, the number of left endpoints satisfying the last-digit condition is exactly:

```python
residue_counts[(right - x) % 10]
```

Adding that bucket to `answer` counts all subarrays ending at this right endpoint whose sum lies in the current leading-digit interval and ends in `x`.

Python's modulo operation returns a value from zero through nine even when `right-x` is negative, so it remains a valid bucket index. In practice, an empty numerical window then contributes zero.

**Why both pointers move only forward**

Within one magnitude pass, successive `right` values are strictly increasing. Therefore both window boundaries

$$
R-\texttt{upper}
\quad\text{and}\quad
R-\texttt{lower}
$$

also increase.

Once a prefix becomes small enough to fall below the left boundary, it can never become eligible again for a later `R`. Once a prefix has entered through the right boundary, it never needs to be “un-added.” Thus `add` and `remove` only move forward.

Each prefix is inserted at most once and removed at most once during one power-of-ten pass. The apparent nested `while` loops do not make the pass quadratic.

The pointers and residue buckets reset for every new decimal magnitude because `lower` and `upper` change. A prefix eligible for sums in `[10x,10x+9]` is not governed by the same window as one eligible for `[100x,100x+99]`.

**Walking through the sample structure**

For `nums=[1,100,1]`, the prefix sums are

$$
[0,1,101,102].
$$

With `x=1`, relevant leading-digit intervals include `[1,1]`, `[10,19]`, and `[100,199]`.

- The interval `[1,1]` counts the two one-element sums equal to one.
- The interval `[10,19]` finds none.
- The interval `[100,199]` considers sums such as `101`. For right prefix `101`, left prefix zero gives sum `101`; for right prefix `102`, left prefix one gives another `101`.

All four qualifying subarrays are counted. A sum belongs to only one magnitude interval, so these contributions do not overlap.

**Why the residue bucket is enough**

Inside the active numerical window, the leading-digit requirement has already been enforced by the difference bounds. Among those prefixes, the final digit depends only on the prefix remainder modulo ten. Exact prefix values no longer matter to the last-digit test, so ten counters replace a potentially large set of individual checks.

The method counts index pairs rather than distinct sums. If several left prefixes in the window have the required residue, each represents a different subarray and each must contribute one. The bucket stores multiplicity, not just presence.

## Complexity detail

Let

$$
n=\lvert\texttt{nums}\rvert
\qquad\text{and}\qquad
S=\sum_{v\in\texttt{nums}}v.
$$

Building the prefix array takes `O(n)` time.

The number of powers `1,10,100,\ldots` for which `x\cdot power\le S` is `O(\log S)`. During one such pass:

- the outer scan visits `n` right prefix values;
- `add` advances at most `n+1` times total;
- `remove` advances at most `n+1` times total;
- every residue operation is constant time.

One magnitude therefore costs `O(n)`, and total time is

$$
O(n\log S).
$$

The prefix array uses `O(n)` space. The exact loop `for right in prefix[1:]` also creates a sliced list of `n` prefix values for each pass; only one such slice exists at a time, so peak space remains `O(n)`. The residue array has constant size ten, and all other state is scalar.

The algorithm does not modify `nums`.

The answer can be as large as `n(n+1)/2`. Python integers store it exactly.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintaining a running sum avoids cubic work but still takes `O(n^2)` time, which is too large for `n=10^5`.

- **Binary-search prefix bounds for every right endpoint:** Two binary searches can locate the numerical window, but counting only prefixes with one residue would still need additional indexed data. The monotone pointers and ten buckets solve both parts in linear time per magnitude.

- **Use one window for all leading-digit lengths:** Numbers beginning with `x` occupy separated intervals such as `[x,x]`, `[10x,10x+9]`, and `[100x,100x+99]`. Their union is not one continuous range.

- **Count only numerical-window size:** This enforces the first digit but ignores the required final digit. Residue buckets provide the missing condition.

- **Store active prefixes in a set:** Equal residues and different indices must all count. A set would lose multiplicity; counters are required.

- **Use `right % 10 == x` directly:** The subarray sum is a difference of two prefixes. Its last digit depends on both `R` and `L`, leading to the residue equation `L\equiv R-x\pmod{10}`.

- **Incorrect lower-bound removal:** Prefixes equal to `R-upper` produce sum exactly `upper` and must remain. The source correctly removes only values strictly smaller.

- **Incorrect upper-bound insertion:** Prefixes equal to `R-lower` produce sum exactly `lower` and must be included. The source correctly uses `<=`.

- **Single-element array:** Prefix zero and the one nonzero prefix are processed normally. The sole subarray is counted exactly when its value begins and ends with `x`.

- **One-digit qualifying sum:** It belongs to the `power=1` interval `[x,x]` and must equal `x`, which automatically satisfies both digit conditions.

- **No qualifying magnitude:** The loop stops as soon as the smallest sum beginning with `x` exceeds `S`. The answer remains unchanged.

- **Upper interval beyond `S`:** It is harmless when `upper>S`. No actual prefix difference exceeds `S`, and the window inequalities still count all feasible sums in the truncated intersection.

- **Positive array requirement:** Strictly increasing prefix sums make numerical order match index order and enable forward-only pointers. Negative values would destroy this monotonic structure and require a different data structure.

- **Zeros outside the stated contract:** Nondecreasing rather than strictly increasing prefixes would complicate the implicit earlier-index argument. The source relies on the positive-input guarantee.

- **Duplicate subarray sums:** Different endpoint pairs are supposed to be counted separately. Residue counts preserve all eligible left-prefix occurrences.

- **Reset per power:** Reusing `add`, `remove`, or residue counts across different leading-digit intervals would mix incompatible numerical windows and corrupt the answer.

- **Slice allocation:** Iterating prefix indices from one through `n` could avoid the temporary `prefix[1:]` copy, but the exact source creates it. Peak asymptotic space is still `O(n)`.

- **Decimal growth factor:** Multiplying `power` by ten enumerates exactly the possible digit lengths. No logarithm or floating-point calculation is needed, avoiding precision issues near powers of ten.
