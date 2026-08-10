## General

A valid subsequence must remember more than its length. To decide whether a new value can extend it, the algorithm must also know the sign of its most recent difference. The exact solution therefore keeps two dynamic-programming states for every possible ending index.

- `f[i]` is the maximum length of a wiggle subsequence ending at `nums[i]` whose final difference is positive.
- `g[i]` is the maximum length of a wiggle subsequence ending at `nums[i]` whose final difference is negative.

A one-element subsequence has no difference, but it can serve as the starting point before either an upward or downward first step. Both arrays consequently begin with ones.

Despite the manifest's linear-time constant-space summary, the checked-in source compares every index with every earlier index and stores two full arrays. It is the quadratic dynamic-programming approach, not the adjacent-scan optimization.

**Why two ending states are necessary.**

Suppose a subsequence currently ends with a positive difference. Its next selected value must be smaller, producing a negative difference. Another larger value would create two consecutive positive differences and break alternation.

Similarly, a subsequence whose last difference is negative can be extended only by a larger value. The numerical last value is supplied by its ending index; the state type supplies the sign that must alternate.

Keeping only one best length per index would lose this sign information. Two subsequences of equal length ending at the same value but with opposite last directions have different valid next moves.

**Transition for an upward final step.**

For current index `i`, the inner loop considers every earlier `j < i`. If `nums[j] < nums[i]`, selecting `nums[i]` after `nums[j]` creates a positive difference.

To alternate correctly, the preceding subsequence should end with a negative difference, represented by `g[j]`. Appending the current value gives length `g[j] + 1`, so the source performs

```text
f[i] = max(f[i], g[j] + 1)
```

Trying all valid earlier endpoints ensures that `f[i]` keeps the longest possible upward-ending result.

**Transition for a downward final step.**

If `nums[j] > nums[i]`, the new difference is negative. It can extend a positive-ending subsequence from `f[j]`, producing

```text
g[i] = max(g[i], f[j] + 1)
```

Again, the maximum across every earlier `j` gives the best downward-ending subsequence at `i`.

**Why equal values are ignored.**

When `nums[j] == nums[i]`, the difference is zero. The definition requires differences to alternate strictly between positive and negative, so zero cannot be a wiggle step. The `elif` chain performs no update in this case.

Ignoring the current equal value does not lose a better answer. A later transition may use whichever equal occurrence has the more useful position, while a zero difference itself never needs to be included.

**A trace of the fully alternating example.**

For `[1,7,4,9,2,5]`:

- At `7`, the earlier `1` produces an upward sequence of length two.
- At `4`, the sequence `[1,7]` ends upward, so appending `4` creates a downward sequence of length three.
- At `9`, that downward state extends upward to length four.
- At `2`, the upward state extends downward to length five.
- At `5`, the downward state extends upward to length six.

The whole array is recovered in length, even though the implementation stores lengths rather than predecessor links.

**A monotone input.**

For `[1,2,3,4]`, every later value is greater than earlier ones. Each `f[i]` can reach length two by taking one earlier value, but no `g` state grows beyond one because no negative difference exists. The maximum answer is two, matching the rule that any two unequal values form a trivial wiggle sequence but a third increasing value cannot alternate.

**Why the scan order makes dependencies available.**

The outer loop processes indices from left to right. Every transition into index `i` reads only `f[j]` or `g[j]` for `j < i`, so those states are already final. There are no cyclic dependencies.

Within one `i`, updates to `f[i]` and `g[i]` do not incorrectly feed each other because the inner loop reads only earlier indices. Thus a current value cannot be selected twice in the same subsequence.

**Tracking the global result.**

The longest wiggle subsequence may end at any input position; it does not have to include the final array element. After completing each `i`, the source updates

```text
ans = max(ans, f[i], g[i])
```

`ans` begins at one because the input is nonempty and one element is always valid. Taking a maximum over all endpoints and both final directions covers every possible longest subsequence.

**Why the recurrence is correct.**

Take any optimal positive-ending subsequence at index `i`. Remove its last element. If its length was greater than one, the remaining subsequence ends at some earlier `j` with `nums[j] < nums[i]`, and its last difference must be negative. Its length is at most `g[j]`, so the transition considers a candidate at least as long as the original.

Conversely, every `g[j] + 1` candidate used for `f[i]` appends a strictly positive difference to a negative-ending wiggle sequence, so it is valid. The same argument with signs reversed proves `g[i]`. Induction over increasing `i` establishes both state definitions, and the global maximum is therefore the desired optimum.

The algorithm returns only a length. Reconstructing actual values would require predecessor information for the chosen `f` and `g` transitions.

## Complexity detail

Let $n$ be the length of `nums`. For each `i`, the inner loop visits all `i` earlier indices. The number of comparisons is

$$
1+2+\cdots+(n-1)=\frac{n(n-1)}{2}=O(n^2).
$$

Total running time is $O(n^2)$, not the manifest's $O(n)$ follow-up bound.

The `f` and `g` arrays each contain $n$ integers, so auxiliary space is $O(n)$, not $O(1)$. The scalar result and loop variables use constant additional space.

The published maximum of 1000 elements makes the quadratic work feasible, but the source does not implement the strongest asymptotic approach requested by the follow-up.

## Alternatives and edge cases

- **Linear two-scalar DP:** Maintain only the best `up` and `down` lengths while scanning adjacent values. A rise sets `up = down + 1`; a fall sets `down = up + 1`. This achieves $O(n)$ time and $O(1)$ space and matches the manifest, but it is not the checked-in source.

- **Greedy turning-point count:** Ignore repeated values and count changes between rising and falling trends. Keeping only local peaks and valleys gives the same optimal length in linear time.

- **Brute-force subsequences:** Enumerate every keep/delete choice and test alternation. This is exponential and unnecessary once ending-sign states are identified.

- **One element:** Both states and `ans` remain one, which is a valid wiggle sequence by definition.

- **Two unequal elements:** One of the upward or downward states becomes two.

- **Two equal elements:** Zero difference is ignored, so the maximum remains one.

- **All values equal:** No transition fires and the answer is one.

- **Strictly increasing or decreasing input:** The answer is two when at least two elements exist.

- **Repeated plateaus between trends:** Equal comparisons do not change states; a later strict rise or fall may still continue an alternating subsequence.

- **Multiple optimal endings:** `ans` stores only the length, so tie choice is irrelevant.

- **Input preservation:** The method reads `nums` without sorting or modifying it, preserving subsequence order semantics.
