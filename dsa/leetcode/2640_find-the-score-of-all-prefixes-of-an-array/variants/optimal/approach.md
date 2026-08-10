## General

**Each new prefix adds exactly one conversion value**

For index $i$, define the running maximum:

$$
M_i=\max(\texttt{nums[0]},\ldots,\texttt{nums[i]}).
$$

The conversion value at position $i$ is:

$$
C_i=\texttt{nums[i]}+M_i.
$$

The score of prefix zero through $i$ is:

$$
S_i=C_0+C_1+\cdots+C_i.
$$

Neighboring prefix scores therefore satisfy:

$$
S_i=S_{i-1}+C_i.
$$

This recurrence means the algorithm can extend the previous answer instead of recomputing the conversion array for every prefix.

**Maintain the prefix maximum**

`mx` begins at zero. All input values are positive, so before processing the first number zero is a safe value below or equal to the eventual maximum.

At index $i$ with value $x$, the code executes:

`mx = max(mx, x)`.

After this update, `mx` is exactly $M_i$:

- the old `mx` was the maximum through index $i-1$;
- comparing it with $x$ adds the only new prefix element.

The update must happen before calculating the conversion value because the current element is included in `max(nums[0..i])`.

**Use the previous output as the running sum**

The code stores all required prefix scores in `ans`. For the current position:

`ans[i] = x + mx + (0 if i == 0 else ans[i - 1])`.

The first two terms are $C_i$. The final term is:

- zero for the first prefix, which has no preceding score;
- $S_{i-1}$ for every later position.

Thus the assignment is exactly the recurrence $S_i=S_{i-1}+C_i$.

No separate running-sum variable is necessary because `ans[i - 1]` already stores it.

**Trace the first example**

For `nums = [2,3,7,5,10]`:

- index zero: `mx=2`, conversion is $2+2=4$, score four;
- index one: `mx=3`, conversion is $3+3=6$, score $4+6=10$;
- index two: `mx=7`, conversion is 14, score 24;
- index three: `mx` remains seven, conversion is $5+7=12$, score 36;
- index four: `mx=10`, conversion is 20, score 56.

This yields `[4,10,24,36,56]`.

The fourth element illustrates why the running maximum must persist: even though current value five is smaller than seven, its conversion still uses seven.

**Why recomputing each prefix is wasteful**

A direct method could, for every endpoint $i$:

1. rescan `nums[0..i]` to build running maxima;
2. build its conversion array;
3. sum it.

Work across all prefix lengths would be:

$$
1+2+\cdots+n=O(n^2).
$$

But extending a prefix changes neither earlier maxima nor earlier conversion values. It adds only $C_i$. The one-pass recurrence reuses exactly that overlap.

**Two invariants prove correctness**

Before processing index $i$, assume:

- `mx` equals the maximum of elements before $i$, or zero when $i=0$;
- if $i>0$, `ans[i - 1]` equals the score of prefix ending at $i-1$.

Updating `mx` with $x$ makes it the maximum through $i$. Then `x + mx` is the current conversion value. Adding the previous prefix score produces the complete score through $i$.

The assignment establishes both invariants for the next iteration. By induction, every output position is correct.

**Why positive input simplifies initialization**

Because `nums[i] >= 1`, initializing `mx = 0` cannot incorrectly dominate the first prefix.

For a generalized array allowing negative numbers, the algorithm should initialize `mx` to negative infinity or to the first element. The exact initialization relies on the stated positive-value constraint.

**Large totals**

Individual values reach $10^9$, and a prefix score can grow on the order of $n\cdot10^9$. Fixed-width languages may need 64-bit integers.

Python integers grow automatically, so the stored implementation cannot overflow.

**Output space is required**

The problem asks for the score of every prefix, so $n$ values must be returned. The algorithm fills a preallocated $n$-entry list.

Its computational state beyond that output is only the running maximum and loop variables. It never stores the conversion array separately.

**Input preservation**

The loop only reads `nums`. Prefix maxima and scores live in local variables and `ans`, so the caller's array remains unchanged.

## Complexity detail

Let $n=\texttt{nums.length}$. Each element is visited once, with constant-time maximum, addition, and assignment. Time complexity is $O(n)$.

The returned array contains $n$ scores and uses $O(n)$ space. Excluding required output, auxiliary space is $O(1)$ because only `mx` and loop state are retained.

## Alternatives and edge cases

- **Build the conversion array first:** Also $O(n)$ time but allocates another $O(n)$ list unnecessarily.
- **Recompute every prefix:** Correct but $O(n^2)$ because earlier work is repeated.
- **Separate running sum:** Maintain `score` instead of reading `ans[i-1]`; behavior and complexity are equivalent.
- **Single element:** Its score is twice its value.
- **Strictly increasing values:** Every current value becomes the new maximum.
- **Repeated values:** The running maximum remains stable and each conversion still includes the current value.
- **Value below prior maximum:** Conversion uses the earlier maximum, not the current value twice.
- **Positive-value assumption:** It makes zero a safe initial maximum.
- **Large score:** Python integer arithmetic avoids overflow.
- **Input preservation:** The source array is never modified.
